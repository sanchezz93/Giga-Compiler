import sys
sys.path.insert(0, "../..")

from Cube import *

if sys.version_info[0] >= 3:
	raw_input = input

#Define global variables

globalVarCount = {}			#10000
globalVarCount[BOOL] = 0	#10000
globalVarCount[INT] = 0		#12500
globalVarCount[FLOAT] = 0	#15000
globalVarCount[CHAR] = 0	#17500

localVarCount = {}			#20000
localVarCount[BOOL] = 0		#20000
localVarCount[INT] = 0		#22500
localVarCount[FLOAT] = 0	#25000
localVarCount[CHAR] = 0		#27500

tempVarCount = {}			#30000
tempVarCount[BOOL] = 0		#30000
tempVarCount[INT] = 0		#32500
tempVarCount[FLOAT] = 0		#35000
tempVarCount[CHAR] = 0		#37500

constVarCount = {}			#40000
constVarCount[BOOL] = 2		#40000
constVarCount[INT] = 1		#42500
constVarCount[FLOAT] = 0	#45000
constVarCount[CHAR] = 0		#47500

quadruples = []
operandStack = []
operationStack = []

constants = {'true':{'value':True, 'type':BOOL, 'dir':''}, 'false':{'value':False, 'type':BOOL}, '-1':{'type':2, 'dir':0, 'value':-1}}
varGlobal = {}
varLocal = {}
funcGlobal = {}
funcParameters = []
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

def p_vars4(p):
	'''vars4 : constant
			| PLUS constant
			| MINUS constant'''
	p[0] = p[1]
	if len(p) > 2:
		p[0] = p[2]
		if p[1] == '-':
			p[0] = '-'+p[2]
def p_vars3(p):
	'''vars3 : empty
			| LEFTSQBKT cteN RIGHTSQBKT convertVariableToArray'''
def p_vars2(p):
	'''vars2 : empty
			| COMMA vars1'''
def p_vars1(p):
	'''vars1 : ID addVariable vars3 ASSIGN vars4'''
	print('vars1')
	print(p[1])
	print(p[5])
	var = {}
	if p[1] in varLocal.keys():
		var = varLocal[p[1]]
	else:
		var = varGlobal[p[1]]
	if '-' in p[5]:
		p[5] = p[5].replace('-','')
		addQuadruple('*', constants['-1'], constants[p[5]], var)
	else:
		addQuadruple('=', constants[p[5]], '', var)


	# var1 = {}
	# if p[1] in varLocal.keys():
	# 	var1 = varLocal[p[1]]
	# else:
	# 	var1 = varGlobal[p[1]]
	# operand = operandStack.pop()
	# resultType = getResultType(var1['type'], '=', operand['type']%10)
	# if resultType > 0:
	# 	addQuadruple('=', operand, '', var1)
	# else:
	# 	print('Error: Assignment type mismatch')
	# 	exit(1)

def p_vars(p):
	'''vars : type vars1 vars2 SEMICOLON'''

def p_func2(p):
	'''func2 : empty
			| RETURN expression SEMICOLON
			| statute func2'''
def p_func1(p):
	'''func1 : VOID saveFuncTypeVoid ID saveFuncName LEFTPAREN parameters RIGHTPAREN LEFTBKT func2 RIGHTBKT
			| funcTypeNext type ID saveFuncName LEFTPAREN parameters RIGHTPAREN LEFTBKT func2 RIGHTBKT'''
	addFunction(lastFuncName, funcType, funcParameters)
	print('local vars: %s' % varLocal)
	resetLocalCounters()
def p_funcg(p):
	'''funcg : FUNC changeToLocalScope func1 changeToGlobalScope'''

