# Document Loaders:
# > LLM's works better with structured inputs.
# > Document loaders helps us load data from various external systems into a standard Document format.

# > Each document typically has:

# page_content -> Actual text
# metadata -> Source info (Filename, url)

# Types of Document Loaders
# 1. Text Loader |



## ------ TEXT LOADER ------------##

from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path='sample.txt')

docs = loader. load()

print(docs)

print(docs[0].metadata)

print(docs[0].page_content)


## ------- PDF LOADER ----------- # (pip install pypdf )

# PDF Loader
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Core Python.pdf')

docs = loader. load_and_split()

print(docs)     


## ---------  Web loader - Web Scraping  -------# (pip install beautifulsoup4)

from langchain_community. document_loaders import WebBaseLoader

urls = ['https://en.wikipedia.org/wiki/Narendra_Modi']   # you can give multiple urls on one go sinces its a list.

loader = WebBaseLoader(urls)

docs = loader. load_and_split()

print(docs[0].page_content)


## ------- CSV Loader  ------#
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='students.csv')

docs = loader. load()

print(docs)

### Youtube transcript loader  ------#  (pip install youtube-transcript-api)

from langchain community.document loaders import YoutubeLoader

loader = YoutubeLoader. from_youtube_url('https://www.youtube.com/watch?v=KW6qncswzHw')

docs = loader. load()

print(docs)