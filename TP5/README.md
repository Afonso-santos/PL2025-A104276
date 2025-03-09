# TPC4: Analisador Léxico para Consultas SPARQL

2025-03-09

## Autor:
![Nome do Autor](../profile.jpg)  
- Afonso Dionísio Santos
- A104276

## Resumo

Este programa, desenvolvido em Python, simula o funcionamento de uma máquina de vendas automática. Ele permite que os utilizadores interajam com a máquina através de comandos para listar produtos, inserir moedas e notas, selecionar produtos para compra e sair da simulação, recebendo o troco adequado.

## Resolução

O programa utiliza a biblioteca `ply` para realizar a análise léxica e interpretar os comandos fornecidos pelo utilizador. Seguem-se os principais componentes e funcionalidades do programa:

### Análise Léxica com PLY

- **Tokens:** Definem-se tokens para diferentes tipos de entrada, incluindo `LISTAR`, `MOEDA`, `NOTA`, `SELECIONAR` e `SAIR`.
- **Expressões Regulares:** Utilizam-se padrões regex para identificar cada comando e processá-lo corretamente.
- **Funções de Tokenização:** Cada token é analisado e convertido para um comando correspondente.

### Interação com o Utilizador

- **Entrada de Comandos:** O utilizador introduz comandos através do terminal.
- **Processamento de Comandos:** O programa interpreta e executa as ações associadas a cada comando.
- **Feedback ao Utilizador:** A máquina responde informando o saldo, stock e o troco devolvido.

### Manipulação de Dados

- **Carregamento de Stock:** Os produtos disponíveis são carregados a partir de um ficheiro JSON.
- **Gestão de Stock:** A quantidade dos produtos é atualizada conforme as compras são realizadas.
- **Gestão de Saldo:** O saldo do utilizador é atualizado de acordo com as moedas e notas inseridas.
- **Cálculo de Troco:** O programa determina a melhor combinação de notas e moedas para devolver o troco.

## Instruções de Utilização

Para executar o programa, utilize o seguinte comando:

```sh
python3 vending_machine.py stock.json
```

### Comandos Disponíveis

- **LISTAR** - Exibe a lista de produtos disponíveis.
- **MOEDA <valor>** - Adiciona moedas ao saldo.
- **NOTA <valor>** - Adiciona notas ao saldo (apenas notas de 5, 10 e 20 euros são aceites).
- **SELECIONAR <código>** - Seleciona um produto para compra.
- **SAIR** - Sai do programa e devolve o troco restante.

## Exemplo de Utilização

```sh
maq: 2025-03-09 Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido
>>listar
     Number        |            Name                               |       Stock      |    Price
--------------------------------------------------------------------------------------------------------
        A01        |        Água 0.5L                              |      10          |      0.7
        A02        |        Coca-Cola 33cl                         |      7           |      1.2
        A03        |        Pepsi 33cl                             |      6           |      1.2
...
>> Selecionar A05
O Preço do produto é: 1.1€
>> moeda 2e, 50c
Saldo: 2.50€
>> nota 5e
Saldo: 7.50
>> Selecionar A05
Produto: Ice Tea Pêssego 33cl - 1.10€
Saldo restante: 6.40€
>> Sair
maq: Pode retirar o troco: 1x 5e, 1x 1e e 2x 20c
maq: Até à próxima!
```

## Dificuldades Encontradas

Durante o desenvolvimento do programa, enfrentaram-se alguns desafios, como:

- **Gestão correta das expressões regulares** para capturar os comandos de forma precisa.
- **Evitar erros de precisão com números decimais** ao calcular o troco.
- **Garantir que apenas notas válidas fossem aceites**, evitando erros no saldo.
- **Lidar com casos de produtos esgotados ou saldo insuficiente** de forma intuitiva para o utilizador.

Este projeto foi uma excelente oportunidade para explorar análise léxica e a interação entre um programa Python e ficheiros JSON.
