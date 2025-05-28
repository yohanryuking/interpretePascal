class Interpreter:
    def __init__(self, environment):
        self.environment = environment

    def interpret(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    # Visit methods for different AST node types
    def visit_BinaryOperationNode(self, node):
        left = self.interpret(node.left)
        right = self.interpret(node.right)
        if node.operator.type in ('PLUS', 'TokenType.PLUS'):
            return left + right
        elif node.operator.type in ('MINUS', 'TokenType.MINUS'):
            return left - right
        elif node.operator.type in ('MULTIPLY', 'TokenType.MULTIPLY'):
            return left * right
        elif node.operator.type in ('DIVIDE', 'TokenType.DIVIDE'):
            return left / right
        elif node.operator.type in ('POWER', 'TokenType.POWER'):
            return left ** right
        else:
            raise Exception(f'Unknown operator: {node.operator.type}')

    def visit_LiteralNode(self, node):
        return node.value

    def visit_StringNode(self, node):
        return node.value

    def visit_CharNode(self, node):
        return node.value

    def visit_BooleanNode(self, node):
        return node.value

    def visit_SetNode(self, node):
        return set(self.interpret(item) for item in node.elements)

    def visit_VariableNode(self, node):
        return self.environment.get(node.name)

    def visit_AssignmentNode(self, node):
        value = self.interpret(node.expression)
        self.environment.set(node.variable, value)
        return value

    def visit_IfStatementNode(self, node):
        condition = self.interpret(node.condition)
        if condition:
            return self.interpret(node.then_branch)
        elif node.else_branch:
            return self.interpret(node.else_branch)

    def visit_WhileStatementNode(self, node):
        while self.interpret(node.condition):
            self.interpret(node.body)

    def visit_ReadNode(self, node):
        value = input(f'Enter value for {node.variable.name}: ')
        self.environment.set(node.variable.name, value)

    def visit_WriteNode(self, node):
        value = self.interpret(node.value)
        print(value)