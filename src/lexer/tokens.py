class TokenType:
    # Literals
    INTEGER = 'INTEGER'
    REAL = 'REAL'
    CHAR = 'CHAR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    SET = 'SET'
    
    # Identifiers
    IDENTIFIER = 'IDENTIFIER'
    
    # Arithmetic operators
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    STAR = 'MULTIPLY'  # Alias para compatibilidad con tests
    DIVIDE = 'DIVIDE'
    POWER = 'POWER'
    
    # Relational operators
    EQUAL = 'EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'
    GREATER = 'GREATER'
    GREATER_EQUAL = 'GREATER_EQUAL'
    LESS = 'LESS'
    LESS_EQUAL = 'LESS_EQUAL'
    
    # Set operations
    IN = 'IN'
    
    # Punctuation
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'
    SEMICOLON = 'SEMICOLON'
    COLON = 'COLON'
    ASSIGN = 'ASSIGN'
    COMMA = 'COMMA'
    QUESTION = 'QUESTION'  # Para operador ternario
    
    # Keywords
    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    read = 'read'
    WRITE = 'WRITE'
    
    # Special
    EOF = 'EOF'

class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type  # Cambiado de token_type a type para consistencia
        self.token_type = token_type  # Mantener ambos por compatibilidad
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'