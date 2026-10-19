"""One finite numeric answer with absolute OR relative error at most 1e-6."""
from decimal import Decimal, DecimalException
from pathlib import Path
import sys


TOLERANCE = Decimal('0.000001')


def check(expected, candidate):
    reference, answer = expected.split(), candidate.split()
    if len(reference) != 1 or len(answer) != 1:
        return False
    try:
        target, actual = Decimal(reference[0]), Decimal(answer[0])
        if not target.is_finite() or not actual.is_finite():
            return False
        return abs(actual - target) <= TOLERANCE * max(Decimal(1), abs(target))
    except DecimalException:
        return False


def main():
    if not check(Path(sys.argv[2]).read_text(), Path(sys.argv[3]).read_text()):
        print('Expected one finite area within absolute or relative error 1e-6')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
