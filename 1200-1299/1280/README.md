# 1280. Topological sorting

[Timus 1280](https://acm.timus.ru/problem.aspx?space=1&num=1280) · difficulty 140 · graphs

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N ≤ 1000 subjects and M ≤ 100 000 rules "s u": subject s
must be studied before subject u. Is the given order of all N subjects
consistent with every rule?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, the M rules, then the order of the N subjects.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 3 4 5 2
```

Output:

```
YES
```

### Example 2

Input:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 2 4 5 3
```

Output:

```
NO
```

## Solution

There is no need to sort anything: record the place of each subject in
the given order and check that every rule goes forward, that is, s
comes before u. If the rules contain a cycle, some rule on it must go
backwards in any order, so the check already says `NO`, as the
statement wants. `O(N + M)`.

Pitfalls:

- one violated rule is enough for `NO`; the plan in test 02 violates
  three rules: 3 → 5, 5 → 2, and 4 → 2;
- a rule may lead from a subject to itself, which no order satisfies
  (test 04);
- rules may repeat (test 07);
- with no rules every order is right (test 06).

## Language notes

- All languages store the places in an array and scan the rules once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1280_graphs.cpp](1280_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.109 s | 976 KB |
| [1280_graphs.go](1280_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.125 s | 3416 KB |
| [1280_graphs.java](1280_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 1324 KB |
| [1280_graphs.py](1280_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 24372 KB |
| [1280_graphs.rs](1280_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 3688 KB |
