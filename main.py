from lexer import analyze_tokens
from interpreter import Engine9Interpreter

SOURCE_FILE = "program.e9"

def main():
    print("===== ENGINE9 TOKEN REPORT =====")
    analyze_tokens(SOURCE_FILE)

    print("\n===== ENGINE9 PROGRAM OUTPUT =====")
    interpreter = Engine9Interpreter()
    interpreter.run_file(SOURCE_FILE)

    print("\n===== SYMBOL TABLE =====")
    interpreter.symbol_table.print_table()

if __name__ == "__main__":
    main()
