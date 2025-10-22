""" Created by: Ono' Uviase
    Date: 2025-10-22
    Time: 11:32a.m.
    Author Email: 
    File Name: modulo_functions.py
"""
from src.integer_state import IntegerStateMachine

def mod_three(state_machine: IntegerStateMachine, binary_str: str) -> int:
    state = state_machine.process_input(binary_str)
    final_state_mappings = {'S0': 0, 'S1': 1, 'S2': 2}
    return final_state_mappings.get(state)