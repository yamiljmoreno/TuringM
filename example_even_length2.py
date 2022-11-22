from tmsim import *

value = input('Enter a Palindrome:\n')

Algorithm({
    'q_even': {
        '0': ('q_odd', '->'),
        '1': ('q_odd', '->'),
        '[]': True,
    },
    'q_odd': {
        '0': ('q_even', '->'),
        '1': ('q_even', '->'),
        '[]': False,
    }
}, initial_state='q_even').test(
    generate_words({type(value)}, 1),
    lambda word: len(word) % 2 == 0
)
