import streamlit as st
import requests

API_URL = "http://localhost:8000/query"

st.title("Responsible AI Assistant")

query = st.text_input("Ask your question")

if st.button("Submit"):

    response = requests.post(
        API_URL,
        json={"query": query}
    )

    result = response.json()

    st.write("### Response")
    st.write(result["response"])

    st.write("Status:", result["status"])