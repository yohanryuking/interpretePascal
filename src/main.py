# Entry point for the Pascal-like interpreter
import sys
from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.environment import Environment

def main():
    print("Welcome to the Pascal-like Interpreter!")
    
    # Create environment once
    environment = Environment()
    
    # Check if reading from file or stdin
    if not sys.stdin.isatty():  # Reading from file/pipe
        print("Reading from file...")
        try:
            source_code = sys.stdin.read().strip()
            if source_code:
                result = process_code(source_code, environment)
                if result is not None:
                    print("Result:", result)
                else:
                    print("No result to display")
        except Exception as e:
            print("Error:", e)
        return
    
    # Interactive mode
    print("Enter Pascal-like code (or 'exit' to quit):")
    while True:
        try:
            # Read user input
            source_code = input("> ")
            if source_code.lower() == 'exit':
                break
            
            if source_code.strip():  # Only process non-empty input
                result = process_code(source_code, environment)
                if result is not None:
                    print("Result:", result)
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print("Error:", e)

def process_code(source_code, environment):
    """Process a line of Pascal code and return the result"""
    try:
        # Initialize the lexer
        lexer = Lexer()
        lexer.input(source_code)
        tokens = lexer.tokenize()
        
        # Skip empty token lists
        if not tokens or (len(tokens) == 1 and tokens[0].type == 'EOF'):
            return None
        
        # Initialize parser and interpreter
        parser = Parser(tokens)
        interpreter = Interpreter(environment)
        
        # Try to parse as expression first (for simple calculations)
        try:
            ast = parser.expression()
            result = interpreter.interpret(ast)
            return result
        except:
            # If expression parsing fails, try as full program
            parser = Parser(tokens)  # Reset parser
            ast = parser.parse()
            result = interpreter.interpret(ast)
            return result
            
    except Exception as e:
        raise Exception(f"Processing error: {e}")

if __name__ == "__main__":
    main()