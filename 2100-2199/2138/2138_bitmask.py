BITS = 8
MASK = (1 << BITS) - 1
BYTES = 4

_, number = open(0, "rb").read().split()
value = int(number)
result = 0
for _ in range(BYTES):
    result = (result << BITS) | (value & MASK)
    value >>= BITS
print(result)
