from interpreter import Engine9Interpreter

def main():
    print("===== Engine9 Interactive Mode =====")
    print("Type Engine9 code below.")
    print("Type 'run' to execute.")
    print("Type 'exit' to quit.\n")

    lines = []

    while True:
        line = input("E9> ")

        if line.lower() == "exit":
            print("Goodbye.")
            break

        if line.lower() == "run":
            interpreter = Engine9Interpreter()
            print("\n===== PROGRAM OUTPUT =====")
            interpreter.run_lines(lines)

            print("\n===== SYMBOL TABLE =====")
            interpreter.symbol_table.print_table()

            lines = []
            print("\nYou can type a new Engine9 program now.\n")
            continue

        lines.append(line)

if __name__ == "__main__":
    main()
