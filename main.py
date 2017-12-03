class AutomatonArguments(object):
	def __init__(self, composition = [], pointPosition = 0, read = 0):
		self.composition = composition
		self.pointPosition = pointPosition
		self.read = read

class ValidItems(object):
	def __init__(self, automatonProductions = {}, checked = 0, complete = 0):
		self.automatonProductions = automatonProductions
		self.checked = checked
		self.complete = complete

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

# It's a set of non-Terminal with compositions and productions
automaton = {}  	# Automaton.update({'A': 15})
noTerminals = [] 	# noTerminals.append('A')
validItems = []  	# validItems.append(ValidItems())

# It's a set of non-Terminal with first set and of non-Terminal with follow set
automatonFirstsSet = {}
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
			automaton.update({lineAutomaton+'\'': [AutomatonArguments([lineAutomaton, '$'], 0, 0)]})
			count += 1

		for lineComposition in lineCompositions:
			composition = lineComposition.strip().split(" ")
			arguments.append(AutomatonArguments(composition, 0, 0))

		noTerminals.append(lineAutomaton)
		automaton.update({lineAutomaton: arguments});

def iterateInTheDot(validItem):
	altered = 0
	for composition in validItem.automatonProductions.keys():
		print composition
		for production in validItem.automatonProductions[composition]:
			if production.read == 1:
				print "---------------------------------------"
				print "producao lida"
				continue

			print "Item: ",
			print production.composition[production.pointPosition]
			if not production.composition[production.pointPosition]:
				print "---------------------------------------"
				print "item completo"
				production.read = 1
				validItem.complete = 1
				continue

			dotItem = production.composition[production.pointPosition]
			if dotItem not in noTerminals:
				continue

			if dotItem not in validItem.automatonProductions:
				validItem.automatonProductions.update({dotItem: automaton[dotItem]})
				production.read = 1
				altered = 1

	print altered
	if altered == 1:
		iterateInTheDot(validItem)

def makeValidItems():
	for validItem in validItems:
		if validItem.checked == 1:
			continue

		iterateInTheDot(validItem)
		print validItem.automatonProductions.keys()

	# We'll asume that the first state is the beginning state, so, we have to create the antecessor of the grammax
	# print "making Valid Items"

	# automaton[noTerminals[0]][0] = "." + automaton[noTerminals[0]][0].strip(" ")

	# for noTerminal in noTerminals:
		# print (noTerminal + ' ::= '),
		# for automatonArguments in automaton[noTerminal]:
			# print automatonArguments.pointPosition,

		# print '\n'


def makeGrammaxFirst():
    print "making first"

def makeGrammaxFollow():
    print "making follow"

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
