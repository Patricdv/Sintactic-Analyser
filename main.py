class AutomatonLine(object):
	def __init__(self, composition = [], productions = {}):
		self.composition = composition
		self.productions = productions

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
automaton = {}
#Automaton.update({'A': 15})

# It's a set of non-Terminal with first set
automatonFirstsSet = {}

# It's a set of non-Terminal with follow set
automatonFollowsSet = {}

# It's a set of valid items with it's compositions
parsingTable = {}

def makeGrammax(model):
    for line in model:
        line = line.replace("\r", "").replace("\n", "")
        if "::=" not in line:
            continue

        line = line.split("::=")

        lineAutomaton = line[0]
        lineArguments = line[1].split("|")
        print lineAutomaton
        print lineArguments
        print '---------------------------------------------------'

def makeGrammaxFirst(model):
    print "making first"

def makeGrammaxFollow(model):
    print "making follow"

def makeValidItems(model):
    print "making Valid Items"

def makeGrammaxReductions(model):
    print "making grammax reductions"

def makeGrammaxTransitions(model):
    print "making grammax transitions"

print "Open grammax File"
file = open("grammax", "r")
model = file.readlines()

makeGrammax(model)

file.close()

## Abertura e Leitura do arquivo referente a GLC da gramatica

## FIRST e FOLLOW da GLC da gramatica

## Itens Validos da GLC

## Construcao da Tabela de Transicoes
