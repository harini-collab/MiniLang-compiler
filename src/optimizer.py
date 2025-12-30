from ast_nodes import *

def optimize(node):
    if isinstance(node, BinaryOpNode):
        left = optimize(node.left)
        right = optimize(node.right)

        if isinstance(left, NumberNode) and isinstance(right, NumberNode):
            if node.op == "+": return NumberNode(left.value + right.value)
            if node.op == "-": return NumberNode(left.value - right.value)
            if node.op == "*": return NumberNode(left.value * right.value)

        return BinaryOpNode(left, node.op, right)

    if isinstance(node, LetNode):
        return LetNode(node.name, optimize(node.expr))

    if isinstance(node, PrintNode):
        return PrintNode(optimize(node.expr))

    return node

