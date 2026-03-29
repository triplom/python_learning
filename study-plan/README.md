# Study Plan — Python from Zero to AI

> Phase-by-phase curriculum covering Python fundamentals through machine learning, computer vision, NLP, and deployment.

**Duration:** ~6 months (self-paced) · **Approach:** Theory → Hands-on Lab → Mini-project  
**Prerequisites:** None — absolute beginner friendly

**Primary Courses:**
- [Python Do Zero a IA 2026](https://www.udemy.com/course/programacao-python-do-basico-ao-avancado/) — Andre Iacono, 34h, PT-BR
- [Python & MySQL](https://www.udemy.com/course/python-mysql/) — Alfahelix, 6h18m, PT-BR
- [Aprenda Programação Python para Iniciantes](https://www.udemy.com/course/python-iniciantes-programacao/) — Andre Iacono, 1h55m, PT-BR
- [GeeksForGeeks OOP Concepts](https://www.geeksforgeeks.org/python-oops-concepts/) — reference

---

## Roadmap

```
Phase 1  (Weeks 1–2)   →  Basics + Control Flow + Data Structures
Phase 2  (Weeks 3–5)   →  Functions + OOP + Files + Advanced Python
Phase 3  (Weeks 6–7)   →  MySQL + Data Visualization
Phase 4  (Weeks 8–11)  →  Data Science + Machine Learning + Deep Learning
Phase 5  (Weeks 12–14) →  NLP + Computer Vision + Generative AI
Phase 6  (Weeks 15–16) →  Bioinformatics + Streamlit deployment
```

---

## Phase 1 — Python Foundations (Weeks 1–2)

**Goal:** Write, run, and debug basic Python programs confidently.

### Week 1 — Absolute Basics

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1 | Setup, Hello World, how Python runs | `01-basics/hello_world.py` | Course 2 §1, Course 4 §1 |
| 2 | Variables, types, type conversions | `01-basics/variables.py` | Course 2 §2, Course 4 §2 |
| 3 | Strings: slicing, methods, f-strings | `01-basics/strings.py` | Course 2 §2, Course 4 §3 |
| 4 | Numbers: int, float, math, operators | `01-basics/numbers.py` | Course 2 §2, Course 4 §4 |
| 5 | User input — `input()`, casting | `01-basics/user_input.py` | Course 2 §2 |
| 6–7 | Mini-project: Calculator | `01-basics/calculator.py` | Course 2 §3 |

**Checklist:**
- [ ] Can write and run a `.py` file from the terminal
- [ ] Understand `int`, `float`, `str`, `bool`
- [ ] Can format output with f-strings
- [ ] Completed the calculator mini-project

### Week 2 — Control Flow & Data Structures

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1–2 | if/elif/else, comparison operators | `02-control-flow/conditionals.py` | Course 2 §4, Course 4 §6 |
| 3 | for loops, range() | `02-control-flow/for_loops.py` | Course 4 §7 |
| 4 | while loops, break, continue | `02-control-flow/while_loops.py` | Course 4 §7 |
| 5 | Lists: creation, indexing, mutation | `03-data-structures/lists.py` | Course 2 §4, Course 4 §8 |
| 6 | Dicts, tuples, sets | `03-data-structures/dicts_tuples_sets.py` | Course 4 §9 |
| 7 | Practice exercises | `03-data-structures/exercises/` | — |

**Checklist:**
- [ ] Can use if/elif/else for branching logic
- [ ] Can iterate with for and while loops
- [ ] Can create and manipulate lists and dicts
- [ ] Understand the difference between mutable and immutable types

---

## Phase 2 — Intermediate Python (Weeks 3–5)

**Goal:** Write reusable, well-structured Python code using functions and OOP.

### Week 3 — Functions

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1–2 | Defining functions, return values, scope | `04-functions/basics.py` | Course 1 §3, Course 4 §10 |
| 3 | `*args`, `**kwargs`, default params | `04-functions/args_kwargs.py` | Course 4 §10 |
| 4 | Lambda, map, filter | `04-functions/lambda_map_filter.py` | Course 1 §4 |
| 5 | reduce, zip, enumerate | `04-functions/reduce_zip_enum.py` | Course 1 §4 |
| 6–7 | Mini-project: functional data pipeline | `04-functions/project_pipeline.py` | — |

### Week 4 — OOP

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1 | Classes, `__init__`, instance vs class attrs | `05-oop/classes_basics.py` | Course 4 §11, GFG |
| 2 | Single inheritance, `super()` | `05-oop/inheritance.py` | Course 4 §11, GFG |
| 3 | Multiple & multilevel inheritance | `05-oop/inheritance_advanced.py` | Course 4 §11 |
| 4 | Polymorphism, method overriding | `05-oop/polymorphism.py` | Course 4 §11, GFG |
| 5 | Encapsulation, private attrs, properties | `05-oop/encapsulation.py` | Course 4 §11, GFG |
| 6 | Abstraction, ABCs | `05-oop/abstraction.py` | GFG |
| 7 | Mini-project: library system OOP design | `05-oop/projects/library_system.py` | — |

### Week 5 — Files, Exceptions & Advanced Python

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1–2 | File I/O: read, write, append, `with` | `06-files-exceptions/file_io.py` | Course 1 §3 |
| 3 | try/except/finally, raising exceptions | `06-files-exceptions/exceptions.py` | Course 1 §3 |
| 4 | List and dict comprehensions | `07-advanced-python/comprehensions.py` | Course 1 §4 |
| 5 | enumerate, zip, generators | `07-advanced-python/enumerate_zip_gen.py` | Course 1 §4 |
| 6–7 | Mini-project: CSV data processor | `07-advanced-python/project_csv.py` | — |

**Checklist (Phase 2):**
- [ ] Can write functions with parameters, return values, and default args
- [ ] Can build a class hierarchy with inheritance
- [ ] Understand encapsulation and can use properties
- [ ] Can handle exceptions gracefully
- [ ] Can read/write files

---

## Phase 3 — Data & Databases (Weeks 6–7)

**Goal:** Connect Python to a real database and produce charts from data.

### Week 6 — MySQL + Python

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1 | MySQL fundamentals: CREATE, INSERT, SELECT | `08-mysql/setup.sql` | Course 1 §5 |
| 2 | mysql-connector-python: connect + SELECT | `08-mysql/crud_select.py` | Course 1 §6 |
| 3 | INSERT, UPDATE, DELETE with Python | `08-mysql/crud_insert.py`, `crud_update.py`, `crud_delete.py` | Course 1 §6 |
| 4 | JOINs, foreign keys | `08-mysql/joins.py` | Course 1 §5 |
| 5 | Users, privileges | `08-mysql/users.sql` | Course 1 §5 |
| 6–7 | Mini-project: contacts database app | `08-mysql/projects/contacts_app.py` | — |

**Setup:**
```bash
cd 08-mysql
docker compose up -d   # starts MySQL 8 container
python crud_select.py
```

### Week 7 — Data Visualization

| Day | Topic | Lab | Course Ref |
|-----|-------|-----|-----------|
| 1 | Line charts, title, labels, legend | `09-data-visualization/line_chart.py` | Course 1 §7 |
| 2 | Bar charts (vertical + horizontal) | `09-data-visualization/bar_chart.py` | Course 1 §7 |
| 3 | Scatter plots | `09-data-visualization/scatter.py` | Course 1 §7 |
| 4 | Boxplots, histograms | `09-data-visualization/boxplot.py` | Course 1 §7 |
| 5 | Subplots, figure layout | `09-data-visualization/subplots.py` | Course 1 §7 |
| 6–7 | Mini-project: visualize database query results | `09-data-visualization/project_db_viz.py` | — |

---

## Phase 4 — Data Science & AI (Weeks 8–11)

**Goal:** Analyse datasets and build ML models.

### Week 8 — NumPy & Pandas

| Day | Topic | Lab |
|-----|-------|-----|
| 1–2 | NumPy: arrays, broadcasting, math ops | `10-data-science/numpy_basics.py` |
| 3–4 | Pandas: Series, DataFrame, read_csv | `10-data-science/pandas_basics.py` |
| 5–6 | Data cleaning: nulls, duplicates, dtypes | `10-data-science/data_cleaning.py` |
| 7 | Mini-project: EDA on a public dataset | `10-data-science/project_eda.py` |

### Weeks 9–10 — Machine Learning with Scikit-learn

| Topic | Lab |
|-------|-----|
| Linear & logistic regression | `11-machine-learning/regression.py` |
| Decision trees, Random Forests | `11-machine-learning/trees.py` |
| K-Means clustering | `11-machine-learning/clustering.py` |
| Train/test split, cross-validation | `11-machine-learning/evaluation.py` |
| Feature engineering, pipelines | `11-machine-learning/pipelines.py` |
| Mini-project: Titanic classifier | `11-machine-learning/project_titanic.py` |

### Week 11 — Deep Learning with TensorFlow/Keras

| Topic | Lab |
|-------|-----|
| Tensors, layers, activations | `12-deep-learning/keras_basics.py` |
| Training loop, callbacks, history | `12-deep-learning/training.py` |
| CNNs: Conv2D, MaxPool, Flatten | `12-deep-learning/cnn.py` |
| Model saving and loading | `12-deep-learning/save_load.py` |
| Mini-project: digit classifier (MNIST) | `12-deep-learning/project_mnist.py` |

---

## Phase 5 — Specialized AI (Weeks 12–14)

**Goal:** Apply AI to text, images, and recommendations.

### Week 12 — NLP & Text Search

| Topic | Lab | Course Ref |
|-------|-----|-----------|
| Text preprocessing, tokenization | `13-nlp/preprocessing.py` | Course 6 |
| TF-IDF, keyword search | `13-nlp/tfidf_search.py` | Course 6 |
| Content-based recommendation | `13-nlp/content_recommender.py` | Course 5 |
| Collaborative filtering | `13-nlp/collaborative_filter.py` | Course 5 |

### Week 13 — Computer Vision & Face Detection

| Topic | Lab | Course Ref |
|-------|-----|-----------|
| OpenCV basics: read, show, resize | `14-computer-vision/opencv_basics.py` | Course 7 |
| Drawing shapes, adding text | `14-computer-vision/drawing.py` | Course 7 |
| Haar cascade face detection | `14-computer-vision/face_detection.py` | Course 7 |
| Video capture + real-time detection | `14-computer-vision/video_face.py` | Course 7 |

### Week 14 — Generative AI

| Topic | Lab | Course Ref |
|-------|-----|-----------|
| HuggingFace Transformers pipeline | `15-generative-ai/transformers_intro.py` | Course 4 §advanced |
| Text generation, summarization | `15-generative-ai/text_generation.py` | Course 4 |
| Prompt engineering basics | `15-generative-ai/prompt_engineering.py` | Course 4 |

---

## Phase 6 — Applied Python (Weeks 15–16)

**Goal:** Apply Python to bioinformatics and build deployable apps.

### Week 15 — Bioinformatics

| Topic | Lab | Course Ref |
|-------|-----|-----------|
| FASTA parsing, Biopython intro | `16-bioinformatics/fasta_parser.py` | Course 1 §8, Course 3 |
| GC content, codon tables | `16-bioinformatics/gc_content.py` | Course 3 |
| Protein sequence analysis | `16-bioinformatics/protein_analysis.py` | Course 3 |
| Genome comparison (pairwise alignment) | `16-bioinformatics/genome_comparison.py` | Course 1 §8, Course 3 |
| Brazilian population case study | `16-bioinformatics/population_study.py` | Course 1 §8 |

### Week 16 — Streamlit Deployment

| Topic | Lab | Course Ref |
|-------|-----|-----------|
| Streamlit basics: text, widgets | `17-streamlit/hello_streamlit.py` | Course 4 §final |
| Charts in Streamlit | `17-streamlit/charts_app.py` | Course 4 |
| ML model dashboard | `17-streamlit/ml_dashboard.py` | Course 4 |
| Capstone: full interactive data app | `17-streamlit/capstone_app.py` | Course 4 |

---

## Capstone Project Ideas

After completing all phases, pick one:

| Project | Skills Used |
|---------|------------|
| Patient data analysis app | Pandas + MySQL + Matplotlib + Streamlit |
| Movie recommendation system | NLP + Collaborative filtering + Streamlit |
| Real-time face attendance tracker | OpenCV + MySQL |
| Genome sequence browser | Bioinformatics + Streamlit |
| Stock price predictor | Pandas + Scikit-learn + Streamlit |

---

## Resources

- [Python Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com) — practical tutorials
- [Kaggle Datasets](https://www.kaggle.com/datasets) — free datasets for practice
- [HuggingFace](https://huggingface.co) — pretrained models
- [GeeksForGeeks Python](https://www.geeksforgeeks.org/python-programming-language/) — reference
