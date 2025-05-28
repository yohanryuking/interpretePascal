import re
from .tokens import Token, TokenType

class Lexer:
    def __init__(self, source_code=""):
        self.source_code = source_code
        self.position = 0
        self.current_char = self.source_code[self.position] if source_code else None

    def input(self, source_code):
        """Set new source code for tokenization"""
        self.source_code = source_code
        self.position = 0
        self.current_char = self.source_code[self.position] if source_code else None

    def error(self):
        raise Exception(f'Invalid character at position {self.position}: {self.current_char}')

    def advance(self):
        """Move to the next character"""
        self.position += 1
        if self.position >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.position]

    def skip_whitespace(self):
        """Skip whitespace characters"""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def read_number(self):
        """Read integer or real numbers"""
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        
        if '.' in result:
            return Token(TokenType.REAL, float(result))
        else:
            return Token(TokenType.INTEGER, int(result))

    def read_string(self, quote_char):
        """Read string literals"""
        result = ''
        self.advance()  # Skip opening quote
        
        while self.current_char is not None and self.current_char != quote_char:
            result += self.current_char
            self.advance()
        
        if self.current_char == quote_char:
            self.advance()  # Skip closing quote
            if quote_char == "'" and len(result) == 1:
                return Token(TokenType.CHAR, result)
            else:
                return Token(TokenType.STRING, result)
        else:
            raise Exception("Unterminated string")

    def read_identifier(self):
        """Read identifiers and keywords"""
        result = ''
        while (self.current_char is not None and 
               (self.current_char.isalnum() or self.current_char == '_')):
            result += self.current_char
            self.advance()
        
        # Check for keywords
        keywords = {
            'true': Token(TokenType.BOOLEAN, True),
            'false': Token(TokenType.BOOLEAN, False),
            'if': Token(TokenType.IF, 'if'),
            'then': Token('THEN', 'then'),
            'else': Token('ELSE', 'else'),
            'while': Token('WHILE', 'while'),
            'do': Token('DO', 'do'),
            'var': Token('VAR', 'var'),
            'begin': Token('BEGIN', 'begin'),
            'end': Token('END', 'end'),
            'program': Token('PROGRAM', 'program'),
            'integer': Token('TYPE', 'integer'),
            'real': Token('TYPE', 'real'),
            'char': Token('TYPE', 'char'),
            'boolean': Token('TYPE', 'boolean'),
            'string': Token('TYPE', 'string'),
            'set': Token('TYPE', 'set'),
            'of': Token('OF', 'of'),
            'in': Token(TokenType.IN, 'in'),
            'read': Token('READ', 'read'),
            'write': Token('WRITE', 'write'),
        }
        
        return keywords.get(result.lower(), Token('IDENTIFIER', result))

    def next_token(self):
        """Get the next token"""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.read_number()

            if self.current_char.isalpha():
                return self.read_identifier()

            if self.current_char in ('"', "'"):
                return self.read_string(self.current_char)

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/')
            
            if self.current_char == '^':
                self.advance()
                return Token(TokenType.POWER, '^')
            
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            
            if self.current_char == '[':
                self.advance()
                return Token('LBRACKET', '[')
            
            if self.current_char == ']':
                self.advance()
                return Token('RBRACKET', ']')
            
            if self.current_char == ';':
                self.advance()
                return Token('SEMICOLON', ';')
            
            if self.current_char == ':':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.ASSIGN, ':=')
                return Token('COLON', ':')
            
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.EQUAL, '=')
            
            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.GREATER_EQUAL, '>=')
                return Token(TokenType.GREATER, '>')
            
            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.LESS_EQUAL, '<=')
                elif self.current_char == '>':
                    self.advance()
                    return Token(TokenType.NOT_EQUAL, '<>')
                return Token(TokenType.LESS, '<')
            
            if self.current_char == '?':
                self.advance()
                return Token(TokenType.QUESTION, '?')
            
            if self.current_char == ',':
                self.advance()
                return Token('COMMA', ',')
            
            if self.current_char == '.':
                self.advance()
                return Token('DOT', '.')

            self.error()

        return Token(TokenType.EOF, None)

    def tokenize(self):
        """Tokenize the entire source code"""
        tokens = []
        token = self.next_token()
        while token.token_type != TokenType.EOF:
            tokens.append(token)
            token = self.next_token()
        tokens.append(token)  # Add EOF token
        return tokens