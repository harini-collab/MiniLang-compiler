from ast_nodes import *

class SemanticAnalyzer:
    def __init__(self):
        self.symbols = set()
        self.warnings = []

    def analyze(self, statements):
        for stmt in statements:
            self.visit(stmt)
        for w in self.warnings:
            print("Warning:", w)

    def visit(self, node):
        if isinstance(node, LetNode):
            if node.name in self.symbols:
                self.warnings.append(f"Variable '{node.name}' redefined")
            self.visit(node.expr)
            self.symbols.add(node.name)

        elif isinstance(node, PrintNode):
            self.visit(node.expr)

        elif isinstance(node, VariableNode):
            if node.name not in self.symbols:
                self.warnings.append(
                    f"Variable '{node.name}' used before definition"
                )

        elif isinstance(node, BinaryOpNode):
            self.visit(node.left)
            self.visit(node.right)
