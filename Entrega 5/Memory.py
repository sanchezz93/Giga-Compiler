from Giga import *

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

		self.tempBools = (tempVariables[BOOL] - 30000 ) * [""]
		self.tempInts = (tempVariables[INT] - 32500) * [""]
		self.tempFloats = (tempVariables[FLOAT] - 35000) * [""]
		self.tempString = (tempVariables[STRING] - 37500) * [""]
		

# globalVarCount = {}			#10000
# globalVarCount[BOOL] = 10000
# globalVarCount[INT] = 12500
# globalVarCount[FLOAT] = 15000
# globalVarCount[CHAR] = 17500

# localVarCount = {}			#20000
# localVarCount[BOOL] = 20000
# localVarCount[INT] = 22500
# localVarCount[FLOAT] = 25000
# localVarCount[CHAR] = 27500

	def offsetAddress(self, address):




	def getValueAtAddress(self, address, constants):





	def storeValue(self, address, value):



