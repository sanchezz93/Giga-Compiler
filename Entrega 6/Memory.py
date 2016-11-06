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

		if(tempVariables != 0):
			self.tempBools = (tempVariables[BOOL] - INITIALTEMPBOOL) * [""]
			self.tempInts = (tempVariables[INT] - INITIALTEMPINT) * [""]
			self.tempFloats = (tempVariables[FLOAT] - INTIALTEMPFLOAT) * [""]
			self.tempString = (tempVariables[STRING] - INITIALTEMPSTRING) * [""]
		
	def getGeneralInfo(self, address):
		if address >= INITIALGLOBALBOOL and address < INITIALGLOBALSTRING:
			if address >= INITIALGLOBALBOOL and address < INITIALGLOBALINT:
				offset = address - INITIALGLOBALBOOL 
				variableType = BOOL
				return ['GLOBAL', offset , variableType]

			elif address >= INITIALGLOBALINT and address < INITIALGLOBALFLOAT:
				offset = address - INITIALGLOBALINT
				variableType = INT
				return ['GLOBAL', offset, variableType]

			elif adress >= INITIALGLOBALFLOAT and address < INITIALGLOBALBOOL:
				offset = address - INITIALGLOBALFLOAT 
				variableType = FLOAT
				return ['GLOBAL', offset, variableType]

			elif address >= INITIALGLOBALBOOL and address < INTIALLOCALBOOL:
				offset = address - INITIALGLOBALBOOL
				variableType = STRING
				return ['GLOBAL', offset, variableType]

		elif address >= INTIALLOCALBOOL and address < INTIALLOCALSTRING:
			if address >= INTIALLOCALBOOL and address < INTIALLOCALINT:
				offset = address - INTIALLOCALBOOL 
				variableType = BOOL
				return ['LOCAL', offset , variableType]

			elif address >= INTIALLOCALINT and address < INTIALLOCALFLOAT:
				offset = address - INTIALLOCALINT
				variableType = INT
				return ['LOCAL', offset, variableType]

			elif adress >= INTIALLOCALFLOAT and address < INTIALLOCALSTRING:
				offset = address - INTIALLOCALFLOAT 
				variableType = FLOAT
				return ['LOCAL', offset, variableType]

			elif address >= INTIALLOCALSTRING and address < INITIALTEMPBOOL:
				offset = address - INTIALLOCALSTRING
				variableType = STRING
				return ['LOCAL', offset, variableType]

		elif address >= INITIALTEMPBOOL and address < INITIALTEMPSTRING:
			if address >= INITIALTEMPBOOL and address < INITIALTEMPINT:
				offset = address - INITIALTEMPBOOL 
				variableType = BOOL
				return ['TEMP', offset , variableType]

			elif address >= INITIALTEMPINT and address < INTIALTEMPFLOAT:
				offset = address - INITIALTEMPINT
				variableType = INT
				return ['TEMP', offset, variableType]

			elif adress >= INTIALTEMPFLOAT and address < INITIALTEMPSTRING:
				offset = address - INTIALTEMPFLOAT 
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
		if address == '':
			return
		print(address)
		print(self.getGeneralInfo(address))
		scope = self.getGeneralInfo(address)[0]
		offset = self.getGeneralInfo(address)[1]
		variableType = self.getGeneralInfo(address)[2]

		if scope != 'CONSTANT':
			mem = getArrayOfType(scope, variableType)
			if offset > len(mem):
				print("Error variable doesn't exist")
				exit(1)
			if variableType == BOOL:
				return mem[offset]
			elif variableType == INT:
				return int(mem[offset])
			elif variableType == FLOAT:
				return float(mem[offset])
			elif variableType == STRING:
				return mem[offset]

		else:
			keys = constants.keys()
			counter = 0 
			for key in constants:
				if(constants[key]['dir'] == address):
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






