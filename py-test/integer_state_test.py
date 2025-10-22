import sys
import unittest
from pathlib import Path

# Ensure project root is on sys.path so `src.*` imports work when running tests from the repository root
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.integer_state_fsm import IntegerStateMachine
from src.modulo_three_fsm import ModThreeStateMachine

# NOTE: These test are fully AI generated dues to lack of time:🙂:

class TestIntegerStateMachineInitialization(unittest.TestCase):
    def test_init_raises_for_invalid_initial_state(self):
        with self.assertRaises(ValueError):
            IntegerStateMachine(
                states={'A'},
                input_values={'0'},
                initial_state='B',  # not in states
                final_states={'A'},
                transitions={}
            )

    def test_init_raises_when_final_states_not_subset(self):
        with self.assertRaises(ValueError):
            IntegerStateMachine(
                states={'A'},
                input_values={'0'},
                initial_state='A',
                final_states={'B'},  # B not in states
                transitions={}
            )

    def test_init_raises_for_invalid_transition_state_or_input(self):
        # invalid transition state
        with self.assertRaises(ValueError):
            IntegerStateMachine(
                states={'A'},
                input_values={'0'},
                initial_state='A',
                final_states={'A'},
                transitions={('X', '0'): 'A'}  # 'X' not in states
            )
        # invalid transition input
        with self.assertRaises(ValueError):
            IntegerStateMachine(
                states={'A'},
                input_values={'0'},
                initial_state='A',
                final_states={'A'},
                transitions={('A', '1'): 'A'}  # '1' not in input_values
            )


class TestIntegerStateMachineProcessing(unittest.TestCase):
    def test_process_input_raises_for_missing_transition_and_invalid_input(self):
        transitions = {('A', '0'): 'A'}  # no ('A','1') transition
        m = IntegerStateMachine(
            states={'A', 'B'},
            input_values={'0', '1'},
            initial_state='A',
            final_states={'B'},
            transitions=transitions
        )
        # missing transition should raise
        with self.assertRaises(ValueError):
            m.process_input('1')
        # invalid input character should raise
        with self.assertRaises(ValueError):
            m.process_input('2')

    def test_validate_method_behavior(self):
        m = IntegerStateMachine(
            states={'A', 'B'},
            input_values={'0'},
            initial_state='A',
            final_states={'B'},
            transitions={('A', '0'): 'B'}
        )
        self.assertTrue(m.validate('B'))
        self.assertFalse(m.validate('A'))
        self.assertFalse(m.validate('C'))  # not even a known state


class TestModThreeStateMachine(unittest.TestCase):
    def test_mod_three_computes_correct_remainder(self):
        cases = [
            ("", 0),        # empty input -> initial state S0 -> remainder 0
            ("0", 0),
            ("1", 1),
            ("10", 2),      # 2 decimal -> 2 mod 3
            ("11", 0),      # 3 decimal -> 0 mod 3
            ("1101", 1),    # 13 decimal -> 1 mod 3
            ("111111", 0),  # 63 decimal -> 0 mod 3
            ("1010101", int(int("1010101", 2) % 3)),
        ]
        m = ModThreeStateMachine()
        for binary, expected in cases:
            with self.subTest(binary=binary):
                self.assertEqual(m.mod_three(binary), expected)

    def test_mod_three_raises_on_invalid_character(self):
        m = ModThreeStateMachine()
        with self.assertRaises(ValueError):
            m.mod_three("10a01")  # contains invalid 'a'

    def test_long_input_performance_and_correctness(self):
        long_bin = "1" * 1000
        expected = int(int(long_bin, 2) % 3)
        m = ModThreeStateMachine()
        self.assertEqual(m.mod_three(long_bin), expected)


if __name__ == "__main__":
    unittest.main()


