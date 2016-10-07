import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

#Define global variables

varGlobal = {}
varLocal = {}
funcGlobal = {}
funcArguments = []
variableType = None
funcType = None
lastVarName = None
lastFuncName = None
funcTypeNext = False
scope = 'global'



# Tokens

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
    'string' : 'TSTRING',
    'return' : 'RETURN'
}

tokens = [
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESSTHAN', 'GREATERTHAN', 'LESSTHANEQ', 'GREATERTHANEQ', 'EQUAL', 'DIFFERENT', 'OR', 'AND',
    'LEFTBKT', 'RIGHTBKT', 'LEFTSQBKT', 'RIGHTSQBKT', 'LEFTPAREN', 'RIGHTPAREN', 'COMMA', 'SEMICOLON',

    'ID', 'NUMBERINT', 'NUMBERFLT', 'STRING'
] + list(reserved.values())

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

t_ignore = " \t"

def  t_ID(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
	r'\".*\"'
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
            | LEFTSQBKT cteN RIGHTSQBKT convertVariableToArray'''
def p_vars2(p):
    '''vars2 : empty
            | COMMA vars1'''
def p_vars1(p):
    '''vars1 : ID addVariable vars3 ASSIGN constant'''
def p_vars(p):
    '''vars : type vars1 vars2 SEMICOLON'''

def p_func2(p):
	'''func2 : empty
    		| RETURN expression SEMICOLON
			| statute func2'''
def p_func1(p):
	'''func1 : VOID saveFuncTypeVoid ID saveFuncName LEFTPAREN arguments RIGHTPAREN LEFTBKT func2 RIGHTBKT
	        | funcTypeNext type ID saveFuncName LEFTPAREN arguments RIGHTPAREN LEFTBKT func2 RIGHTBKT'''
	global varLocal
	global funcArguments
	addFunction(lastFuncName, funcType, funcArguments)
	print('local vars: %s' % varLocal)
	varLocal = {}
	funcArguments = []
def p_funcg(p):
	'''funcg : FUNC changeToLocalScope func1 changeToGlobalScope'''

def p_maing(p):
	'''maing : MAIN changeToLocalScope block'''
	print('local vars: %s' % varLocal)
	print('global vars: %s' % varGlobal)
	print('functions: %s' % funcGlobal)

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
            | PLUS exp exp1
            | MINUS exp exp1'''
def p_exp(p):
    '''exp : term exp1'''

def p_term1(p):
    '''term1 : empty
            | TIMES term term1
            | DIVIDE term term1'''
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
    '''statute : call
            | assignement
            | vars
            | condition
            | readg
            | write
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
            | COMMA type ID addArgument arguments1'''
def p_arguments(p):
    '''arguments : empty
    		| type ID addArgument arguments1'''

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
	'''type : TBOOL addType
			| TINT addType
			| TFLOAT addType
			| TCHAR addType
			| TSTRING addType'''



# extra grammar
def p_convertVariableToArray(p):
	'''convertVariableToArray : empty'''
	convertVariableToArray()

def p_addVariable(p):
    '''addVariable : empty'''
    global lastVarName
    lastVarName = p[-1]
    variableName = lastVarName
    addVariable(variableName, variableType)

def p_saveFuncName(p):
    '''saveFuncName : empty'''
    global lastFuncName
    lastFuncName = p[-1]

def p_funcTypeNext(p):
	'''funcTypeNext : empty'''
	global funcTypeNext
	funcTypeNext = True

def p_saveFuncTypeVoid(p):
	'''saveFuncTypeVoid : empty'''
	global funcType
	funcType = typesValues['void']

def p_addArgument(p):
    '''addArgument : empty'''
    global lastVarName
    global funcArguments
    lastVarName = p[-1]
    variableName = lastVarName
    addVariable(variableName, variableType)
    funcArguments.append(varLocal[variableName])

def p_addType(p):
	'''addType : empty'''
	global variableType
	global funcTypeNext
	global funcType
	if funcTypeNext:
		funcType = typesValues[p[-1]]
	else:
		variableType = typesValues[p[-1]]
	funcTypeNext = False

def p_changeToLocalScope(p):
	'''changeToLocalScope : empty'''
	global scope
	scope = 'local'

def p_changeToGlobalScope(p):
	'''changeToGlobalScope : empty'''
	global scope
	scope = 'global'




def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)#p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc
yacc.yacc()



#Functions

# from enum import Enum
# @unique
# class Types(Enum):
#     boolType = 1
#     boolArrayType = 11
#     intType = 2
#     intArrayType = 22
#     floatType = 3
#     floatArrayType = 33
#     charType = 4
#     charArrayType = 44

typesValues = {'void':0,
				'bool':1,
				'boolArray':11,
				'int':2,
				'intArray':22,
				'float':3,
				'floatArray':33,
				'char':4,
				'charArray':44}


def addVariable(variable, varType):
    global varGlobal
    global varLocal
    if scope == 'global':
        if not variable in varGlobal.keys():
            varGlobal[variable] = {'name':variable, 'type':varType}
        else:
            print("Variable error : Variable is already declared globally")
    else:
        if not variable in varLocal.keys():
            varLocal[variable] = {'name':variable, 'type':varType}
        else:
            print("Variable error : Variable is already declared locally")

def convertVariableToArray():
    global varGlobal
    global varLocal
    if scope == 'global':
        varGlobal[lastVarName]['type'] += 10
    else:
       varLocal[lastVarName]['type'] += 10

def addFunction(name, funType, parameters):
    global funcGlobal
    if not name in funcGlobal.keys():
        funcGlobal[name] = {'name':name, 'type':funType, 'parameters':parameters}
    else:
        print ("Function error : Function is already declared")

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