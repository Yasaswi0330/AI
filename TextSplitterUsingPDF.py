from langchain_community.document loaders import PyPDFLoader

loader = PyPDFLoader('Leave-and-Holiday-Policy.pdf')
docs = loader. load_and_split()

all_chunks = [doc.page_content for doc in docs] # extract text

for i, chunk in enumerate[Any](all_chunks, start=1):
    print(f"Chunk {i}:\n{chunk}\n{'-'*50}")