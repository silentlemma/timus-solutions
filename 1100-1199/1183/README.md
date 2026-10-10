# 1183. The shortest regular bracket sequence containing a given one

[Timus 1183](https://acm.timus.ru/problem.aspx?space=1&num=1183) · difficulty 196 · dp

Original problem by Andrew Stankevich, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given up to 100 characters from `(`, `)`, `[`, `]`, print a shortest
regular bracket sequence that contains them as a subsequence.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The brackets on one line, possibly empty.

## Output

A shortest regular sequence containing them.

## Checking

Any sequence is accepted if it is regular, contains the given brackets
in order and is as short as the stored answer.

## Examples

### Example 1

Input:

```
([(]
```

Output:

```
()[()]
```

## Solution

Let `add[i][j]` be the fewest brackets to add so that the piece
`s[i..j)` becomes regular. A single bracket needs one partner. A longer
piece either has a matching pair at its ends, wrapped around the best
fix of the inside, or splits into two parts fixed separately:

`add[i][j] = min(add[i+1][j−1] if s[i], s[j−1] match, min over k of add[i][k] + add[k][j])`.

Recording which choice won lets the sequence be rebuilt: a lone bracket
is printed with its partner, a wrapped pair around its inside, a split as
its two halves. `O(n³)` for `n ≤ 100`.

Pitfalls:

- the input line may be empty, and then the answer is an empty line;
- ties between choices must still record a real choice, otherwise the
  rebuild treats a long piece as a lone bracket;
- `([)]` needs two more brackets, and both `()[()]` and `([])[]` are
  shortest; any such answer is accepted.

The answers were compared with a separately written solution on 300
random lines of up to 100 brackets, and every printed sequence passed the
checker.

## Language notes

- Python rebuilds the answer with an explicit stack; the other languages
  recurse, which is at most 100 levels deep.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1183_dp.cpp](1183_dp.cpp) | G++ 13.2 x64 | dp | O(n³) | AC | 0.015 s | 460 KB |
| [1183_dp.go](1183_dp.go) | Go 1.14 x64 | dp | O(n³) | AC | 0.031 s | 1232 KB |
| [1183_dp.java](1183_dp.java) | Java 1.8 | dp | O(n³) | AC | 0.078 s | 616 KB |
| [1183_dp.py](1183_dp.py) | Python 3.12 x64 | dp | O(n³) | AC | 0.078 s | 876 KB |
| [1183_dp.rs](1183_dp.rs) | Rust 1.75 x64 | dp | O(n³) | AC | 0.001 s | 308 KB |
