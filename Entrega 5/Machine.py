from Memory import *
from Giga import *

def executeVirtualMachine(functions, quadruples, constants):

	print("Virtual machine running...")

	countQuadruples = 0

	activeMemory = Memory()
	globalMemory = Memory()
	

	while quadruples[countQuadruples]['op'] != 'END' :
		quadruple = quadruples[0]
		print(quadruple)
		#Change to the real values when handling memory 
		if quadruple[countQuadruples]['op'] == '+':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 + valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '-':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']
			
			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 - valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '=':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 = valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '*':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 * valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '/':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 / valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '<=':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 <= valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '>=':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 >= valueVar2

			activeMemory.storeValue(result, resultValue)


		elif quadruple[countQuadruples]['op'] == '<':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 < valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '>':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 > valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '==': 
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 == valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '!=':

			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 != valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '||':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 or valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == '&&':
			var1 = quadruple[countQuadruples]['var1']
			var2 = quadruple[countQuadruples]['var2']
			result = quadruple[countQuadruples]['result']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			if var2 >= 10000 and var2 < 20000
				valueVar2 = globalMemory.getValueAtDirection()
			else:
				valueVar2 = activeMemory.getValueAtDirection()

			resultValue = valueVar1 and valueVar2

			activeMemory.storeValue(result, resultValue)

		elif quadruple[countQuadruples]['op'] == 'PRINT':
			var1 = quadruple[countQuadruples]['resultado']

			if var1 >= 10000 and var1 < 20000
				valueVar1 = globalMemory.getValueAtDirection()
			else:
				valueVar1 = activeMemory.getValueAtDirection()

			print(valueVar1)

		elif quadruple[countQuadruples]['op'] == 'ARR':

		elif quadruple[countQuadruples]['op'] == 'ENDFUNC':

		elif quadruple[countQuadruples]['op'] == 'GOTO':

		elif quadruple[countQuadruples]['op'] == 'GOTOF':

		elif quadruple[countQuadruples]['op'] == 'GOTOT':
	
		#This is the GOSUB function
		elif quadruple[countQuadruples]['op'] == 'GOFUNC':
		
		#This is the ERA function
		elif quadruple[countQuadruples]['op'] == 'MEMORY':

		elif quadruple[countQuadruples]['op'] == 'PARAM':

		elif quadruple[countQuadruples]['op'] == 'RETURN':
			
		elif quadruple[countQuadruples]['op'] == 'READ':

	countQuadruples += 1
