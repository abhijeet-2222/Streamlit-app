
import streamlit as st
import pandas as pd

st.title("File Upload Demo 📂")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("Here is your uploaded data:")
    st.dataframe(df)
else:
    st.write("Please upload a file to view it.")

