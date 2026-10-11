# 1260. The fussy photographer

[Timus 1260](https://acm.timus.ru/problem.aspx?space=1&num=1260) · difficulty 111 · dp

Original problem by Alexander Ipatov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N students aged 1, 2, …, N years (1 ≤ N ≤ 55) sit in a row. The one
aged 1 sits at the left end, and the ages of any two neighbours differ by
at most 2. How many such rows are there?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The number of rows.

## Examples

### Example 1

Input:

```
4
```

Output:

```
4
```

## Solution

Let a(k) be the number of rows for the ages 1..k. Look at who sits
second:

- age 2: the rest is a row of 2..k starting with 2, the same problem
  shifted by one, a(k − 1) ways;
- age 3, then age 2: the next must be 4, and the rest is a row of 4..k
  starting with 4, a(k − 3) ways;
- age 3, but 2 later: the neighbours of 2 can only be 1, 3 and 4, and 1
  and 3 are already taken next to each other, so 2 sits at the right end
  next to 4. This forces the zigzag 1, 3, 5, … up the odd ages and back
  down the even ones to 4, 2: exactly one row.

So a(k) = a(k − 1) + a(k − 3) + 1, with a(1) = a(2) = 1 and a(3) = 2.
Running the rule backwards gives a(0) = 0 and a(−1) = −1, which lets the
loop start from k = 1 with no special cases. a(55) = 1 388 937 263
still fits in 32 bits, but the solutions use 64. `O(N)`.

Pitfalls:

- the third case is easy to miss: for N = 5 it is the row 1, 3, 5, 4, 2
  (test 05);
- N = 1 and N = 2 both have a single row (tests 02, 03).

The recurrence was compared with listing all permutations for N up to
10.

## Language notes

- All languages keep the last three values in three variables.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1260_dp.cpp](1260_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB |
| [1260_dp.go](1260_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 1076 KB |
| [1260_dp.java](1260_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 1568 KB |
| [1260_dp.py](1260_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 404 KB |
| [1260_dp.rs](1260_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 232 KB |
