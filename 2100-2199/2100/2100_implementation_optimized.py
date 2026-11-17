from sys import stdin

HOSTS = 2
UNLUCKY = 13
PRICE = 100

read = stdin.buffer.readline
guests = int(read())
people = HOSTS + guests + sum(read().rstrip().endswith(b"+one") for _ in range(guests))
print((people + (people == UNLUCKY)) * PRICE)
