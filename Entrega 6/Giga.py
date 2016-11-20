import sys
sys.path.insert(0, "../..")

from Cube import *
from Machine import * 

if sys.version_info[0] >= 3:
	raw_input = input

#Define global variables

globalVarCount = {}			#10000
globalVarCount[BOOL] = INITIALGLOBALBOOL
globalVarCount[INT] = INITIALGLOBALINT
globalVarCount[FLOAT] = INITIALGLOBALFLOAT
globalVarCount[STRING] = INITIALGLOBALSTRING

localVarCount = {}			#20000
localVarCount[BOOL] = INITIALLOCALBOOL
localVarCount[INT] =  INITIALLOCALINT
localVarCount[FLOAT] =  INITIALLOCALFLOAT
localVarCount[STRING] =  INITIALLOCALSTRING

tempVarCount = {}			#30000
tempVarCount[BOOL] = INITIALTEMPBOOL
tempVarCount[INT] =  INITIALTEMPINT
tempVarCount[FLOAT] = INITIALTEMPFLOAT
tempVarCount[STRING] = INITIALTEMPSTRING

constVarCount = {}			#40000
constVarCount[BOOL] = INITIALCONSTBOOL
constVarCount[INT] = INITIALCONSTINT
constVarCount[FLOAT] = INITIALCONSTFLOAT
constVarCount[STRING] = INITIALCONSTSTRING

pointerCount = INITIALPOINTER

quadruples = []
operandStack = []
operationStack = []
jumpStack = []
cteArrayStack = []
sendParams = []
argumentCount = 0

constants = {'true':{'value':True, 'type':BOOL, 'dir':constVarCount[BOOL]+1}, 'false':{'value':False, 'type':BOOL, 'dir':constVarCount[BOOL]}, '-1':{'value':-1, 'type':INT, 'dir':constVarCount[INT]}}
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

constVarCount[BOOL] += 2
constVarCount[INT] += 1

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
	r'\"[^\"]*\"'
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



def p_functions(p):
	'''functions : empty
			| funcg functions'''
def p_globalVars(p):
	'''globalVars : empty
			| vars globalVars'''
def p_moduleg(p):
	'''moduleg : MODULE ID LEFTBKT globalVars jumpToMain functions maing RIGHTBKT'''


def p_vars3(p):
	'''vars3 : LEFTSQBKT cteN RIGHTSQBKT'''
	convertVariableToArray(num(p[2]))
def p_vars2(p):
	'''vars2 : empty
			| COMMA vars1 vars2'''
def p_vars1(p):
	'''vars1 : ID addVariable ASSIGN signedCte
			| ID addVariable vars3 ASSIGN constantArray'''
	var = {}
	verifyVar(p[1])
	if p[1] in varLocal.keys():
		var = varLocal[p[1]]
	else:
		var = varGlobal[p[1]]
	if var['type'] < 10:
		if '-' in p[4]:
			p[4] = p[4].replace('-','')
			addQuadruple('*', constants['-1']['dir'], constants[p[4]]['dir'], var['dir'])
		else:
			addQuadruple('=', constants[p[4]]['dir'], '', var['dir'])
		if getResultType(var['type']%10, '=', constants[p[4]]['type']%10) < 0:
			error('Error: Assignment type mismatch')
	else:#array
		if var['size'] == len(cteArrayStack):
			dir = var['dir']
			local = False
			if var in varLocal.keys():
				local = True
			for i in range(0, var['size']):
				value = cteArrayStack.pop()
				if getResultType(var['type']%10, '=', constants[value]['type']%10) < 0:
					error('Error: Assignment type mismatch')
				addQuadruple('=', constants[value]['dir'], '', dir)
				dir += 1
				if local:
					localVarCount[var['type']%10] += 1
				else:
					globalVarCount[var['type']%10] += 1
		else:
			error('Error: Assignment of array does not match the size of the array declared')

def p_vars(p):
	'''vars : type vars1 vars2 SEMICOLON'''

def p_func3(p):
	'''func3 : empty
			| RETURN expression funcReturn SEMICOLON
			| statute func3'''
def p_func2(p):
	'''func2 : empty
			| statute func2'''
