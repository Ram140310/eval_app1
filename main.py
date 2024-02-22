import streamlit as st
import google.generativeai as genai
GOOGLE_API_KEY="AIzaSyB0u9m1csGnS6HAT2O5iU5N0YK-jrAaBPQ"
prompt="""You are a teacher that gave a task to your Data science 
students. You challenged them to create a model on the dataset you 
gave them. Now you need to evaluate the model they built and write a 
review as to how was the model. Now this task has some limitations
1. Students are not allowed to increase the size of data
2. Students are not allowed to use any pre trained models
Score shoud be given on a scale of A to E
The review should be written in this format
Score :
Comments :
 - How was the implemantation
 - Scope of improvement
And the code for model building is given below
code : 
 {}"""
genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel("gemini-pro")
uploaded_file=st.file_uploader("Upload your file",type=["py"],key="upload_file")
def read_file(file):
    with open(file.name, 'wb') as f:
        f.write(file.getbuffer())
    with open(file.name, 'r') as f:
        contents = f.readlines()
    return contents
if st.session_state["upload_file"]:
    contents=read_file(uploaded_file)
    code=contents[8:]
    ip=prompt.format(code)
    responce=model.generate_content(ip)
    tex=[]
    for i in responce:
        tex.append(i.text)
    st.write(" ".join(tex))
