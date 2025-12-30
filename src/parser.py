from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, symbol):
        if self.current() and self.current()[1] == symbol:
            self.pos += 1
        else:
            print(f"Warning: Expected '{symbol}', inserting default")
    
    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            if self.current()[1] == ";":
                self.pos += 1
                continue
            statements.append(self.statement())
        return statements

    def statement(self):
        tok = self.current()

        if tok[1] == "LET":
            self.pos += 1
            name = self.current()[1]
            self.pos += 1
            self.eat("=")
            expr = self.expr()
            if self.current() and self.current()[1] == ";":
                self.pos += 1
            return LetNode(name, expr)

        if tok[1] == "PRINT":
            self.pos += 1
            expr = self.expr()
            if self.current() and self.current()[1] == ";":
                self.pos += 1
            return PrintNode(expr)

        print("Warning: Invalid statement skipped")
        self.pos += 1
        return PrintNode(NumberNode(0))

    def expr(self):
        node = self.term()
        while self.current() and self.current()[1] in ("+", "-"):
            op = self.current()[1]
            self.pos += 1
            node = BinaryOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current() and self.current()[1] in ("*", "/"):
            op = self.current()[1]
            self.pos += 1
            node = BinaryOpNode(node, op, self.factor())
        return node

    def factor(self):
        tok = self.current()

        if tok is None:
            print("Warning: Missing operand, using 0")
            return NumberNode(0)

        if tok[0] == "NUMBER":
            self.pos += 1
            return NumberNode(tok[1])

        if tok[0] == "IDENT":
            self.pos += 1
            return VariableNode(tok[1])

        # INVALID FACTOR 
        print(f"Warning: Invalid factor '{tok[1]}', using 0")
        self.pos += 1
        return NumberNode(0)

