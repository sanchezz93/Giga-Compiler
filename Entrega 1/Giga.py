import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'MODULE', 'MAIN', 'FUNC', 'TYPE', 'PRINT', 'READ', 'IF', 'ELSE', 'IFELSE', 'TRUE', 'FALSE', 'VOID', 
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESSTHAN', 'GREATERTHAN', 'LESSTHANEQ', 'GREATERTHANEQ', 'EQUAL', 'DIFFERENT', 'OR', 'AND'
    'LEFTBKT', 'RIGHTBKT', 'LEFTSQBKT', 'RIGHTSQBKT', 'LEFTPAREN', 'RIGHTPAREN', 'COLON', 'COMMA', 'SEMICOLON',

    'ID', 'NUMBERINT', 'NUMBERFLT', 'STRING'
)

#literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

t_MODULE = r'module'
t_MAIN = r'main'
t_FUNC = r'func'
t_TYPE = r'bool|int|float|char|string'
t_PRINT = r'print'
t_READ = r'read'
t_IF = r'if'
t_ELSE = r'else'
t_IFELSE = r'ifelse'
t_TRUE = r'true'
t_FALSE = r'false'
t_VOID = r'void'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_LESSTHANEQ = r'\<='
t_GREATERTHANEQ = r'\>='
t_EQUAL = r'=='
t_DIFFERENT = r'!='
t_OR = r'\|\|'
t_AND = r'&&'
t_LEFTBKT = r'\{'
t_RIGHTBKT = r'\}'
t_LEFTSQBKT = r'\['
t_RIGHTSQBKT = r'\]'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_COLON = r'\:'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

t_ID = r'[a-z_][a-zA-Z0-9_]*'
t_NUMBERINT = r'[0-9]+'
t_NUMBERFLT = r'[0-9]+\.[0-9]+'
t_STRING = r'[a-zA-Z0-9_]+'

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
# precedence = (
#     ('left', '+', '-'),
#     ('left', '*', '/'),
#     ('right', 'UMINUS'),
# )

start = 'module'

# For using ε
def p_empty(p):
    '''empty :'''
    pass

def p_module(p):
    '''module : MODULE ID LEFTBKT module1 main RIGHTBKT'''
def p_module1(p):
    '''module1 : empty
            | vars module1
            | func module1'''

def p_vars(p):
    '''vars : TYPE vars1 vars2 SEMICOLON'''
def p_vars1(p):
    '''vars1 : ID vars3 ASSIGN constant'''
def p_vars2(p):
    '''vars2 : empty
            | COMMA vars1'''
def p_vars3(p):
    '''vars3 : empty
            | LEFTSQBKT constantN RIGHTSQBKT'''

def p_func(p):
    '''func : FUNC VOID ID LEFTPAREN arguments RIGHTPAREN LEFTBKT  RIGHTBKT
            | FUNC TYPE ID LEFTPAREN arguments RIGHTPAREN LEFTBKT  RIGHTBKT'''

def p_main(p):
    '''main : MAIN block'''

def p_block1(p):
    '''block1 : empty
            | statute block1'''
def p_block(p):
    '''block : LEFTBKT block1 RIGHTBKT'''

def p_print(p):
    '''print : PRINT LEFTPAREN cte RIGHTPAREN SEMICOLON'''

def p_read(p):
    '''read : READ LEFTPAREN ID RIGHTPAREN SEMICOLON'''


def p_expression1(p):
    '''expression1 : empty
            | GREATERTHAN exp
            | LESSTHAN exp
            | GREATERTHANEQ exp
            | LESSTHANEQ exp
            | EQUAL exp
            | DIFFERENT exp
            | OR exp
            | AND exp
            | '''
def p_expression(p):
    '''expression : exp expression1'''

def p_exp1(p):
    '''exp1 : empty
            | PLUS term exp1
            | MINUS term exp1'''
def p_exp(p):
    '''exp : term exp1'''

def p_term1(p):
    '''term1 : empty
            | TIMES term1
            | DIVIDE term1'''
def p_term(p):
    '''term : factor term1'''

def p_factor1(p):
    '''factor1 : empty
            | PLUS
            | MINUS'''
def p_factor(p):
    '''factor : LEFTPAREN expression RIGHTPAREN
            | factor1 varcte'''

def p_statute(p):
    '''statute : assignement
            | condition
            | read
            | write
            | call
            | cycle'''




def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)#p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
