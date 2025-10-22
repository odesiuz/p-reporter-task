""" Created by: Ono' Uviase
    Date: 2025-10-22
    Time: 11:34a.m.
    Author Email: 
    File Name: main.py
"""
from src.integer_state import IntegerStateMachine
from src.modulo_functions import mod_three

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

    finite_state_machine = IntegerStateMachine(states=states, input_values=input_values, initial_state=initial_state,
                                               final_states=final_states, transitions=transitions)

    binary_input = "1101"
    result = mod_three(finite_state_machine, binary_input)
    print(f"The integer value of binary '{binary_input}' modulo 3 is: {result}")
