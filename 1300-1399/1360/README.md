# 1360. Philosophical Dispute

[Timus 1360](https://acm.timus.ru/problem.aspx?space=1&num=1360) · difficulty 1284 · math

Original problem: idea by Den Raskovalov, prepared by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

As t grows, the point x = sin(√t), y = cos(t) runs around the square
[−1, 1]². Given a dot of radius ε ≥ 10⁻⁴ centred at (x₀, y₀) inside the
square, print any t in [0, 10¹²] at which the curve is inside the dot,
or `FAIL` if there is none.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

x₀ and y₀ on the first line, ε on the second.

## Output

A moment t, or `FAIL`.

## Examples

### Example 1

Input:

```
0.744 0.554
0.01
```

Output:

```
5.3
```

## Solution

The two coordinates move at very different speeds. Write s = √t, so
x = sin(s) and y = cos(s²). Near a large s, a change of s by δ moves x
by at most δ, but moves t = s² by about 2sδ, which is more than a whole
period of cos once s is large enough.

So pick s₀ = asin(x₀) + 2πk with k = ⌈1/ε⌉ + 1, which makes
sin(s₀) = x₀ and s₀ > 2π/ε. Within π of t₀ = s₀² there is a t with
cos(t) = y₀ exactly: t = acos(y₀) + 2πj for the nearest whole j. Its
root differs from s₀ by about |t − t₀| / (2s₀) ≤ π / (2s₀) < ε/4, so
x is off by less than ε/4 and y not at all. The answer never is `FAIL`.
`O(1)`.

Pitfalls:

- for ε = 10⁻⁴ the answer is about 4·10⁹, well inside [0, 10¹²], so t
  must be printed with enough digits: six decimals move cos(t) by at
  most 10⁻⁶;
- a dot can be larger than the square (test 05);
- clamp x₀ and y₀ to [−1, 1] before asin and acos.

The distance from the curve to the dot was checked on 307 dots,
including all four corners and the centre with ε = 10⁻⁴; it never
exceeded 0.25·ε. The tests are judged by a checker that recomputes the
point of the curve at the printed t.

## Language notes

- All five solutions use the same formula; Java prints with
  `Locale.US` so the decimal point is a dot.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1360_math.cpp](1360_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 164 KB |
| [1360_math.go](1360_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1088 KB |
| [1360_math.java](1360_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1920 KB |
| [1360_math.py](1360_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 368 KB |
| [1360_math.rs](1360_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 264 KB |
