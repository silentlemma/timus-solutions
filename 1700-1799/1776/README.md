# 1776. Anniversary Firework

[Timus 1776](https://acm.timus.ru/problem.aspx?space=1&num=1776) · difficulty 465 · dp

Original problem by Alex Samsonov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n rockets stand in a row. The first volley launches the two end
rockets. Before each next volley, in every non-empty stretch of
rockets between two launched neighbours one rocket is chosen uniformly
at random, and all chosen rockets fly in that volley. Volleys are ten
seconds apart, and the show ends with the volley that launches the last
rocket. Find the expected length of the show in seconds.

## Input

n (3 ≤ n ≤ 400).

## Output

The expected length with an absolute or relative error of at most
10⁻⁶.

## Examples

### Example 1

Input:

```
5
```

Output:

```
26.66666666666
```

## Solution

After the first volley the m = n − 2 inner rockets form one stretch,
and a stretch of i rockets splits at its random rocket into stretches
of l and i − 1 − l rockets, for each l with chance 1/i, which then go
on independently. Let done(i, j) be the chance that a stretch of i
rockets is gone within j more volleys: done(0, j) = 1, done(i, j) = 1
for i ≤ j, and otherwise

done(i, j) = (1/i) · Σ done(l, j − 1) · done(i − 1 − l, j − 1).

The expected number of further volleys is Σ (1 − done(m, j)) over
j ≥ 0, and the answer is ten times that. The number of volleys behaves
like the height of a random search tree, about 4.3 ln m, and its tail
falls off very fast, so the sum stops once 1 − done(m, j) drops below
10⁻¹⁵: a few dozen rounds of `O(m²)` each instead of `O(m³)`.

With five rockets the three inner ones split at the middle one with
chance 1/3, leaving two more volleys, and otherwise need three: 10 ×
(2/3 · 3 + 1/3 · 2) = 26.67 seconds.

Pitfalls:

- the first volley starts the show and adds no time;
- the stretches split independently, so the chance for a stretch is a
  product of the chances for its two parts;
- summing all m rounds also works but costs `O(m³)`, too slow in some
  languages.

The answers agree with an independent accepted implementation, which
sums all rounds, for many values of n up to 400, to 10⁻⁹.

## Optimized solutions

The Go and Rust alternatives reuse two rows of completion probabilities done(i, j) from the recurrence above. They pair equal convolution terms l and i − 1 − l, adding a middle square for odd i. They sum the entire finite horizon j = 0, …, m − 1 for m = n − 2. Each additional volley launches at least one remaining rocket, so the tail probability is zero from j = m onward. The same split recurrence applies; time is O(m³), with symmetric pairs reducing the constant, and O(m) storage without per-round row allocations. This is a storage/constant-factor alternative and can do more rounds than the early-stop base. Round the computed seconds to nine decimal places; formatting error is at most 0.5·10⁻⁹, below the judge tolerance. Go uses standard handles and Rust uses C standard I/O. C++, Java and Python reuse their admitted bases.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.015 s for the base and uses 52 KB versus 240 KB.

The accepted base implementations [1776_dp.cpp](1776_dp.cpp), [1776_dp.java](1776_dp.java), [1776_dp.py](1776_dp.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1776_dp.cpp](1776_dp.cpp) | G++ 13.2 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.015 s | 192 KB | 11328299 |
| [1776_dp.go](1776_dp.go) | Go 1.14 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.031 s | 1228 KB | 11289721 |
| [1776_dp.java](1776_dp.java) | Java 1.8 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.14 s | 1932 KB | 11328301 |
| [1776_dp.py](1776_dp.py) \* | Python 3.12 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.265 s | 1296 KB | 11328302 |
| [1776_dp.rs](1776_dp.rs) | Rust 1.75 x64 | dp | O(m^2) per volley, a few dozen volleys | AC | 0.015 s | 240 KB | 11289726 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1776_dp_optimized.go](1776_dp_optimized.go) \* | Go 1.14 x64 | dp | O(m³) | AC | 0.015 s | 308 KB | 11315269 |
| [1776_dp_optimized.rs](1776_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(m³) | AC | 0.046 s | 52 KB | 11315900 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
