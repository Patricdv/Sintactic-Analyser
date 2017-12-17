# It's a set of non-Terminal with compositions and productions
terminals = {}		# number: name
nonTerminals = {} 	# number: name
rules = {}			# number: name
validItems = []  	# validItems.append(ValidItems())

# It's a set of valid items with it's compositions
parsingTable = {}
parseStates = []
parseCompositions = []

# The Actual Parse State and last Read State to help's on the parsing table building
actualParseState = 0
readState = ''

# The two control variables to sintatic analysis
stack = [0]
tape = []

def ParsingAction(action, transition):
	return {'action': action, 'transition': transition}

def makeParsingTable(model):
	global readState
	for line in model:
		if line and not line.isspace():
			if readState == '' and 'Terminals' in line:
				readState = 'terminals'
				continue

			if readState == '':
				continue

			if line == '========================================\n':
				continue

			if readState == 'terminals' and 'Nonterminals' in line:
				readState = 'nonterminals'
				continue

			if readState == 'terminals':
				line = [x for x in line.replace("\r", "").replace("\n", "").split(" ") if x]
				terminals.update({int(line[0]): line[1]})

			if readState == 'nonterminals' and 'Rules' in line:
				readState = 'rules'
				continue

			if readState == 'nonterminals':
				line = [x for x in line.replace("\r", "").replace("\n", "").split(" ") if x]
				nonTerminals.update({int(line[0]): line[1]})

			if readState == 'rules' and 'LALR States' in line:
				readState = 'lalr'
				continue

			if readState == 'rules':
				line = [x for x in line.replace("\r", "").replace("\n", "").split(" ") if x]
				number = int(line[0])
				line.pop(0)
				ruleNoTerminal = line[0]
				line.pop(0)
				line.pop(0)
				rules.update({number: {'noTerminal': ruleNoTerminal, 'size': 2*len(line)}})

			if readState == 'lalr':
				if 'State ' in line:
					line = line.split(" ")
					actualParseState = int(line[1])
					parsingTable.update({actualParseState: {}})
					continue

				if 'Prior States' in line:
					#print line
					continue

				if '::=' not in line:
					line = [x for x in line.replace("\r", "").replace("\n", "").split(" ") if x]
					if len(line) == 2:
						line.append('')
					else:
						line[2] = int(line[2])

					parsingTable[actualParseState].update({line[0]: ParsingAction(line[1], line[2])})

def readTape(model):
	global tape
	for line in model:
		tape += [x for x in line.replace("\r", "").replace("\n", "").split(" ") if x]

	tape.append('(EOF)')

def syntaticRecognizement(stack, stackPosition, tape):
	print '\n\n=================================================='
	print stack
	print '-------------------------------------------'
	if stack[stackPosition] not in parsingTable.keys():
		print "Error: State not recognized"
		return False

	if tape[0] not in parsingTable[stack[stackPosition]].keys():
		print "Error: Invalid Entry"
		return False

	if parsingTable[stack[stackPosition]][tape[0]]['action'] == 's':
		stack.append(tape[0])
		stack.append(parsingTable[stack[stackPosition]][tape[0]]['transition'])
		tape.pop(0)
		stackPosition += 2
		print stack
		syntaticRecognizement(stack, stackPosition, tape)
		return True

	elif parsingTable[stack[stackPosition]][tape[0]]['action'] == 'r':
		print 'Reducing'
		print stack
		print rules[parsingTable[stack[stackPosition]][tape[0]]['transition']]
		size = rules[parsingTable[stack[stackPosition]][tape[0]]['transition']]['size']
		newRule = rules[parsingTable[stack[stackPosition]][tape[0]]['transition']]['noTerminal']

		print 'Size: ',
		print size
		print 'Rule: ',
		print newRule
		if size != 0:
			for x in range(size):
				stack.pop()
			stackPosition = stackPosition - size

		stack.append(newRule)
		newPosition = parsingTable[stack[stackPosition]][newRule]['transition']
		stack.append(newPosition)
		stackPosition += 2
		syntaticRecognizement(stack, stackPosition, tape)
		return True

	elif parsingTable[stack[stackPosition]][tape[0]]['action'] == 'a':
		print "This entry is syntaticly right"
		return True


print "Open grammax File"
file = open("grammax.txt", "r")
model = file.readlines()

makeParsingTable(model)
file.close()

print "Reading tape"
file = open("tape", "r")
model = file.readlines()

readTape(model)
file.close()

print 'Stack: ',
print stack

print 'Tape: ',
print tape

stackPosition = 0
syntaticRecognizement(stack, stackPosition, tape)

raw_input()
