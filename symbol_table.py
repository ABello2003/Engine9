class SymbolTable:
    def __init__(self):
        self.table = {}

    def set(self, name, value):
        if isinstance(value, int):
            t = "int"
        elif isinstance(value, float):
            t = "float"
        else:
            t = "unknown"

        self.table[name] = {"type": t, "value": value}

    def get(self, name):
        return self.table[name]["value"]

    def print_table(self):
        print("\nSYMBOL TABLE")
        for k, v in self.table.items():
            print(f"{k} → {v}")
