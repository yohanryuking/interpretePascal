class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, declarations, statements):
        self.declarations = declarations
        self.statements = statements

class VariableDeclarationNode(ASTNode):
    def __init__(self, var_type, var_name):
        self.var_type = var_type
        self.var_name = var_name

class AssignmentNode(ASTNode):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

class IfStatementNode(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileStatementNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ExpressionNode(ASTNode):
    pass

class BinaryOperationNode(ExpressionNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOperationNode(ExpressionNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class LiteralNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

class VariableNode(ExpressionNode):
    def __init__(self, name):
        self.name = name

class SetNode(ExpressionNode):
    def __init__(self, elements):
        self.elements = elements

class BooleanNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

class CharNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

class StringNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

class InNode(ExpressionNode):
    def __init__(self, element, set_expression):
        self.element = element
        self.set_expression = set_expression

class ConditionalExpressionNode(ExpressionNode):
    def __init__(self, condition, true_expr, false_expr):
        self.condition = condition
        self.true_expr = true_expr
        self.false_expr = false_expr