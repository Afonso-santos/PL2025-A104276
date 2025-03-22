import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()