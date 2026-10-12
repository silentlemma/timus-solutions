# 1324. Extra Spaces

[Timus 1324](https://acm.timus.ru/problem.aspx?space=1&num=1324) · difficulty 929 · greedy

Original problem: idea by Stanislav Vasiliev, prepared by Stanislav Vasiliev and Igor Goldberg, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text has runs of 1 to L spaces, L < 2 000 000. An editor command
replaces every group of exactly k spaces by one space in a single pass
from left to right, without looking again at what it has just replaced.
So with k = 2 a run of six spaces becomes three, not one.

Find the smallest number of commands, with chosen lengths k, that turn
every run of up to L spaces into a single space. Among such plans choose
one that handles every run of up to K spaces for the largest possible K.
Any such plan is accepted.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The number L.

## Output

The number of commands R, then R lines with the length replaced by each
command, in the order they are run.

## Checking

The checker requires the same number of commands as the expected plan
and computes, for both plans, the longest K such that every run of 1 to
K spaces ends up as one space. The plan must reach L and the same K as
the expected plan.

## Examples

### Example 1

Input:

```
22
```

Output:

```
4
6
3
2
2
```

## Solution

One command with length k turns a run of n spaces into n div k + n mod k
spaces. Go back from the end, where only a single space may remain, and
let M be the longest run that the commands chosen so far turn into one
space. A run of n = q · k + r spaces becomes q + r, and the first run
that becomes longer than M is (M − k + 2) · k + (k − 1). So a command
with 2 ≤ k ≤ M + 1 handles every run of up to (M + 3 − k) · k − 2
spaces, and a longer k gains nothing: the run of k − 1 spaces stays as
it is.

That reach grows with M, so the best choice at every step back is the k
with the largest reach, k = ⌊(M + 3) / 2⌋, the top of the parabola. Each
step then gives the largest possible M, and the first R with M ≥ L is
the smallest number of commands. Starting from M = 1 the reaches are 2,
4, 10, 40, 460, 53 590 and 718 052 410, so no more than seven commands
are ever needed. The plan is printed from the first command to the
last, which is the reverse of the order in which it was found. `O(R)`.

Pitfalls:

- for L = 1 nothing needs to be replaced and the answer is a single 0
  (test 02);
- even M give two equally good k, so several plans are optimal and a
  checker is needed: for 22 both 6, 3, 2, 2 and 7, 4, 3, 2 reach 40;
- the reach after seven commands, 718 052 410, still fits a 32-bit
  integer, but the solutions use 64-bit numbers anyway.

The formula for one command was compared with direct runs for all M up
to 79 and k up to 89, and the plans with all lists of up to four lengths
up to 23 for every L up to 40.

## Language notes

- All five solutions build the plan the same way.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1324_greedy.cpp](1324_greedy.cpp) | G++ 13.2 x64 | greedy | O(R) | AC | 0.015 s | 196 KB |
| [1324_greedy.go](1324_greedy.go) | Go 1.14 x64 | greedy | O(R) | AC | 0.031 s | 1068 KB |
| [1324_greedy.java](1324_greedy.java) | Java 1.8 | greedy | O(R) | AC | 0.109 s | 1620 KB |
| [1324_greedy.py](1324_greedy.py) | Python 3.12 x64 | greedy | O(R) | AC | 0.093 s | 460 KB |
| [1324_greedy.rs](1324_greedy.rs) | Rust 1.75 x64 | greedy | O(R) | AC | 0.031 s | 224 KB |
