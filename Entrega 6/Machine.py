from Memory import *
from Giga import *
from Cube import *


def executeVirtualMachine(functions, quadruples, constants, globalVarCount, tempVarCount, localVarCount, pointerCount):

	print("Virtual machine running...")
	print("---------------------------")
	countQuadruples = 0
	activeMemory = Memory('module', localVarCount, globalVarCount , tempVarCount, pointerCount)
	
	while quadruples[countQuadruples]['op'] != 'END' :
		quadruple = quadruples[countQuadruples]
		# print("QUADRUPLE")
		# print(quadruple)
		# print("CONSTANTS")
		# print(constants)
		
		#Change to the real values when handling memory
		if quadruple['op'] == '+':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if quadruples[countQuadruples - 1]['op'] == 'VERIFY':
				resultValue = var1 + activeMemory.getValueAtAddress(var2, constants)
				activeMemory.storeValue(result, resultValue)
				
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

				resultValue = valueVar1 + valueVar2

				activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '-':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']
			
			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 - valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '=':
			var1 = quadruple['var1']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			resultValue = valueVar1 
			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '*':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)


			resultValue = valueVar1 * valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '/':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 / valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '<=':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 <= valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '>=':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 >= valueVar2

			activeMemory.storeValue(result, resultValue)


		elif quadruple['op'] == '<':

			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 < valueVar2
			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '>':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 > valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '==': 
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 == valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '!=':

			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 != valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '||':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 or valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '&&':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 and valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == 'PRINT':
			var1 = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			print(valueVar1)

		elif quadruple['op'] == 'VERIFY':
			var1 = quadruple['var1']
			valueVar1 = activeMemory.getValueAtAddress(var1, constants)


			if not(valueVar1 >= 0 and valueVar1 < quadruple['result']):
				error("Out of bounds array")

		# elif quadruple[countQuadruples]['op'] == 'ENDFUNC':

		elif quadruple['op'] == 'GOTO':

			countQuadruples = quadruple['result'] - 1

		elif quadruple['op'] == 'GOTOF':
			var1 = quadruple['var1']
			
			valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if not valueVar1:
				countQuadruples = quadruple['result'] - 1

		# #This is the GOSUB function
		# elif quadruple[countQuadruples]['op'] == 'GOFUNC':
		
		# #This is the ERA function
		# elif quadruple[countQuadruples]['op'] == 'MEMORY':

		# elif quadruple[countQuadruples]['op'] == 'PARAM':

		# elif quadruple[countQuadruples]['op'] == 'RETURN':
			
		# elif quadruple[countQuadruples]['op'] == 'READ':

		countQuadruples += 1
