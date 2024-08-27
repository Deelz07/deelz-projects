class Terminal:
    def __init__(self,name:str):
        self.name = name
    
    def __eq__(self,other):
        return self.name == other.name
    
    def __str__(self):
        return (self.name)

class CFG:
    """
    constructs a class for context free grammars.
    """

    def __init__(self,start:str):
        self.start = start
        self.rules = {}
    
    def __addrule__(self,input:Terminal, output:list):
        try:
            self.rules[input].append(output)
        except:
            self.rules[input]=[]
            self.rules[input].append(output)
    

def remove_epsilon_transitions(grammar:CFG) -> CFG:
#     #1. We will add replace non-terminal with epsilon in all possible places.

def convert_to_CNF(grammar:CFG):
#     #First we will remove all epsilon transitions
#     for k,v in values(grammar.rules):

#         #
#     #2. Remove all productions of the form A -> B

#     #3. Remove all


#Test-cases
a = Terminal('B')
b = Terminal('A')
print(a==b)


print(['a'] in [['a'],['b',3]])