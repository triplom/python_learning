# Generative AI with Python — Transformers & HuggingFace
# Course 4 §Generative AI section
# pip install transformers torch sentencepiece

# ═══════════════════════════════════════
#  HUGGINGFACE TRANSFORMERS — QUICK START
# ═══════════════════════════════════════

try:
    from transformers import pipeline
except ImportError:
    print("Install: pip install transformers torch sentencepiece")
    raise SystemExit

# ─── Text Generation ──────────────────────────────────────────────────────────
print("=== Text Generation ===")
generator = pipeline("text-generation", model="distilgpt2")

result = generator(
    "Python is a great programming language because",
    max_new_tokens=50,
    num_return_sequences=2,
    truncation=True,
)
for i, r in enumerate(result, 1):
    print(f"\n[{i}] {r['generated_text']}")

# ─── Sentiment Analysis ───────────────────────────────────────────────────────
print("\n=== Sentiment Analysis ===")
sentiment = pipeline("sentiment-analysis")

texts = [
    "Python is amazing for data science!",
    "This code is slow and hard to understand.",
    "I love working with machine learning models.",
    "The documentation is confusing and outdated.",
]
results = sentiment(texts)
for text, res in zip(texts, results):
    print(f"[{res['label']:8} {res['score']:.3f}] {text}")

# ─── Text Summarization ───────────────────────────────────────────────────────
print("\n=== Summarization ===")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

long_text = """
Python is a high-level, general-purpose programming language. Its design philosophy
emphasizes code readability with the use of significant indentation. Python is
dynamically typed and garbage-collected. It supports multiple programming paradigms,
including structured, object-oriented and functional programming. It is often described
as a batteries included language due to its comprehensive standard library. Python
was created by Guido van Rossum and first released in 1991. The Python Software
Foundation manages the development of the language. Python consistently ranks among
the most popular programming languages. It is widely used for web development, data
science, machine learning, artificial intelligence, and scientific computing.
"""

summary = summarizer(long_text, max_length=60, min_length=20, do_sample=False)
print(summary[0]["summary_text"])

# ─── Named Entity Recognition ─────────────────────────────────────────────────
print("\n=== Named Entity Recognition ===")
ner = pipeline("ner", grouped_entities=True)

text = "Guido van Rossum created Python in the Netherlands. Google and Microsoft both use Python extensively."
entities = ner(text)
for ent in entities:
    print(f"  [{ent['entity_group']:5}] {ent['word']:30} score={ent['score']:.3f}")

# ─── Zero-shot Classification ─────────────────────────────────────────────────
print("\n=== Zero-shot Classification ===")
classifier = pipeline("zero-shot-classification")

text = "This tutorial explains how to train a neural network for image recognition."
labels = ["technology", "sports", "politics", "science", "entertainment"]
result = classifier(text, candidate_labels=labels)

print(f"Text: {text[:60]}...")
for label, score in zip(result["labels"], result["scores"]):
    bar = "█" * int(score * 30)
    print(f"  {label:15} {score:.3f} {bar}")

# ─── Text-to-Text Translation ─────────────────────────────────────────────────
print("\n=== Translation (EN → FR) ===")
try:
    translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    sentences = [
        "Python is easy to learn.",
        "Machine learning is fascinating.",
        "Hello, how are you?",
    ]
    translations = translator(sentences)
    for orig, trans in zip(sentences, translations):
        print(f"  EN: {orig}")
        print(f"  FR: {trans['translation_text']}\n")
except Exception as e:
    print(f"Translation model not available: {e}")

# ═══════════════════════════════════════
#  PROMPT ENGINEERING BASICS
# ═══════════════════════════════════════

print("\n=== Prompt Engineering Patterns ===")

# Zero-shot prompt
zero_shot = "Classify the sentiment of this review: 'The product quality exceeded my expectations.'\nSentiment:"

# Few-shot prompt
few_shot = """Classify movie reviews as POSITIVE or NEGATIVE.

Review: "This film was a masterpiece." → POSITIVE
Review: "Terrible acting and boring plot." → NEGATIVE
Review: "The cinematography was breathtaking." → POSITIVE
Review: "I fell asleep halfway through." → NEGATIVE
Review: "Outstanding performances by all actors." → """

print("Zero-shot prompt structure:")
print(zero_shot)
print("\nFew-shot prompt structure (last → to complete):")
print(few_shot)

# Chain-of-thought
chain_of_thought = """
Solve step by step:
Q: If a train travels at 120 km/h and needs to cover 300 km, how long does it take?
A: Let me work through this step by step.
   - Distance = 300 km
   - Speed = 120 km/h
   - Time = Distance / Speed = 300 / 120 = 2.5 hours
   - 2.5 hours = 2 hours and 30 minutes
Answer: 2 hours and 30 minutes.

Q: A store sells books for R$45 each. With a 20% discount, how much do 3 books cost?
A:"""
print("\nChain-of-thought prompt (to complete):")
print(chain_of_thought)

# LAB EXERCISES
# 1. Use the sentiment pipeline on a list of product reviews from a CSV.
#    Plot the distribution of positive vs negative with matplotlib.
# 2. Experiment with different max_new_tokens values in text generation.
#    How does it affect coherence?
# 3. Try zero-shot classification on 10 news headlines with labels:
#    ["technology", "politics", "economy", "sports", "health"]
# 4. Build a simple question-answering chatbot using the Q&A pipeline:
#    pipeline("question-answering") with a fixed context paragraph.
