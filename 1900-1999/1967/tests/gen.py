"""Print seed mode: exact prints seed as n; certify prints exhaustive work bounds up to n.
Both modes require 2 <= seed <= 100000. Only exact generates test inputs.
"""
from array import array
import hashlib
import json
import sys


MAXIMUM = 100000
DECIMAL_BASE = 10


def certify(maximum):
    parts = [bin(value)[2:] for value in range(1, maximum + 1)]
    bits = ''.join(parts)
    endpoints = {}
    position = 0
    for value, part in enumerate(parts, 1):
        position += len(part)
        endpoints[position] = value
    size = len(bits) + 1
    cuts = array('I', [0]) * size
    trials_path = array('I', [0]) * size
    chars_path = array('Q', [0]) * size
    blocks_path = array('I', [0]) * size
    powers = []
    power = 1
    max_bits = max_trials = max_chars = first_end = 0
    worst_trials = worst_chars = worst_blocks = (0, 0)
    for end in range(1, size):
        index = trials = chars = 0
        while True:
            if index == len(powers):
                power *= DECIMAL_BASE
                powers.append(bin(power)[2:])
            threshold = powers[index]
            length = len(threshold)
            trials += 1
            if length > max_bits:
                max_bits, first_end = length, end
            if length >= end:
                previous = 0
                break
            start = end - length
            if bits[start] == '1':
                chars += length
                if bits[start:end] < threshold:
                    previous = start
                    break
            index += 1
        cuts[end] = previous
        trials_path[end] = trials + trials_path[previous]
        chars_path[end] = chars + chars_path[previous]
        blocks_path[end] = 1 + blocks_path[previous]
        max_trials, max_chars = max(max_trials, trials), max(max_chars, chars)
        value = endpoints.get(end)
        if value is not None and value >= 2:
            worst_trials = max(worst_trials, (trials_path[end], value))
            worst_chars = max(worst_chars, (chars_path[end], value))
            worst_blocks = max(worst_blocks, (blocks_path[end], value))
    assert cuts.itemsize == 4
    if sys.byteorder != 'little':
        cuts.byteswap()
    return {
        'all_prefix_ends_checked': len(bits),
        'all_allowed_n': maximum - 1,
        'bits_sha256': hashlib.sha256(bits.encode()).hexdigest(),
        'cut_map_sha256': hashlib.sha256(cuts.tobytes()).hexdigest(),
        'maximum_tested_power_bitlength': max_bits,
        'first_prefix_end_attaining_max_search': first_end,
        'maximum_local_trials': max_trials,
        'maximum_local_compared_character_bound': max_chars,
        'maximum_path_trials': {'value': worst_trials[0], 'n': worst_trials[1]},
        'maximum_path_compared_character_bound': {'value': worst_chars[0], 'n': worst_chars[1]},
        'maximum_path_blocks': {'value': worst_blocks[0], 'n': worst_blocks[1]},
    }


def main():
    maximum = int(sys.argv[1])
    mode = sys.argv[2]
    if mode not in ('exact', 'certify') or not 2 <= maximum <= MAXIMUM:
        raise ValueError('Expected n exact/certify, with 2 <= n <= 100000')
    if mode == 'exact':
        print(maximum)
    else:
        print(json.dumps(certify(maximum), indent=2))


if __name__ == '__main__':
    main()
