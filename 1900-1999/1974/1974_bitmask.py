import sys


OCTAVE_COUNT = 8
SEMITONES_PER_OCTAVE = 12
PITCH_COUNT = OCTAVE_COUNT * SEMITONES_PER_OCTAVE
NATURAL_OFFSETS = (9, 11, 0, 2, 4, 5, 7)
SLOT_BITS = 10
SLOT_MASK = (1 << SLOT_BITS) - 1


def parse_note(token):
    pitch = (token[0] - ord('1')) * SEMITONES_PER_OCTAVE
    pitch += NATURAL_OFFSETS[token[1] - ord('A')]
    if len(token) > 2:
        pitch += 1 if token[2] == ord('+') else -1
    return pitch


def pack_source(notes):
    masks = [0] * PITCH_COUNT
    for position, pitch in enumerate(notes):
        masks[pitch] |= 1 << (position * SLOT_BITS)
    return masks


def absolute_similarity(masks, source_length, song):
    totals = 0
    shift = (len(song) - 1) * SLOT_BITS
    for pitch in song:
        totals += masks[pitch] << shift
        shift -= SLOT_BITS
    bound = min(source_length, len(song))
    best = 0
    while totals:
        best = max(best, totals & SLOT_MASK)
        if best == bound:
            return best
        totals >>= SLOT_BITS
    return best


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    source_length = int(next(tokens))
    source = [parse_note(next(tokens)) for _ in range(source_length)]
    masks = pack_source(source)
    answers = []
    for _ in range(int(next(tokens))):
        length = int(next(tokens))
        song = [parse_note(next(tokens)) for _ in range(length)]
        best = absolute_similarity(masks, source_length, song)
        answers.append(f'{best / length:.12f}')
    sys.stdout.write('\n'.join(answers) + '\n')


if __name__ == '__main__':
    main()
