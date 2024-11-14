import re


def convert_dates(text):
    text=re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\1-\2',text)
    return text


with open('abc.txt','r') as f:
    content=f.read()

convert=convert_dates(content)

with open('abc.txt','w') as f:
    f.write(convert)