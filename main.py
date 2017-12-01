class AutomatonLine(object):
	def __init__(self, composition = []):
		self.composition = composition

class AutomatonArguments(object):
	def __init__(self, composition = [], pointPosition = 0, read = 0):
		self.composition = composition
		self.pointPosition = pointPosition
		self.read = read

class AutomatonFirstsSet(object):
    def __init__(self, firsts = []):
        self.firsts

class AutomatonFollowsSet(object):
    def __init__(self, follows = []):
        self.follows

class ParsingActions(object):
    def __init__(self, action = '', transition = ''):
        self.action = action
        self.transition = transition

class ParsingTable(object):
    def __init__(self, states = {}):
        self.states = states

class ValidItems(object):
	def __init__(self, automatonProductions = {}, checked = 0, complete = 0):
		self.automatonProductions = automatonProductions
		self.checked = checked
		self.complete = complete

# It's a set of non-Terminal with compositions and productions
automaton = {}   # Automaton.update({'A': 15})
noTerminals = [] # noTerminals.append('A')
validItems = []
# It's a set of non-Terminal with first set
automatonFirstsSet = {}

# It's a set of non-Terminal with follow set
automatonFollowsSet = {}

# It's a set of valid items with it's compositions
parsingTable = {}

def makeGrammax(model):
	count = 0
	for line in model:
		line = line.replace("\r", "").replace("\n", "")
		if "::=" not in line:
			continue

		line = line.split("::=")

		lineAutomaton = line[0].strip(" ")
		lineCompositions = line[1].split("|")
		arguments = []

		if (count == 0):
			noTerminals.append(lineAutomaton+'\'')
			automaton.update({lineAutomaton+'\'': [AutomatonArguments({1: lineAutomaton + ' $'}, 0, 0)]})
			count += 1

		for lineComposition in lineCompositions:
			arguments.append(AutomatonArguments(lineComposition.split(" "), 0, 0))

		noTerminals.append(lineAutomaton)
		automaton.update({lineAutomaton: arguments});

def makeGrammaxFirst():
    print "making first"

def makeGrammaxFollow():
    print "making follow"

def makeValidItems():
	for validItem in validItems:
		if validItem.checked == 1:
			continue

		for composition in validItem.automatonProductions:
			if composition.read == 1:
				continue

			if composition.arguments[composition.pointPosition] in noTerminals:

			print composition

	# We'll asume that the first state is the beginning state, so, we have to create the antecessor of the grammax
	# print "making Valid Items"

	# automaton[noTerminals[0]][0] = "." + automaton[noTerminals[0]][0].strip(" ")

	# for noTerminal in noTerminals:
		# print (noTerminal + ' ::= '),
		# for automatonArguments in automaton[noTerminal]:
			# print automatonArguments.pointPosition,

		# print '\n'


def makeGrammaxReductions():
    print "making grammax reductions"

def makeGrammaxTransitions():
    print "making grammax transitions"

print "Open grammax File"
file = open("grammax", "r")
model = file.readlines()

makeGrammax(model)
file.close()

## Itens Validos da GLC
validItems.append(ValidItems({noTerminals[0]: automaton[noTerminals[0]]}, 0, 0))
makeValidItems()

## FIRST e FOLLOW da GLC da gramatica

## Construcao da Tabela de Transicoes
