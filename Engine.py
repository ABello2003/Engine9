from parser import parse_line
from interpreter import Engine9Interpreter


def run_file(filename):
    ast = []

    with open(filename, "r") as f:
        for line in f:
            node = parse_line(line)
            if node is not None:
                ast.append(node)

    engine = Engine9Interpreter()
    engine.interpret(ast)


def main():
    print("===== Engine9 Interpreter =====")
    print("Type 'sample' to run example or 'exit' to quit")

    while True:
        cmd = input(">> ")

        if cmd == "exit":
            print("Goodbye.")
            break

        elif cmd == "sample":
            run_file("sample.e9")

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
