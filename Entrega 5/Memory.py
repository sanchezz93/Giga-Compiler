from Giga import *
from Cube import *

class Memory:

	def __init__(self, name, variables, tempVariables):
		self.name = name
		# alocates memory by data type 
		# variables 
		# self.int = variables[Amount of type] * [""] 
		# creates a list of variables 
		
		self.bools = variables[BOOL] * [""]
		self.ints = variables[INT] * [""]
		self.floats = variables[FLOAT] * [""]
		self.strings = variables[STRING] * [""]

		self.tempBools = (tempVariables[BOOL] - INITIALTEMPBOOL) * [""]
		self.tempInts = (tempVariables[INT] - INITIALTEMPINT) * [""]
		self.tempFloats = (tempVariables[FLOAT] - INITIALTEMPFLOAT) * [""]
		self.tempString = (tempVariables[STRING] - INITIALTEMPSTRING) * [""]
		
	def getGeneralInfo(self, address):
		if address >= INITALGLOBALBOOL and address < INITIALGLOBALSTRING:
			if address >= INITIALGLOBALBOOL and address < INITIALGLOABLINT:
				offset = address - INITIALGLOBALBOOL 
				variableType = BOOL
				return ['GLOBAL', offset , variableType]

			elif address >= INITIALGLOABLINT and address < INITIALGLOBALFLOAT:
				offset = address - INITIALGLOABLINT
				variableType = INT
				return ['GLOBAL', offset, variableType]

			elif adress >= INITIALGLOBALFLOAT and address < INITIALGLOBALSTRING:
				offset = address - INITIALGLOBALFLOAT 
				variableType = FLOAT
				return ['GLOBAL', offset, variableType]

			elif address >= INITIALGLOBALSTRING and address < INITIALLOCALBOOL:
				offset = address - INITIALGLOBALSTRING
				variableType = STRING
				return ['GLOBAL', offset, variableType]

		elif address >= INITIALLOCALBOOL and address < INITIALLOCALSTRING:
			if address >= INITIALLOCALBOOL and address < INITIALLOCALINT:
				offset = address - INITIALLOCALBOOL 
				variableType = BOOL
				return ['LOCAL', offset , variableType]

			elif address >= INITIALLOCALINT and address < INITIALLOCALFLOAT:
				offset = address - INITIALLOCALINT
				variableType = INT
				return ['LOCAL', offset, variableType]

			elif adress >= INITIALLOCALFLOAT and address < INITIALLOCALSTRING:
				offset = address - INITIALLOCALFLOAT 
				variableType = FLOAT
				return ['LOCAL', offset, variableType]

			elif address >= INITIALLOCALSTRING and address < INITIALTEMPBOOL:
				offset = address - INITIALLOCALSTRING
				variableType = STRING
				return ['LOCAL', offset, variableType]

		elif address >= INITIALTEMPBOOL and address < INITIALTEMPSTRING:
			if address >= INITIALTEMPBOOL and address < INITIALTEMPINT:
				offset = address - INITIALTEMPBOOL 
				variableType = BOOL
				return ['TEMP', offset , variableType]

			elif address >= INITIALTEMPINT and address < INITIALTEMPFLOAT:
				offset = address - INITIALTEMPINT
				variableType = INT
				return ['TEMP', offset, variableType]

			elif adress >= INITIALTEMPFLOAT and address < INITIALTEMPSTRING:
				offset = address - INITIALTEMPFLOAT 
				variableType = FLOAT
				return ['TEMP', offset, variableType]

			elif address >= INITIALTEMPSTRING and address < INITIALCONSTBOOL:
				offset = address - INITIALTEMPSTRING
				variableType = STRING
				return ['TEMP', offset, variableType]

		elif address >= INITIALCONSTBOOL and address < INTIALCONSTSTRING:
			if address >= INITIALCONSTBOOL and address < INITIALCONSTINT:
				offset = address - INITIALCONSTBOOL 
				variableType = BOOL
				return ['CONSTANT', offset , variableType]

			elif address >= INITIALCONSTINT and address < INITIALCONSTFLOAT:
				offset = address - INITIALCONSTINT
				variableType = INT
				return ['CONSTANT', offset, variableType]

			elif adress >= INITIALCONSTFLOAT and address < INTIALCONSTSTRING:
				offset = address - INITIALCONSTFLOAT 
				variableType = FLOAT
				return ['CONSTANT', offset, variableType]

			elif address >= INTIALCONSTSTRING and address < MAXVARIABLECOUNT:
				offset = address - INTIALCONSTSTRING
				variableType = STRING
				return ['CONSTANT', offset, variableType]

	def getArrayOfType(self, scope, varType):
		if scope == 'GLOBAL' or scope == 'LOCAL':
			if varType == BOOL:
				return self.bools
			elif varType == INT:
				return self.ints
			elif varType == FLOAT:
				return self.floats
			elif varType == STRING:
				return self.strings
		elif scope == 'TEMP':
			if varType == BOOL:
				return self.tempBools
			elif varType == INT:
				return self.tempInts
			elif varType == FLOAT:
				return self.tempFloats
			elif varType == STRING:
				return self.tempString


	def getValueAtAddress(self, address, constants):
		scope = self.getGeneralInfo(address)[0]
		offset = self.getGeneralInfo(adress)[1]
		variableType = self.getGeneralInfo(address)[2]

		if scope != 'CONSTANT':
			mem = getArrayOfType(scope, variableType)
			if offset > len(mem) 
				print("Error variable doesn't exist")
				exit(1)
			return mem[offset]
		else:
			keys = constants.keys()
			counter = 0 
			for key in constants:
				if(constants[key]['Dir'] == address):
					return keys[counter]
				counter +=1


	def storeValue(self, address, value):
		scope = self.getGeneralInfo(address)[0]
		offset = self.getGeneralInfo(address)[1]
		variableType = self.getGeneralInfo(address)[2]
		mem = self.getArrayOfType(scope, variableType)

		if offset >= len(mem):
			print(" Error address doesn't exist")
			exit(1)
		mem[offset] = value






