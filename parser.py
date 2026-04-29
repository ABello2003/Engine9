from ast_nodes import LetNode, PrintNode, FuncCallNode

def parse(tokens):
    ast = []
    i = 0

    while i < len(tokens):
        if tokens[i] == "let":
            name = tokens[i+1]
            expr = tokens[i+3:]
            ast.append(LetNode(name, expr))
            break

        elif tokens[i] == "print":
            ast.append(PrintNode(tokens[i+1]))
            break

        i += 1

    return ast
