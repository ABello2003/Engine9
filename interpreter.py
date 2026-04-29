from symbolTable import SymbolTable
import functions

symbol_table = SymbolTable()

def eval_expr(expr):
    expr = " ".join(expr)

    # replace variables
    for var in symbol_table.table:
        expr = expr.replace(var, str(symbol_table.get(var)))

    # replace functions
    expr = expr.replace("force", "functions.force")
    expr = expr.replace("kinetic_energy", "functions.kinetic_energy")
    expr = expr.replace("ohm_current", "functions.ohm_current")

    return eval(expr)

def interpret(ast):
    for node in ast:
        if hasattr(node, "name"):
            val = eval_expr(node.expression)
            symbol_table.set(node.name, val)

        elif hasattr(node, "value"):
            val = symbol_table.get(node.value)
            print(val)

    symbol_table.print_table()
