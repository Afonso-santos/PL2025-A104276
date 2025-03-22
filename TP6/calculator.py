import sys
from Yaccer import parser

def main():
    while True:
        try:
            s = input("calc > ")
            if s.lower() in ('exit', 'quit'):
                break
        except EOFError:
            break
        if not s:
            continue
        try:
            parser.success = True
            result = parser.parse(s)
            if parser.success:
              print("Result:", result)
            else:
              print("Error: Invalid Expression")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()