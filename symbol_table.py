class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_or_update(self, name, value):
        if isinstance(value, int):
            data_type = "int"
        elif isinstance(value, float):
            data_type = "float"
        else:
            data_type = "unknown"

        self.table[name] = {
            "type": data_type,
            "value": value
        }

    def get_value(self, name):
        if name not in self.table:
            raise NameError(f"Variable '{name}' is not defined.")
        return self.table[name]["value"]

    def print_table(self):
        print("Variable\tType\tValue")
        print("-----------------------------")
        for name, info in self.table.items():
            print(f"{name}\t\t{info['type']}\t{info['value']}")
