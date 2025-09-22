import streamlit as st
st.title("🚀 My First Streamlit App")
name = st.text_input("Enter your name:")
number = st.slider("Choose a number:", 1, 100, 25)
if st.button("Submit"):
    st.success(f"Hello {name}, you selected number {number}!")
    st.write(f"The square of {number} is **{number**2}**")
    st.balloons()
st.subheader("Random Chart Example")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(df)
