import sys

# CSV Column Indices
COMPOSITOR = 1
OBRA = 4
PERIODO = 3  # Assuming column index 3 contains period information

def process_csv(file_path):
    """Lê o ficheiro CSV e retorna as linhas, saltando o cabeçalho, sem usar csv module"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines() 
            return [line.strip().split(",") for line in lines[1:]]      
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def process_obras(linhas, compositors, obras, periodos):
    """ Processa as linhas e da update as estruturas de dados"""
    for line in linhas:
        if len(line) < max(COMPOSITOR, OBRA, PERIODO) + 1:
            #print(f"Skipping invalid line: {line}")  # Debugging message
            continue

        process_compositor(line, compositors)
        process_obra(line, obras)
        process_periodo(line, periodos)

def process_compositor(line, compositors):
    """Adiciona o compositor à lista se ainda não estiver presente."""

    compositor = line[COMPOSITOR]
    if compositor not in compositors:
        compositors.append(compositor)

def process_obra(line, obras):
    """Associa uma obra ao seu compositor no dicionário."""
    obra = line[OBRA]
    compositor = line[COMPOSITOR]

    if obra not in obras:
        obras[obra] = [compositor]
    else:
        if compositor not in obras[obra]:
            obras[obra].append(compositor)

def process_periodo(line, periodos):
    """categoriza as obras por periodo"""
    periodo = line[PERIODO]
    obra = line[OBRA]

    if periodo not in periodos:
        periodos[periodo] = [obra]
    else:
        if obra not in periodos[periodo]:
            periodos[periodo].append(obra)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <CSV_FILE_PATH>")
        sys.exit(1)

    print(
        "1. Lista ordenada alfabeticamente dos compositores musicais\n"
        "2. Distribuição das obras por período\n"
        "3. Dicionário com obras organizadas por período"
    )

    file_path = sys.argv[1]
    linhas = process_csv(file_path)

    compositors = []
    obras = {}
    periodos = {}

    process_obras(linhas, compositors, obras, periodos)

    try:
        option = int(input("Escolha uma opção (1-3): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        sys.exit(1)

    match option:
        case 1:
            print("\n Compositores musicais (Ordem alfabetica):")
            print("\n".join(sorted(compositors, key=lambda x: (x.lower(), x))))
        case 2:
            print("\nObras catalogadas em cada perodo:")
            for periodo, obras_list in periodos.items():
                print(f"{periodo}: {len(obras_list)} ")
        case 3:
            print("\n Lista alfabética dos titulos associados a cada período:")
            for periodo, obras_list in periodos.items():
                print(f"{periodo}: {sorted(obras_list, key=lambda x: (x.lower(), x))}")
        case _:
            print("Invalid option. Exiting...")
            sys.exit(1)

if __name__ == "__main__":
    main()
