import os
from sys import stdout

LOW_MARK = 3
MIDDLE_MARK = 4

values = map(int, open(0, "rb", buffering=0).read().split())
count = next(values)
has_low = False
fours = 0
for _ in range(count):
    grade = next(values)
    has_low |= grade == LOW_MARK
    fours += grade == MIDDLE_MARK
if has_low:
    scholarship = "None"
elif fours == 0:
    scholarship = "Named"
elif 2 * fours <= count:
    scholarship = "High"
else:
    scholarship = "Common"
print(scholarship)

# Flush before skipping interpreter finalization in this standalone judge program.
stdout.flush()
os._exit(0)
