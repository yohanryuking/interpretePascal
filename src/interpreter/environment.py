class Environment:
    def __init__(self):
        self.variables = {}
        self.global_scope = {}

    def define(self, name, value):
        self.global_scope[name] = value

    def get(self, name):
        if name in self.global_scope:
            return self.global_scope[name]
        raise NameError(f"Variable '{name}' is not defined.")

    def assign(self, name, value):
        if name in self.global_scope:
            self.global_scope[name] = value
        else:
            raise NameError(f"Variable '{name}' is not defined.")

    def __str__(self):
        return str(self.global_scope)