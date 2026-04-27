from symbol_table import SymbolTable

class Engine9Interpreter:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def run_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "" or line.startswith("#"):
                    continue

                self.run_line(line)

    def run_line(self, line):
        if line.startswith("let "):
            self.handle_let(line)

        elif line.startswith("print "):
            self.handle_print(line)

        else:
            print("Unknown statement:", line)

    def handle_let(self, line):
        # Example: let force = mass * accel
        line = line.replace("let ", "", 1)

        if "=" not in line:
            print("Syntax Error: missing =")
            return

        name, expression = line.split("=", 1)
        name = name.strip()
        expression = expression.strip()

        value = self.evaluate_expression(expression)
        self.symbol_table.add_or_update(name, value)

    def handle_print(self, line):
        # Example: print force
        expression = line.replace("print ", "", 1).strip()
        value = self.evaluate_expression(expression)
        print(value)

    def evaluate_expression(self, expression):
        # Replace variable names with their values
        parts = expression.split()
        new_parts = []

        for part in parts:
            if part in self.symbol_table.table:
                new_parts.append(str(self.symbol_table.get_value(part)))
            else:
                new_parts.append(part)

        safe_expression = " ".join(new_parts)

        try:
            return eval(safe_expression)
        except Exception:
            print("Error evaluating expression:", expression)
            return 0
