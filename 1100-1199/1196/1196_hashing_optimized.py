import sys
from itertools import islice

# every line holds one date, so each line is converted as it is, and the
# known dates are counted with map instead of a Python loop
years = map(int, sys.stdin.buffer)
known = set(islice(years, next(years)))
queries = next(years)
# every date the student wrote counts once for each time it is written
print(sum(map(known.__contains__, islice(years, queries))))
