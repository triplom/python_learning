# NLP — Text Search and Recommendation Systems
# Course 5 (Recommendation Systems) · Course 6 (Text Search)
# pip install scikit-learn nltk

import re
import math
from collections import Counter

# ═══════════════════════════════════════
#  TEXT PREPROCESSING
# ═══════════════════════════════════════

STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "it",
    "in",
    "on",
    "at",
    "of",
    "for",
    "to",
    "and",
    "or",
    "but",
    "with",
    "this",
    "that",
    "are",
    "was",
    "be",
    "as",
    "by",
    "from",
    "have",
    "has",
    "had",
    "not",
    "do",
}


def preprocess(text):
    """Lowercase, remove punctuation, tokenize, remove stopwords."""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    return tokens


sample = "The quick brown fox jumps over the lazy dog."
print(preprocess(sample))

# ═══════════════════════════════════════
#  TF-IDF FROM SCRATCH
# ═══════════════════════════════════════

documents = [
    "Python is a great programming language for data science",
    "Machine learning with Python is very powerful",
    "Data science requires statistics and programming",
    "Deep learning is a subset of machine learning",
    "Python supports object oriented programming",
]


def tf(doc_tokens):
    """Term frequency: count / total_terms."""
    count = Counter(doc_tokens)
    total = len(doc_tokens)
    return {word: cnt / total for word, cnt in count.items()}


def idf(all_docs_tokens):
    """Inverse document frequency: log(N / df)."""
    N = len(all_docs_tokens)
    df = Counter()
    for doc in all_docs_tokens:
        for word in set(doc):
            df[word] += 1
    return {word: math.log(N / freq) for word, freq in df.items()}


def tfidf_matrix(docs):
    all_tokens = [preprocess(d) for d in docs]
    idf_scores = idf(all_tokens)
    vocab = list(idf_scores.keys())
    matrix = []
    for tokens in all_tokens:
        tf_scores = tf(tokens)
        row = [tf_scores.get(w, 0) * idf_scores.get(w, 0) for w in vocab]
        matrix.append(row)
    return matrix, vocab


def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a**2 for a in v1))
    norm2 = math.sqrt(sum(b**2 for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot / (norm1 * norm2)


# ─── Text Search ──────────────────────────────────────────────────────────────
matrix, vocab = tfidf_matrix(documents)


def search(query, top_k=3):
    query_tokens = preprocess(query)
    idf_scores = {w: math.log(len(documents) / 1) for w in vocab}
    tf_q = tf(query_tokens)
    query_vec = [tf_q.get(w, 0) * idf_scores.get(w, 0) for w in vocab]
    scores = [
        (i, cosine_similarity(query_vec, doc_vec)) for i, doc_vec in enumerate(matrix)
    ]
    scores.sort(key=lambda x: x[1], reverse=True)
    print(f"\nQuery: '{query}'")
    for i, score in scores[:top_k]:
        print(f"  [{score:.4f}] {documents[i]}")


search("machine learning data science")
search("Python programming")

# ═══════════════════════════════════════
#  RECOMMENDATION SYSTEM
# ═══════════════════════════════════════

# ─── Content-based (using sklearn for simplicity) ────────────────────────────
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine

movies = {
    "The Matrix": "sci-fi action computer simulation virtual reality AI",
    "Inception": "sci-fi thriller dream subconscious mind heist action",
    "Interstellar": "sci-fi space time travel black hole relativity",
    "The Terminator": "sci-fi action AI robots future war time travel",
    "Ex Machina": "sci-fi AI robots consciousness human experiment",
    "Blade Runner 2049": "sci-fi AI androids future society dystopia",
    "Arrival": "sci-fi aliens language communication time",
    "Her": "romance AI relationship future technology",
}

titles = list(movies.keys())
descriptions = list(movies.values())

vectorizer = TfidfVectorizer()
tfidf_mat = vectorizer.fit_transform(descriptions)
sim_matrix = sklearn_cosine(tfidf_mat, tfidf_mat)


def recommend_movies(title, top_k=3):
    if title not in titles:
        print(f"'{title}' not found")
        return
    idx = titles.index(title)
    scores = list(enumerate(sim_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    print(f"\nBecause you liked '{title}', you might enjoy:")
    count = 0
    for i, score in scores:
        if i == idx:
            continue
        print(f"  {score:.3f} — {titles[i]}")
        count += 1
        if count >= top_k:
            break


recommend_movies("The Matrix")
recommend_movies("Interstellar")

# ─── Collaborative Filtering (user-item) ─────────────────────────────────────
import numpy as np

# User-item rating matrix (0 = not rated)
users = ["Alice", "Bob", "Carol", "David"]
items = ["Matrix", "Inception", "Interstellar", "Terminator", "Ex Machina"]

ratings = np.array(
    [
        [5, 4, 0, 3, 0],  # Alice
        [4, 0, 3, 0, 5],  # Bob
        [0, 5, 4, 0, 3],  # Carol
        [3, 0, 0, 5, 4],  # David
    ]
)


def user_similarity(ratings):
    """Cosine similarity between all user pairs."""
    n = ratings.shape[0]
    sim = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            u, v = ratings[i], ratings[j]
            mask = (u > 0) & (v > 0)  # only rated by both
            if mask.sum() == 0:
                continue
            sim[i, j] = sklearn_cosine(u[mask].reshape(1, -1), v[mask].reshape(1, -1))[
                0, 0
            ]
    return sim


sim = user_similarity(ratings)


def predict_rating(user_idx, item_idx, ratings, sim, k=2):
    """Predict rating for user on unrated item using top-k similar users."""
    user_sims = [
        (j, sim[user_idx, j])
        for j in range(len(users))
        if j != user_idx and ratings[j, item_idx] > 0
    ]
    user_sims.sort(key=lambda x: x[1], reverse=True)
    top_k = user_sims[:k]
    if not top_k:
        return 0
    weighted = sum(s * ratings[j, item_idx] for j, s in top_k)
    total_sim = sum(abs(s) for _, s in top_k)
    return weighted / total_sim if total_sim > 0 else 0


# Recommend items for Alice (user 0) that she hasn't rated
print("\nRecommendations for Alice:")
alice_ratings = ratings[0]
unrated = [i for i, r in enumerate(alice_ratings) if r == 0]
preds = [(items[i], predict_rating(0, i, ratings, sim)) for i in unrated]
preds.sort(key=lambda x: x[1], reverse=True)
for item, pred in preds:
    print(f"  {item}: predicted rating {pred:.2f}")

# LAB
# 1. Add more movies and users to the collaborative filter. Does it improve?
# 2. Implement item-based collaborative filtering.
# 3. Use scikit-learn TruncatedSVD for matrix factorization on the ratings matrix.
