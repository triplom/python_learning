# Streamlit App Examples
# Course 4 §Streamlit section
# pip install streamlit pandas matplotlib scikit-learn
# Run: streamlit run hello_streamlit.py

import streamlit as st
import pandas as pd
import numpy as np

# ═══════════════════════════════════════
#  BASIC STREAMLIT ELEMENTS
# ═══════════════════════════════════════

st.title("Python Learning Lab — Streamlit Demo")
st.markdown("---")

# ─── Text elements ────────────────────────────────────────────────────────────
st.header("1. Text Elements")
st.write("st.write() handles almost anything: text, dataframes, charts, markdown.")
st.text("Fixed-width text using st.text()")
st.markdown("**Bold**, *italic*, `code`, [links](https://python.org)")
st.caption("This is a caption — smaller grey text")
st.code("print('Hello, Streamlit!')", language="python")

# ─── Widgets ──────────────────────────────────────────────────────────────────
st.header("2. Widgets")

name = st.text_input("Your name:", value="Alice")
age = st.slider("Your age:", min_value=1, max_value=120, value=25)
city = st.selectbox("Your city:", ["São Paulo", "Rio de Janeiro", "Curitiba", "Other"])
agree = st.checkbox("I agree to the terms")

if st.button("Submit"):
    if agree:
        st.success(f"Hello, {name}! You are {age} years old from {city}.")
    else:
        st.warning("Please accept the terms.")

# ─── Data display ─────────────────────────────────────────────────────────────
st.header("3. DataFrames and Charts")

# Sample dataset
rng = np.random.default_rng(42)
df = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales_2025": rng.integers(10000, 20000, 6).tolist(),
        "Sales_2026": rng.integers(12000, 25000, 6).tolist(),
    }
)

st.dataframe(df)
st.line_chart(df.set_index("Month"))
st.bar_chart(df.set_index("Month"))

# ─── Columns layout ───────────────────────────────────────────────────────────
st.header("4. Layout — Columns")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales 2025", f"R${df['Sales_2025'].sum():,}", delta="+12%")
with col2:
    st.metric("Total Sales 2026", f"R${df['Sales_2026'].sum():,}", delta="+18%")
with col3:
    st.metric("Best Month", df.loc[df["Sales_2026"].idxmax(), "Month"])

# ─── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.header("Filters")
selected_cols = st.sidebar.multiselect(
    "Show columns:", df.columns.tolist(), default=df.columns.tolist()
)
st.sidebar.write("Filtered data:")
st.sidebar.dataframe(df[selected_cols])

# ─── Expander ─────────────────────────────────────────────────────────────────
with st.expander("Show raw data"):
    st.write(df)

# ─── File upload ──────────────────────────────────────────────────────────────
st.header("5. File Upload")
uploaded = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded:
    user_df = pd.read_csv(uploaded)
    st.write(f"Loaded {len(user_df)} rows × {len(user_df.columns)} columns")
    st.dataframe(user_df.head(10))
    st.bar_chart(user_df.select_dtypes(include="number").head(20))

st.info("This is the base demo. See ml_dashboard.py for the ML dashboard app.")
