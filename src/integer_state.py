""" Created by: Ono' Uviase
    Date: 2025-10-19
    Time: 5:15 p.m.
    Author Email: 
    File Name: integer_state.py
"""
class IntegerStateMachine:
    def __init__(self, initial_value: str):
        self.value = int(initial_value, 2)
        self.modulus_value = None



def mod_three(state: IntegerStateMachine):
    state.modulus_value = state.value % 3
    return state.modulus_value

if __name__ == '__main__':
    state = IntegerStateMachine('1111')
    result = mod_three(state)
    print(f"Modulus of {state.value} by 3 is: {result}")

