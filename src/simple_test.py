from lexer.lexer import Lexer
from lexer.tokens import TokenType

def test_lexer():
    print("=== Probando Lexer ===")
    
    # Prueba simple
    code = "a := 5 + 3;"
    lexer = Lexer(code)
    
    print(f"Código: {code}")
    print("Tokens:")
    
    tokens = lexer.tokenize()
    for token in tokens:
        print(f"  {token}")
    
    print("\n" + "="*50 + "\n")

def test_numbers():
    print("=== Probando números ===")
    
    codes = ["123", "45.67", "true", "false"]
    
    for code in codes:
        print(f"Código: {code}")
        lexer = Lexer(code)
        token = lexer.next_token()
        print(f"Token: {token}")
        print()

def test_strings():
    print("=== Probando strings y chars ===")
    
    codes = ["'a'", '"Hello World"', "'Hello'"]
    
    for code in codes:
        print(f"Código: {code}")
        lexer = Lexer(code)
        token = lexer.next_token()
        print(f"Token: {token}")
        print()

if __name__ == "__main__":
    test_lexer()
    test_numbers()
    test_strings()