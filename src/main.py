from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer
from optimizer import optimize
from codegen_python import generate as pygen
from codegen_stack import generate as stackgen

with open("program.txt") as f:
    code = f.read()

tokens = tokenize(code)
parser = Parser(tokens)
ast = parser.parse()

analyzer = SemanticAnalyzer()
analyzer.analyze(ast)

optimized_ast = [optimize(s) for s in ast]

print(" PYTHON CODE")
print(pygen(optimized_ast))

print("\nSTACK CODE")
print(stackgen(optimized_ast))
