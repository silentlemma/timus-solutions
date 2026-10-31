import sys
from array import array
from itertools import islice

# sieving this range gives 15000 primes, enough for every statement query.
LIMIT = 163842
FIRST_ODD_PRIME = 3
OUTPUT_BATCH_SIZE = 1024


def main():
    # index i represents 2*i+1; even numbers other than two cannot be prime.
    odd_count = LIMIT // 2
    sieve = bytearray([1]) * odd_count
    sieve[0] = 0
    p = FIRST_ODD_PRIME
    while p * p < LIMIT:
        if sieve[p // 2]:
            start = p * p // 2
            sieve[start::p] = bytes(len(range(start, odd_count, p)))
        p += 2
    # computed primes are below LIMIT and fit a four-byte unsigned int.
    primes = array("I", [2])
    primes.extend(2 * i + 1 for i in range(1, odd_count) if sieve[i])
    del sieve
    # consume lines incrementally instead of retaining all input tokens.
    tokens = (int(word) for line in sys.stdin.buffer for word in line.split())
    queries = next(tokens)
    # bounded output batches avoid keeping one string per query in memory.
    while queries:
        count = min(queries, OUTPUT_BATCH_SIZE)
        sys.stdout.write("\n".join(str(primes[n - 1]) for n in islice(tokens, count)) + "\n")
        queries -= count


main()
