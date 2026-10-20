# 2137. Extending a binary string to maximize the periods of its borders

[Timus 2137](https://acm.timus.ru/problem.aspx?space=1&num=2137) · difficulty 6004 · dp, strings

Original problem by Alexey Kotelnikov and idea by Mikhail Rubinchik and special thanks to Vladislav Isenbaev, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A border of a string is a proper non-empty prefix that is also a suffix.
The complexity of a string is the number of distinct periods among its
borders, and its dynamic complexity is the sum of the complexities of
all its prefixes. For a binary string S and every i from 1 to 25, find
the largest dynamic complexity of a string S + T with |T| = i. The
limits are 2 seconds and 64 MB.

## Input

S, 0 ≤ |S| ≤ 10⁵, over the characters "X" and ".".

## Output

25 numbers, the answers for i = 1 … 25.

## Examples

### Example 1

Input:

```
X.X
```

Output:

```
2
4
5
7
9
12
14
16
19
21
23
26
30
32
35
38
41
45
47
50
54
58
62
67
70
```

## Solution

The borders of a prefix are its longest border π, the longest border of
that, and so on, the chain of the prefix function. The period of a
border b is b − π(b), and along the chain equal periods come in runs.
So with rank(0) = 0 and rank(b) = rank(π(b)) + [the period of b differs
from that of π(b)], the complexity of a prefix with longest border π is
rank(π). Appending a character updates π, the period and the rank in
amortized O(1), and removing characters again is a plain truncation.

The prefixes of S contribute a fixed amount, so the task is to choose T
to maximize the sum of rank(π) over the new prefixes. The first half of
T, about a dozen characters, is enumerated exhaustively with this
append-and-undo routine. For the rest of T the next longest border
depends only on the current one and the next character, and two cases
remain.

- The longest border is shorter than the text built so far: it lies in
  known text, so the next border follows the KMP automaton of that text
  with transitions for both characters. A DP over automaton states keeps
  the best total for every reachable state and every extra length.
- The longest border is at least as long as the built text: then the
  string has a short period p, at most the number of characters left.
  Keeping that border means repeating the period, which is simulated
  directly for every such p along the border chain. Breaking the period
  at some step drops the border into known text, and that state is fed
  into the DP as a new start.

The best value seen for every length is the answer. The exhaustive
first half and the bounded number of reachable states keep the work
within the limits; all five solutions agree with an independent
accepted implementation on random and periodic strings.

In the example "X.X" can be extended by "." for complexity 2: the
prefix "X.X." has the border "X." with period 2, and "X.X" itself
contributes the border "X".

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2137_dp_strings.cpp](2137_dp_strings.cpp) | G++ 13.2 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.031 s | 2976 KB |
| [2137_dp_strings.go](2137_dp_strings.go) | Go 1.14 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.062 s | 12116 KB |
| [2137_dp_strings.java](2137_dp_strings.java) | Java 1.8 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.156 s | 7392 KB |
| [2137_dp_strings.py](2137_dp_strings.py) | Python 3.12 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.875 s | 15324 KB |
| [2137_dp_strings.rs](2137_dp_strings.rs) | Rust 1.75 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.046 s | 4816 KB |
