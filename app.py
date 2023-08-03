import streamlit as st
from llm_api import generate_mcq

st.title("Q-Easy")
 
number_of_question = st.slider("Pick number of question to be created", 1, 5)
content = st.text_input("Enter content")

if st.button("Generate MCQ") :
    mcqs = generate_mcq(number_of_question, content)
    
    for mcq in mcqs : 
        st.write(mcq['question'])
        for option in mcq["options"] :
            st.write(option)
        st.write(mcq['answer'])
        
        st.divider()