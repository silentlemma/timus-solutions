# 1967. Optimal Decimal Concatenation of Binary Blocks

[Timus 1967](https://acm.timus.ru/problem.aspx?space=1&num=1967) · difficulty 5145 · greedy

Original problem by Ilya Zvigintsev, from the Open Ural FU Personal Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Concatenate the binary representations of the integers 1,2,…,n into a
string S. Partition S into nonempty blocks, allowing a cut only before
a bit 1, so no block has a leading zero. Convert each block to a positive
decimal integer and concatenate those decimal representations in order.
Minimize the resulting integer and output any optimal partition as bit
lengths. The initial representation of 1 is part of S. Limits: 1 second,
64 MB.

## Input

One integer n, 2≤n≤100,000.

## Output

Two lines: the number of blocks, then their positive lengths in bits,
in left-to-right order. They must cover S exactly. Any partition yielding
the minimum decimal integer is accepted.

## Checking

A checker verifies the count, the total length and the legal starts of
the blocks, and checks optimality with the exchange criterion proved
below; any optimal split is accepted.

## Examples

```
5
```

```
2
1 10
```

## Solution

For n=5, S=11011100101. The four-bit suffix 0101 cannot start a block.
The seven-bit suffix 1100101 represents 101, which is not less than 100.
The ten-bit suffix 1011100101 represents 741, less than 1000. The rule
below therefore takes the last ten bits and leaves the first bit alone.
The decimal result is 1||741=1741; merging everything would give 1765.

### Strict exchange rule

Let consecutive binary blocks A,B represent positive integers a,b.
Let B have q bits and b have d decimal digits. Keeping them separate
produces a·10^d+b, while merging them produces a·2^q+b. Thus splitting
strictly improves the number exactly when 10^d<2^q. Call B economical
in this case. Otherwise merging strictly improves it. Equality is
impossible for positive d: a power of ten has a factor five.

Replacing a local positive decimal number by a smaller one also improves
the whole concatenation with fixed outer blocks. A shorter representation
reduces the total digit count; an equally long smaller representation
wins lexicographically after the same prefix. Therefore the exchange
rule applies inside an arbitrary partition, not just to two isolated blocks.

### The last block is forced

If an optimal partition has multiple blocks, its last block must be
economical; otherwise merge the last two and improve. If that last block
contains a shorter economical suffix, split it before that suffix and
improve. Consequently the last block must be the shortest proper
economical suffix of the entire remaining string. A one-block partition
cannot be optimal if such a suffix exists, since splitting before it improves.

Choose that suffix and recurse on the remaining prefix. The prefix must
be optimal too: appending the fixed last decimal block preserves numeric
order. If no proper economical suffix exists, any multiple-block answer
would have a non-economical last block; the entire prefix is optimal as
one block. This proves the greedy algorithm for every binary string
starting with 1.

### Find the suffix without floating point

A q-bit value satisfies 2^(q−1)≤b<2^q. If economical, its threshold
T=10^d lies between b and 2^q, so the binary length of T is q.
Conversely, if T=10^d has q bits and a q-bit suffix is smaller than T,
then b≥2^(q−1)>10^(d−1), so b really has d decimal digits and is economical.

Enumerate T=10,100,1000,… in increasing binary length. For each q, require
the suffix to begin with 1, then compare its q bits lexicographically
with the binary representation of T. The first strict match is the
shortest economical suffix. If q reaches the remaining string length,
there is no proper match: emit the whole prefix. Record lengths while
peeling from right to left, then reverse them.

Grow and cache powers lazily. The native versions multiply an arbitrary
binary string by ten using a right-to-left carry. Python multiplies an
integer and converts it to binary. There is no fixed block-length cap,
machine-integer restriction, logarithmic approximation or conversion of
the whole resulting number to decimal.

Let L=|S| and K be the largest tested threshold bit length. A conservative
bound is `O(n log n + L K²)` time and `O(L+K²)` space, including cached
binary powers and the output. One suffix search tests `O(K)` thresholds
and compares at most `O(K²)` bits. Forming S takes `O(n log n)` time.

For this finite input domain, `python tests/gen.py 100000 certify` checks every
one of the 1,568,946 prefix ends of S for n=100,000 and accumulates search
work for every allowed n. It finds K≤226, at most 461,145 threshold tests
and 2,780,158 compared-character bounds along any answer path, and at most
131,447 output blocks. The code never assumes these bounds or truncates
a search; correctness follows from exchange, while the reproducible
certificate explains the full-domain workload.

Minimize numerically: digit count comes before lexicographic order. Include
the initial bit 1. Cuts before zero are illegal. The comparison with 10^d
is strict. Search suffixes from shortest to longest and reverse output
lengths at the end. Neither 64 nor 128 bits suffice for thresholds; even
small actual inputs use longer blocks. Avoid a guessed length limit or
floating-point logarithms.

## Language notes

C++, Go 1.14, Java 8 and Rust 1.75 keep powers as binary strings or byte
vectors and implement multiplication by ten with a small carry. Python
3.12 uses exact integers and bin, never a giant decimal conversion. Java
compares characters in place to avoid substring allocations. All versions
use only their standard libraries and no recursion.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1967_greedy.cpp](1967_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n+L*K^2) | AC | 0.031 s | 3456 KB |
| [1967_greedy.go](1967_greedy.go) | Go 1.14 x64 | greedy | O(n log n+L*K^2) | AC | 0.062 s | 10772 KB |
| [1967_greedy.java](1967_greedy.java) | Java 1.8 | greedy | O(n log n+L*K^2) | AC | 0.187 s | 14964 KB |
| [1967_greedy.py](1967_greedy.py) | Python 3.12 x64 | greedy | O(n log n+L*K^2) | AC | 0.343 s | 9656 KB |
| [1967_greedy.rs](1967_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n+L*K^2) | AC | 0.031 s | 4704 KB |
