class SymbolTable:
    def __init__(self):
        self.table = {}

    def set(self, name, value):
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

    def get(self, name):
        if name not in self.table:
            raise NameError(f"Variable '{name}' is not defined.")
        return self.table[name]["value"]

    def print_table(self):
        print("\n===== SYMBOL TABLE =====")
        print(f"{'Variable':<15}{'Type':<10}{'Value':<10}")
        print("-" * 35)

        for name, data in self.table.items():
            print(f"{name:<15}{data['type']:<10}{data['value']:<10}")
