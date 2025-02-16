# TPC1: Análise de um dataset de obras musicais

2025-02-16

## Autor:
![Afonso Dionísio ](../profile.jpg)  
- Afonso Dionísio Santos
- A104276

## Resumo
### Problema

- Neste TPC, é proibido usar o módulo CSV do Python;

Deverás ler o dataset, processá-lo e criar os seguintes resultados:
1. Lista ordenada alfabeticamente dos compositores musicais;
2. Distribuição das obras por período: quantas obras catalogadas em cada período;
3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

### Funcionamento

Na construção da solução para o exercício, optei por criar vários métodos, cada um responsável por uma operação específica.

No início do programa, ao receber o caminho para o ficheiro CSV, a estrutura de dados utilizada para armazenar as informações é inicializada.  

De seguida, o ficheiro CSV é lido linha a linha, e os dados são extraídos e inseridos nas respetivas estruturas, garantindo que as informações fiquem corretamente organizadas.  

Após o processamento dos dados, o utilizador é apresentado com um menu onde pode escolher que tipo de informação deseja visualizar. As opções disponíveis incluem a listagem dos compositores ordenados alfabeticamente, a distribuição das obras por período e um dicionário com os títulos das obras organizados por período.  



## Instrução de utilização
- Indicando o path do ficheiro
 ```sh
    $ python3 statistcs.py <file_path>
```

- Após a execução do programa, será apresentado um menu no terminal com as seguintes opções, sendo necessário escolher uma delas.

```sh
    1. Lista ordenada alfabeticamente dos compositores musicais
    2. Distribuição das obras por período
    3. Dicionário com obras organizadas por período
    Escolha uma opção (1-3):
```