#Semantic Cube for the project Giga Compiler 
# Variables defined 


VOID = 0
BOOL = 1
BOOLARRAY = 11
INT = 2
INTARRAY = 22
FLOAT = 3
FLOATARRAY = 33
CHAR = 4
CHARARRAY = 44

ASSIGN = 100
PLUS = 101
MINUS = 102
TIMES = 103
DIVIDE = 104
LESSTHAN = 105
GREATERTHAN = 106
LESSTHANEQ = 107
GREATERTHANEQ = 108
EQUAL = 109
DIFFERENT = 110
OR = 111
AND = 112



varDictionary = {}

#Assign
varDictionary['bool=bool'] = BOOL
varDictionary['int=int'] = INT
varDictionary['float=int'] = FLOAT
varDictionary['float=float'] = FLOAT
varDictionary['char=char'] = CHAR

#Sums
varDictionary['int+int'] = INT
varDictionary['int+float'] = FLOAT
varDictionary['float+int'] = FLOAT
varDictionary['float+float'] = FLOAT

#Substraction
varDictionary['int-int'] = INT
varDictionary['int-float'] = FLOAT
varDictionary['float-int'] = FLOAT
varDictionary['float-float'] = FLOAT

#Multiplication
varDictionary['int*int'] = INT
varDictionary['int*float'] = FLOAT
varDictionary['float*float'] = FLOAT
varDictionary['float*int'] = FLOAT

#Division
varDictionary['int/int'] = FLOAT
varDictionary['int/float'] = FLOAT
varDictionary['float/int'] = FLOAT
varDictionary['float/float'] = FLOAT

#Less Than
varDictionary['int<int'] = BOOL
varDictionary['int<float'] = BOOL
varDictionary['float<int'] = BOOL
varDictionary['float<float'] = BOOL

#Greater Than
varDictionary['int>int'] = BOOL
varDictionary['int>float'] = BOOL
varDictionary['float>int'] = BOOL
varDictionary['float>float'] = BOOL


#Less than or equal to
varDictionary['int<=int'] = BOOL
varDictionary['int<=float'] = BOOL
varDictionary['float<=int'] = BOOL
varDictionary['float<=float'] = BOOL


#Greater than or equal to
varDictionary['int>=int'] = BOOL
varDictionary['int>=float'] = BOOL
varDictionary['float>=int'] = BOOL
varDictionary['float>=float'] = BOOL


#Is equal
varDictionary['bool==bool'] = BOOL
varDictionary['int==int'] = BOOL
varDictionary['int==float'] = BOOL
varDictionary['float==int'] = BOOL
varDictionary['float==float'] = BOOL
varDictionary['char==char'] = BOOL


#Different
varDictionary['bool!=bool'] = BOOL
varDictionary['int!=int'] = BOOL
varDictionary['int!=float'] = BOOL
varDictionary['float!=int'] = BOOL
varDictionary['float!=float'] = BOOL
varDictionary['char!=char']  = BOOL


def getTypeString(type):
	if type == 1:
		return 'bool'
	elif type == 11:
		return 'boolArray'
	elif type == 2:
		return 'int'
	elif type == 22:
		return 'intArray'
	elif type == 3:
		return 'float'
	elif type == 33:
		return 'floatArray'
	elif type == 4:
		return 'char'
	elif type == 44:
		return 'charArray'

def getTypeValue(type):
	if 'bool' == type:
		return BOOL
	elif 'boolArray' == type:
		return BOOLARRAY
	elif 'int' == type:
		return INT
	elif 'intArray' == type:
		return INTARRAY
	elif 'float' == type:
		return FLOAT
	elif 'floatArray' == type:
		return FLOATARRAY
	elif 'char' == type:
		return CHAR
	elif 'charArray' == type:
		return CHARARRAY

def getResultType(operand1, operator, operand2):
	s1 = getTypeString(operand1)
	s2 = operator
	s3 = getTypeString(operand2)
	key = s1+s2+s3
	if not key in varDictionary.keys():
		return -1
	else:
		return varDictionary[key]



