# TPC1: Somador on/off

2025-02-07

## Autor:
- Afonso Dionísio Santos
- A104276

## Resumo

### Problema
1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

### Funcionamento
O programa lê um texto caractere por caractere para identificar números inteiros positivos e somá-los, mas essa soma só ocorre se um modo estiver ativado. Para isso, criei uma flag que controla se os números devem ser considerados ou ignorados. Essa flag é ativada e desativada conforme aparecem as palavras "on" e "off" no texto, independentemente de estarem em maiúsculas ou minúsculas.  

Ao percorrer o texto, verifico se o caractere atual é um dígito. Se for e a flag estiver ativada, extraio o número inteiro completo e o adiciono ao total. Caso contrário, continuo analisando o texto. Se o caractere for "o" (maiúsculo ou minúsculo), verifico os próximos caracteres para determinar se formam "on" ou "off". Se for "on", ativo a flag e continuo a leitura. Se for "off", desativo a flag e ignoro os números subsequentes até encontrar um novo "on".  

Se o caractere encontrado for "=", imprimo o total acumulado até aquele momento. O programa pode processar tanto a entrada digitada pelo usuário quanto um arquivo passado como argumento.  

**Notas:**  
Assumo que é necessário ativar o modo de soma antes de considerar qualquer número, ou seja, deve haver um "on" inicial. Além disso, qualquer ocorrência de "on" ou "off" no texto será considerada, mesmo que faça parte de uma palavra maior. Isso significa que palavras como "one" serão interpretadas como um "on" válido.

## Instrução de utilização
Há duas maneiras de executar o programa .

1. Indicando o path do ficheiro
 ```sh
    $ python3 somador_OnOff.py <file_path>
```

2. Utilizando o stdin
 ```sh
    $ python3 somador_OnOff.py
```