# Machine Learning with Scikit-learn
# Course 4 §ML section

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    mean_squared_error,
    r2_score,
)
from sklearn.pipeline import Pipeline
import warnings

warnings.filterwarnings("ignore")

# ═══════════════════════════════════════
#  1. LINEAR REGRESSION
# ═══════════════════════════════════════
print("=" * 50)
print("LINEAR REGRESSION")
print("=" * 50)

rng = np.random.default_rng(42)
X = rng.uniform(20, 100, (200, 1))  # study hours (synthetic)
y = 2.5 * X.ravel() + rng.normal(0, 10, 200)  # score with noise

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Coefficient: {model.coef_[0]:.4f}")
print(f"Intercept:   {model.intercept_:.4f}")
print(f"R² Score:    {r2_score(y_test, y_pred):.4f}")
print(f"RMSE:        {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# ═══════════════════════════════════════
#  2. LOGISTIC REGRESSION
# ═══════════════════════════════════════
print("\n" + "=" * 50)
print("LOGISTIC REGRESSION — Iris Dataset")
print("=" * 50)

from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

pipeline = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=200)),
    ]
)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ═══════════════════════════════════════
#  3. RANDOM FOREST CLASSIFIER
# ═══════════════════════════════════════
print("=" * 50)
print("RANDOM FOREST")
print("=" * 50)

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Feature importances
importances = pd.Series(rf.feature_importances_, index=cancer.feature_names)
print("\nTop 5 features:")
print(importances.sort_values(ascending=False).head())

# Cross-validation
cv_scores = cross_val_score(rf, cancer.data, cancer.target, cv=5)
print(f"\nCross-val (5-fold): {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# ═══════════════════════════════════════
#  4. K-MEANS CLUSTERING
# ═══════════════════════════════════════
print("\n" + "=" * 50)
print("K-MEANS CLUSTERING")
print("=" * 50)

# Synthetic 2D data with 3 natural clusters
from sklearn.datasets import make_blobs

X_blobs, y_true = make_blobs(n_samples=300, centers=3, random_state=42)

# Elbow method — find optimal k
inertias = []
for k in range(1, 9):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_blobs)
    inertias.append(km.inertia_)
print("Inertias for k=1..8:", [f"{v:.0f}" for v in inertias])

# Fit with best k=3
km = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = km.fit_predict(X_blobs)
print(f"Cluster centers:\n{km.cluster_centers_}")

# LAB EXERCISES
# 1. Load the Titanic dataset (seaborn or CSV). Predict survival using
#    LogisticRegression + RandomForest. Compare accuracy.
# 2. Use GridSearchCV to tune RandomForest hyperparameters (n_estimators, max_depth).
# 3. Apply KMeans to the Iris dataset features (ignore labels).
#    Compare resulting clusters to the actual species.
