from bs4 import BeautifulSoup

import re

def clean_text(text):
    text = BeautifulSoup(text,'html.parser').get_text()
    text = re.sub(r'htpp\S+|www\S+','',text)
    text = re.sub(r'[^\x00-\x7f]+','',text)
    text = re.sub(r'[^A-Za-z0-9\s]','',text)
    text = re.sub(r'\s+',' ',text)
    return text

raw_text = """
        <div>
            Hello!!! 😊 Welcome to <b>OpenAI</b>.

            Visit: https://openai.com
            Also check: www.example.com
            Broken URL: htpp://invalid-link.com

            Café naïve résumé 中文 العربية

            Contact us @ support#123!
            Price: $99.99 (50% OFF)

            Multiple     spaces,
            tabs\t\tand
            newlines.


        </div>
"""

clean_text= clean_text(raw_text)

print(clean_text)