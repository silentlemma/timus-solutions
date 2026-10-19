# 1896. War Games 2.1

[Timus 1896](https://acm.timus.ru/problem.aspx?space=1&num=1896) · difficulty 864 · fenwick, bitmask

Problem prepared by Maxim Pivko.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Arrange labels 1 through N in a circle. Count K currently remaining
labels, starting with 1, and remove the last counted label. Resume
counting from its next remaining successor and repeat until the circle
is empty. The first removed label is K.

If sᵢ is the label removed at step i, compute the bitwise XOR of
|i − sᵢ| over all steps i from 1 through N. The limits are 0.5 seconds
and 6 MB; the statement allows only C, C++ and Pascal; the submit form also offers Rust.

## Input

One line contains N and K, with 1 ≤ N ≤ 1 100 000 and 1 ≤ K ≤ N.

## Output

Print the resulting integer XOR.

## Checking

Outputs are compared token by token as integers.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
2
```

## Solution

Keep the remaining labels in increasing order and let r be the
zero-based rank at which counting resumes, initially 0. With c labels
left, the next removal rank is (r + K − 1) modulo c. Find the label of
that rank, combine its absolute difference from the current step into
the XOR, and delete it. Leave r equal to the removed rank; it now
identifies the successor, with wraparound handled by the next modulo.

To support rank selection within the memory limit, divide the labels
into words of 64 alive bits. A set bit means the corresponding label
is still present. Above these words, maintain a Fenwick tree of their
set-bit counts. Its prefix search finds the first word whose cumulative
count exceeds the required zero-based rank r. Subtract the count of
earlier words to obtain the zero-based rank within that word.

Selection inside one word takes constant time: use set-bit counts to
choose between consecutive halves of the word until the bit is located.
The word size is fixed at 64 bits. Clear the selected bit and decrement
its word's Fenwick count.

The Fenwick prefix counts always equal the numbers of surviving labels.
Therefore its search, followed by selection within the word, returns
exactly the required surviving rank. The rank recurrence is precisely
the circular counting rule, so every removed label and every XOR term
is correct.

For W = ⌈N/64⌉, each removal takes `O(1 + log W)` time and the total
is `O(N(1 + log W))`, also bounded by `O(N log N)`. Storage is `O(W)`
machine words. The full elimination order is never stored.

In the example, removals are 3, 1, 5, 2, 4. The absolute differences
are 2, 1, 2, 2, 1, whose XOR is 2.

Pitfalls:

- K counts surviving labels, including the current starting label;
- ranks start at 0, while labels and step numbers start at 1;
- do not increment r after deletion, or the successor is skipped;
- clear unused bits of the final word;
- use unsigned 64-bit masks and handle a full word without shifting by 64;
- do not retain a per-label tree or the output permutation unnecessarily.

## Language notes

The statement allows only C, C++ and Pascal, but the Timus submit form
also offers Rust 1.75, so there are C++ and Rust solutions; Go, Python
and Java cannot be submitted. Both keep about 17 000 words and counters,
far below 6 MB.

The answers agree with a direct simulation of the eliminations on 1625
cases, including the largest N and sizes at word boundaries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1896_fenwick_bitmask.cpp](1896_fenwick_bitmask.cpp) | G++ 13.2 x64 | fenwick, bitmask | O(N log N) | AC | 0.156 s | 628 KB |
| [1896_fenwick_bitmask.rs](1896_fenwick_bitmask.rs) | Rust 1.75 x64 | fenwick, bitmask | O(N log N) | AC | 0.187 s | 364 KB |
