from ast_nodes import *

def gen_expr(node, out):
    if isinstance(node, NumberNode):
        out.append(f"PUSH {node.value}")
    elif isinstance(node, VariableNode):
        out.append(f"LOAD {node.name}")
    elif isinstance(node, BinaryOpNode):
        gen_expr(node.left, out)
        gen_expr(node.right, out)
        out.append(node.op)

def generate(statements):
    out = []
    for s in statements:
        if isinstance(s, LetNode):
            gen_expr(s.expr, out)
            out.append(f"STORE {s.name}")
        elif isinstance(s, PrintNode):
            gen_expr(s.expr, out)
            out.append("PRINT")
    return "\n".join(out)