def p_func1(p):
	'''func1 : VOID saveFuncTypeVoid ID saveFuncName LEFTPAREN parameters RIGHTPAREN funcStart LEFTBKT func2 RIGHTBKT funcEnd
			| funcTypeNext type ID saveFuncName LEFTPAREN parameters RIGHTPAREN funcStart LEFTBKT func3 RIGHTBKT funcEnd'''
def p_funcg(p):
	'''funcg : FUNC changeToLocalScope func1 changeToGlobalScope'''

def p_maing(p):
	'''maing : MAIN changeToLocalScope completeJumpToMain block'''
	addQuadruple('END', '', '', '')
	print(globalVarCount)
	print('-------- quadruples')
	for i in range(0, len(quadruples)):
		q = quadruples[i]
		print('%s	{var1:%s }		{op:%s }		{var2:%s }		{result:%s }' % (i, q['var1'], q['op'], q['var2'], q['result']))

def p_block1(p):
	'''block1 : empty
			| statute block1'''
def p_block(p):
	'''block : LEFTBKT block1 RIGHTBKT'''

def p_write(p):
	'''write : PRINT LEFTPAREN cte RIGHTPAREN SEMICOLON'''
	var = {}
	if p[3] in varLocal.keys():
		var = varLocal[p[3]]
	elif p[3] in varGlobal.keys():
		var = varGlobal[p[3]]
	else:
		var = constants[p[3]]
	if var['type'] > 10:
		addQuadruple('PRINT', '', '', operandStack.pop()['dir'])
	else:
		addQuadruple('PRINT', '', '', var['dir'])


def p_readg(p):
	'''readg : READ LEFTPAREN varID RIGHTPAREN SEMICOLON'''
	var = {}
	if p[3] in varLocal.keys():
		var = varLocal[p[3]]
	else:
		var = varGlobal[p[3]]
	addQuadruple('READ', '', '', var['dir'])


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
			operand2 = operandStack.pop()
			operation = operationStack.pop()
			operand1 = operandStack.pop()
			resultType = getResultType(operand1['type'], operation, operand2['type'])
			if resultType > 0:
				tempVar = {'dir':tempVarCount[resultType], 'type':resultType}
				addQuadruple(operation, operand1['dir'], operand2['dir'], tempVar['dir'])
				operandStack.append(tempVar)
				tempVarCount[resultType] += 1
			else:
				error('Error: Expression type mismatch')
			p[0] = tempVar
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

def p_term1(p):
	'''term1 : empty
			| TIMES saveOperation term term1
			| DIVIDE saveOperation term term1'''
def p_term(p):
	'''term : factor term1 termEnded'''

def p_factor1(p):
	'''factor1 : cte
			| PLUS cte
			| MINUS cte'''
	global operandStack
	operand = {}
	if len(p) == 3:
		operand = getOperand(p[2])
		if p[1] == '-':
			resultType = getResultType(operand['type'], '*', INT)
			tempVar = {'dir':tempVarCount[resultType], 'type':resultType}
			addQuadruple('*', constants['-1']['dir'], operand, tempVar['dir'])
			operand = tempVar
			tempVarCount[resultType] += 1
	else:
		operand = getOperand(p[1])
	if operand['type'] < 10:
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
	if p[1] is not None:
		if p[1] != VOID:
			print('Warning: Unused function return value.')
			operandStack.pop()


def p_cycle(p):
	'''cycle : WHILE whileStart LEFTPAREN expression RIGHTPAREN whileCheck block whileEnd'''

def p_call2(p):
	'''call2 : empty
			| COMMA expression addArgument call2'''
	global argumentCount
	if argumentCount != len(sendParams):
		error('Error: Number of arguments doesn\'t match number of parameters declared')
	if len(p) == 5:
		argumentCount -= 1
		argument = operandStack.pop()
		parameter = sendParams.pop()
		resultType = getResultType(parameter['type']%10, '=', argument['type']%10)
		if resultType > 0:
			addQuadruple('PARAM', argument['dir'], '', parameter['dir'])
		else:
			error('Error: Argument type doesn\'t match the type of the parameter declared')
