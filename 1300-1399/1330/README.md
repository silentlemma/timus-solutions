# 1330. Intervals

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · difficulty 96 · prefix_sums

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 10 000 sensors give integer readings from −10 000 to 10 000. Answer
up to 100 000 questions: the sum of the readings of sensors i to j,
i ≤ j.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then N readings, then Q and Q pairs i, j.

## Output

One sum per line.

## Examples

### Example 1

Input:

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

Output:

```
9
-1
5
```

## Solution

Keep before[i], the sum of the first i readings, with before[0] = 0.
The sum from i to j is then before[j] − before[i − 1], one subtraction
per question. `O(N + Q)`.

Pitfalls:

- the sums lie between −10⁸ and 10⁸, which fits a 32-bit integer;
- there may be no questions at all (test 03);
- with 100 000 questions the input and the output have to be read and
  written in large pieces to stay within 0.5 seconds.

## Language notes

- Java reads the input through its own byte buffer and collects the
  answers in one string.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.109 s | 7492 KB |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB |
