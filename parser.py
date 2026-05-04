from ast_nodes import LetNode, PrintNode

def parse_line(line):
    line = line.strip()

    if line == "" or line.startswith("#"):
        return None

    if line.startswith("let "):
        statement = line.replace("let ", "", 1)

        if "=" not in statement:
            raise SyntaxError("Missing = in let statement")

        name, expression = statement.split("=", 1)
        return LetNode(name.strip(), expression.strip())

    if line.startswith("print "):
        value = line.replace("print ", "", 1).strip()
        return PrintNode(value)

    raise SyntaxError(f"Unknown statement: {line}")
