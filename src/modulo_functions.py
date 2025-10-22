""" Created by: Ono' Uviase
    Date: 2025-10-22
    Time: 11:32a.m.
    Author Email: 
    File Name: modulo_functions.py
"""
from src.integer_state import IntegerStateMachine

class ModThreeStateMachine(IntegerStateMachine):
    def __init__(self):
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

        super().__init__(states=states, input_values=input_values, initial_state=initial_state,
                         final_states=final_states, transitions=transitions)

    def mod_three(self, binary_str: str) -> int:
        state = self.process_input(binary_str)
        final_state_mappings = {'S0': 0, 'S1': 1, 'S2': 2}
        return final_state_mappings.get(state)