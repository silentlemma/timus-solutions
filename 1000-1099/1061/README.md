# 1061. The cheapest window of unlocked buffers

[Timus 1061](https://acm.timus.ru/problem.aspx?space=1&num=1061) · difficulty 670 · prefix_sums

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` buffers (`1 ≤ N ≤ 100000`), each locked (`*`) or holding a
value from 0 to 9. Choose `K` consecutive buffers (`1 ≤ K ≤ 10000`), none
of them locked, with the smallest total value, and print the number `L`
of the first one; among equal totals the smallest `L`. Print `0` if no
such window exists.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `K`, then the `N` states, 80 characters per line (the last line
may be shorter).

## Output

`L`, or `0`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
100 53
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Output:

```
0
```

### Example 2

Input:

```
100 10
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Output:

```
36
```

## Solution

Two prefix sums over the buffers: the total value and the number of
locked buffers among the first `i`. A window `[L, L + K − 1]` is allowed
when the lock count does not change across it, and its value is a
difference of the value sums. Checking all `N − K + 1` windows from left
to right and keeping a strictly smaller value gives the smallest `L`
among the cheapest. `O(N)`.

Pitfalls:

- `K > N`: no window at all, the answer is `0`;
- ties: keep the first window, so replace the best only on a strictly
  smaller value;
- the states are split over lines of 80 characters: read characters and
  skip the line breaks;
- locked buffers have no value; they only block windows.

## Language notes

- **C++**, **Go**, **Java**: the states are read character by character
  after the two numbers.
- **Python**, **Rust**: the whole input is split into words and the rows
  are joined.

## Optimized solutions

The Python version divides the input into runs of unlocked buffers. Within each run it slides a window of K buffers, subtracting the value that leaves and adding the value that enters. A strictly smaller sum updates the answer, preserving the first position in a tie. The search takes O(N) time and O(N) space including the input and runs. Submission 11317122 took 0.093 s and 1048 KB, compared with 0.125 s and 9992 KB for the base.

Go reads the states as a stream and keeps the last K values in a byte ring buffer. A locked buffer clears the window. The scan takes O(N) time and O(K) space. Submission 11317123 took 0.015 s and 1088 KB, compared with 0.031 s and 2704 KB for the base.

Rust reads the states as a stream and keeps the last K values in a byte ring buffer. A locked buffer clears the window. The scan takes O(N) time and O(K) space. Submission 11317124 took 0.015 s and 204 KB, compared with 0.015 s and 2196 KB for the base.

C++ reads the states as a stream and keeps the last K values in a byte ring buffer. A locked buffer clears the window. The scan takes O(N) time and O(K) space. Submission 11317125 took 0.015 s and 184 KB, compared with 0.015 s and 1356 KB for the base.

Java reads the states as a stream and keeps the last K values in a byte ring buffer. A locked buffer clears the window. The scan takes O(N) time and O(K) space. Submission 11317126 took 0.093 s and 408 KB, compared with 0.109 s and 1592 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322104 · Go 1.14 x64 №11322105 · Java 1.8 №11322106 · Python 3.12 x64 №11322107 · Rust 1.75 x64 №11322108.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1061_prefix_sums.cpp](1061_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 1356 KB | 11322104 |
| [1061_prefix_sums.go](1061_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 2704 KB | 11322105 |
| [1061_prefix_sums.java](1061_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 1592 KB | 11322106 |
| [1061_prefix_sums.py](1061_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.125 s | 9992 KB | 11322107 |
| [1061_prefix_sums.rs](1061_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.015 s | 2196 KB | 11322108 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1061_two_pointers.py](1061_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.093 s | 1048 KB | 11317122 |
| [1061_two_pointers.go](1061_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.015 s | 1088 KB | 11317123 |
| [1061_two_pointers.rs](1061_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.015 s | 204 KB | 11317124 |
| [1061_two_pointers.cpp](1061_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 184 KB | 11317125 |
| [1061_two_pointers.java](1061_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.093 s | 408 KB | 11317126 |
