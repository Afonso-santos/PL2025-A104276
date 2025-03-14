import ply.lex as lex
import sys
import json
from datetime import date

tokens = (
    "LISTAR",
    "SAIR",
    "SELECIONAR",
    "MOEDA",
    "NOTA",
    )

# Data Storage
stock = {}
coins = {}
notes = {}
t_ignore = ' \t\n'

def t_LISTAR(t): r'(?i)LISTAR'; return t
def t_SAIR(t): r'(?i)SAIR'; return t

def t_SELECIONAR(t): r'(?i)SELECIONAR[ ]+[a-zA-Z0-9]+'; return t

def t_MOEDA(t): r'(?i)MOEDA\s+((1e|2e|50c|20c|10c|5c|2c|1c),?\s*)+'; return t
def t_NOTA(t): r'(?i)NOTA\s+([5e|10e|20e|50e|100e|200e|500e],?\s*)+'; return t
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)


def LISTAR()-> None: 
    print('     Number        |            Name                               |       Stock      |    Price    ')
    print('--------------------------------------------------------------------------------------------------------')
    for product in stock.values():
        print(f"        {product['cod']}        |        {product['nome']: <30}         |      {product['quant']: <5}       |      {product['preco']: <5}")

def TROCO(saldo: float) -> str:
    notes = {50: "50e", 20: "20e", 10: "10e", 5: "5e"}
    coins = {2: "2e", 1: "1e", 0.50: "50c", 0.20: "20c", 0.10: "10c", 0.05: "5c", 0.02: "2c", 0.01: "1c"}
    
    troco_count = {}

    for value in sorted(list(notes.keys()) + list(coins.keys()), reverse=True):
        while saldo >= value:
            saldo = round(saldo - value, 2)  # Avoid floating-point precision errors
            troco_count[value] = troco_count.get(value, 0) + 1

    # Create the output string
    troco_str_parts = [f"{count}x {coins.get(value, notes.get(value))}" for value, count in troco_count.items()]
    troco_str = ", ".join(troco_str_parts[:-1]) + (" e " + troco_str_parts[-1] if len(troco_str_parts) > 1 else "")

    return troco_str


def vending_machine() -> None:
    print(f"maq: {date.today()} Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido")
    lexer = lex.lex()
    saldo = 0

    for line in sys.stdin:
        lexer.input(line)

        for token in lexer:
            if token.type == "LISTAR":
                LISTAR()

            elif token.type == "SELECIONAR":
                cod = token.value.split()[1]  
                product = stock.get(cod)
                if saldo == 0:
                    print(f"O Preço do produto é: {product['preco']}€")
                    continue

                elif saldo < product["preco"]:
                    print(f"maq: Saldo insufuciente para satisfazer o seu pedido.")
                    print(f"maq: Saldo = {saldo}€ Pedido = {product['preco']}€")
                    continue
                elif product["quant"] == 0:
                    print(f"Produto esgotado.")
                    continue

                print(f"Produto: {product['nome']} - {product['preco']:.2f}€")
                product["quant"] -= 1
                saldo -= product["preco"]
                print(f"Saldo restante: {saldo:.2f}€")

           
            elif token.type == "MOEDA":
                moedas_str = " ".join(token.value.split()[1:]) #create a single string.
                moedas = moedas_str.split(",") #split the string by commas.
                for moeda in moedas:
                    moeda = moeda.strip()
                    if moeda:
                        if moeda.endswith('e'):
                            saldo += int(moeda[:-1]) 
                        elif moeda.endswith('c'):
                            saldo += int(moeda[:-1])/100

                print(f"Saldo: {saldo:.2f}€")
            
            elif token.type == "NOTA":
                notas_str = " ".join(token.value.split()[1:])
                notas = notas_str.split(",")
                for nota in notas:
                    nota = nota.strip()
                    if nota:
                        if nota.endswith('e') and int(nota[:-1]) > 20:
                            saldo = 0
                            print("Nota inválida. Adicione notas de 5, 10 ou 20)")
                            continue
                        elif nota.endswith('e'):
                            saldo += int(nota[:-1])
                    
                        print(f"Saldo: {saldo:.2f}€")

            elif token.type == "SAIR":
                if saldo > 0:
                    troco=TROCO(saldo)
                    print(f"maq: Pode retirar o troco: {troco}")

                print("maq: Até à próxima!")
                exit(0)
                break


def storage_machine(data: dict) -> None:
    for product in data["stock"]:
        stock[product["cod"]] = product
    
    for coin in data["moedas"]:
        coins[coin["valor"]] = coin
    
    for note in data["notas"]:
        notes[note["valor"]] = note



def main(argv: list) -> None:

    if len(argv) == 1:
        print("Usage: python Vending_Machine.py <file_path>")
        return

    file_path = argv[1]

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        storage_machine(data)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    vending_machine()

if __name__ == "__main__":
    main(sys.argv)
