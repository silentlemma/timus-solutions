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

The five direct simulations add each ticket to every segment it crosses in O(N³) time and O(N) space. They serve as teaching bases alongside the original matrix-prefix solutions. The optimized Python reads one row per station. Its right suffix sums give the contributions to forward segments, and its left prefix sums give those to backward segments. Each vector is packed into an integer with 32-bit fields. Shifting by one field and dividing by 2^32−1 forms the suffix sums. Multiplication by a radix repunit followed by truncation forms the prefix sums. Each field is at most 1000N², so the integer operations do not carry between fields. The largest load in either direction divided by 36 and rounded up gives the answer. The algorithm takes O(N²) time and O(N) working space. The recorded gain is in time, with higher memory use than the direct simulation.

- `1869_prefix_sums_optimized.py`: 0.062 s / 468 KB; base `1869_simulation.py`: 0.093 s / 396 KB; relative change: time -33.3%, memory +18.2%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1869_simulation.cpp`; covering source `1869_simulation.cpp`; time/memory places 1/1, other-author entries 45/45.

- Go: preferred teaching base `1869_simulation.go`; covering source `1869_simulation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1869_simulation.java`; covering source `1869_simulation.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1869_simulation.py`; covering source `1869_prefix_sums_optimized.py`; time/memory places 1/1, other-author entries 9/9.

- Rust: preferred teaching base `1869_simulation.rs`; covering source `1869_simulation.rs`; time/memory places 1/1, other-author entries 0/0.

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
