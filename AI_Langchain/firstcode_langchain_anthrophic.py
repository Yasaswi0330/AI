import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

# Initialize the Anthropic model
# Popular models: 'claude-3-5-sonnet-latest', 'claude-3-5-haiku-latest'
llm = ChatAnthropic(
model="claude-3-5-sonnet-latest",
anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
temperature=0.5
)

#  Invoke  function

response = llm.invoke("What is the capital of India?")

print(response.content)

#  Stream function                                        keep only 1 either invoke or chunk

for chunk in llm.Stream("What is the capital of India?"):
    print(chunk.content, end='', flush=True)