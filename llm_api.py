import openai
from api_key import chat_gpt_api_key

openai.api_key = chat_gpt_api_key

prompt = '''create {no_of_ques} short mcq using the following and give the correct answer of each mcq\n\n{content}'''

# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         {"role": "user", "content": ""},
#         {"role": "assistant", "content": ""},
#         {"role": "user", "content": ""},
#     ]
# )


def create_mcq(no_ques, content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": '''create 5 short mcq using the following and give the correct answer of each mcq\n\nGit is a distributed version control system that revolutionized the way developers collaborate and manage their code. Created by Linus Torvalds in 2005, Git provides a robust and efficient platform for tracking changes to source code during software development. It allows multiple developers to work on the same project simultaneously, ensuring smooth collaboration by merging their changes seamlessly. Git's decentralized nature enables developers to work offline and synchronize their code later, enhancing productivity and flexibility. With its easy branching and merging capabilities, Git empowers developers to experiment and iterate freely, making it a fundamental tool for modern software development and fostering an open-source community that thrives on collective innovation.'''},
            {"role": "assistant", "content": '''1. What is Git primarily used for?\na) Managing software projects\nb) Tracking changes in source code\nc) Hosting websites\nd) Running virtual machines\nCorrect answer: b) Tracking changes in source code\n\n2. Who is the creator of Git?\na) Steve Jobs\nb) Bill Gates\nc) Linus Torvalds\nd) Mark Zuckerberg\nCorrect answer: c) Linus Torvalds\n\n3. What does Git's decentralized nature allow developers to do?\na) Work offline and synchronize code later\nb) Collaborate with designers\nc) Compile code faster\nd) Access remote servers\nCorrect answer: a) Work offline and synchronize code later\n\n4. How does Git facilitate collaboration among developers?\na) By providing a central server to host code\nb) By restricting access to the codebase\nc) By merging changes seamlessly from multiple developers\nd) By imposing strict branching rules\nCorrect answer: c) By merging changes seamlessly from multiple developers\n\n5. Why is Git considered a fundamental tool for modern software development?\na) It has a user-friendly interface.\nb) It was created by Linus Torvalds.\nc) It fosters an open-source community.\nd) It enables easy branching and merging.\nCorrect answer: d) It enables easy branching and merging.'''},
            {"role": "user", "content": prompt.format(
                no_of_ques=no_ques, content=content)}
        ]
    )

    # return format_response(response["choices"][0]["message"])
    return response["choices"][0]["message"]["content"]
