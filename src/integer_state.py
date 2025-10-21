""" Created by: Ono' Uviase
    Date: 2025-10-19
    Time: 5:15 p.m.
    Author Email: 
    File Name: integer_state.py
"""
class IntegerStateMachine:
    def __init__(self, states: set, input_symbols: set, initial_state: str, final_states: set, transitions: dict = None):
        self.states = states
        self.input_values = input_symbols
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions if transitions else {}
        self.modulus_value = None

    def process_input(self, values: str):
        state = self.initial_state
        for input_value in values:
            if input_value not in self.input_values:
                raise ValueError(f"Invalid input value: {input_value}. Allowed values are: {self.input_values}")
            key = (state, input_value)
            if key not in self.transitions:
                raise ValueError(f"No transition defined for state {state} with input {input_value}")
            state = self.transitions[key]
        return state

    def validate(self, state: str):
        return state in self.final_states



def mod_three(state_machine: IntegerStateMachine, binary_str: str):
    state = state_machine.process_input(binary_str)
    final_state_mappings = {'S0': 0, 'S1': 1, 'S2': 2}
    return final_state_mappings.get(state)

if __name__ == '__main__':
    states = {'S0', 'S1', 'S2'}
    input_symbols = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S0', 'S1', 'S2'}
    transitions = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2',
    }

    fsm = IntegerStateMachine(states, input_symbols, initial_state, final_states, transitions)

    binary_input = "1101"
    result = mod_three(fsm, binary_input)
    print(f"The integer value of binary '{binary_input}' modulo 3 is: {result}")
