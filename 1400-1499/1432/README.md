# 1432. Twofold Luck

[Timus 1432](https://acm.timus.ru/problem.aspx?space=1&num=1432) · difficulty 7793 · greedy

Original problem by Evgeny Krokhalev, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tickets have 2N digits (4 ≤ 2N ≤ 1500, leading zeros allowed) and run
up to all nines. A ticket is lucky if the digit sums of its two halves
are equal, or if the sums of the digits at odd and at even places are
equal. Starting from the given ticket, find the first pair of
consecutive tickets t, t + 1 that are both lucky (the given ticket may
be t), or print "No solution".

Time limit: 1 second. Memory limit: 64 MB.

## Input

The current ticket.

## Output

The two tickets, or "No solution".

## Examples

### Example 1

Input:

```
293087
```

Output:

```
293149 293150
```

## Solution

Write the balance of a ticket as a sum of signed digits: the halves rule
counts the first half with + and the second with −, the places rule
alternates + and −; a ticket is lucky when one of the two balances is 0.
Choose which rule makes t lucky and which makes t + 1 lucky: four
combinations, each solved on its own, and the smallest answer wins.

If t ends with nines after a digit at position p that is at most 8,
then t + 1 has that digit one larger and zeros after it. So for a fixed
p the conditions are two linear equations on the digits up to p, with
the nines after p only adding constants. And t ≥ s holds exactly when
the digits of t up to p are not less than those of s, so the task for
each p is to find the smallest digit string x ≥ s[0..p] with x_p ≤ 8
meeting two equations with weights ±1.

Whether some digits can still meet the equations is an interval test.
Positions fall into four classes by the signs of their two weights, the
sum of each class can be any whole number between its bounds, and the
two equations become conditions on the difference of the "both +" and
"both −" sums and of the two mixed ones, plus a parity check. With
prefix counts per class the test takes O(1). The smallest x keeps the
longest possible prefix of s, so for each p try the positions where x
first exceeds s from the end, take the smallest digit there that still
fits, then fill the rest greedily with the smallest digits that fit.
Candidates from different p and combinations are compared by where they
first exceed s and the digit there, and the full strings only on a tie.
`O(L²)` for L = 2N.

Pitfalls:

- the given ticket and the next may already be the answer (test 08);
- t = all nines has no next ticket, and some tickets have no pair at
  all (tests 04, 05, 07, gen3);
- the two tickets may use different rules (test 01);
- a carry across many nines changes both balances at once (tests 10,
  12, gen2).

## Language notes

- Python runs under PyPy: the largest tests take about 2 s with CPython
  and about 0.4 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1432_greedy.cpp](1432_greedy.cpp) | G++ 13.2 x64 | greedy | O(L^2) | AC | 0.078 s | 3680 KB |
| [1432_greedy.go](1432_greedy.go) | Go 1.14 x64 | greedy | O(L^2) | AC | 0.140 s | 6868 KB |
| [1432_greedy.java](1432_greedy.java) | Java 1.8 | greedy | O(L^2) | AC | 0.468 s | 5536 KB |
| [1432_greedy.py](1432_greedy.py) | PyPy 3.10 x64 | greedy | O(L^2) | AC | 0.984 s | 12228 KB |
| [1432_greedy.rs](1432_greedy.rs) | Rust 1.75 x64 | greedy | O(L^2) | AC | 0.078 s | 416 KB |
