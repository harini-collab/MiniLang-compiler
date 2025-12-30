from ast_nodes import *

def gen_expr(node):
    if isinstance(node, NumberNode):
        return str(node.value)
    if isinstance(node, VariableNode):
        return node.name
    if isinstance(node, BinaryOpNode):
        return f"({gen_expr(node.left)} {node.op} {gen_expr(node.right)})"

def generate(statements):
    out = []
    for s in statements:
        if isinstance(s, LetNode):
            out.append(f"{s.name} = {gen_expr(s.expr)}")
        elif isinstance(s, PrintNode):
            out.append(f"print({gen_expr(s.expr)})")
    return "\n".join(out)
