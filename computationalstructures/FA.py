# Multiline-comment = cmd (ctl) + /
class regex:
    def __init__(self):
        return None
    

class DFA:
    def __init__(self,states:list,alphabet:list,transition_function:dict,start_state:str,accept_states:list):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def process_input(self,input_string:str):
        current_state = self.start_state
        for ch in input_string:
            if (current_state, ch) in self.transition_function:
                current_state = self.transition_function[(current_state,ch)]
            else:
                print('Invalid transition')
                return False
        return current_state in self.accept_states
    

    
    def dfa_minimise(self,input_string:str):
        """
        """
        non_accept = set()
        
        groups = []
        
        for 


class DFA2:
    def __init__(self,alphabet:list,transition_function:list,start_state:int,accept_states:list):
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    #How to implement this without knowling length of string at beginning
    def process_input(self,input_string:str):
        current_state = self.start_state
        for ch in input_string:
            if ch == 'a':
                current_state = self.transition_function[current_state][0]
            elif ch == 'b':
                current_state = self.transition_function[current_state][0]
            else:
                raise ValueError('Invalid input string')
        return current_state in self.accept_states
    
    
    
    def dfa_minimise(self,input_string:str):
        """
        """
        non_accept:
        groups = []
        
        for 


            

# class NFA:
#     def __init__(self,states:list,alphabet:list,transition_function,start_state:str,accept_states:list):
#         self.states = states
#         self.alphabet = alphabet
#         self.transition_function = transition_function
#         self.start_state = start_state
#         self.accept_states = accept_states

#     def  


test_tf = {
    ('q1','a'):'q2',
    ('q1','b'):'q2',
    ('q2','a'):'q1',
    ('q2','b'):'q1'
}
oddlengthdfa = DFA(['q1','q2'],['a','b'],test_tf,'q1',['q2'])

print(oddlengthdfa.process_input('ab'))
print(oddlengthdfa.process_input('abc'))
print(oddlengthdfa.process_input('abaab'))