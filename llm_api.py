import openai
from api_key import chat_gpt_api_key

openai.api_key = chat_gpt_api_key

prompt = '''create {no_of_ques} short {difficulty_level} mcq using the following and give the correct answer of each mcq\n\n{content}'''


def format_response(input_str):
    # print(input_str)
    try:
        questions = input_str.split("\n\n")
        result = []

        for question in questions:
            q_data = question.split("\n")
            q = q_data[0]
            options = q_data[1:-1]
            answer = q_data[-1].split(": ")[1]

            question_dict = {
                "question": q,
                "options": options,
                "answer": answer
            }

            result.append(question_dict)

        return {"result": True, "response": result}

    except:
        
        return {"result": False, "response": "Please add more content"}


def generate_mcq(no_ques, content, difficulty_level):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": '''create 5 short mcq using the following and give the correct answer of each mcq\n\nGit is a distributed version control system that revolutionized the way developers collaborate and manage their code. Created by Linus Torvalds in 2005, Git provides a robust and efficient platform for tracking changes to source code during software development. It allows multiple developers to work on the same project simultaneously, ensuring smooth collaboration by merging their changes seamlessly. Git's decentralized nature enables developers to work offline and synchronize their code later, enhancing productivity and flexibility. With its easy branching and merging capabilities, Git empowers developers to experiment and iterate freely, making it a fundamental tool for modern software development and fostering an open-source community that thrives on collective innovation.'''},
            {"role": "assistant", "content": '''1. What is Git primarily used for?\na) Managing software projects\nb) Tracking changes in source code\nc) Hosting websites\nd) Running virtual machines\nCorrect answer: b) Tracking changes in source code\n\n2. Who is the creator of Git?\na) Steve Jobs\nb) Bill Gates\nc) Linus Torvalds\nd) Mark Zuckerberg\nCorrect answer: c) Linus Torvalds\n\n3. What does Git's decentralized nature allow developers to do?\na) Work offline and synchronize code later\nb) Collaborate with designers\nc) Compile code faster\nd) Access remote servers\nCorrect answer: a) Work offline and synchronize code later\n\n4. How does Git facilitate collaboration among developers?\na) By providing a central server to host code\nb) By restricting access to the codebase\nc) By merging changes seamlessly from multiple developers\nd) By imposing strict branching rules\nCorrect answer: c) By merging changes seamlessly from multiple developers\n\n5. Why is Git considered a fundamental tool for modern software development?\na) It has a user-friendly interface.\nb) It was created by Linus Torvalds.\nc) It fosters an open-source community.\nd) It enables easy branching and merging.\nCorrect answer: d) It enables easy branching and merging.'''},
            {"role": "user", "content": prompt.format(
                no_of_ques=no_ques, content=content, difficulty_level=difficulty_level)}
        ]
    )

    return format_response(response["choices"][0]["message"]["content"])


# print(generate_mcq(3, '''Khaled Hosseini, born on March 4, 1965, is an acclaimed Afghan-American novelist, physician, and humanitarian. He rose to international literary fame with his debut novel, "The Kite Runner," published in 2003. The book explores themes of friendship, betrayal, redemption, and the impact of war on individuals and society. Hosseini's writing style is known for its poignant storytelling, vivid characters, and emotional depth, which have resonated with readers worldwide. Beyond his literary accomplishments, Hosseini is also dedicated to charitable work and serves as a Goodwill Envoy for the United Nations High Commissioner for Refugees. His subsequent novels, including "A Thousand Splendid Suns" and "And the Mountains Echoed," further solidified his reputation as a masterful storyteller and a voice for the voiceless, shedding light on the complexities of Afghanistan's history and culture. Through his writing and philanthropy, Khaled Hosseini continues to leave a lasting impact on both the literary world and the lives of those in need.'''))
