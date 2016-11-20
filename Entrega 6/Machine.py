from Memory import *
from Giga import *
from Cube import *


def executeVirtualMachine(functions, quadruples, constants, globalVarCount, tempVarCount, localVarCount, pointerCount):

	print("Virtual machine running...")
	print("---------------------------")
	countQuadruples = 0
	quadruplesStack = []
	activeMemory = Memory('module', localVarCount, globalVarCount , tempVarCount, pointerCount)
	returnDirection = None
	
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
			resultValue = 0

			if result >= MAXVARIABLECOUNT:
				if var1 >= MAXVARIABLECOUNT:
					resultNumber = activeMemory.pointer[ var1 - MAXVARIABLECOUNT]
					resultValue = activeMemory.getValueAtAddress(var1, constants)
					resultPointer = activeMemory.pointer[ result - MAXVARIABLECOUNT]
					activeMemory.storeValue(resultPointer, resultValue)
				else:
					resultValue = activeMemory.getValueAtAddress(var1, constants)
					resultPointer = activeMemory.pointer[ result - MAXVARIABLECOUNT]
					activeMemory.storeValue(resultPointer, resultValue)
			else:
				resultValue = activeMemory.getValueAtAddress(var1, constants)
				activeMemory.storeValue(result, resultValue)
			
			# print('---')
			# print(quadruple)
			# print(var1)
			# print(result)
			# print(resultValue)
			# print(activeMemory.getValueAtAddress(result, constants))
			
			

		elif quadruple['op'] == '*':
			var1 = quadruple['var1']
			var2 = quadruple['var2']
			result = quadruple['result']
			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
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
			#ESTE NO SE BORRA
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
		elif quadruple['op'] == 'GOFUNC':
			activeMemory.sleepMemory()
			quadruplesStack.append(countQuadruples+1)
			countQuadruples = num(quadruple['result'])-1
			
		# #This is the ERA function
		elif quadruple['op'] == 'MEMORY':
			result = quadruple['result']
			activeMemory.memoryFunc(result)
			returnDirection = result['dir']

		elif quadruple['op'] == 'PARAM':
			var1 = quadruple['var1']
			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			result = quadruple['result']
			activeMemory.storeParam(result, valueVar1)


		elif quadruple['op'] == 'RETURN':
			var1 = quadruple['result']

			valueVar1 = activeMemory.getValueAtAddress(var1, constants)
			activeMemory.storeValue(returnDirection, valueVar1)


		elif quadruple['op'] == 'ENDFUNC':
			activeMemory.wakeMemory()
			countQuadruples = quadruplesStack.pop()-1
			
		elif quadruple['op'] == 'READ':
			result = quadruple['result']
			scope = activeMemory.getScopeOfAddress(result)[0]
			variableType = activeMemory.getVariableType(result, scope)[0]
			if variableType == 1:
				var = raw_input()
				activeMemory.storeValue(result, var)
			elif variableType == 2:
				var = num(raw_input())
				activeMemory.storeValue(result, var)
			elif variableType == 3:
				var = num(raw_input())
				activeMemory.storeValue(result, var)
			elif variableType == 4:
				var = raw_input()
				activeMemory.storeValue(result, var)

		countQuadruples += 1
