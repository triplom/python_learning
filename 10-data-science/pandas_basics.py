# Pandas Basics
# Course 4 §Data Science section

import pandas as pd
import numpy as np

# ═══════════════════════════════════════
#  SERIES
# ═══════════════════════════════════════
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
print(s["b"])  # 20
print(s[s > 15])  # filter

# ═══════════════════════════════════════
#  DATAFRAME CREATION
# ═══════════════════════════════════════
data = {
    "name": ["Alice", "Bob", "Carol", "David", "Eva"],
    "age": [28, 35, 22, 41, 30],
    "city": ["São Paulo", "Rio de Janeiro", "Curitiba", "São Paulo", "Belo Horizonte"],
    "salary": [85000, 95000, 65000, 120000, 78000],
    "dept": ["Engineering", "Marketing", "Engineering", "Management", "Design"],
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print(df.shape)  # (5, 5)
print(df.info())

# ═══════════════════════════════════════
#  INSPECTION
# ═══════════════════════════════════════
print(df.head(3))  # first 3 rows
print(df.tail(2))  # last 2 rows
print(df.describe())  # stats for numeric columns

# ═══════════════════════════════════════
#  SELECTION
# ═══════════════════════════════════════
# Column
print(df["name"])
print(df[["name", "salary"]])

# Row by index label (loc) or position (iloc)
print(df.loc[0])  # first row by label
print(df.iloc[1:3])  # rows 1 and 2 by position
print(df.loc[df["city"] == "São Paulo"])

# Boolean filtering
high_earners = df[df["salary"] > 80000]
print(high_earners[["name", "salary"]])

sp_eng = df[(df["city"] == "São Paulo") & (df["dept"] == "Engineering")]
print(sp_eng)

# ═══════════════════════════════════════
#  MUTATIONS
# ═══════════════════════════════════════
df["salary_k"] = df["salary"] / 1000  # new column
df["senior"] = df["age"] >= 35  # boolean column

# Apply a function
df["name_upper"] = df["name"].str.upper()

# map / apply
df["dept_short"] = df["dept"].map(
    {
        "Engineering": "ENG",
        "Marketing": "MKT",
        "Management": "MGT",
        "Design": "DES",
    }
)

print(df.head())

# ═══════════════════════════════════════
#  GROUP BY AND AGGREGATION
# ═══════════════════════════════════════
dept_stats = df.groupby("dept")["salary"].agg(["mean", "min", "max", "count"])
print(dept_stats)

city_avg = df.groupby("city")["salary"].mean().sort_values(ascending=False)
print(city_avg)

# ═══════════════════════════════════════
#  SORTING
# ═══════════════════════════════════════
print(df.sort_values("salary", ascending=False)[["name", "salary"]])

# ═══════════════════════════════════════
#  CSV I/O
# ═══════════════════════════════════════
df.to_csv("employees.csv", index=False)
df2 = pd.read_csv("employees.csv")
print(df2.head(2))

# ═══════════════════════════════════════
#  MISSING DATA
# ═══════════════════════════════════════
df_missing = pd.DataFrame(
    {
        "a": [1, np.nan, 3],
        "b": [4, 5, np.nan],
        "c": [np.nan, np.nan, 9],
    }
)
print(df_missing.isna().sum())  # count NaN per column
print(df_missing.dropna())  # drop rows with any NaN
print(df_missing.fillna(0))  # fill NaN with 0
print(df_missing.fillna(df_missing.mean()))  # fill with column mean

import os

os.remove("employees.csv")  # cleanup

# --- LAB EXERCISES ---
# 1. Download the Titanic dataset from Kaggle or use seaborn's built-in:
#    import seaborn as sns; df = sns.load_dataset('titanic')
#    Find: survival rate by sex, mean age by class, top 5 most common embarkation ports.
# 2. Read a CSV of your choice. Clean it: drop duplicates, fill missing values,
#    rename columns, and export a cleaned version.
# 3. Group a dataset by two columns simultaneously and compute multiple aggregates.
