# 1487. Chinese Football

[Timus 1487](https://acm.timus.ru/problem.aspx?space=1&num=1487) · difficulty 1244 · graphs

Original problem by Sergey Pupyrev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N teams (2 ≤ N ≤ 1000) have played some matches without draws, given
as a table of wins, and results are transitive: if A beat B and B beat
C, A beats C too. A is stronger than B if A beat B or beat some team
stronger than B. A plays better than B if A is not weaker than any team
that is stronger than B. Answer Q ≤ 50000 questions "does A play better
than B?" with "YES" or "No".

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, the N × N table of 0s and 1s, Q, then Q lines A B.

## Output

"YES" or "No" for each question.

## Examples

### Example 1

Input:

```
3
011
000
000
2
2 3
1 3
```

Output:

```
No
YES
```

## Solution

"Stronger" is reachability along the wins, and the wins form an
acyclic graph because the results are transitive. A is not weaker than
C when C does not reach A. So A plays better than B when no team that
reaches B also reaches A: the two sets of stronger teams are disjoint.

Those sets are bit sets. Taking the teams in topological order (Kahn's
algorithm on the wins), the set of a team is the union of the sets of
the teams that beat it, plus those teams. That is one bit-set union of
N/64 words per match. Each question is then one intersection.
`O(N³/64 + Q·N/64)`.

Pitfalls:

- the answers are "YES" and "No", in different cases (all tests);
- every team plays better than a team nobody is stronger than, even if
  it lost to that team (tests 02, 03);
- a common winner above both teams makes the answer "No" both ways
  (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1487_graphs.cpp](1487_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^3 / 64 + Q N / 64) | AC | 0.125 s | 2904 KB |
| [1487_graphs.go](1487_graphs.go) | Go 1.14 x64 | graphs | O(N^3 / 64 + Q N / 64) | AC | 0.140 s | 11660 KB |
| [1487_graphs.java](1487_graphs.java) | Java 1.8 | graphs | O(N^3 / 64 + Q N / 64) | AC | 0.156 s | 15288 KB |
| [1487_graphs.py](1487_graphs.py) | Python 3.12 x64 | graphs | O(N^3 / 64 + Q N / 64) | AC | 0.515 s | 20988 KB |
| [1487_graphs.rs](1487_graphs.rs) | Rust 1.75 x64 | graphs | O(N^3 / 64 + Q N / 64) | AC | 0.062 s | 8396 KB |
