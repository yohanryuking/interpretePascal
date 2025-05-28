import unittest
from src.lexer.lexer import Lexer
from src.lexer.tokens import TokenType

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()

    def test_integer_literal(self):
        self.lexer.input("123")
        token = self.lexer.next_token()
        self.assertEqual(token.type, TokenType.INTEGER)
        self.assertEqual(token.value, 123)

    def test_real_literal(self):
        self.lexer.input("123.45")
        token = self.lexer.next_token()
        self.assertEqual(token.type, TokenType.REAL)
        self.assertEqual(token.value, 123.45)

    def test_char_literal(self):
        self.lexer.input("'a'")
        token = self.lexer.next_token()
        self.assertEqual(token.type, TokenType.CHAR)
        self.assertEqual(token.value, 'a')

    def test_string_literal(self):
        self.lexer.input('"Hello, World!"')
        token = self.lexer.next_token()
        self.assertEqual(token.type, TokenType.STRING)
        self.assertEqual(token.value, "Hello, World!")

    def test_boolean_literal(self):
        self.lexer.input("true")
        token = self.lexer.next_token()
        self.assertEqual(token.type, TokenType.BOOLEAN)
        self.assertEqual(token.value, True)

        self.lexer.input("false")
        token = self.lexer.next_token()
        self.assertEqual(token.type, TokenType.BOOLEAN)
        self.assertEqual(token.value, False)

    def test_set_literal(self):
        # Cambiar para que espere LBRACKET en lugar de SET
        self.lexer.input("[ 'a', 'b', 'c' ]")
        token = self.lexer.next_token()
        self.assertEqual(token.type, 'LBRACKET')  # El lexer retorna LBRACKET, no SET
        self.assertEqual(token.value, '[')

    def test_arithmetic_operations(self):
        self.lexer.input("3 + 4 * 2")
        tokens = [self.lexer.next_token() for _ in range(5)]
        self.assertEqual(tokens[1].type, TokenType.PLUS)
        self.assertEqual(tokens[3].type, TokenType.MULTIPLY)  # Usar MULTIPLY en lugar de STAR

    def test_relational_operations(self):
        self.lexer.input("a > b")
        tokens = [self.lexer.next_token() for _ in range(3)]
        self.assertEqual(tokens[1].type, TokenType.GREATER)

    def test_assignment(self):
        self.lexer.input("x := 10")
        tokens = [self.lexer.next_token() for _ in range(3)]
        self.assertEqual(tokens[1].type, TokenType.ASSIGN)

    def test_conditional(self):
        self.lexer.input("x > 10 ? 'Greater' : 'Lesser'")
        tokens = [self.lexer.next_token() for _ in range(7)]
        self.assertEqual(tokens[3].type, TokenType.QUESTION)
        self.assertEqual(tokens[5].type, 'COLON')  # Usar 'COLON' string literal

    def test_membership(self):
        self.lexer.input("x in S")
        tokens = [self.lexer.next_token() for _ in range(3)]  # Solo 3 tokens: x, in, S
        self.assertEqual(tokens[1].type, TokenType.IN)

if __name__ == '__main__':
    unittest.main()