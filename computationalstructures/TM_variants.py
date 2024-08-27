import TM_basic

class StationaryDTM:
    def __init__(self,states:list,alphabet,tape_alphabet,transition_function,start_state,accept_state,reject_state):
        """ Same as a single tape DTM except there are multiple tapes. """
        self.states:list = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function:dict = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
    
    def validate_string(self,input_string:str,compute:bool=False):
        """
        Processes a tape by just the first symbol.
        """
        #setting up the tapes
        current_state = self.start_state
        #pointer = 0
        endvalues = (self.accept_state,self.reject_state)
        maintape = []
        for _ in range(self.tapecount):
            maintape.append([])
            #Need to create a pointer for all of the tapes

        for ch in input_string:
            maintape[0].append(ch)
        maintape[0].append('#')

        #processing through the tape until it reaches reject or accept state 
        while current_state not in endvalues:
            #Test-case
            for i in range(k):
                print(f'current_states in tape {i+1} is {current_state,maintape[i+1]}') #Need to add pointers

            #Actual code
            tf_input = [current_state]
            for i in range(self.tapecount):
                tf_input.append(maintape[i]) #Need to figure out pointers again.
            next_states = self.transition_function[(current_state,tape[pointer])] #are turing machines deterministic??
            current_state = next_states[0]
            if next_states[1] != "":
                tape[pointer]=next_states[1]
            if next_states[2] == 'L':
                pointer -= 1
            else:
                pointer += 1

        if current_state == self.accept_state:
            if compute:
                return tape
            else:
                return True
        else:
            if compute:
                print('Invalid input')
            return False
class MultiTapeDTM:
    def __init__(self,states:list,alphabet,tape_alphabet,transition_function,start_state,accept_state,reject_state,k):
        """ Same as a single tape DTM except there are multiple tapes. """
        self.states:list = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function:dict = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tapecount = k
    
    def validate_string(self,input_string:str,compute:bool=False):
        """
        Processes a tape in a more general fashion to the single tape DTM.

        To do: Create a pointer for all of the different tapes.
        """
        #setting up the tapes
        current_state = self.start_state
        #pointer = 0
        endvalues = (self.accept_state,self.reject_state)
        maintape = []
        for _ in range(self.tapecount):
            maintape.append([])
            #Need to create a pointer for all of the tapes

        for ch in input_string:
            maintape[0].append(ch)
        maintape[0].append('#')

        #processing through the tape until it reaches reject or accept state 
        while current_state not in endvalues:
            #Test-case
            for i in range(k):
                print(f'current_states in tape {i+1} is {current_state,maintape[i+1]}') #Need to add pointers

            #Actual code
            tf_input = [current_state]
            for i in range(self.tapecount):
                tf_input.append(maintape[i]) #Need to figure out pointers again.
            next_states = self.transition_function[(current_state,tape[pointer])] #are turing machines deterministic??
            current_state = next_states[0]
            if next_states[1] != "":
                tape[pointer]=next_states[1]
            if next_states[2] == 'L':
                pointer -= 1
            else:
                pointer += 1

        if current_state == self.accept_state:
            if compute:
                return tape
            else:
                return True
        else:
            if compute:
                print('Invalid input')
            return False

