# TPC6: Analisador Sintático Recursivo Descendente para Expressões Aritméticas

2025-03-22

## Autor:
![Nome do Autor](../profile.jpg)  
- Afonso Dionísio Santos    
- a104276

## Resumo

Este projeto, desenvolvido em Python, implementa um analisador sintático recursivo descendente para expressões aritméticas. O objetivo principal foi criar um interpretador capaz de reconhecer expressões e calcular o seu valor, utilizando as bibliotecas `ply` para a análise léxica e sintática.  

## Resolução

O projeto é composto por três ficheiros principais:  

### 1. Análise Léxica (`Lexer.py`)

- **Tokens:** Foram definidos tokens para números inteiros (`NUMBER`), operadores aritméticos (`PLUS`, `MINUS`, `TIMES`, `DIVIDE`) e parênteses (`LPAREN`, `RPAREN`).
- **Expressões Regulares:** São usadas regex para identificar cada token de forma clara e eficiente.
- **Gestão de Erros:** Caso apareçam caracteres ilegais, o analisador léxico reporta o erro e ignora o caracter.

### 2. Análise Sintática (`Yaccer.py`)

- **Parser Recursivo Descendente:**  
  O parser segue a gramática fornecida no enunciado e suporta operações de soma, subtração, multiplicação e divisão, bem como expressões aninhadas entre parênteses.
- **Regras Principais:**  
  - `expression` → define somas e subtrações  
  - `term` → define multiplicações e divisões  
  - `factor` → trata números ou expressões entre parênteses
- **Cálculo do Resultado:**  
  Cada produção é avaliada para devolver o valor da expressão à medida que é processada.

### 3. Programa Principal (`calculator.py`)

- **Interface em linha de comandos:**  
  O utilizador pode escrever expressões diretamente no terminal.
- **Comandos suportados:**  
  - Qualquer expressão aritmética válida (por exemplo: `2+3`, `(5+3)*2`)  
  - `exit` ou `quit` para sair do programa
- **Interpretação:**  
  O parser interpreta a expressão e apresenta o resultado. Caso a expressão seja inválida, é mostrada uma mensagem de erro.

## Instruções de Utilização

Para executar o programa, utilizar o seguinte comando no terminal:

```bash
python3 calculator.py
calc > 2+3
Result: 5

calc > 67-(2+3*4)
Result: 53

calc > (9-2)*(13-4)
Result: 63

calc > 5*(2+7)/3
Result: 15.0

calc > exit
```

## Dificuldades Encontradas
Durante o desenvolvimento deste analisador sintático, surgiram algumas dificuldades, tais como:

- Gerir corretamente a precedência e associação dos operadores, garantindo que a multiplicação e divisão são avaliadas antes da soma e subtração.

- Evitar erros de divisão por zero, que poderiam causar falhas de execução.

- Garantir a deteção de expressões mal formadas e apresentar mensagens de erro claras.

- Tratar corretamente a recursividade e situações em que a expressão termina de forma inesperada.
