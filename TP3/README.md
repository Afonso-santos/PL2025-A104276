# TPC3:Conversor de MarkDown para HTML

2025-02-23

## Autor:
![Afonso Dionísio ](../profile.jpg)  
- Afonso Dionísio Santos
- A104276

## Resumo
### Problema
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:


Cabeçalhos: linhas iniciadas por ```# texto```, ou ```## texto``` ou ```### texto```
```
In: # Exemplo
Out: <h1>Exemplo</h1>
```
Bold: pedaços de texto entre ```**```:
```
In: Este é um **exemplo** ...
Out: Este é um <b>exemplo</b> ...
```
Itálico: pedaços de texto entre ```*```:
```
In: Este é um *exemplo* ...
Out: Este é um <i>exemplo</i> ...
```

Lista numerada:
```
In:
1. Primeiro item
2. Segundo item
3. Terceiro item

Out:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

Link: [texto](endereço URL)
```
In: Como pode ser consultado em [página da UC](http://www.uc.pt)
Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
```

Imagem: ![texto alternativo](path para a imagem)
```
In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem
dum coelho"/> ...
```


### Funcionamento

O programa tem como objetivo converter um ficheiro de texto em Markdown para HTML. Para isso, lê linha a linha o conteúdo do ficheiro e aplica regras de substituição para transformar os elementos de Markdown nos seus equivalentes em HTML.

Inicialmente, o programa recebe como argumento o caminho para o ficheiro de entrada e, opcionalmente, o caminho para o ficheiro de saída. Se não for especificado um ficheiro de saída, a conversão é exibida diretamente no terminal.

A função ```convert_lines``` percorre as linhas do ficheiro e converte cabeçalhos, texto em negrito e itálico, imagens, links e listas numeradas. Cada tipo de elemento é tratado com expressões regulares que identificam e substituem a sintaxe de Markdown pela correspondente em HTML.

Se for detetada uma lista ordenada, o programa garante que a tag ```<ol>``` seja aberta antes dos itens da lista e fechada corretamente no final. Para isso, utiliza a variável inside_ol, que controla se o programa já está dentro de uma lista ordenada.

## Dificuldades Encontradas
Uma das dificuldades encontradas foi garantir que a conversão de listas numeradas fosse feita corretamente. Inicialmente, ao processar linha a linha, cada item era tratado individualmente, e a estrutura ```<ol>``` não era aberta e fechada corretamente, resultando em listas inválidas no HTML. Para resolver isso, foi necessário introduzir um mecanismo que controla quando abrir e fechar a lista.

Outro desafio foi garantir que as expressões regulares para os diferentes elementos do Markdown fossem aplicadas na ordem correta. Algumas regras, se aplicadas antes de outras, poderiam interferir na substituição e gerar resultados inesperados. Por exemplo, processar primeiro os cabeçalhos antes de converter texto em negrito e itálico garantiu que os estilos fossem mantidos dentro das tags ```<h1>```, ```<h2>```, ```<h3>```.

## Instrução de utilização
- Indicando o path do ficheiro , o programa irá ler do ficheiro e escrever no stdout
 ```sh
    $ python3 MarckDown_to_HTML.py <file_path>
```

- Caso for indicado mais um parametro ```<name file>``` irá escrever nesse ficheiro
 ```sh
    $ python3 MarckDown_to_HTML.py <file_path> <name file>
```