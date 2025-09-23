import streamlit as st

# Set the title of the app
st.title("My First Streamlit App")

# Add a text input widget
user_input = st.text_input("Enter your name:")

# Add a button widget
if st.button('Say Hello'):
    if user_input:
        st.write(f"Hello, {user_input}!")
    else:
        st.write("Hello, stranger!")
    
# Add a slider to adjust a number
slider_value = st.slider("Select a number", min_value=0, max_value=100, step=1)
st.write(f"The selected number is {slider_value}")

# Display a simple chart (example with a line chart)
import pandas as pd
import numpy as np

# Create some data for the chart
data = pd.DataFrame({
    'x': np.arange(0, 100),
    'y': np.random.randn(100).cumsum()
})

# Display the chart
st.line_chart(data)

