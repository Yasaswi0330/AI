#required package  - langchain-core 

import os

from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

template = """
You are a helpful tutor.
Explain the following in simple terms:

Topic: {topic}
"""

prompt = PromptTemplate. from_template(template)

final_prompt = prompt.format(topic='Machine Learning')

llm = ChatOpenAI(
model='gpt-40-mini',
temperature=0.5,
)

response = llm. invoke(final_prompt)
print(response.content)



####  ---- Instruction prompt ------


template ="""
            you are a writing assistance
            follow these rules strictly:

            1. Answer in 3 bullet points
            2. Keep each point under 10 words.
            3. Response should be concise

            Question: {question}
           """
prompt = PromptTemplate.from_template(template) 
final_prompt = prompt.format(question='what is Machine Learning')
response = llm. invoke(final_prompt)
print(response.connect)



# ------------  Chain of thought template  ------------


template = """
Solve this problem step by step, then return the answer.

Problem: {problem}

Step by step reasoning:

        """
prompt = PromptTemplate. from_template(template)

final_prompt = prompt.format(problem = 'What is 25 * 56 + 89')

response = llm.invoke(final_prompt)

print(response.content)



# --------   Tone / Persona Template + Role -------------


template = """
You are a friendly math tutor.
Explain the answer as if teachng a 15 year old student.

Question: {question}
"""

prompt = PromptTemplate. from_template(template)

final_prompt = prompt.format(question = 'What is fraction?')

response = llm. invoke(final_prompt)

print(response.content)



#------------- Task specific template ---------

template = """
Translate the following text to Spanish
Keep the meaning accurate.

Text: {text}
"""

prompt = PromptTemplate. from_template(template)

final_prompt = prompt. format(text = 'What are the benefits of journaling daily?')

response = llm. invoke(final_prompt)

print(response.content)
