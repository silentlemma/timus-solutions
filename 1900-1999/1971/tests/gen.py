"""Print seed mode. Seed shifts power by 0..9; every mode has 100000 changes.
Modes: off_two, off_hundred, toggle_low, toggle_high,
no_options_resolution, many_options_resolution. Option names have length ten.
"""
import sys


LIMIT = 100000
ALPHABET_SIZE = 26
NAME_DIGITS = 4


def name(index):
    letters = []
    for _ in range(NAME_DIGITS):
        letters.append(chr(ord('a') + index % ALPHABET_SIZE))
        index //= ALPHABET_SIZE
    return 'option' + ''.join(reversed(letters))


def build(seed, mode):
    shift = seed % 10
    if mode in ('off_two', 'off_hundred'):
        factor = 2 if mode == 'off_two' else 100
        lines = [str(LIMIT)]
        lines += [f'{name(i)} {factor}' for i in range(LIMIT)]
        lines += [f'320 200 {1000000000 - shift}', str(LIMIT)]
        lines += [f'Off {name(i)}' for i in range(LIMIT)]
    elif mode in ('toggle_low', 'toggle_high'):
        power = (1279999 if mode == 'toggle_low' else 7679999) - shift
        lines = ['1', 'optionaaaa 2', f'320 200 {power}', str(LIMIT)]
        lines += [('Off' if i % 2 == 0 else 'On') + ' optionaaaa' for i in range(LIMIT)]
    elif mode in ('no_options_resolution', 'many_options_resolution'):
        count = 0 if mode == 'no_options_resolution' else LIMIT
        lines = [str(count)]
        lines += [f'{name(i)} 2' for i in range(count)]
        lines += [f'320 200 {20000000 + shift}', str(LIMIT)]
        lines += ['Resolution 2560 1600' if i % 2 == 0 else 'Resolution 320 200'
                  for i in range(LIMIT)]
    else:
        raise ValueError('Unknown maximum-size settings mode')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    sys.stdout.write(build(int(sys.argv[1]), sys.argv[2]))
