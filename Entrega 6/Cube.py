#Semantic Cube for the project Giga Compiler 
# Variables defined 


VOID = 0
BOOL = 1
BOOLARRAY = 11
INT = 2
INTARRAY = 22
FLOAT = 3
FLOATARRAY = 33
STRING = 4
STRINGARRAY = 44
POINTER = 5

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


INITIALGLOBALBOOL = 10000
INITIALGLOBALINT = 12500
INITIALGLOBALFLOAT = 15000
INITIALGLOBALSTRING = 17500

INITIALLOCALBOOL = 20000
INITIALLOCALINT = 22500
INITIALLOCALFLOAT = 25000
INITIALLOCALSTRING = 27500

INITIALTEMPBOOL = 30000
INITIALTEMPINT = 32500
INITIALTEMPFLOAT = 35000
INITIALTEMPSTRING = 37500


INITIALCONSTBOOL = 40000
INITIALCONSTINT = 42500
INITIALCONSTFLOAT = 45000
INITIALCONSTSTRING = 47500
MAXVARIABLECOUNT = 50000


INITIALPOINTER = MAXVARIABLECOUNT


varDictionary = {}

#Assign
varDictionary['bool=bool'] = BOOL
varDictionary['int=int'] = INT
varDictionary['float=int'] = FLOAT
varDictionary['float=float'] = FLOAT
varDictionary['string=string'] = STRING

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
varDictionary['int/int'] = INT
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
varDictionary['string==string'] = BOOL


#Different
varDictionary['bool!=bool'] = BOOL
varDictionary['int!=int'] = BOOL
varDictionary['int!=float'] = BOOL
varDictionary['float!=int'] = BOOL
varDictionary['float!=float'] = BOOL
varDictionary['string!=string']  = BOOL


#And
varDictionary['bool&&bool'] = BOOL


#Or
varDictionary['bool||bool'] = BOOL


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
		return 'string'
	elif type == 44:
		return 'stringArray'

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
	elif 'string' == type:
		return STRING
	elif 'stringArray' == type:
		return STRINGARRAY

def getResultType(operand1, operator, operand2):
	s1 = getTypeString(operand1)
	s2 = operator
	s3 = getTypeString(operand2)
	key = s1+s2+s3
	if not key in varDictionary.keys():
		return -1
	else:
		return varDictionary[key]



