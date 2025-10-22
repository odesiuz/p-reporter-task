""" Created by: Ono' Uviase
    Date: 2025-10-22
    Time: 11:32a.m.
    Author Email: 
    File Name: modulo_functions.py
"""
from src.integer_state import IntegerStateMachine

class ModThreeStateMachine(IntegerStateMachine):
    """
    A state machine to compute the modulo 3 of a binary string.

    Inherits from:
        IntegerStateMachine: A generic finite state machine implementation.
    """
    def __init__(self):
        """
        Initializes the ModThreeStateMachine with states, input values, initial state,
        final states, and transitions specific to modulo 3 computation.

        States:
            - 'S0': Represents a remainder of 0 when dividing by 3.
            - 'S1': Represents a remainder of 1 when dividing by 3.
            - 'S2': Represents a remainder of 2 when dividing by 3.

        Input Values:
            - '0': Binary digit 0.
            - '1': Binary digit 1.

        Transitions:
            - ('S0', '0') -> 'S0': Stay in state S0 when input is 0.
            - ('S0', '1') -> 'S1': Move to state S1 when input is 1.
            - ('S1', '0') -> 'S2': Move to state S2 when input is 0.
            - ('S1', '1') -> 'S0': Move to state S0 when input is 1.
            - ('S2', '0') -> 'S1': Move to state S1 when input is 0.
            - ('S2', '1') -> 'S2': Stay in state S2 when input is 1.
        """
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
        """
        Computes the modulo 3 of a binary string.

        :param binary_str: A string of binary digits ('0' and '1') to process.
        :type binary_str: str
        :returns: The remainder when the binary number is divided by 3.
        :rtype: int

        :raises ValueError: If the binary string contains invalid characters.
        """
        state = self.process_input(binary_str)
        final_state_mappings = {'S0': 0, 'S1': 1, 'S2': 2}
        return final_state_mappings.get(state)