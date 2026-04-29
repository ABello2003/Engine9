import re

def tokenize(code):
    tokens = re.findall(r'\d+\.\d+|\d+|[A-Za-z_]+|[=+\-*/(),]', code)
    return tokens
