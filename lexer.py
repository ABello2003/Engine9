import re

RESERVED_WORDS = {"let", "print"}
OPERATORS = {"=", "+", "-", "*", "/", "(", ")"}

def analyze_tokens(filename):
    literals = set()
    operators = set()
    variables = set()
    reserved = set()
    line_count = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "" or line.startswith("#"):
                continue

            line_count += 1

            tokens = re.findall(r'\d+\.\d+|\d+|[A-Za-z_][A-Za-z0-9_]*|[=+\-*/()]', line)

            for token in tokens:
                if token in RESERVED_WORDS:
                    reserved.add(token)
                elif token in OPERATORS:
                    operators.add(token)
                elif re.match(r'^\d+(\.\d+)?$', token):
                    literals.add(token)
                else:
                    variables.add(token)

    print("Lines processed:", line_count)
    print("Literals:", literals)
    print("Operators:", operators)
    print("Variables:", variables)
    print("Reserved Words:", reserved)
