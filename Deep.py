import streamlit as st

st.title("Hello, Streamlit!")

st.write("Welcome to your first Streamlit app!")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You picked: {number}")
