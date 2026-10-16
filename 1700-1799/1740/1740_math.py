l, k, h = map(int, input().split())
# the time to reach x is x h / k plus a part that repeats every k km and
# lies between 0 and h, so the last l mod k km take from 0 to h hours
whole, rest = divmod(l, k)
print("%.8f %.8f" % (whole * h, (whole + (rest > 0)) * h))
