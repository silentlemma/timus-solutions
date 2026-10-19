# 2063. Same colours without looking

[Timus 2063](https://acm.timus.ru/problem.aspx?space=1&num=2063) · difficulty 432 · constructive

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A row holds n balls, each black or white, in an unknown arrangement. A
query `? v u` swaps the balls at positions v and u if v holds a black
ball and u a white one, and does nothing otherwise; the program is never
told what happened. After any number of queries it makes one claim
`! v u`: two positions that now hold balls of the same colour.

One test plays several games, the i-th one with n = i + 1. All tests
except the first have 99 games, n = 2, …, 100, and the program must win
at least 80 of them; the tests are fixed in advance and do not adapt to
the program. The first test is the example and only its format is
checked. At most 500 000 lines may be printed per test. The limits are
1 second and 64 MB.

## Input

The number of games m (99 in every test but the first), then the
starting rows in an encoded form that the program should not try to
read.

## Output

m game descriptions, each a sequence of `? v u` lines followed by one
`! v u` line, with 1 ≤ v, u ≤ n and v ≠ u.

## Checking

A checker plays every game. With 99 games at least 80 claims must be
right; in the example only the format is checked.

## Examples

### Example 1

Input:

```
2
01
101
```

Output:

```
? 1 2
? 2 1
? 1 2
! 2 1
? 1 2
? 3 1
! 1 2
```

## Solution

Sort the balls blindly. A query on neighbours `? i i+1` moves a white
ball left past a black one, so the queries of bubble sort — for every
end from n − 1 down to 1, the pairs (1, 2), (2, 3), …, (end, end + 1) —
put all white balls before all black ones whatever the arrangement was.
This takes n (n − 1) / 2 queries per game, 166 650 lines in all for
n = 2, …, 100, well within the limit.

Now the row is some white balls followed by some black balls. Two
neighbours (j, j + 1) differ only at the single boundary between the
colours, and if the row has one colour there is no boundary at all. A
claim on a neighbouring pair chosen uniformly at random therefore loses
with probability at most 1 / (n − 1), independently of how the tests
were made. Over the 99 games the expected number of losses is at most
1/1 + 1/2 + … + 1/99 ≈ 5.2, and losing 20 or more games happens with
probability about 2.6·10⁻⁹.

A fixed choice, such as always claiming (1, 2), would lose every game of
a test that puts a single white ball first, so the choice has to be
random. The programs use the splitmix64 generator seeded with the
FNV-1a hash of the whole input: the input differs between tests but is
fixed in advance, and the encoded rows are never decoded.

The example only shows the format: in its first game the claim (2, 1)
is wrong, in the second it is right.

## Language notes

The hash and the generator use unsigned 64-bit arithmetic: wrapping
multiplications in Rust, unsigned remainder in Java. All programs build
the output in one buffer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2063_constructive.cpp](2063_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.062 s | 3104 KB |
| [2063_constructive.go](2063_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 980 KB |
| [2063_constructive.java](2063_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 10052 KB |
| [2063_constructive.py](2063_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.125 s | 8008 KB |
| [2063_constructive.rs](2063_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 3212 KB |
