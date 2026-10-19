"""Finite similarity values with absolute or relative tolerance 1e-6."""
from decimal import Decimal,DecimalException
from pathlib import Path
import sys


TOLERANCE = Decimal('0.000001')


def check(expected,candidate):
    reference,answer=expected.split(),candidate.split()
    if not reference or len(reference)!=len(answer):
        return False
    try:
        for target_text,actual_text in zip(reference,answer):
            target,actual=Decimal(target_text),Decimal(actual_text)
            if not target.is_finite() or not actual.is_finite():
                return False
            if abs(actual-target)>TOLERANCE*max(Decimal(1),abs(target)):
                return False
        return True
    except DecimalException:
        return False


def main():
    if not check(Path(sys.argv[2]).read_text(),Path(sys.argv[3]).read_text()):
        print('Expected one finite similarity per melody within error 1e-6')
        return 1
    return 0


if __name__=='__main__':
    sys.exit(main())
