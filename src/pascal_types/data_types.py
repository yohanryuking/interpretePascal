class Integer:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"Integer({self.value})"


class Real:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"Real({self.value})"


class Char:
    def __init__(self, value: str):
        if len(value) != 1:
            raise ValueError("Char must be a single character.")
        self.value = value

    def __repr__(self):
        return f"Char('{self.value}')"


class Boolean:
    def __init__(self, value: bool):
        self.value = value

    def __repr__(self):
        return f"Boolean({self.value})"


class String:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"String('{self.value}')"


class SetOfChar:
    def __init__(self, elements: set):
        if not all(isinstance(el, str) and len(el) == 1 for el in elements):
            raise ValueError("All elements must be single characters.")
        self.elements = elements

    def __repr__(self):
        return f"SetOfChar({self.elements})"

    def union(self, other):
        return SetOfChar(self.elements.union(other.elements))

    def intersection(self, other):
        return SetOfChar(self.elements.intersection(other.elements))

    def contains(self, element: str):
        return element in self.elements


# Example usage:
# int_var = Integer(10)
# real_var = Real(3.14)
# char_var = Char('a')
# bool_var = Boolean(True)
# string_var = String("Hello")
# set_var = SetOfChar({'a', 'b', 'c'})