import streamlit as st

st.subheader("User Input")
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

fruit = st.selectbox("Choose a fruit", ["Apple", "Banana", "Orange"])
st.write(f"You chose: {fruit}")