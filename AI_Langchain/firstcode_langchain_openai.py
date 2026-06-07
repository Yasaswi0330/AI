# # Required packages :
# langchain
# langchain-openai
# openai
# python-dotenv
# C:/Users/name/AppData/Local/Programs/Python/Python313/python.exe -m pip install langchain-openai
# pip install dotenv

from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9,
    api_key=os.getenv("OPENAI_API_KEY")
)

#  Invoke  function

response = llm.invoke("What is the capital of India?")

print(response.content)

#  Stream function                                        keep only 1 either invoke or chunk

for chunk in llm.Stream("What is the capital of India?"):
    print(chunk.content, end='', flush=True)

# batch() 

prompts = [
"Write a motivational quote for students to encourage learning.",
"Explain the importance of time management in simple words.",
"Give 5 practical tips for staying productive while working from home."
]
responses = llm.batch(prompts)

for index, response in enumerate[Any] (responses, start=1):   # enumerate() is used when you need both the index and the value.
    print(f"Iteration: {index}")
    print('-'* 50)
    print(f"{response.content}")



"""
Same code if we want to connect with GEMINI 
https://aistudio.google.com/api-keys  and Generate a key 

store the key in .env file

install this package - langchain-google-genai  - pip install -u langchain-google-genai

refer the code in firstcode_langchain_gemini.py
"""

