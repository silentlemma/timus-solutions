# 1430. Crime and Punishment

[Timus 1430](https://acm.timus.ru/problem.aspx?space=1&num=1430) · difficulty 463 · number_theory

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Goods cost A or B each, any number of each can be bought, and there are
N to spend (1 ≤ A, B, N ≤ 2·10⁹). Find counts x and y with
x·A + y·B ≤ N as large as possible; any best pair will do.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

A, B and N.

## Output

x and y.

## Examples

### Example 1

Input:

```
8 5 22
```

Output:

```
2 1
```

## Solution

Let A ≥ B (otherwise swap them and swap the answer back). If x ≥ B,
then B goods at A can be traded for A goods at B at the same total, so
some best answer has x < B; and x·A ≤ N gives x ≤ N / A. So x runs from
0 to min(N / A, B − 1), and for each x the rest buys y = (N − x·A) / B
goods at B. Since A ≥ B, either B ≤ √N or N / A < √N, so there are at
most about 44 722 values of x; the loop also stops as soon as all N is
spent. `O(√N)`.

Pitfalls:

- sums like x·A exceed 32 bits (tests 03, 06);
- if both prices exceed N, nothing is bought (test 12);
- the answer is not unique, so the tests use a checker (test 01).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1430_number_theory.cpp](1430_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 128 KB |
| [1430_number_theory.go](1430_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 1068 KB |
| [1430_number_theory.java](1430_number_theory.java) | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 1684 KB |
| [1430_number_theory.py](1430_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt N) | AC | 0.109 s | 468 KB |
| [1430_number_theory.rs](1430_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N) | AC | 0.062 s | 220 KB |
