# 1869. New Year Cruise

[Timus 1869](https://acm.timus.ru/problem.aspx?space=1&num=1869) · difficulty 239 · prefix_sums, simulation

Original problem by Denis Dublennykh, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A train goes from Vladivostok (station 1) to Moscow (station n),
stopping at stations 1, …, n, and then back the same way. aᵢⱼ people
bought tickets from station i to station j: they ride the outbound
train when i < j and the return train when i > j. Every car has 36
seats. How many cars does the train need so that everybody gets a
seat?

## Input

n (2 ≤ n ≤ 100), then the n × n matrix aᵢⱼ (0 ≤ aᵢⱼ ≤ 1000, aᵢᵢ = 0).

## Output

The least number of cars.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
3
0 180 180
0 0 180
360 0 0
```

Output:

```
10
```

## Solution

The train must hold the largest number of people on board at once, on
any leg in either direction. For each direction, add aᵢⱼ at the lower-numbered
station and subtract it at the higher-numbered one. The running sum
of these changes in station order is the load on each leg. The answer
is the largest load divided by 36 and rounded up. `O(n²)`.

In the example 360 people ride the outbound train on both legs (the
180 from station 1 to 3 together with the 180 from 1 to 2 or from 2 to
3), and 360 ride back all the way: 10 cars.

Pitfalls:

- the two directions are separate trips, so their loads must not be
  added;
- the division rounds up: 37 people need two cars;
- with no tickets at all the answer is 0.

The answers agree with an independent accepted implementation on 150
random matrices.

## Optimized solutions

`1869_prefix_sums_optimized.go`. Accumulate boarding and leaving differences separately for each direction while reading the matrix, prefix-sum both arrays, and round the larger peak up by 36. The Go variant keeps the original O(n²) difference algorithm and replaces formatted scanning with fixed-buffer integer I/O; it also drops the unused sentinel cells. For Rust this has O(n²) time rather than the O(n³) retained direct simulation; a separate original prefix-sum source also remains, so the new implementation has the prefix_sums_optimized name. Both stream matrix entries without retaining the matrix or input text and use O(n) signed 64-bit load storage. With n<=100 and entries<=1000 all totals fit safely; zero demand yields zero cars.

Compared with `1869_prefix_sums.go`: time 0.031 s → 0.015 s; memory 1244 KB → 816 KB.

`1869_prefix_sums_optimized.rs`. Accumulate boarding and leaving differences separately for each direction while reading the matrix, prefix-sum both arrays, and round the larger peak up by 36. The Go variant keeps the original O(n²) difference algorithm and replaces formatted scanning with fixed-buffer integer I/O; it also drops the unused sentinel cells. For Rust this has O(n²) time rather than the O(n³) retained direct simulation; a separate original prefix-sum source also remains, so the new implementation has the prefix_sums_optimized name. Both stream matrix entries without retaining the matrix or input text and use O(n) signed 64-bit load storage. With n<=100 and entries<=1000 all totals fit safely; zero demand yields zero cars.

Compared with `1869_simulation.rs`: time 0.046 s → 0.015 s; memory 320 KB → 64 KB.

The five direct simulations add each ticket to every segment it crosses in O(N³) time and O(N) space. They serve as teaching bases alongside the original matrix-prefix solutions. The optimized Python reads one row per station. Its right suffix sums give the contributions to forward segments, and its left prefix sums give those to backward segments. Each vector is packed into an integer with 32-bit fields. Shifting by one field and dividing by 2^32−1 forms the suffix sums. Multiplication by a radix repunit followed by truncation forms the prefix sums. Each field is at most 1000N², so the integer operations do not carry between fields. The largest load in either direction divided by 36 and rounded up gives the answer. The algorithm takes O(N²) time and O(N) working space. The recorded gain is in time, with higher memory use than the direct simulation.

- `1869_prefix_sums_optimized.py`: 0.062 s / 468 KB; base `1869_simulation.py`: 0.093 s / 396 KB; relative change: time -33.3%, memory +18.2%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1869_prefix_sums_optimized.go`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

`1869_prefix_sums_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1869_simulation.cpp](1869_simulation.cpp) | G++ 13.2 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 108 KB | 11308691 |
| [1869_simulation.go](1869_simulation.go) | Go 1.14 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 1228 KB | 11308696 |
| [1869_simulation.java](1869_simulation.java) | Java 1.8 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 388 KB | 11308693 |
| [1869_simulation.py](1869_simulation.py) | Python 3.12 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 396 KB | 11308701 |
| [1869_simulation.rs](1869_simulation.rs) | Rust 1.75 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.046 s | 320 KB | 11308699 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums.cpp](1869_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 180 KB | 11309204 |
| [1869_prefix_sums.go](1869_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.031 s | 1244 KB | 11290934 |
| [1869_prefix_sums.java](1869_prefix_sums.java) | Java 1.8 | prefix_sums | O(n^2) | AC | 0.093 s | 444 KB | 11309206 |
| [1869_prefix_sums.py](1869_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n^2) | AC | 0.078 s | 1324 KB | 11309207 |
| [1869_prefix_sums.rs](1869_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 336 KB | 11309208 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums_optimized.py](1869_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N^2) time, O(N) working space | AC | 0.062 s | 468 KB | 11310099 |
| [1869_prefix_sums_optimized.go](1869_prefix_sums_optimized.go) \* | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 816 KB | 11328315 |
| [1869_prefix_sums_optimized.rs](1869_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 64 KB | 11325130 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
