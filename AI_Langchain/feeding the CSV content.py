from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import ChatGoogleGenerativeAI

loader = CSVLoader("/workspaces/AI/AI_Basics/DataCleaniningTechniques/people100.csv")

question = input("What do you want to know about the data? ")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="give your google api key here",
)

docs = loader.load()

prompt = f"""
Data:
{docs}

Question:
{question}
"""

response = llm.invoke(prompt)

print(response.content)