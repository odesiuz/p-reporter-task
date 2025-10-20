""" Created by: Ono' Uviase
    Date: 2025-10-19
    Time: 5:15 p.m.
    Author Email: 
    File Name: integer_state.py
"""
class IntegerStateMachine:
    def __init__(self, states: set, input_values: set, initial_state: str, final_states: set, transitions: dict = None):
        self.states = states
        self.input_values = input_values
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions if transitions else {}
        self.value = int(initial_state)
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



def mod_three(state: IntegerStateMachine):
    state.modulus_value = state.value % 3
    return state.modulus_value

if __name__ == '__main__':
    state = IntegerStateMachine('1111')
    result = mod_three(state)
    print(f"Modulus of {state.value} by 3 is: {result}")

