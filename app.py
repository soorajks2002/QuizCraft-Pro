import streamlit as st
from llm_api import generate_mcq

st.title("Q-Easy")

c1, c2 = st.columns(2)
number_of_question = c1.slider("Pick number of question to be created", 1, 5)
difficulty_level = c2.selectbox("Select Difficulty Level", [
                                "Easy", "Medium", "Hard"])
content = st.text_area("Enter content", height=200)

if st.button("Generate MCQ"):
    st.divider()
    response = generate_mcq(number_of_question, content, difficulty_level)
    
    if response["result"] :
        mcqs = response["response"]
        for mcq in mcqs:
            st.markdown("### {question}".format(question=mcq['question']))
            for option in mcq["options"]:
                if option == mcq['answer']:
                    st.success(option)
                else:
                    st.markdown("###### {question}".format(question=option))
            st.divider()

    else :
        st.error(response["response"])