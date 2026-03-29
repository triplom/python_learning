# Python Learning Lab

> A complete, structured Python learning environment — hands-on labs, study plan, cheatsheets, Docker lab, and curated resources — from absolute beginner to AI/ML practitioner.

**Author:** [@triplom](https://github.com/triplom) · **Updated:** March 2026

---

## What's Inside

| Section | Description |
|---------|-------------|
| [Study Plan](./study-plan/) | Phase-by-phase curriculum, beginner → AI |
| [01 — Basics](./01-basics/) | Variables, strings, numbers, input, calculator project |
| [02 — Control Flow](./02-control-flow/) | Conditionals, loops |
| [03 — Data Structures](./03-data-structures/) | Lists, dicts, tuples, sets |
| [04 — Functions](./04-functions/) | Functions, lambda, map/filter/reduce/zip |
| [05 — OOP](./05-oop/) | Classes, inheritance, polymorphism, encapsulation, abstraction |
| [06 — Files & Exceptions](./06-files-exceptions/) | File I/O, error handling |
| [07 — Advanced Python](./07-advanced-python/) | List comprehension, enumerate, zip, generators |
| [08 — MySQL](./08-mysql/) | MySQL CRUD with Python, Docker MySQL lab |
| [09 — Data Visualization](./09-data-visualization/) | Matplotlib: line, bar, scatter, boxplot |
| [10 — Data Science](./10-data-science/) | NumPy, Pandas, data analysis |
| [11 — Machine Learning](./11-machine-learning/) | Scikit-learn models |
| [12 — Deep Learning](./12-deep-learning/) | TensorFlow, Keras, CNNs |
| [13 — NLP](./13-nlp/) | Text processing, search, recommendation systems |
| [14 — Computer Vision](./14-computer-vision/) | OpenCV, face detection |
| [15 — Generative AI](./15-generative-ai/) | Transformers, generative models |
| [16 — Bioinformatics](./16-bioinformatics/) | Protein sequences, genome comparison |
| [17 — Streamlit](./17-streamlit/) | Deploying Python apps |
| [Cheatsheets](./cheatsheets/) | Quick-reference cards per topic |
| [Resources](./resources/) | Course links, mapping, external refs |

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/triplom/python_learning.git
cd python_learning
```

### 2. Set up Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # install when file is present
```

### 3. Start the MySQL lab (for module 08)

```bash
cd 08-mysql
docker compose up -d
```

### 4. Pick your starting point

```
Phase 1  →  Basics + Control Flow + Data Structures (Modules 01–03)
Phase 2  →  Functions + OOP + Advanced Python (Modules 04–07)
Phase 3  →  MySQL + Data Visualization (Modules 08–09)
Phase 4  →  Data Science + ML + Deep Learning (Modules 10–12)
Phase 5  →  NLP + Computer Vision + Generative AI (Modules 13–15)
Phase 6  →  Bioinformatics + Deployment (Modules 16–17)
```

→ See the full [Study Plan](./study-plan/README.md)

---

## Source Courses

| # | Course | Instructor | Language | Hours |
|---|--------|-----------|----------|-------|
| 1 | [Python & MySQL](https://www.udemy.com/course/python-mysql/) | Alfahelix Treinamentos | PT-BR | 6h18m |
| 2 | [Aprenda Programação Python para Iniciantes](https://www.udemy.com/course/python-iniciantes-programacao/) | Andre Iacono | PT-BR | 1h55m |
| 3 | [Python para Bioinformática](https://www.udemy.com/course/python_para_bioinformatica/) | — | PT-BR | — |
| 4 | [Python Do Zero a IA 2026](https://www.udemy.com/course/programacao-python-do-basico-ao-avancado/) | Andre Iacono | PT-BR | 34h |
| 5 | [IA — Sistemas de Recomendação em Python](https://www.udemy.com/course/inteligencia-artificial-sistemas-de-recomendacao-em-python/) | — | PT-BR | — |
| 6 | [IA — Buscas em Textos com Python](https://www.udemy.com/course/inteligencia-artificial-buscas-em-textos-com-python/) | — | PT-BR | — |
| 7 | [Detecção de Faces com Python e OpenCV](https://www.udemy.com/course/deteccao-de-faces-com-python-e-opencv/) | — | PT-BR | — |
| 8 | [GeeksForGeeks — Python OOP Concepts](https://www.geeksforgeeks.org/python-oops-concepts/) | GeeksForGeeks | English | — |
| 9 | LinkedIn Learning — Descubra o Python | — | PT-BR | — |

→ Full mapping: [Resources](./resources/README.md)

---

## Module Overview

### Phase 1 — Foundations

```
01-basics/          Variables, types, strings, numbers, user input
02-control-flow/    if/elif/else, for, while, break, continue
03-data-structures/ Lists, dicts, tuples, sets — creation, mutation, iteration
```

### Phase 2 — Intermediate Python

```
04-functions/       def, return, *args, **kwargs, lambda, map, filter, reduce, zip
05-oop/             Classes, __init__, self, inheritance, polymorphism, encapsulation, abstraction
06-files-exceptions/ open(), read/write, with, try/except/finally, custom exceptions
07-advanced-python/  List comprehension, dict comprehension, enumerate, zip, generators
```

### Phase 3 — Data & Databases

```
08-mysql/           mysql-connector-python, CRUD, joins, foreign keys, Docker MySQL
09-data-visualization/ Matplotlib: line, bar, scatter, boxplot, subplots, saving figures
```

### Phase 4 — Data Science & AI

```
10-data-science/    NumPy arrays, Pandas DataFrames, data cleaning
11-machine-learning/ Scikit-learn: regression, classification, clustering, evaluation
12-deep-learning/   TensorFlow/Keras, CNNs, training loops, model saving
```

### Phase 5 — Specialized AI

```
13-nlp/             Text preprocessing, TF-IDF, text search, recommendation systems
14-computer-vision/ OpenCV basics, Haar cascades, face detection, video capture
15-generative-ai/   Transformers, HuggingFace pipeline, text generation
```

### Phase 6 — Applied

```
16-bioinformatics/  FASTA parsing, protein sequences, GC content, genome comparison
17-streamlit/       Building and deploying interactive Python web apps
```

---

## Cheatsheets

| Topic | File |
|-------|------|
| Python Basics | [cheatsheets/python-basics.md](./cheatsheets/python-basics.md) |
| OOP | [cheatsheets/oop.md](./cheatsheets/oop.md) |
| MySQL | [cheatsheets/mysql.md](./cheatsheets/mysql.md) |
| Matplotlib | [cheatsheets/matplotlib.md](./cheatsheets/matplotlib.md) |
| NumPy & Pandas | [cheatsheets/numpy-pandas.md](./cheatsheets/numpy-pandas.md) |
| Scikit-learn | [cheatsheets/scikit-learn.md](./cheatsheets/scikit-learn.md) |
| OpenCV | [cheatsheets/opencv.md](./cheatsheets/opencv.md) |

---

## Related Projects

This repo sits at the centre of the learning ecosystem — its skills feed directly into several other projects.

| Project | Relationship | Relevant Modules |
|---------|-------------|-----------------|
| [machine-learning-lab](https://github.com/triplom/machine-learning-lab) | **Direct continuation** — deeper ML/DL curriculum built on top of this repo's Modules 10–13 | 10-data-science, 11-machine-learning, 12-deep-learning, 13-nlp |
| [kali-hacking-lab](https://github.com/triplom/kali-hacking-lab) | **Month 8 (Python for Hacking)** uses Python scripting skills from this repo: socket programming, Scapy, web automation, wireless tools | 04-functions, 05-oop, 07-advanced-python |
| [LearningGamification](https://github.com/triplom/LearningGamification) | DAML project — ML/data-science concepts (scoring, recommendations) can extend the gamification engine | 11-machine-learning, 13-nlp |
| [lpic3-study-lab](https://github.com/triplom/lpic3-study-lab) | LPIC-OT 701 DevOps track uses Python scripting and container automation | 04-functions, 07-advanced-python |

---

## License

MIT © 2026 [@triplom](https://github.com/triplom)
