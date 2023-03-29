import streamlit as st
import pandas as pd

expander1 = st.expander("セクション1")
with expander1:
    st.write("セクション1の内容をここに書く")

expander2 = st.expander("セクション2")
with expander2:
    st.write("セクション2の内容をここに書く")

expander3 = st.expander("セクション3")
with expander3:
    st.write("セクション3の内容をここに書く")


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "San Francisco", "Los Angeles"],
}

df = pd.DataFrame(data)

with st.container():
    st.write("フィルタリング前のデータフレーム:")
    st.write(df)

    min_age = st.slider("最低年齢を選択:", 18, 50, 18)

    filtered_df = df[df["Age"] >= min_age]

    st.write("フィルタリング後のデータフレーム:")
    st.write(filtered_df)

