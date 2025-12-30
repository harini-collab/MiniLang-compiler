class NumberNode:
    def __init__(self, value):
        self.value = value

class VariableNode:
    def __init__(self, name):
        self.name = name

class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class LetNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class PrintNode:
    def __init__(self, expr):
        self.expr = expr
