from bs4 import BeautifulSoup

text = '<div> Please let me know your availability on weekdays, and we can schedule another 1-hour call at a convenient time for you.</div>'

cleaned_text = BeautifulSoup(text, 'html.parser').get_text()

                   

print(cleaned_text)