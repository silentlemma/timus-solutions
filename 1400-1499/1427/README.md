# 1427. SMS

[Timus 1427](https://acm.timus.ru/problem.aspx?space=1&num=1427) · difficulty 364 · greedy

Original problem by Dmitry Kovalioff, Nikita Rybak and Ilya Grebnov, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of up to 100 000 characters (Latin letters, spaces, digits and
the marks . , ; : ! ? - ") is cut into consecutive SMS messages. A
message of only letters and spaces may be up to M characters long; any
other message only up to N (1 ≤ N ≤ M ≤ 10 000). Find the smallest
number of messages.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N and M, then the text on its own line.

## Output

The smallest number of messages.

## Examples

### Example 1

Input:

```
10 15
On the 11-th of February, 2006 the contest "Timus Top Coders: First Challenge" is held!
```

Output:

```
8
```

## Solution

Let run(i) be the number of letters and spaces starting at position i.
A message starting at i can end anywhere up to i + max(N, min(M,
run(i))). This farthest end never moves back as i grows (i + N and the
end of the run of letters both only grow), and with such a monotone
reach the greedy that always sends the longest possible message is
optimal: any other plan is at each step no farther ahead. The runs are
counted from the end of the text. `O(L)`.

Pitfalls:

- the text may start with spaces, so the second line must be read whole
  and not after skipping whitespace (test 04);
- digits do not count as letters (tests 03, 06);
- a message of letters may be shorter than N anyway; the long form only
  helps when the run is longer than N (test 05).

## Optimized solutions

C++ and Go extend the current message while reading the text. Keep its length and whether every character so far is a letter or space. Once the next character would exceed the applicable limit, finish the current message and use that character to start the next. This implements the same longest-message rule in O(L) time with O(1) extra space.

The accepted base implementations [1427_greedy.java](1427_greedy.java), [1427_greedy.py](1427_greedy.py), [1427_greedy.rs](1427_greedy.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1427_greedy.cpp](1427_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 924 KB | 11286185 |
| [1427_greedy.go](1427_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 3196 KB | 11286186 |
| [1427_greedy.java](1427_greedy.java) \* | Java 1.8 | greedy | O(L) | AC | 0.093 s | 1612 KB | 11286188 |
| [1427_greedy.py](1427_greedy.py) \* | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 4392 KB | 11286187 |
| [1427_greedy.rs](1427_greedy.rs) \* | Rust 1.75 x64 | greedy | O(L) | AC | 0.031 s | 1252 KB | 11286189 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1427_greedy_optimized.cpp](1427_greedy_optimized.cpp) \* | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 112 KB | 11310456 |
| [1427_greedy_optimized.go](1427_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 912 KB | 11310457 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
