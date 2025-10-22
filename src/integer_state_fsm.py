""" Created by: Ono' Uviase
    Date: 2025-10-19
    Time: 5:15p.m.
    Author Email: 
    File Name: integer_state_fsm.py
"""
class IntegerStateMachine:
    """
    A class to represent a deterministic finite state machine (FSM) for processing input sequences.

    Methods:
        process_input(values: str) -> str:
            Processes a sequence of input values and returns the final state after processing.

        validate(state: str) -> bool:
            Checks if a given state is a valid final/accepting state.
    """
    def __init__(self, states: set, input_values: set, initial_state: str, final_states: set, transitions: dict):
        """
        Initializes the IntegerStateMachine with the given states, input values, initial state, final states, and transitions.

        :param states: A set of all possible states.
        :type states: set
        :param input_values: A set of all valid input values.
        :type input_values: set
        :param initial_state: The initial state of the FSM.
        :type initial_state: str
        :param final_states: A set of final/accepting states.
        :type final_states: set
        :param transitions: A dictionary defining state transitions.
        :type transitions: dict

        Raises:
            ValueError: If the initial state is not in the set of states.
            ValueError: If the final states are not a subset of the set of states.
            ValueError: If any state or input value in the transitions is invalid.
        """
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

    def process_input(self, values: str) -> str:
        """
        Processes a sequence of input values and determines the final state.

        :param values: A string of input values to process.
        :type values: str

        Returns:
            str: The final state after processing the input values.

        Raises:
            ValueError: If an input value is invalid or if no transition is defined for a given state and input.
        """
        state = self.initial_state
        for input_value in values:
            if input_value not in self.input_values:
                raise ValueError(f"Invalid input value: {input_value}. Allowed values are: {self.input_values}")
            key = (state, input_value)
            if key not in self.transitions:
                raise ValueError(f"No transition defined for state {state} with input {input_value}")
            state = self.transitions.get(key)
        return state

    def validate(self, state: str) -> bool:
        return state in self.final_states