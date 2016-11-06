from Memory import *
from Giga import *
from Cube import *


def executeVirtualMachine(functions, quadruples, constants):

	print("Virtual machine running...")

	countQuadruples = 0



	activeMemory = Memory('module', constVarCount , tempVarCount)
	globalMemory = Memory('main', globalVarCount , 0)
	
	while quadruples[countQuadruples]['op'] != 'END' :
		quadruple = quadruples[countQuadruples]
		print(quadruple)
		#Change to the real values when handling memory
		if quadruple['op'] == '+':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 + valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '-':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']
			
			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 - valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '=':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 = valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '*':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)
			
			resultValue = float(valueVar1) * float(valueVar2)

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '/':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 / valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '<=':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 <= valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '>=':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 >= valueVar2

			activeMemory.storeValue(result, resultValue)


		elif quadruple['op'] == '<':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 < valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '>':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 > valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '==': 
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 == valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '!=':

			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 != valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '||':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 or valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == '&&':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			if var2 >= 10000 and var2 < 20000:
				valueVar2 = globalMemory.getValueAtAddress(var2, constants)
			else:
				valueVar2 = activeMemory.getValueAtAddress(var2, constants)

			resultValue = valueVar1 and valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple['op'] == 'PRINT':
			var1 = quadruple['resultado']

			if var1 >= 10000 and var1 < 20000:
				valueVar1 = globalMemory.getValueAtAddress(var1, constants)
			else:
				valueVar1 = activeMemory.getValueAtAddress(var1, constants)

			print(valueVar1)

		# elif quadruple[countQuadruples]['op'] == 'ARR':

		# elif quadruple[countQuadruples]['op'] == 'ENDFUNC':

		# elif quadruple[countQuadruples]['op'] == 'GOTO':

		# elif quadruple[countQuadruples]['op'] == 'GOTOF':

		# elif quadruple[countQuadruples]['op'] == 'GOTOT':
	
		# #This is the GOSUB function
		# elif quadruple[countQuadruples]['op'] == 'GOFUNC':
		
		# #This is the ERA function
		# elif quadruple[countQuadruples]['op'] == 'MEMORY':

		# elif quadruple[countQuadruples]['op'] == 'PARAM':

		# elif quadruple[countQuadruples]['op'] == 'RETURN':
			
		# elif quadruple[countQuadruples]['op'] == 'READ':

		countQuadruples += 1