def p_maing(p):
	'''maing : MAIN changeToLocalScope block'''
	print('-------- quadruples')
	print(quadruples)
	print('--------')
	print('-------- stacks')
	print(operandStack)
	print(operationStack)
	print('--------')
	print('global vars: %s' % varGlobal)
	print('functions: %s' % funcGlobal)
	print('constants: %s' % constants)

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
			| GREATERTHANEQ saveOperation exp
			| LESSTHANEQ saveOperation exp
			| GREATERTHAN saveOperation exp
			| LESSTHAN saveOperation exp
			| EQUAL saveOperation exp
			| DIFFERENT saveOperation exp
			| OR saveOperation exp
			| AND saveOperation exp'''
	global operationStack
	global operandStack
	if len(operationStack) > 0:
		if operationStack[-1] == '<' or operationStack[-1] == '>' or operationStack[-1] == '<=' or operationStack[-1] == '>=' or operationStack[-1] == '==' or operationStack[-1] == '!=':
			operand1 = operandStack.pop()
			operation = operationStack.pop()
			operand2 = operandStack.pop()
			print('???')
			print(operand1)
			print(operation)
			print(operand2)
			print('???')
			resultType = getResultType(operand1['type']%10, operation, operand2['type']%10)
			print(resultType)
			if resultType > 0:
				addQuadruple(operation, operand1, operand2, 0)
				operandStack.append({'value':0, 'type':resultType})
			else:
				print('Error: Expression type mismatch')
				exit(1)
def p_expression(p):
	'''expression : exp expression1'''


def p_exp1(p):
	'''exp1 : empty
			| PLUS saveOperation exp exp1
			| MINUS saveOperation exp exp1'''
	p[0] = p[1]
	if len(p) > 2:
		p[0] = p[3]
def p_exp(p):
	'''exp : term exp1'''
	p[0] = p[1]
	# print('exp----')
	# print(p[1])
	# print(p[2])

def p_term1(p):
	'''term1 : empty
			| TIMES saveOperation term term1
			| DIVIDE saveOperation term term1'''
def p_term(p):
	'''term : factor term1 termEnded'''

def p_factor1(p):
	'''factor1 : constant
			| PLUS constant
			| MINUS constant'''
	global operandStack
	print(operandStack)
	operand = {}
	if len(p) == 3:
		operand = getOperand(p[2])
	else:
		operand = getOperand(p[1])
	operandStack.append(operand)
def p_factor(p):
	'''factor : LEFTPAREN addFakeBottom expression RIGHTPAREN removeFakeBottom factorEnded
			| factor1 factorEnded'''	

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
	print("call " + p[1])

def p_parameters1(p):
	'''parameters1 : empty
			| COMMA type ID addParameter parameters1'''
def p_parameters(p):
	'''parameters : empty
			| type ID addParameter parameters1'''

def p_constant1(p):
	'''constant1 : empty
			| COMMA cte constant1'''
def p_constant(p):
	'''constant : cte
			| LEFTSQBKT cte constant1 RIGHTSQBKT'''
	if len(p) == 2:
		p[0] = p[1]

def p_cte(p):
	'''cte : ID
			| varArr
			| TRUE
			| FALSE
			| cteN
			| cteS'''
	p[0] = p[1]

def p_cteN(p):
	'''cteN : NUMBERINT addConstant
			| NUMBERFLT addConstant'''
	p[0] = p[1]
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
	p[0] = p[1]
	if not p[1] in varLocal.keys() and not p[1] in varGlobal.keys():
		print('Error: Cannot assign undeclared variable')
		exit(1)
def p_assignement(p):
	'''assignement : assignement1 ASSIGN assignement2 SEMICOLON'''
	print("--------assign ")
	print(operandStack)
	print(operationStack)
	var1 = {}
	if p[1] in varLocal.keys():
		var1 = varLocal[p[1]]
	else:
		var1 = varGlobal[p[1]]
	operand = operandStack.pop()
	resultType = getResultType(var1['type'], '=', operand['type']%10)
	if resultType > 0:
		addQuadruple('=', operand, '', var1)
	else:
		print('Error: Assignment type mismatch')
		exit(1)
	print('--------')

def p_varArr(p):
	'''varArr : ID LEFTSQBKT exp RIGHTSQBKT'''

def p_type(p):
	'''type : TBOOL addType
			| TINT addType
			| TFLOAT addType
			| TCHAR addType'''



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
	
def p_addConstant(p):
	'''addConstant : empty'''
	constType = -1
	cte = num(p[-1])
	if type(cte) is int:
		constType = INT
	else:
		constType = FLOAT
	global constants
	if not str(cte) in constants.keys():
		constants[str(cte)] = {'value':cte, 'type':constType, 'dir':constVarCount[constType]}
		constVarCount[constType] += 1

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
	funcType = VOID

def p_addParameter(p):
	'''addParameter : empty'''
	global lastVarName
	global funcParameters
	lastVarName = p[-1]
	variableName = lastVarName
	addVariable(variableName, variableType)
	funcParameters.append(varLocal[variableName])

def p_addType(p):
	'''addType : empty'''
	global variableType
	global funcTypeNext
	global funcType
	if funcTypeNext:
		funcType = getTypeValue(p[-1])
	else:
		variableType = getTypeValue(p[-1])
	funcTypeNext = False


def p_saveOperation(p):
	'''saveOperation : empty'''
	global operationStack
	operationStack.append(p[-1])

def p_termEnded(p):
	'''termEnded : empty'''
	global operationStack
	global operandStack
	if len(operationStack) > 0:
		if operationStack[-1] == '+' or operationStack[-1] == '-' or operationStack[-1] == '||':
			operand2 = operandStack.pop()
			operation = operationStack.pop()
			operand1 = operandStack.pop()
			resultType = getResultType(operand1['type']%10, operation, operand2['type']%10)
			if resultType > 0:
				addQuadruple(operation, operand1, operand2, 0)
				operandStack.append({'dir':0, 'type':resultType})
			else:
				print('Error: Term type mismatch')
				exit(1)
	p[0] = "hio"

def p_factorEnded(p):
	'''factorEnded : empty'''
	global operationStack
	global operandStack
	if len(operationStack) > 0:
		if operationStack[-1] == '*' or operationStack[-1] == '/' or operationStack[-1] == '&&':
			operand2 = operandStack.pop()
			operation = operationStack.pop()
			operand1 = operandStack.pop()
			resultType = getResultType(operand1['type']%10, operation, operand2['type']%10)
			if resultType > 0:
				addQuadruple(operation, operand1, operand2, 0)
				operandStack.append({'dir':0, 'type':resultType})
			else:
				print('Error: Factor type mismatch')
				exit(1)

def p_addFakeBottom(p):
	'''addFakeBottom : empty'''
	global operationStack
	operationStack.append('(')
def p_removeFakeBottom(p):
	'''removeFakeBottom : empty'''
	global operationStack
	print(operationStack)
	operationStack.pop()

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
	exit(1)


import ply.yacc as yacc
yacc.yacc()



#Functions

def addVariable(variable, varType):
	global varGlobal
	global varLocal
	if variable in funcGlobal.keys():
		print("Variable error: Variable cannot have the same name as a function")
		exit(1)
	if scope == 'global':
		if not variable in varGlobal.keys():
			varGlobal[variable] = {'name':variable, 'type':varType, 'dir':globalVarCount[varType]}
			globalVarCount[varType] += 1
		else:
			print("Variable error: Variable is already declared globally")
			exit(1)
	else:
		if not variable in varLocal.keys():
			varLocal[variable] = {'name':variable, 'type':varType, 'dir':localVarCount[varType]}
			localVarCount[varType] += 1
		else:
			print("Variable error: Variable is already declared locally")
			exit(1)

def convertVariableToArray():
	global varGlobal
	global varLocal
	if scope == 'global':
		varGlobal[lastVarName]['type'] *= 11
	else:
	   varLocal[lastVarName]['type'] *= 11

def addFunction(name, funType, parameters):
	global funcGlobal
	if name in varGlobal.keys():
		print("Function error: Function cannot have the same name as a variable")
		exit(1)
	if not name in funcGlobal.keys():
		funcGlobal[name] = {'name':name, 'type':funType, 'parameters':parameters, 'boolCount':localVarCount[BOOL], 'intCount':localVarCount[INT], 'floatCount':localVarCount[FLOAT], 'charCount':localVarCount[CHAR], 'boolTempCount':tempVarCount[BOOL], 'intTempCount':tempVarCount[INT], 'floatTempCount':tempVarCount[FLOAT], 'charTempCount':tempVarCount[CHAR]}
	else:
		print("Function error: Function is already declared")
		exit(1)

def addQuadruple(operation, var1, var2, result):
	global quadruples
	quadruples.append({'op':operation, 'var1':var1, 'var2':var2, 'result':result})

def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)

def getOperand(key):
	if key in constants.keys():
		return constants[key]
	elif key in varLocal.keys():
		return varLocal[key]
	elif key in varGlobal.keys():
		return varGlobal[key]

def resetLocalCounters():
	global varLocal
	global funcParameters
	global localVarCount
	global tempVarCount
	varLocal = {}
	funcParameters = []
	localVarCount[BOOL] = 0
	localVarCount[INT] = 0
	localVarCount[FLOAT] = 0
	localVarCount[CHAR] = 0
	tempVarCount[BOOL] = 0
	tempVarCount[INT] = 0
	tempVarCount[FLOAT] = 0
	tempVarCount[CHAR] = 0

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