# Scikit-learn Cheatsheet

## Workflow

```python
# 1. Import
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Preprocess + model in a Pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    LogisticRegression()),
])

# 4. Train
pipeline.fit(X_train, y_train)

# 5. Evaluate
y_pred = pipeline.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

## Common Models

```python
# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor

# Clustering
from sklearn.cluster import KMeans, DBSCAN

# All follow the same API:
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)   # probabilities (classifiers)
model.score(X_test, y_test)
```

## Preprocessing

```python
from sklearn.preprocessing import (
    StandardScaler,      # mean=0, std=1
    MinMaxScaler,        # scale to [0,1]
    LabelEncoder,        # encode target labels
    OneHotEncoder,       # one-hot for categorical
    OrdinalEncoder,
)

from sklearn.impute import SimpleImputer    # fill missing values

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit+transform on train
X_test_scaled  = scaler.transform(X_test)       # only transform on test
```

## Evaluation

```python
# Classification
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score
)

# Regression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
rmse = mean_squared_error(y_test, y_pred, squared=False)

# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(f"{scores.mean():.4f} ± {scores.std():.4f}")
```

## Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

param_grid = {
    "clf__n_estimators": [50, 100, 200],
    "clf__max_depth":    [None, 5, 10],
}
grid = GridSearchCV(pipeline, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)
```

## Feature Selection & Importance

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

rf = RandomForestClassifier().fit(X_train, y_train)
importances = pd.Series(rf.feature_importances_, index=feature_names)
print(importances.sort_values(ascending=False).head(10))

from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=10).fit(X_train, y_train)
X_selected = selector.transform(X_test)
```

## Saving / Loading Models

```python
import joblib
joblib.dump(model, "model.pkl")
model = joblib.load("model.pkl")
```