def p_call1(p):
	'''call1 : empty
			| expression addArgument call2'''
	global argumentCount
	if argumentCount != len(sendParams):
		error('Error: Number of arguments doesn\'t match number of parameters declared')
	if len(p) == 4:
		argument = operandStack.pop()
		parameter = sendParams.pop()
		resultType = getResultType(parameter['type']%10, '=', argument['type']%10)
		if resultType > 0:
			addQuadruple('PARAM', argument['dir'], '', parameter['dir'])
		else:
			error('Error: Argument type doesn\'t match the type of the parameter declared')
def p_call(p):
	'''call : ID prepareParams LEFTPAREN call1 RIGHTPAREN SEMICOLON'''
	global argumentCount
	argumentCount = 0
	addQuadruple('GOFUNC', '', '', funcGlobal[p[1]]['startQuadruple'])
	if funcGlobal[p[1]]['type'] != VOID:
		operandStack.append(funcGlobal[p[1]])
	p[0] = funcGlobal[p[1]]['type']

def p_prepareParams(p):
	'''prepareParams : empty'''
	global sendParams
	sendParams = list(funcGlobal[p[-1]]['parameters'])
	print(funcGlobal[p[-1]])
	addQuadruple('MEMORY', '', '', funcGlobal[p[-1]])
def p_addArgument(p):
	'''addArgument : empty'''
	global argumentCount
	argumentCount += 1

def p_parameters1(p):
	'''parameters1 : empty
			| COMMA type ID addParameter parameters1'''
def p_parameters(p):
	'''parameters : empty
			| type ID addParameter parameters1'''

def p_constantArray1(p):
	'''constantArray1 : empty
			| COMMA signedCte constantArray1'''
	if len(p) > 2:
		cteArrayStack.append(p[2])
def p_constantArray(p):
	'''constantArray : LEFTSQBKT signedCte constantArray1 RIGHTSQBKT'''
	cteArrayStack.append(p[2])

def p_signedCte(p):
	'''signedCte : cte
			| PLUS cte
			| MINUS cte'''
	p[0] = p[1]
	if len(p) > 2:
		p[0] = p[2]
		if p[1] == '-':
			p[0] = '-'+p[2]
