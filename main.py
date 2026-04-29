from engine9 import Engine9Interpreter

def main():
    interpreter = Engine9Interpreter()

    print("===== Engine9 Interactive Interpreter =====")
    print("Type Engine9 code.")
    print("Type run to execute.")
    print("Type sample to run sample_engine9.e9.")
    print("Type clear to clear current code.")
    print("Type exit to quit.\n")

    lines = []

    while True:
        line = input("E9> ").strip()

        if line.lower() == "exit":
            print("Goodbye.")
            break

        elif line.lower() == "clear":
            lines = []
            print("Code cleared.\n")

        elif line.lower() == "run":
            interpreter = Engine9Interpreter()
            interpreter.run_lines(lines)
            interpreter.print_symbol_table()
            lines = []

        elif line.lower() == "sample":
            interpreter = Engine9Interpreter()
            interpreter.run_file("sample_engine9.e9")
            interpreter.print_symbol_table()

        else:
            lines.append(line)

if __name__ == "__main__":
    main()
