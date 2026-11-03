# 1795. Husband in a Shop

[Timus 1795](https://acm.timus.ru/problem.aspx?space=1&num=1795) · difficulty 253 · simulation

Original problem by Andrew Gein, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shop has m products in given amounts, and n husbands stand in line
before Mark, each wanting some amount of one product. At the counter,
which takes a minute, a husband buys his amount if there is enough, or
leaves if the product is absent or gone. If there is some but not
enough, he lets the next person ahead and calls home, standing second;
told to take the rest, he comes back and buys it all if the amount is
unchanged, leaves if nothing is left, and otherwise lets one more
person ahead and calls again. How many minutes pass before Mark reaches
the counter?

## Input

m (1 ≤ m ≤ 1000) lines "amount of name", then n (1 ≤ n ≤ 1000) lines in
the same form for the husbands, front of the line first. Amounts are
from 1 to 1000, names are up to 20 lowercase letters, and a husband may
want a product the shop does not sell.

## Output

The number of minutes.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
2 of sweets
4 of milk
1 of sausage
4
2 of milk
3 of sweets
3 of milk
1 of cheese
```

Output:

```
6
```

## Solution

Simulate the line. Each visit to the counter is a minute. Keep, for
every husband, the amount he was told at his last visit. A husband who
must call is put back into the line behind the next person; if there
is nobody left before Mark, Mark is next and the count stops there.
When he returns, the amount is compared with the one he was told: the
same means he takes it all, zero means he leaves, anything else means
another call. The line holds at most 1000 husbands and each call moves
the caller back by one place, so the simulation is quick. `O(n²)`.

In the example the first husband buys 2 of the 4 milk. The second
finds only 2 sweets and steps back behind the third, who finds only 2
milk and steps back too. Then both return to unchanged amounts and buy
them, and the last husband finds no cheese: 6 visits before Mark.

Pitfalls:

- a husband who returns to an unchanged amount buys all of it, even
  though it is less than he wanted;
- a husband who must call while last in line lets Mark ahead, so Mark
  is at the counter right after that minute;
- every visit counts as a minute, including the one that ends in a
  call.

The answers agree with an independent accepted implementation on 300
random cases, among them a single stock with rare buyers of everything
who call again after every small purchase.

## Optimized solutions

Keep the counter-visit simulation but resolve product names to integer IDs only while reading. Represent the waiting customers by arrays and a front index. A customer swapping with the next one is an in-place swap, not an insertion or removal that shifts the remaining queue. Missing products use a zero-stock entry. This preserves every visit and stock update while removing repeated string lookup, queue copying and full-input retention.

- `1795_simulation_optimized.cpp`: 0.031 s / 272 KB; base `1795_simulation.cpp`: 0.031 s / 552 KB; relative change: time -0.0%, memory -50.7%.
- `1795_simulation_optimized.go`: 0.031 s / 1132 KB; base `1795_simulation.go`: 0.046 s / 6376 KB; relative change: time -32.6%, memory -82.2%.
- `1795_simulation_optimized.java`: 0.093 s / 1076 KB; base `1795_simulation.java`: 0.125 s / 4688 KB; relative change: time -25.6%, memory -77.0%.
- `1795_simulation_optimized.py`: 0.078 s / 612 KB; base `1795_simulation.py`: 0.078 s / 1100 KB; relative change: time -0.0%, memory -44.4%.
- `1795_simulation_optimized.rs`: 0.031 s / 508 KB; base `1795_simulation.rs`: 0.062 s / 632 KB; relative change: time -50.0%, memory -19.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1795_simulation.cpp`; covering source `1795_simulation_optimized.cpp`; time/memory places 47/1, other-author entries 53/53.

- Go: preferred teaching base `1795_simulation.go`; covering source `1795_simulation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1795_simulation.java`; covering source `1795_simulation.java`; time/memory places 1/1, other-author entries 1/1.

- Python/PyPy: preferred teaching base `1795_simulation.py`; covering source `1795_simulation.py`; time/memory places 1/1, other-author entries 6/6.

- Rust: preferred teaching base `1795_simulation.rs`; covering source `1795_simulation.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1795_simulation.cpp](1795_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2) | AC | 0.031 s | 552 KB | 11308937 |
| [1795_simulation.go](1795_simulation.go) | Go 1.14 x64 | simulation | O(n^2) | AC | 0.046 s | 6376 KB | 11289883 |
| [1795_simulation.java](1795_simulation.java) | Java 1.8 | simulation | O(n^2) | AC | 0.125 s | 4688 KB | 11308939 |
| [1795_simulation.py](1795_simulation.py) | Python 3.12 x64 | simulation | O(n^2) | AC | 0.078 s | 1100 KB | 11308940 |
| [1795_simulation.rs](1795_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2) | AC | 0.062 s | 632 KB | 11308942 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1795_simulation_optimized.cpp](1795_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 272 KB | 11308816 |
| [1795_simulation_optimized.go](1795_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 1132 KB | 11308817 |
| [1795_simulation_optimized.java](1795_simulation_optimized.java) | Java 1.8 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.093 s | 1076 KB | 11308818 |
| [1795_simulation_optimized.py](1795_simulation_optimized.py) | Python 3.12 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.078 s | 612 KB | 11308814 |
| [1795_simulation_optimized.rs](1795_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 508 KB | 11308820 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
