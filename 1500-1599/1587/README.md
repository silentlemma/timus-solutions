# 1587. Flying Pig

[Timus 1587](https://acm.timus.ru/problem.aspx?space=1&num=1587) · difficulty 819 · greedy

Original problem by Sergey Pupyrev, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The spectators give a pig n marks (1 ≤ n ≤ 50000), each an integer from
−3 to 3. Find the largest product of a non-empty run of consecutive
marks.

Time limit: 0.75 seconds. Memory limit: 64 MB.

## Input

n, then the n marks.

## Output

The largest product, written in full.

## Examples

### Example 1

Input:

```
3
1 2 -1
```

Output:

```
2
```

## Solution

Zeros cut the marks into runs. Inside a run every mark is at least 1 in
absolute value, so a longer piece never has a smaller absolute product,
and the product is ±2ᵃ·3ᵇ, where a and b count the marks ±2 and ±3.
With an even number of negative marks the whole run is positive. With an
odd number, the best positive piece drops either everything up to the
first negative mark or everything from the last one. Prefix counts give
a and b of each candidate, and candidates are compared by
a·ln 2 + b·ln 3; distinct pairs (a, b) never come close enough for the
doubles to mix them up. Only the winner is turned into a big number.

If no positive piece exists, every run is a single negative mark: the
answer is 0 when there is a zero and the mark itself otherwise (then
n = 1). `O(n + B(n))`, where B(n) is the cost of building and printing
the bigint (`O(n²)` in C++/Rust). The results were checked
against trying every run with exact products on small inputs.

Pitfalls:

- the answer can reach 3⁵⁰⁰⁰⁰, almost 24000 digits; C++ and Rust
  multiply by hand in base 10⁹, and Python 3.12 has to lift its limit
  on converting long integers to text;
- multiplying big numbers run after run is too slow; compare exponents
  and build only the answer;
- a single negative mark is its own answer, while −1 0 −1 gives 0.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1587_greedy.cpp](1587_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + B(n)) | AC | 0.046 s | 844 KB |
| [1587_greedy.go](1587_greedy.go) | Go 1.14 x64 | greedy | O(n + B(n)) | AC | 0.031 s | 4040 KB |
| [1587_greedy.java](1587_greedy.java) | Java 1.8 | greedy | O(n + B(n)) | AC | 0.125 s | 4860 KB |
| [1587_greedy.py](1587_greedy.py) | Python 3.12 x64 | greedy | O(n + B(n)) | AC | 0.109 s | 7880 KB |
| [1587_greedy.rs](1587_greedy.rs) | Rust 1.75 x64 | greedy | O(n + B(n)) | AC | 0.031 s | 1336 KB |
