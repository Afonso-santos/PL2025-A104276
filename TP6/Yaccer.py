import ply.yacc as yacc
from Lexer import tokens
import sys

def p_geral(p):
    '''
    geral : expression
    '''
    p[0] = p[1]

def p_expression(p):
    '''
    expression : term expres
    '''
    p[0] = p[1] + p[2] if isinstance(p[2], int) else p[1]

def p_expres_plus(p):
    '''
    expres : PLUS expression
    '''
    p[0] = p[2]

def p_expres_minus(p):
    '''
    expres : MINUS expression
    '''
    p[0] = -p[2]

def p_expres_empty(p):
    '''
    expres : empty
    '''
    p[0] = 0

def p_term(p):
    '''
    term : factor termaux
    '''
    p[0] = p[1] * p[2] if isinstance(p[2], int) else p[1]

def p_termaux_times(p):
    '''
    termaux : TIMES term
    '''
    p[0] = p[2]

def p_termaux_divide(p):
    '''
    termaux : DIVIDE term
    '''
    p[0] = 1 / p[2]

def p_termaux_empty(p):
    '''
    termaux : empty
    '''
    p[0] = 1

def p_factor_parentheses(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = p[2]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = int(p[1])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = 1

def p_error(p):
    print("Erro sintático:", p)
    parser.success = False

parser = yacc.yacc()

