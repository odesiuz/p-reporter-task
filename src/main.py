""" Created by: Ono' Uviase
    Date: 2025-10-22
    Time: 11:34a.m.
    Author Email: 
    File Name: main.py
"""
from src.modulo_functions import ModThreeStateMachine
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Compute the modulo 3 of a binary number using a state machine.')
    parser.add_argument('binary_input', type=str, help='Binary string input (e.g., "1101")')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    mod_three_machine = ModThreeStateMachine()

    binary_input = args.binary_input # we can also add a check for valid binary input here though the state machine will handle invalid inputs
    result = mod_three_machine.mod_three(binary_input)

    print(f"The number represented by binary '{binary_input}' modulo 3 is: {result}")