class SingleTapeDTM:
    def __init__(self,states:list,alphabet,tape_alphabet,transition_function,start_state,accept_state,reject_state):
        #note the tape_alphabet needs to be a subset of 
        self.states:list = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function:dict = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

        #the alphabet needs to be a subset of the tape_alphabet. Therefore we will raise an error if the Tm doesn't satisfy this condition.
        for symbol in alphabet: #O(a*t) - can we do a sort and make it O(tlogt+a)
            if symbol not in tape_alphabet:
                raise ValueError
        


    def validate_string(self,input_string:str,compute:bool=False):

        #error testing
        #setting up the tape
        current_state = self.start_state
        pointer = 0
        endvalues = (self.accept_state,self.reject_state)
        tape = []
        for ch in input_string:
            tape.append(ch)
        tape.append('#')

        #processing through the tape until it reaches reject or accept state 
        while current_state not in endvalues:
            #Test-case
            print(f'current_state is {current_state,tape[pointer]}')

            #Actual code
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


tfanbn1 = {
    ('q0','a'):('q1','x','R'),
    ('q0','y'):('q0','','R'),
    ('q0','b'):('q3','z','R'),
    ('q0','#'):('qr','','R'),
    ('q1','b'):('q2','y','L'),
    ('q1','a'):('q1','','R'),
    ('q1','y'):('q1','','R'),
    ('q1','#'):('qr','','R'),
    ('q2','a'):('q2','','L'),
    ('q2','y'):('q2','','L'),
    ('q2','x'):('q0','','R'),
    ('q3','#'):('qa','','L'),
    ('q3','a'):('qr','','L'),
    ('q3','b'):('qr','','L'),
           }      

#Testing for the language #anbn+1
anbn1 = SingleTapeDTM(['q0','q1','q2','q3','qa','qr'],['a','b'],['a','b','x','y','z',"#"],tfanbn1,'q0','qa','qr')  
# o2nwrong = TM(['q1','q2','q3'],['0'],['1','x',')'],{},'q1','q1','q2')  

# print(f'b: {anbn1.validate_string('b')}')
# print(f': {anbn1.validate_string('')}')
# print(f'aabbb: {anbn1.validate_string('aabbb')}')
# print(f'aaaaaabbbbbbb: {anbn1.validate_string('aaaaaabbbbbbb')}')
# print(f'aaba: {anbn1.validate_string('aaba')}')
# print(f'abaababba: {anbn1.validate_string('abaababba')}')

#Testing for the TM that computes f(n)=n/2
def decimaltounary(k:int):
    out = ''
    for _ in range(k):
        out += '1'
    return out

tfhalfn = {
    ('q0','1'):('q1','a','R'),
    ('q0','#'):('qa','','R'),
    ('q1','1'):('q1','','R'),
    ('q1','#'):('q2','','L'),
    ('q2','1'):('q3','#','L'),
    ('q2','a'):('qr','','R'),
    ('q3','#'):('q0','','L'),
    ('q3','1'):('q3','','L'),
    ('q3','a'):('q0','1','R'),
           }    

halfn = SingleTapeDTM(['q0','q1','q2','q3','qa','qr'],['1'],['1','#','a'],tfhalfn,'q0','qa','qr')

#print(decimaltounary(4))
four = decimaltounary(4)
print(f'11: {halfn.validate_string('11',True)}')
print(f'4: {halfn.validate_string('1111',True)}')
print(f'1: {halfn.validate_string('1',True)}')
print(f'111: {halfn.validate_string('111',True)}')

print(f'111111111111: {halfn.validate_string('111111111111',True)}')


