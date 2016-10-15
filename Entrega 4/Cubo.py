#Semantic Cube for the project Giga Compiler 
# Variables defined 

typesValues = {'void':0,
				'bool':1,
				'boolArray':11,
				'int':2,
				'intArray':22,
				'float':3,
				'floatArray':33,
				'char':4,
				'charArray':44}

#Assign
varDictionary['bool=bool'] = typesValues['bool']
varDictionary['int=int'] = typesValues['int']
varDictionary['float=int'] = typesValues['float']
varDictionary['float=float'] = typesValues['float']
varDictionary['char=char'] = typesValues['char']

#Sums
varDictionary['int+int'] = typesValues['int']
varDictionary['int+float'] = typesValues['float']
varDictionary['float+int'] = typesValues['float']
varDictionary['float+float'] = typesValues['float']

#Substraction
varDictionary['int-int'] = typesValues['int']
varDictionary['int-float'] = typesValues['float']
varDictionary['float-int'] = typesValues['float']
varDictionary['float-float'] = typesValues['float']

#Multiplication
varDictionary['int*int'] = typesValues['int']
varDictionary['int*float'] = typesValues['float']
varDictionary['float*float'] = typesValues['float']
varDictionary['float*int'] = typesValues['float']

#Division
varDictionary['int/int'] = typesValues['float']
varDictionary['int/float'] = typesValues['float']
varDictionary['float/int'] = typesValues['float']
varDictionary['float/float'] = typesValues['float']

#Less Than
varDictionary['int<int'] = typesValues['bool']
varDictionary['int<float'] = typesValues['bool']
varDictionary['float<int'] = typesValues['bool']
varDictionary['float<float'] = typesValues['bool']

#Greater Than
varDictionary['int>int'] = typesValues['bool']
varDictionary['int>float'] = typesValues['bool']
varDictionary['float>int'] = typesValues['bool']
varDictionary['float>float'] = typesValues['bool']


#Less than or equal to
varDictionary['int<=int'] = typesValues['bool']
varDictionary['int<=float'] = typesValues['bool']
varDictionary['float<=int'] = typesValues['bool']
varDictionary['float<=float'] = typesValues['bool']


#Greater than or equal to
varDictionary['int>=int'] = typesValues['bool']
varDictionary['int>=float'] = typesValues['bool']
varDictionary['float>=int'] = typesValues['bool']
varDictionary['float>=float'] = typesValues['bool']


#Is equal
varDictionary['bool==bool'] = typesValues['bool']
varDictionary['int==int'] = typesValues['bool']
varDictionary['int==float'] = typesValues['bool']
varDictionary['float==int'] = typesValues['bool']
varDictionary['float==float'] = typesValues['bool']
varDictionary['char==char'] = typesValues['bool']


#Different
varDictionary['bool!=bool'] = typesValues['bool']
varDictionary['int!=int'] = typesValues['bool']
varDictionary['int!=float'] = typesValues['bool']
varDictionary['float!=int'] = typesValues['bool']
varDictionary['float!=float'] = typesValues['bool']
varDictionary['char!=char']  = typesValues['bool']


def determineTypeString(type):
	if type == 1 :  
		return 'bool'
	else if type == 2: 
		return 'int'
	else if type == 3:
		return 'float'
	else if type == 4:
		return 'char'


def getResultType ( operand1,operator,operand2):
	s1 = determineTypeString(operand1)
	s2 = operator
	s3 = determineTypeString(operand2)
	return varDictionary[s1+s2+s3]



