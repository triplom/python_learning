# NumPy & Pandas Cheatsheet

## NumPy

### Array Creation

```python
import numpy as np

np.array([1, 2, 3])              # from list
np.zeros((3, 4))                 # 3×4 zeros
np.ones((2, 3))                  # 2×3 ones
np.eye(3)                        # 3×3 identity
np.arange(0, 10, 2)             # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)            # 5 values 0–1 inclusive
np.random.default_rng(42).random((3,3))  # random floats
```

### Array Operations

```python
a.shape        # (3, 4) — dimensions
a.dtype        # float64
a.ndim         # number of dimensions
a.size         # total elements

a.reshape(2, 6)     # new shape (same data)
a.flatten()         # 1D copy
a.T                 # transpose

a + b    a - b    a * b    a / b    a ** 2   # element-wise
np.dot(a, b)        # dot product / matrix multiply
np.matmul(a, b)     # matrix multiply (preferred)

a[0]               # first row
a[:, 1]            # second column
a[1:3, 0:2]        # submatrix
a[a > 0]           # boolean indexing
```

### Math & Statistics

```python
np.sum(a)           np.sum(a, axis=0)   # column sums
np.mean(a)          np.std(a)
np.min(a)           np.max(a)
np.percentile(a, 75)
np.sqrt(a)          np.log(a)           np.exp(a)
np.sort(a)          np.argsort(a)       # indices that would sort
np.unique(a)
```

---

## Pandas

### Creation

```python
import pandas as pd

s = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame({"col1": [1,2,3], "col2": ["a","b","c"]})
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")
```

### Inspection

```python
df.head(5)      df.tail(3)
df.shape        # (rows, cols)
df.dtypes
df.info()
df.describe()   # stats for numeric cols
df.columns      df.index
```

### Selection

```python
df["col"]                         # Series
df[["col1", "col2"]]             # DataFrame
df.loc[0]                         # row by label
df.iloc[1:3]                      # rows by position
df.loc[df["age"] > 30]           # boolean filter
df[(df["city"] == "SP") & (df["age"] > 25)]  # multiple conditions
df.at[0, "name"]                  # scalar by label
df.iat[0, 1]                      # scalar by position
```

### Mutation

```python
df["new_col"] = df["price"] * 1.1
df["flag"] = df["score"].apply(lambda x: "pass" if x >= 60 else "fail")
df.rename(columns={"old": "new"}, inplace=True)
df.drop(columns=["col"])
df.drop(index=[0, 2])
df.reset_index(drop=True)
```

### Grouping & Aggregation

```python
df.groupby("dept")["salary"].mean()
df.groupby("dept").agg({"salary": ["mean", "min", "max"], "age": "count"})
df.pivot_table(values="sales", index="month", columns="region", aggfunc="sum")
```

### Cleaning

```python
df.isna().sum()               # NaN count per column
df.dropna()                   # drop rows with any NaN
df.fillna(0)                  # fill NaN with 0
df.fillna(df.mean())          # fill with column mean
df.drop_duplicates()
df["col"].astype(int)         # cast column type
df["date"] = pd.to_datetime(df["date"])
```

### Sorting & Merging

```python
df.sort_values("salary", ascending=False)
df.sort_values(["dept", "salary"])

pd.merge(df1, df2, on="id", how="left")   # SQL-style join
pd.concat([df1, df2], ignore_index=True)   # stack rows
```

### Export

```python
df.to_csv("out.csv", index=False)
df.to_excel("out.xlsx", index=False)
df.to_json("out.json", orient="records")
```
