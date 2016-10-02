import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

reserved = {
    'module' : 'MODULE',
    'main' : 'MAIN',
    'func' : 'FUNC',
    'print' : 'PRINT',
    'read' : 'READ',
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'void' : 'VOID',
    'while' : 'WHILE',
    'bool' : 'TBOOL',
    'int' : 'TINT',
    'float' : 'TFLOAT',
    'char' : 'TCHAR',
    'string' : 'TSTRING'
}

tokens = [
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESSTHAN', 'GREATERTHAN', 'LESSTHANEQ', 'GREATERTHANEQ', 'EQUAL', 'DIFFERENT', 'OR', 'AND',
    'LEFTBKT', 'RIGHTBKT', 'LEFTSQBKT', 'RIGHTSQBKT', 'LEFTPAREN', 'RIGHTPAREN', 'COMMA', 'SEMICOLON',

    'ID', 'NUMBERINT', 'NUMBERFLT', 'STRING'
] + list(reserved.values())

#literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

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
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

t_NUMBERINT = r'[0-9]+'
t_NUMBERFLT = r'[0-9]+\.[0-9]+'
t_STRING = r'\"[a-zA-Z0-9_]*\"'

t_ignore = " \t"

def  t_ID(t):
    r'[a-z_][a-zA-Z0-9_]*'
    # print(t)
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()


start = 'moduleg'

# For using empty
def p_empty(p):
    '''empty :'''
    pass

def p_moduleg(p):
    '''moduleg : MODULE ID LEFTBKT module1 maing RIGHTBKT'''
def p_module1(p):
    '''module1 : empty
            | vars module1
            | funcg module1'''

def p_vars3(p):
    '''vars3 : empty
            | LEFTSQBKT cteN RIGHTSQBKT'''
def p_vars2(p):
    '''vars2 : empty
            | COMMA vars1'''
def p_vars1(p):
    '''vars1 : ID vars3 ASSIGN constant'''
def p_vars(p):
    '''vars : type vars1 vars2 SEMICOLON'''

def p_func1(p):
    '''func1 : VOID ID LEFTPAREN arguments RIGHTPAREN LEFTBKT RIGHTBKT
            | type ID LEFTPAREN arguments RIGHTPAREN LEFTBKT RIGHTBKT'''
def p_funcg(p):
    '''funcg : FUNC func1'''

def p_maing(p):
    '''maing : MAIN block'''

def p_block1(p):
    '''block1 : empty
            | statute block1'''
def p_block(p):
    '''block : LEFTBKT block1 RIGHTBKT'''

def p_write(p):
    '''write : PRINT LEFTPAREN cte RIGHTPAREN SEMICOLON'''

def p_readg(p):
    '''readg : READ LEFTPAREN ID RIGHTPAREN SEMICOLON'''


def p_expression1(p):
    '''expression1 : empty
            | GREATERTHANEQ exp
            | LESSTHANEQ exp
            | GREATERTHAN exp
            | LESSTHAN exp
            | EQUAL exp
            | DIFFERENT exp
            | OR exp
            | AND exp'''
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
            | factor1 constant'''

def p_statute(p):
    '''statute : assignement
            | vars
            | condition
            | readg
            | write
            | call
            | cycle'''

def p_cycle(p):
    '''cycle : WHILE LEFTPAREN expression RIGHTPAREN block'''

def p_call2(p):
    '''call2 : empty
            | COMMA exp call2'''
def p_call1(p):
    '''call1 : empty
            | exp call2'''
def p_call(p):
    '''call : ID LEFTPAREN call1 RIGHTPAREN SEMICOLON'''

def p_arguments1(p):
    '''arguments1 : empty
            | COMMA type ID arguments1'''
def p_arguments(p):
    '''arguments : empty
    		| type ID arguments1'''

def p_constant1(p):
    '''constant1 : empty
            | COMMA cte constant1'''
def p_constant(p):
    '''constant : cte
            | LEFTSQBKT cte constant1 RIGHTSQBKT'''

def p_cte(p):
    '''cte : ID
            | varArr
            | TRUE
            | FALSE
            | cteN
            | cteS'''

def p_cteN(p):
    '''cteN : NUMBERINT
            | NUMBERFLT'''

def p_cteS(p):
    '''cteS : STRING'''

def p_condition2(p):
    '''condition2 : empty
            | ELSE block'''
def p_condition1(p):
    '''condition1 : empty
            | ELSEIF LEFTPAREN expression RIGHTPAREN block condition1'''
def p_condition(p):
    '''condition : IF LEFTPAREN expression RIGHTPAREN block condition1 condition2'''

def p_assignement2(p):
    '''assignement2 : call
            | expression'''
def p_assignement1(p):
    '''assignement1 : ID
            | varArr'''
def p_assignement(p):
    '''assignement : assignement1 ASSIGN assignement2 SEMICOLON'''

def p_varArr(p):
    '''varArr : ID LEFTSQBKT exp RIGHTSQBKT'''

def p_type(p):
	'''type : TBOOL
			| TINT
			| TFLOAT
			| TCHAR
			| TSTRING'''

# module id { main { int i=0; }}

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)#p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc
yacc.yacc()


# Main
if __name__ == '__main__':
	# Check for file
	if (len(sys.argv) > 1):
		file = sys.argv[1]
		# Open file
		try:
			f = open(file, 'r')
			data = f.read()
			f.close()
			# Parse the data
			if (yacc.parse(data, tracking = True) == 'OK'):
				print(dirProc);
		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')
		while 1:
		    try:
		        s = raw_input('')
		    except EOFError:
		        break
		    if not s:
		        continue
		    yacc.parse(s)