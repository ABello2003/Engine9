class LetNode:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

class PrintNode:
    def __init__(self, value):
        self.value = value

class FuncCallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args