def p_cte(p):
	'''cte : varID
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
	cte = p[1]
	if '\"' in cte:
		cte = cte.replace('\"','')
	global constants
	if not cte in constants.keys():
		constants[cte] = {'value':cte, 'type':STRING, 'dir':constVarCount[STRING]}
		constVarCount[STRING] += 1
	p[0] = cte

def p_condition2(p):
	'''condition2 : empty ifEnd
			| ELSE block ifEnd'''
def p_condition1(p):
	'''condition1 : empty
			| ELSEIF LEFTPAREN expression RIGHTPAREN ifStart2 block ifContinue condition1'''
def p_condition(p):
	'''condition : IF LEFTPAREN expression RIGHTPAREN ifStart block ifContinue condition1 condition2'''

def p_assignement2(p):
	'''assignement2 : call
			| expression SEMICOLON'''
	if p[1] == VOID:
		error('Error: Cannot assign a function of type void.')
def p_assignement1(p):
	'''assignement1 : varID
			| varArr'''
	p[0] = p[1]
	
def p_assignement(p):
	'''assignement : assignement1 ASSIGN assignement2'''
	var = {}
	if p[1] in varLocal.keys():
		var = varLocal[p[1]]
	else:
		var = varGlobal[p[1]]
	operand = operandStack.pop()
	resultType = getResultType(var['type']%10, '=', operand['type']%10)
	if resultType > 0:
		if var['type'] < 10:
			addQuadruple('=', operand['dir'], '', var['dir'])
		else:
			addQuadruple('=', operand['dir'], '', operandStack.pop()['dir'])
	else:
		error('Error: Assignment type mismatch')

def p_varArr(p):
	'''varArr : ID LEFTSQBKT exp RIGHTSQBKT'''
	global pointerCount
	verifyVar(p[1])
	var = {}
	if p[1] in varLocal.keys():
		var = varLocal[p[1]]
	else:
		var = varGlobal[p[1]]
	position = operandStack.pop()['dir']
	addQuadruple('VERIFY', position, '', var['size'])
	addQuadruple('+', var['dir'], position, pointerCount)
	operandStack.append({'dir':pointerCount, 'type':var['type']%10})
	pointerCount += 1
	p[0] = p[1]

def p_varID(p):
	'''varID : ID'''
	verifyVar(p[1])
	var = p[1]
	usesArrayVar = False
	if var in varLocal.keys():
		if varLocal[var]['type'] > 10:
			usesArrayVar = True
	if var in varGlobal.keys():
		if varGlobal[var]['type'] > 10:
			usesArrayVar = True
	if usesArrayVar:
		error('Cannot use array variable without specifying an index.')
	p[0] = p[1]

def p_type(p):
	'''type : TBOOL addType
			| TINT addType
			| TFLOAT addType
			| TSTRING addType'''

def verifyVar(var):
	if not var in varLocal.keys() and not var in varGlobal.keys():
		error('Error: Cannot assign undeclared variable')

# extra grammar
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
			resultType = getResultType(operand1['type'], operation, operand2['type'])
			if resultType > 0:
				tempVar = {'dir':tempVarCount[resultType], 'type':resultType}
				addQuadruple(operation, operand1['dir'], operand2['dir'], tempVar['dir'])
				operandStack.append(tempVar)
				tempVarCount[resultType] += 1
			else:
				error('Error: Term type mismatch')
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
			resultType = getResultType(operand1['type'], operation, operand2['type'])
			if resultType > 0:
				tempVar = {'dir':tempVarCount[resultType], 'type':resultType}
				addQuadruple(operation, operand1['dir'], operand2['dir'], tempVar['dir'])
				operandStack.append(tempVar)
				tempVarCount[resultType] += 1
			else:
				error('Error: Factor type mismatch')

def p_addFakeBottom(p):
	'''addFakeBottom : empty'''
	global operationStack
	operationStack.append('(')
def p_removeFakeBottom(p):
	'''removeFakeBottom : empty'''
	global operationStack
	operationStack.pop()

def p_changeToLocalScope(p):
	'''changeToLocalScope : empty'''
	global scope
	scope = 'local'

def p_changeToGlobalScope(p):
	'''changeToGlobalScope : empty'''
	global scope
	scope = 'global'

def p_ifStart(p):
	'''ifStart : empty'''
	jumpStack.append('IF')
	p_ifStart2(p)

def p_ifStart2(p):
	'''ifStart2 : empty'''
	condition = operandStack.pop()
	if condition['type'] == BOOL:
		addQuadruple('GOTOF', condition['dir'], '', '')
		jumpStack.append(len(quadruples)-1)
	else:
		error('Error: Condition in \'if\' statement must evaluate to a bool.')

def p_ifContinue(p):
	'''ifContinue : empty'''
	addQuadruple('GOTO', '', '', '')
	complete = jumpStack.pop()
	jumpStack.append(len(quadruples)-1)
	completeQuadruple(complete, len(quadruples))

def p_ifEnd(p):
	'''ifEnd : empty'''
	while jumpStack[-1] != 'IF':
		completeQuadruple(jumpStack.pop(), len(quadruples))
	jumpStack.pop()

def p_whileStart(p):
	'''whileStart : empty'''
	jumpStack.append(len(quadruples))

def p_whileCheck(p):
	'''whileCheck : empty'''
	condition = operandStack.pop()
	if condition['type'] == BOOL:
		addQuadruple('GOTOF', condition['dir'], '', '')
		jumpStack.append(len(quadruples)-1)
	else:
		error('Error: Condition in \'if\' statement must evaluate to a bool.')

def p_whileEnd(p):
	'''whileEnd : empty'''
	complete = jumpStack.pop()
	addQuadruple('GOTO', '', '', jumpStack.pop())
	completeQuadruple(complete, len(quadruples))


def p_jumpToMain(p):
	'''jumpToMain : empty'''
	addQuadruple('GOTO', '', '', '')
	jumpStack.append(len(quadruples)-1)

def p_completeJumpToMain(p):
	'''completeJumpToMain : empty'''
	completeQuadruple(jumpStack.pop(), len(quadruples))


def p_funcStart(p):
	'''funcStart : empty'''
	addFunction(lastFuncName, funcType, len(quadruples))
	funcGlobal[lastFuncName]['parameters'] = funcParameters


def p_funcReturn(p):
	'''funcReturn : empty'''
	value = operandStack.pop()
	if value['type'] == funcGlobal[lastFuncName]['type']:
		addQuadruple('RETURN', '', '', value['dir'])
	else:
		error('Error: Type of return value in function doesn\'t match function\'s declared type.')

def p_funcEnd(p):
	'''funcEnd : empty'''
	print('local vars: %s' % varLocal)
	print('temp vars: %s' % tempVarCount)
	funcGlobal[lastFuncName]['boolCount'] = localVarCount[BOOL]
	funcGlobal[lastFuncName]['intCount'] = localVarCount[INT]
	funcGlobal[lastFuncName]['floatCount'] = localVarCount[FLOAT]
	funcGlobal[lastFuncName]['stringCount'] = localVarCount[STRING]
	funcGlobal[lastFuncName]['boolTempCount'] = tempVarCount[BOOL]
	funcGlobal[lastFuncName]['intTempCount'] = tempVarCount[INT]
	funcGlobal[lastFuncName]['floatTempCount'] = tempVarCount[FLOAT]
	funcGlobal[lastFuncName]['stringTempCount'] = tempVarCount[STRING]
	resetLocalCounters()
	addQuadruple('ENDFUNC', '', '', '')


def p_error(p):
	if p:
		error("Syntax error at '%s'" % p)#p.value)
	else:
		error("Syntax error at EOF")


import ply.yacc as yacc
yacc.yacc()



#Functions

def error(str):
	print(str)
	exit(1)

def addVariable(variable, varType):
	global varGlobal
	global varLocal
	if variable in funcGlobal.keys():
		error("Variable error: Variable cannot have the same name as a function")
	if scope == 'global':
		if not variable in varGlobal.keys():
			varGlobal[variable] = {'name':variable, 'type':varType, 'dir':globalVarCount[varType]}
			globalVarCount[varType] += 1
		else:
			error("Variable error: Variable is already declared globally")
	else:
		if not variable in varLocal.keys():
			varLocal[variable] = {'name':variable, 'type':varType, 'dir':localVarCount[varType]}
			localVarCount[varType] += 1
		else:
			error("Variable error: Variable is already declared locally")

def convertVariableToArray(size):
	global varGlobal
	global varLocal
	if scope == 'global':
		globalVarCount[varGlobal[lastVarName]['type']] += (size - 1)
		varGlobal[lastVarName]['type'] *= 11
		varGlobal[lastVarName]['size'] = size
	else:
		localVarCount[varLocal[lastVarName]['type']] += (size - 1)
		varLocal[lastVarName]['type'] *= 11
		varLocal[lastVarName]['size'] = size

def addFunction(name, funType, startQuadruple):
	global funcGlobal
	if name in varGlobal.keys():
		error("Function error: Function cannot have the same name as a variable")
	if not name in funcGlobal.keys():
		funcGlobal[name] = {'name':name, 'type':funType, 'startQuadruple':startQuadruple}
		if funType != 0:
			funcGlobal[name]['dir'] = globalVarCount[funType]
			globalVarCount[funType] += 1
	else:
		error("Function error: Function is already declared")

def addQuadruple(operation, var1, var2, result):
	global quadruples
	quadruples.append({'op':operation, 'var1':var1, 'var2':var2, 'result':result})

def completeQuadruple(index, newValue):
	quadruples[index]['result'] = newValue

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
	localVarCount[BOOL] = 20000
	localVarCount[INT] = 22500
	localVarCount[FLOAT] = 25000
	localVarCount[STRING] = 27500
	tempVarCount[BOOL] = 30000
	tempVarCount[INT] = 32500
	tempVarCount[FLOAT] = 35000
	tempVarCount[STRING] = 37500



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
			executeVirtualMachine(funcGlobal, quadruples, constants, globalVarCount, tempVarCount, localVarCount, pointerCount)
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
