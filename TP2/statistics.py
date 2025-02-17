import sys

# CSV Column Indices
COMPOSITOR = 4
OBRA = 0
PERIODO = 3

# def parse_csv(content):
#     """Parses CSV content manually, handling quoted fields and semicolon delimiters."""
#     rows = []
#     current_row = []
#     inside_quotes = False
#     field = ""

#     for char in content:
#         if char == '"':
#             inside_quotes = not inside_quotes  # Toggle quote state
#         elif char == '\n' and not inside_quotes:
#             current_row.append(field.strip())
#             rows.append(current_row)
#             current_row = []
#             field = ""
#         elif char == ';' and not inside_quotes:
#             current_row.append(field.strip())
#             field = ""
#         else:
#             field += char

#     if field:
#         current_row.append(field.strip())
#     if current_row:
#         rows.append(current_row)

#     return rows[1:]  # Skip header row

def parse_csv(content):
    rows = []
    current_row = []
    field = []
    inside_quotes = False
    
    for char in content:
        if char == '"':
            inside_quotes = not inside_quotes  # Alterna estado das aspas
        elif char == '\n' and not inside_quotes:
            current_row.append(''.join(field).strip())
            rows.append(current_row)
            current_row = []
            field = []
        elif char == ';' and not inside_quotes:
            current_row.append(''.join(field).strip())
            field = []
        else:
            field.append(char)
    
    if field:
        current_row.append(''.join(field).strip())
    if current_row:
        rows.append(current_row)
    
    return rows[1:]  # Ignora o cabeçalho


def process_csv(file_path):
    """Reads CSV file and returns parsed rows."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return parse_csv(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def process_obras(linhas, compositors, obras, periodos):
    """Processes rows and updates data structures."""
    for line in linhas:
        if len(line) <= max(COMPOSITOR, OBRA, PERIODO):  # Skip invalid rows
            continue

        process_compositor(line, compositors)
        process_obra(line, obras)
        process_periodo(line, periodos)

def process_compositor(line, compositors):
    """Adds composer to the list if not already present."""
    compositor = line[COMPOSITOR].strip()
    if compositor and compositor not in compositors:
        compositors.append(compositor)

def process_obra(line, obras):
    """Associates a work with its composer."""
    obra = line[OBRA].strip()
    compositor = line[COMPOSITOR].strip()

    if obra:
        if obra not in obras:
            obras[obra] = [compositor]
        elif compositor not in obras[obra]:
            obras[obra].append(compositor)

def process_periodo(line, periodos):
    """Categorizes works by period."""
    periodo = line[PERIODO].strip()
    obra = line[OBRA].strip()

    if periodo:
        periodos.setdefault(periodo, []).append(obra)

def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "obras.csv"
    linhas = process_csv(file_path)

    compositors = []
    obras = {}
    periodos = {}

    process_obras(linhas, compositors, obras, periodos)

    try:
        option = int(input(
            "1. Lista ordenada alfabeticamente dos compositores musicais\n"
            "2. Distribuição das obras por período\n"
            "3. Dicionário com obras organizadas por período\n"
            "Escolha uma opção (1-3): "
        ))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        sys.exit(1)

    if option == 1:
        print("\nCompositores musicais (Ordem alfabética):")
        print("\n".join(sorted(compositors, key=str.lower)))
    elif option == 2:
        print("\nObras catalogadas em cada período:")
        for periodo, obras_list in sorted(periodos.items()):
            print(f"{periodo}: {len(obras_list)}")
    elif option == 3:
        print("\nLista alfabética dos títulos associados a cada período:")
        for periodo, obras_list in sorted(periodos.items()):
            print(f"{periodo}:")
            for obra in sorted(obras_list, key=str.lower):
                print(f"  {obra}")
    else:
        print("Invalid option. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()


# == Distribuição por período ==
# Barroco: 26
# Clássico: 15
# Medieval: 48
# Renascimento: 41
# Século XX: 18
# Romântico: 19
# Contemporâneo: 7