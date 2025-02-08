import sys

def process_line(line: str , switch :int, total:int) -> int:
    i = 0
    while len(line) > i:
        if line[i] in "0123456789" and switch == 1:
            valor = 0
            while i < len(line) and line[i] in "0123456789":
                valor = valor * 10 + int(line[i])
                i += 1
            total += valor
        elif line[i] in "oO":
            if i + 2 < len(line) and line[i + 1] in "fF" and line[i + 2] in "fF":
                switch = 0
                i += 3
            elif i + 1 < len(line) and line[i + 1] in "nN":
                switch = 1
                i += 2
            else:
                i += 1
        elif line[i] == "=":
            print(total)
            i += 1
        else:
            i += 1
    return total

def main() -> None:
    switch = 0  # Initially OFF
    total = 0   

    if len(sys.argv) > 1:  # If a file path is provided as an argument
        file_path = sys.argv[1]
        try:
            with open(file_path, "r") as file:
                for line in file:
                    total = process_line(line, switch, total)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return
    else:
        print("Enter text (Ctrl+D to stop):")
        for line in sys.stdin:
           total = process_line(line, switch, total)

    print("Final total:", total)

if __name__ == "__main__":
    main()
