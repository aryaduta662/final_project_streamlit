import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Sentimen X", layout="wide")

st.title("Final Project Data Mining")
st.write("Analisis Sentimen Media Sosial X")

# ✅ LOAD DATA (NAMA FILE BENAR)
df = pd.read_csv("Dataset_after_preproses_fix.csv")

st.subheader("Dataset Sentimen")
st.dataframe(df)

st.write("Jumlah data:", len(df))

# ✅ KOLOM SENTIMEN YANG BENAR
kolom_sentimen = "final_label"

# pastikan tidak error
df[kolom_sentimen] = df[kolom_sentimen].astype(str)

# hitung distribusi
sentiment_count = df[kolom_sentimen].value_counts()

st.subheader("Distribusi Sentimen")
st.bar_chart(sentiment_count)

# pie chart
fig, ax = plt.subplots()
ax.pie(
    sentiment_count,
    labels=sentiment_count.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.axis("equal")
st.pyplot(fig)

# filter
st.subheader("Filter Data Berdasarkan Sentimen")
selected = st.selectbox(
    "Pilih sentimen:",
    sentiment_count.index
)

st.dataframe(df[df[kolom_sentimen] == selected])
