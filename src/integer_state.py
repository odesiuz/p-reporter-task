""" Created by: Ono' Uviase
    Date: 2025-10-19
    Time: 5:15 p.m.
    Author Email: 
    File Name: integer_state.py
"""
class IntegerStateMachine:
    def __init__(self, states: set, input_values: set, initial_state: str, final_states: set, transitions: dict):
        self.states = states
        self.input_values = input_values
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

        # Validate the state machine configuration
        if self.initial_state not in self.states:
            raise ValueError(f"Initial state {initial_state} is not in the set of states.")
        if not self.final_states.issubset(self.states):
            raise ValueError("Final states must be a subset of the set of states.")
        for (state, input_value), next_state in transitions.items():
            if state not in self.states:
                raise ValueError(f"State {state} in transitions is not in the set of states.")
            if input_value not in self.input_values:
                raise ValueError(f"Input value {input_value} in transitions is not in the set of input values.")

    def process_input(self, values: str):
        state = self.initial_state
        for input_value in values:
            if input_value not in self.input_values:
                raise ValueError(f"Invalid input value: {input_value}. Allowed values are: {self.input_values}")
            key = (state, input_value)
            if key not in self.transitions:
                raise ValueError(f"No transition defined for state {state} with input {input_value}")
            state = self.transitions.get(key)
        return state

    def validate(self, state: str):
        return state in self.final_states



def mod_three(state_machine: IntegerStateMachine, binary_str: str):
    state = state_machine.process_input(binary_str)
    final_state_mappings = {'S0': 0, 'S1': 1, 'S2': 2}
    return final_state_mappings.get(state)

if __name__ == '__main__':
    states = {'S0', 'S1', 'S2'}
    input_values = {'0', '1'}
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

    finite_state_machine = IntegerStateMachine(states, input_values, initial_state, final_states, transitions)

    binary_input = "1101"
    result = mod_three(finite_state_machine, binary_input)
    print(f"The integer value of binary '{binary_input}' modulo 3 is: {result}")
