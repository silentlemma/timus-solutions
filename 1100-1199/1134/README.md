# 1134. Checking whether numbers read from cards showing k − 1 and k are possible

[Timus 1134](https://acm.timus.ru/problem.aspx?space=1&num=1134) · difficulty 197 · greedy

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n ≤ 1000` cards; card `k` shows `k − 1` on one side and `k` on
the other. A child took `m ≤ n` different cards in some order and read
one side of each. Given the `m` numbers read, decide whether they could
have come from some choice of cards and sides.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `m`, then the `m` numbers, each from `0` to `n`.

## Output

`YES` if the readings are possible, otherwise `NO`.

## Examples

### Example 1

Input:

```
5 4
2 0 1 2
```

Output:

```
NO
```

## Solution

The question is whether every reading can get its own card. The number
`x` appears on cards `x` and `x + 1` (only card 1 for `0`, only card `n`
for `n`), so each reading may use one of two neighbouring cards. Count
the readings of each number and go up from `0`. Readings of `x` first take
card `x`, then card `x + 1`. Taking the lower card first is safe: card
`x` shows only `x − 1` and `x`, and all readings of `x − 1` are already
placed, so nothing later can use it. If some reading of `x` finds both of
its cards taken, no assignment exists. `O(n + m)`.

Pitfalls:

- `0` and `n` each appear on one card only;
- the same number may be read several times, at most twice for a
  possible answer;
- the readings come in arbitrary order; only their counts matter.

The answers were compared with Kuhn's bipartite matching on every test
and on 400 random cases.

## Language notes

- All languages count the readings and run the same pass.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1134_greedy.cpp](1134_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.015 s | 192 KB |
| [1134_greedy.go](1134_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.031 s | 1104 KB |
| [1134_greedy.java](1134_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.078 s | 432 KB |
| [1134_greedy.py](1134_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.078 s | 492 KB |
| [1134_greedy.rs](1134_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.015 s | 204 KB |
