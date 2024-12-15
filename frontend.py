import streamlit as st
import requests
import json
from langchain_groq import ChatGroq
st.set_page_config(page_title="LAM Question Paper Assistant", page_icon="📝", layout="wide")
st.title("LAM Question Paper Assistant")

st.subheader("I will give you the Question paper for you...")

question = st.text_area("Enter your question here:", height=100)


if st.button("Generate Question Paper"):
    if question :
            st.subheader("Genereated Question is:")
            st.text(question)
            url = "http://127.0.0.1:8000/create_user/"
            input = {"data": question}  
            headers = {
                "Content-Type": "application/json"
             }

            response = requests.post(url=url, data=json.dumps(input), headers=headers)
            data=response.json()
            
            print(response.json()) 
            st.success(data['msg1'])
    else:
            st.error("Please enter a question and subject.")