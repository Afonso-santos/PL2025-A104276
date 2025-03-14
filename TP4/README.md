# TPC4: Analisador Léxico para Consultas SPARQL

2025-03-01

## Autor:
![Nome do Autor](../profile.jpg)  
- Afonso Dionísio Santos
- A104276

## Resumo

### Problema
O objetivo deste trabalho é desenvolver um analisador léxico em Python para processar consultas escritas em uma linguagem semelhante a SPARQL. Este analisador tem como função decompor uma string de consulta nos seus respetivos tokens, classificando-os segundo as suas categorias sintáticas, como palavras-chave, variáveis, URIs, números, cadeias de caracteres e símbolos.

Exemplo de entrada e saída do analisador:
```
Entrada:
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

```
Saída:
('select', 'KEYWORD')
('?nome', 'VAR')
('?desc', 'VAR')
('where', 'KEYWORD')
('{', 'SYMBOL')
('?s', 'VAR')
('a', 'UNKNOWN')
('dbo:MusicalArtist', 'URI')
('.', 'SYMBOL')
... (restantes tokens)
```

### Funcionamento
O analisador léxico funciona em três etapas principais. Primeiro, define-se um conjunto de expressões regulares que permitem identificar diferentes tipos de tokens dentro da consulta. Estes padrões incluem palavras-chave como "select" e "where", variáveis precedidas por "?", URIs com prefixos como "dbo:" e "foaf:", cadeias de caracteres delimitadas por aspas, números, símbolos como chaves e pontos, espaços em branco e qualquer caractere desconhecido.

Após definir os padrões, o código percorre a string de entrada utilizando a função `re.finditer()`, que identifica os tokens com base nas expressões regulares. Cada token encontrado é analisado para determinar sua categoria. Espaços em branco são ignorados, enquanto tokens desconhecidos geram um erro.

Por fim, a função retorna uma lista de pares `(valor, tipo)`, representando os tokens extraídos da consulta. Este processo garante uma separação precisa dos elementos da linguagem, permitindo o processamento posterior da consulta.

O código acima define um analisador léxico que:
- Usa **expressões regulares** para identificar os tokens.
- Ignora **espaços em branco**.
- Regista **tokens desconhecidos**, lançando um erro quando encontrados.
- Retorna uma lista de pares `(valor, tipo)` representando cada token identificado.

### Dificuldades Encontradas
Durante o desenvolvimento do analisador léxico, enfrentaram-se alguns desafios. Um dos principais foi garantir que as expressões regulares identificassem corretamente os diferentes tipos de tokens, sem sobreposição ou conflitos. Por exemplo, era necessário diferenciar variáveis de URIs, garantindo que `?nome` fosse identificado como uma variável, enquanto `dbo:MusicalArtist` fosse reconhecido como uma URI.

Outro desafio foi evitar a aceitação de tokens desconhecidos. Inicialmente, qualquer caractere não coberto pelos padrões definidos era silenciosamente ignorado. No entanto, para maior rigor, optou-se por lançar um erro sempre que um token desconhecido fosse encontrado, facilitando a depuração e garantindo que apenas consultas válidas fossem processadas corretamente.

## Instruções de Utilização

Para executar o analisador léxico, basta correr o seguinte comando em Python:
```sh
$ python3 lexical_analyzer.py
```

Este comando irá processar a consulta definida no código e imprimir a lista de tokens extraídos.
