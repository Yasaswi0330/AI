# langchain
# langchain-openai
# openai
# python-dotenv
# langchain-google-genai
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize the Gemini model
# Common models: 'gemini-1.5-flash' (fast) or 'gemini-1.5-pro' (powerful)
llm = ChatGoogleGenerativeAI(
model="gemini-2.5-flash",
google_api_key=os.getenv("GOOGLE_API_KEY"),
temperature=0.5

)

#  Invoke  function

response = llm.invoke("What is the capital of India?")

print(response.content)

#  Stream function                                        keep only 1 either invoke or chunk

for chunk in llm.Stream("What is the capital of India?"):
    print(chunk.content, end='', flush=True)