from langchain text splitters import RecursiveCharacterTextSplitter

txt = """
        LangChain is an open-source framework designed to build applications powered by large language models
        (LLMs). It enables developers to connect LLMs with external data sources, APIs, and databases to create
        intelligent, context-aware systems. LangChain is widely used for building chatbots, AI assistants, and
        Retrieval-Augmented Generation (RAG) applications. It supports integration with popular models such as
        Anthropic, and open-source LLMs. The framework provides tools for prompt management, chaining multiple
        handling structured outputs. It includes document loaders for PDFs, text files, and web content, along
        to process large documents efficiently. LangChain also integrates with vector databases like FAISS and
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 40,
    separators=[""]        # split at character level
    )

chunks = splitter.split_text(txt)

for index, chunk in enumerate[Any] (chunks):
    print(f"Chunk {index + 1}: \n {chunk}")