import re

def tokenize(code):
    token_specification = [
        ('KEYWORD', r'select|where|limit', re.IGNORECASE),
        ('VAR', r'\?[a-zA-Z_][a-zA-Z_0-9]*'),
        ('URI', r'dbo:[a-zA-Z_][a-zA-Z_0-9]*|foaf:[a-zA-Z_][a-zA-Z_0-9]*'),
        ('STRING', r'".*?"(@[a-zA-Z]+)?'),
        ('NUMBER', r'\d+'),
        ('SYMBOL', r'[{}.]'),
        ('WHITESPACE', r'\s+'),
        ('UNKNOWN', r'.'),
    ]

    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex, *_ in token_specification)
    tokens = []
    line_num = 1

    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group(kind)
        
        if kind == 'WHITESPACE':
            line_num += value.count('\n')
        elif kind == 'UNKNOWN':   
            pass
        elif kind == 'NUMBER':
            tokens.append((value, 'NUMBER'))
        elif kind == 'STRING':
            tokens.append((value, 'STRING'))
        elif kind == 'VAR':
            tokens.append((value, 'VAR'))
        elif kind == 'URI':
            tokens.append((value, 'URI'))
        elif kind == 'KEYWORD':
            tokens.append((value, 'KEYWORD'))
        elif kind == 'SYMBOL':
            tokens.append((value, 'SYMBOL'))
    
    return tokens

# Exemplo de uso
query = """
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""

tokens = tokenize(query)
for token in tokens:
    print(token)
