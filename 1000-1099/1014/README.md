# 1014. The smallest number with a given product of digits

[Timus 1014](https://acm.timus.ru/problem.aspx?space=1&num=1014) · difficulty 94 · greedy

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N` (`0 ≤ N ≤ 10^9`), find the smallest positive integer `Q` whose
decimal digits multiply to exactly `N`, or report that there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The integer `N`.

## Output

`Q`, or `-1` if no such number exists.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
36
```

Output:

```
49
```

### Example 2

Input:

```
0
```

Output:

```
10
```

## Solution

Two special cases first:

- `N = 0`: a number has digit product 0 exactly when it contains a zero, and
  the smallest such positive number is `10`;
- `N = 1`: the answer is `1` (not an empty number).

Otherwise no digit is 0 or 1 (a 1 only makes the number longer), so `Q`
consists of digits 2–9. A smaller number has fewer digits, and among numbers
of the same length the one with the digits in increasing order is the
smallest. So the task is to write `N` as a product of the fewest digits.

**Greedy:** divide `N` by 9 as long as possible, then by 8, 7, ..., 2, and
collect the digits. If something other than 1 is left, `N` has a prime
factor above 7 and the answer is `-1`. Print the collected digits in
increasing order.

Why the largest digits first: the powers of 3 are best packed into 9s (two
3s in one digit), the powers of 2 into 8s, and a leftover 3 and 2 form a
6 rather than two digits; dividing by 9, 8, ..., 2 in this order produces
exactly that packing. `O(log N)` division steps.

Pitfalls:

- `N = 0` and `N = 1`;
- the answer can have 12 digits (`10^9 = 2^9 · 5^9` gives `555555555888`):
  do not store it in a 32-bit integer — print the digits as a string.
- counting only divisions misses the cost of prepending digits: even
  [test 05](tests/05.in) builds a 12-digit answer.

## Optimized solutions

The optimized Java solution parses the number byte by byte from
`System.in` instead of using `Scanner`, and appends the digits and
reverses the string once instead of inserting each digit at the front:
380 KB instead of 1604 KB, with the same time.

## Language notes

The same greedy in every language; the digits are collected into a
string. For `k = O(log N)` collected digits, the simple C++, Go and Java
solutions repeatedly prepend, moving or copying the existing digits each
time: `O(k^2) = O((log N)^2)` total time. Python, Rust and the optimized
Java solution append and then reverse the order in `O(log N)` total
time. All solutions use `O(log N)` extra space.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1014_greedy.cpp](1014_greedy.cpp) | G++ 13.2 x64 | greedy | O((log N)^2) | AC | 0.015 s | 192 KB | 11278098 |
| [1014_greedy.go](1014_greedy.go) | Go 1.14 x64 | greedy | O((log N)^2) | AC | 0.031 s | 1096 KB | 11278101 |
| [1014_greedy.java](1014_greedy.java) | Java 1.8 | greedy | O((log N)^2) | AC | 0.125 s | 1604 KB | 11278109 |
| [1014_greedy.py](1014_greedy.py) | Python 3.12 x64 | greedy | O(log N) | AC | 0.093 s | 444 KB | 11278104 |
| [1014_greedy.rs](1014_greedy.rs) | Rust 1.75 x64 | greedy | O(log N) | AC | 0.046 s | 232 KB | 11278114 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1014_greedy_optimized.java](1014_greedy_optimized.java) | Java 1.8 | greedy | O(log N) | AC | 0.109 s | 380 KB | 11303700 |
