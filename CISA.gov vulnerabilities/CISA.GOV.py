import streamlit as st
import requests

def fetch_cisa_vulnerabilities():
    url = "https://www.cisa.gov/api/vulnerabilities"  # Placeholder URL
    response = requests.get(url)
    data = response.json()
    return data

vulnerabilities = fetch_cisa_vulnerabilities()

st.title("CISA Vulnerabilities")

if vulnerabilities:
    for vulnerability in vulnerabilities:
        st.subheader(vulnerability["title"])  # Placeholder key
        st.text(vulnerability["description"])  # Placeholder key
        st.write("---")
else:
    st.write("No vulnerabilities found.")
