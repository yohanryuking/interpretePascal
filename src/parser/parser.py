from .ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        # Start parsing from the program level
        return self.program()

    def program(self):
        # Parse a program structure
        self.expect('PROGRAM')
        identifier = self.expect('IDENTIFIER')
        self.expect('SEMICOLON')
        declarations = self.declarations()
        self.expect('BEGIN')
        statements = self.statements()
        self.expect('END')
        return ProgramNode(identifier, declarations, statements)

    def declarations(self):
        # Parse variable declarations
        declarations = []
        while self.current_token().type == 'VAR':
            self.expect('VAR')
            var_declaration = self.variable_declaration()
            declarations.append(var_declaration)
        return declarations

    def variable_declaration(self):
        # Parse a single variable declaration
        identifier = self.expect('IDENTIFIER')
        self.expect('COLON')
        var_type = self.expect('TYPE')
        self.expect('SEMICOLON')
        return VariableDeclarationNode(identifier, var_type)

    def statements(self):
        # Parse a list of statements
        statements = []
        while self.current_token().type != 'END':
            statement = self.statement()
            statements.append(statement)
        return statements

    def statement(self):
        # Parse a single statement
        if self.current_token().type == 'IDENTIFIER':
            return self.assignment_statement()
        elif self.current_token().type == 'IF':
            return self.if_statement()
        elif self.current_token().type == 'WHILE':
            return self.while_statement()
        else:
            raise SyntaxError("Unexpected token: {}".format(self.current_token()))

    def assignment_statement(self):
        # Parse an assignment statement
        identifier = self.expect('IDENTIFIER')
        self.expect('ASSIGN')
        expression = self.expression()
        self.expect('SEMICOLON')
        return AssignmentNode(identifier, expression)

    def if_statement(self):
        # Parse an if statement
        self.expect('IF')
        condition = self.expression()
        self.expect('THEN')
        true_branch = self.statement()
        false_branch = None
        if self.current_token().type == 'ELSE':
            self.expect('ELSE')
            false_branch = self.statement()
        return IfNode(condition, true_branch, false_branch)

    def while_statement(self):
        # Parse a while statement
        self.expect('WHILE')
        condition = self.expression()
        self.expect('DO')
        body = self.statement()
        return WhileNode(condition, body)

    def expression(self):
        # Parse an expression (simplified)
        left = self.term()
        while self.current_token().type in ('PLUS', 'MINUS'):
            operator = self.current_token()
            self.advance()
            right = self.term()
            left = BinaryOperationNode(left, operator, right)
        return left

    def term(self):
        # Parse a term (simplified)
        left = self.factor()
        while self.current_token().type in ('MULTIPLY', 'DIVIDE'):
            operator = self.current_token()
            self.advance()
            right = self.factor()
            left = BinaryOperationNode(left, operator, right)
        return left

    def factor(self):
        # Parse a factor (simplified)
        if self.current_token().type == 'IDENTIFIER':
            return self.variable()
        elif self.current_token().type in ('INTEGER', 'REAL'):  # Manejar INTEGER y REAL
            return self.number()
        elif self.current_token().type == 'BOOLEAN':  # Manejar BOOLEAN
            token = self.current_token()
            self.advance()
            return LiteralNode(token.value)
        elif self.current_token().type == 'CHAR':  # Manejar CHAR
            token = self.current_token()
            self.advance()
            return CharNode(token.value)
        elif self.current_token().type == 'STRING':  # Manejar STRING
            token = self.current_token()
            self.advance()
            return StringNode(token.value)
        elif self.current_token().type == 'LPAREN':
            self.expect('LPAREN')
            expression = self.expression()
            self.expect('RPAREN')
            return expression
        else:
            raise SyntaxError("Unexpected token: {}".format(self.current_token()))

    def variable(self):
        # Parse a variable
        identifier = self.expect('IDENTIFIER')
        return VariableNode(identifier)

    def number(self):
        # Parse a number
        token = self.current_token()
        if token.type in ('INTEGER', 'REAL'):
            self.advance()
            return LiteralNode(token.value)
        else:
            raise SyntaxError("Expected number, got: {}".format(token.type))

    def current_token(self):
        # Get the current token
        return self.tokens[self.current_token_index]

    def advance(self):
        # Move to the next token
        self.current_token_index += 1

    def expect(self, token_type):
        # Expect a specific token type
        if self.current_token().type == token_type:
            token = self.current_token()
            self.advance()
            return token.value
        else:
            raise SyntaxError("Expected token type: {}, got: {}".format(token_type, self.current_token().type))