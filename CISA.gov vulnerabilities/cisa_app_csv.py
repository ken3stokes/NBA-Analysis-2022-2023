import streamlit as st
import pandas as pd

# Load data from a local CSV file
def load_data_from_file():
    data = pd.read_csv('cisa_vulnerabilities.csv')
    return data

vulnerabilities = load_data_from_file()

st.title("CISA Vulnerabilities")

if not vulnerabilities.empty:
    for _, row in vulnerabilities.iterrows():
        st.subheader(row["title"])  # Assuming the CSV has a 'title' column
        st.text(row["description"])  # Assuming the CSV has a 'description' column
        st.write("---")
else:
    st.write("No vulnerabilities found.")
