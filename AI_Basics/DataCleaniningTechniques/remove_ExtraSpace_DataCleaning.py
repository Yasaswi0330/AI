import re
text = '     hi       im            yasaswi   '

cleaned_text = re.sub(r'\s+',' ',text)

print(cleaned_text)