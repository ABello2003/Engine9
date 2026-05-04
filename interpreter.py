from symbol_table import SymbolTable
import functions


class Engine9Interpreter:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def eval_expr(self, expr):
        # Replace variables with values
        for var in self.symbol_table.table:
            expr = expr.replace(var, str(self.symbol_table.get(var)))

        # Replace built-in Engine9 functions
        expr = expr.replace("force", "functions.force")
        expr = expr.replace("kinetic_energy", "functions.kinetic_energy")
        expr = expr.replace("ohm_current", "functions.ohm_current")
        expr = expr.replace("work", "functions.work")
        expr = expr.replace("power", "functions.power")
        expr = expr.replace("pressure", "functions.pressure")
        expr = expr.replace("density", "functions.density")
        expr = expr.replace("momentum", "functions.momentum")

        return eval(expr)

    def interpret(self, ast):
        for node in ast:
            if hasattr(node, "name"):
                value = self.eval_expr(node.expression)
                self.symbol_table.set(node.name, value)

            elif hasattr(node, "value"):
                value = self.eval_expr(node.value)
                print(value)

        self.symbol_table.print_table()
