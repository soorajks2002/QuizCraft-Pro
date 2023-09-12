import streamlit as st
from llm_api import generate_mcq

st.set_page_config(page_title="QuizCraft", page_icon="🎓", layout='wide')
input_col, result_col = st.columns(2)

input_col.title("QuizCraft Pro 📝")

input_col.markdown("##### Enter The Content")
content = input_col.text_area("Enter content", height=200, label_visibility='collapsed')
c1, c2 = input_col.columns(2)
number_of_question = c1.slider("Pick number of question to be created", 1, 5)
difficulty_level = c2.selectbox("Select Difficulty Level", [
                                "Easy", "Medium", "Hard"])

if input_col.button("Generate Quiz"):
    if content :
        # st.divider()
        response = generate_mcq(number_of_question, content, difficulty_level)
        
        if response["result"] :
            mcqs = response["response"]
            for mcq in mcqs:
                result_col.markdown("#### {question}".format(question=mcq['question']))
                for option in mcq["options"]:
                    if option == mcq['answer']:
                        result_col.success(option)
                    else:
                        result_col.markdown("###### {question}".format(question=option))
                result_col.divider()
                # result_col.markdown("#####")

        else :
            result_col.error(response["response"])
    else :
        input_col.warning("Please Enter Your Content")