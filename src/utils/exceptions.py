class InterpreterError(Exception):
    """Base class for exceptions in the interpreter."""
    pass

class SyntaxError(InterpreterError):
    """Exception raised for syntax errors in the input."""
    def __init__(self, message, line_number):
        super().__init__(message)
        self.line_number = line_number

class TypeError(InterpreterError):
    """Exception raised for type errors during interpretation."""
    def __init__(self, message):
        super().__init__(message)

class UndefinedVariableError(InterpreterError):
    """Exception raised for accessing an undefined variable."""
    def __init__(self, variable_name):
        super().__init__(f"Undefined variable: {variable_name}")

class DivisionByZeroError(InterpreterError):
    """Exception raised for division by zero errors."""
    def __init__(self):
        super().__init__("Division by zero is not allowed.")

class InvalidOperationError(InterpreterError):
    """Exception raised for invalid operations."""
    def __init__(self, operation):
        super().__init__(f"Invalid operation: {operation}")

class OutOfBoundsError(InterpreterError):
    """Exception raised for out of bounds errors in collections."""
    def __init__(self, index):
        super().__init__(f"Index out of bounds: {index}")