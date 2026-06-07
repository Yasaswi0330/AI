import re 

text = 'click here: https://pypi.org/project/beautifulsoup4/'

cleaned_text = re.sub(r'https\S+|www\S+', 'removed link', text)

print(cleaned_text)