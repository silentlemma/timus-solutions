DWARFS = 7
RADIX = 10
ZERO = ord("0")

remainder = 0
for digit in input().strip():
    remainder = (RADIX * remainder + ord(digit) - ZERO) % DWARFS
print(remainder)
