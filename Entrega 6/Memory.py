from Giga import *
from Cube import *

class Memory:

	def __init__(self, name, localVariables, globalVariables, tempVariables, pointerVariables):
		self.name = name
		# alocates memory by data type 
		# variables 
		# self.int = variables[Amount of type] * [""] 
		# creates a list of variables 
		self.localBools = ( localVariables[BOOL] - INITIALLOCALBOOL + 1) * [None] 
		self.localInts = ( localVariables[INT] - INITIALLOCALINT + 1) * [None]
		self.localFloats =  ( localVariables[FLOAT] - INITIALLOCALFLOAT + 1 ) * [None]
		self.localStrings = ( localVariables[STRING] - INITIALLOCALSTRING + 1) * [None]

		self.globalBools = ( globalVariables[BOOL] - INITIALGLOBALBOOL + 1 ) * [None]
		self.globalInts = ( globalVariables[INT] - INITIALGLOBALINT + 1 ) * [None]
		self.globalFloats = ( globalVariables[FLOAT] - INITIALGLOBALFLOAT + 1 ) * [None]
		self.globalStrings = ( globalVariables[STRING] - INITIALGLOBALSTRING + 1 ) * [None]
		
		self.tempBools = (tempVariables[BOOL] - INITIALTEMPBOOL + 1) * [None]
		self.tempInts = (tempVariables[INT] - INITIALTEMPINT + 1) * [None]
		self.tempFloats = (tempVariables[FLOAT] - INITIALTEMPFLOAT + 1) * [None]
		self.tempString = (tempVariables[STRING] - INITIALTEMPSTRING + 1) * [None]

		self.pointer = (pointerVariables - INITIALPOINTER ) * [None]
		
		

	def getArrayOfType(self, scope, variableType):
		if scope == 'GLOBAL':
			if variableType == BOOL:
				return self.globalBools
			elif variableType == INT:
				return self.globalInts
			elif variableType == FLOAT:
				return self.globalFloats
			elif variableType == STRING:
				return self.globalStrings
		elif scope =='LOCAL':
			if variableType == BOOL:
				return self.localBools
			elif variableType == INT:
				return self.localInts
			elif variableType == FLOAT:
				return self.localFloats
			elif variableType == STRING:
				return self.localStrings
		elif scope == 'TEMP':
			if variableType == BOOL:
				return self.tempBools
			elif variableType == INT:
				return self.tempInts
			elif variableType == FLOAT:
				return self.tempFloats
			elif variableType == STRING:
				return self.tempString
		


	def getScopeOfAddress(self, address):
		if address >= INITIALGLOBALBOOL and address < INITIALLOCALBOOL:
			return ['GLOBAL']
		elif address >= INITIALLOCALBOOL and address < INITIALTEMPBOOL:
			return ['LOCAL']
		elif address >= INITIALTEMPBOOL and address < INITIALCONSTBOOL:
			return ['TEMP']
		elif address >= INITIALCONSTBOOL and address < MAXVARIABLECOUNT:
			return ['CONSTANT']
		elif address >= MAXVARIABLECOUNT:
			return ['ARRAY'] 


	def getVariableType(self, address, scope):
		if scope == 'GLOBAL':
			if address >= INITIALGLOBALBOOL and address < INITIALGLOBALINT:
				return [BOOL]
			elif address >= INITIALGLOBALINT and address < INITIALGLOBALFLOAT:
				return [INT]
			elif address >= INITIALGLOBALFLOAT and address < INITIALGLOBALSTRING:
				return [FLOAT]
			elif address >= INITIALGLOBALSTRING and address < INITIALLOCALBOOL:
				return [STRING]
		elif scope == 'LOCAL':
			if address >= INITIALLOCALBOOL and address < INITIALLOCALINT:
				return [BOOL]
			elif address >= INITIALLOCALINT and address < INITIALLOCALFLOAT:
				return [INT]
			elif address >= INITIALLOCALFLOAT and address < INITIALLOCALSTRING:
				return [FLOAT]
			elif address >= INITIALLOCALSTRING and address < INITIALTEMPBOOL:
				return [STRING]
		elif scope == 'TEMP':
			if address >= INITIALTEMPBOOL and address < INITIALTEMPINT:
				return [BOOL]
			elif address >= INITIALTEMPINT and address < INITIALTEMPFLOAT:
				return [INT]
			elif address >= INITIALTEMPFLOAT and address < INITIALTEMPSTRING:
				return [FLOAT]
			elif address >= INITIALTEMPSTRING and address < INITIALCONSTBOOL:
				return [STRING]
		elif scope == 'CONSTANT':
			if address >= INITIALCONSTBOOL and address < INITIALCONSTINT:
				return [BOOL]
			elif address >= INITIALCONSTINT and address < INITIALCONSTFLOAT:
				return [INT]
			elif address >= INITIALCONSTFLOAT and address < INITIALCONSTSTRING:
				return [FLOAT]
			elif address >= INITIALCONSTSTRING and address < MAXVARIABLECOUNT:
				return [STRING]
		


	def getOffset(self, address, scope, varType):
		if scope == 'GLOBAL': 
			if varType == 1:
				return [address - INITIALGLOBALBOOL]
			elif varType == 2:
				return [address - INITIALGLOBALINT]
			elif varType == 3:
				return [address - INITIALGLOBALFLOAT]
			elif varType == 4:
				return [address - INITIALGLOBALSTRING]
		elif scope == 'LOCAL':
			if varType == 1:
				return [address - INITIALLOCALBOOL]
			elif varType == 2:
				return [address - INITIALLOCALINT]
			elif varType == 3:
				return [address - INITIALLOCALFLOAT]
			elif varType == 4:
				return [address - INITIALLOCALSTRING]
		elif scope == 'TEMP':
			if varType == 1:
				return [address - INITIALTEMPBOOL]
			elif varType == 2:
				return [address - INITIALTEMPINT]
			elif varType == 3:	
				return [address - INITIALTEMPFLOAT]
			elif varType == 4:
				return [address - INITIALTEMPSTRING]
		elif scope == 'CONSTANT':
			if varType == 1:
				return [address - INITIALCONSTBOOL]
			elif varType == 2:
				return [address - INITIALCONSTINT]
			elif varType == 3:
				return [address - INITIALCONSTFLOAT]
			elif varType == 4:
				return [address - INITIALCONSTSTRING]


	def getValueAtAddress(self, address, constants):
		if address == '':
			return

		if address >= MAXVARIABLECOUNT :
			offset = address - MAXVARIABLECOUNT
			return self.getValueAtAddress(self.pointer[offset], constants)

		scope = self.getScopeOfAddress(address)[0]
		variableType = self.getVariableType(address, scope)[0]
		offset = self.getOffset(address, scope, variableType)[0]
		if scope != 'CONSTANT':
			mem = self.getArrayOfType(scope, variableType)
			if offset > len(mem):
				error("Error variable doesn't exist")
			if scope == 'GLOBAL':
				if variableType == BOOL:
					return self.globalBools[offset]
				elif variableType == INT:
					return int(self.globalInts[offset])
				elif variableType == FLOAT:
					return float(self.globalFloats[offset])
				elif variableType == STRING:
					return self.globalStrings[offset]
			elif scope =='LOCAL':
				if variableType == BOOL:
					return self.localBools[offset]
				elif variableType == INT:
					return self.localInts[offset]
				elif variableType == FLOAT:
					return self.localFloats[offset]
				elif variableType == STRING:
					return self.localStrings[offset]

			elif scope == 'TEMP':
				if variableType == BOOL:
					return self.tempBools[offset]
				elif variableType == INT:
					return self.tempInts[offset]
				elif variableType == FLOAT:
					return self.tempFloats[offset]
				elif variableType == STRING:
					return self.tempString[offset]
			elif scope == 'ARRAY':
				return self.getValueAtAddress(self.pointerVariables[offset])
		else:
			keys = constants.keys()
			counter = 0 
			for key in constants:
				if(constants[key]['dir'] == address):
					return constants[key]['value']

	def storeValue(self, address, value):
		if address >= MAXVARIABLECOUNT:
			offset = address - MAXVARIABLECOUNT
			self.pointer[offset] = value
			return

		scope = self.getScopeOfAddress(address)[0]
		variableType = self.getVariableType(address, scope)[0]
		offset = self.getOffset(address, scope, variableType)[0]
		mem = self.getArrayOfType(scope, variableType)
		
		if offset >= len(mem):
			error(" Error address doesn't exist")
		if scope == 'GLOBAL':
			if variableType == BOOL:
				self.globalBools[offset]= value
			elif variableType == INT:
				self.globalInts[offset]= value
			elif variableType == FLOAT:
				self.globalFloats[offset]= value
			elif variableType == STRING:
				self.globalStrings[offset]= value
		elif scope =='LOCAL':
			if variableType == BOOL:
				self.localBools[offset]= value
			elif variableType == INT:
				self.localInts[offset]= value
			elif variableType == FLOAT:
				self.localFloats[offset]= value
			elif variableType == STRING:
				self.localStrings[offset]= value
		elif scope == 'TEMP':
			if variableType == BOOL:
				self.tempBools[offset]= value
			elif variableType == INT:
				self.tempInts[offset]= value
			elif variableType == FLOAT:
				self.tempFloats[offset]= value
			elif variableType == STRING:
				self.tempString[offset]= value
		elif scope == 'ARRAY':
			self.storeValue(self.pointer[offset], value)






