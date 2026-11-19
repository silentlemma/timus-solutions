# 1223. The fewest egg drops that find the critical floor

[Timus 1223](https://acm.timus.ru/problem.aspx?space=1&num=1223) · difficulty 292 · dp

Original problem: folklore, proposed by Alexander Klepinin, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `f` floors numbered from 1 to `f` and `e` identical eggs,
with `1 ≤ e, f ≤ 1000`. An unknown `E` lies in `0..f`: an egg survives
at every floor at most `E` and breaks above it. If it breaks at floor 1,
then `E = 0`; if it survives at floor `f`, then `E = f`.

Find the fewest drops needed to determine `E` in the worst case.
Surviving eggs can be reused. There are at most 1000 queries;
the pair `0 0` terminates the input and is not a query.

Time limit: 1 second. Memory limit: 64 MB.

## Input

One query per line: the number of eggs and the number of floors.

## Output

For each query, the fewest drops in the worst case.

## Checking

Compare integer tokens in query order and do not answer the `0 0`
sentinel. Each of the five new teaching sources passed 13 repository
inputs in Docker and obtained its own exact-SHA Accepted. The actual
teaching Python was checked on 21000 queries, in batches of at most
1000: every floor1..1000 for eggs1..20 plus 1000 random queries with up
to1000 eggs. Its independent oracle uses the closed capacity sum
`Σ C(d,i)` and binary search, rather than the minimax or inverse DP.
These are Python executions, not 21000 runs of each native source.
Include one egg, one floor, ten and1000 eggs, exact capacity boundaries,
1000 queries and the terminating sentinel.

## Examples

### Example 1

Input:

```
1 10
2 5
0 0
```

Output:

```
10
3
```

## Solution

The new teaching sources use the literal minimax recurrence. Let
`D(e,f)` be the minimum worst-case drops with `e` eggs and `f` floors.
There are no drops for zero floors, and `D(1,f)=f`. If the first drop is
from floor `x`, breaking leaves `x−1` floors and one fewer egg; surviving
leaves `f−x` floors with the same eggs. Therefore
`D(e,f)=1+min₁≤ₓ≤f max(D(e−1,x−1),D(e,f−x))`. Every strategy has a first
floor and must handle both outcomes, giving the lower bound; choosing
the best floor and recursively using optimal strategies attains it.

Compute increasing eggs and floors. Both terms are already available:
one uses the preceding egg row and the other a smaller floor count.
There are `F+1` possible critical floors and binary outcomes, requiring
at least `ceil(log₂(F+1))` drops. With ten eggs, ordinary binary search
attains that bound for every `F≤1000`, using at most ten drops and losing
at most one egg each time. More than ten eggs cannot help. Thus keeping
ten rows is proved, not an arbitrary cutoff.

With `E=10`, `F=1000`, preprocessing costs `O(EF²)` time and `O(EF)`
integer cells; each query is `O(1)`. All five new files have their own
Accepted and are preferred for learning. The Python teaching source
uses PyPy 3.10. All five former sources are retained byte for byte;
there are no duplicate optimized copies.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1223_dp_optimized.go`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Optimized solutions

`1223_dp_optimized.go`. Keep the inverse egg-drop DP, but solve each query directly instead of retaining best[11][1001] for every floor count. reach[k] is the number of floors distinguishable after the current drop count; update k downwards with reach[k]+=reach[k-1]+1 to use the previous row in place. Stop when reach[min(e,10)]>=f. Ten eggs suffice for f<=1000 because ten binary decisions distinguish 1024 outcomes. For query i with Kᵢ=min(eᵢ,10) and answer Dᵢ, total work is O(Σ Kᵢ·Dᵢ), not O(1) per query. DP storage is eleven int64 values, plus fixed I/O buffers. EOF or 0 0 ends processing without an extra answer. Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `1223_dp.go`: time 0.031 s → 0.015 s; memory 1216 KB → 828 KB.

The retained `dp` algorithm asks the inverse question. With `d`
drops and `e` eggs, let `R(d,e)` be the number of floors resolvable.
The first drop splits into the broken branch, its own floor and the
surviving branch: `R(d,e)=R(d−1,e−1)+1+R(d−1,e)`, with zero boundaries.
The split is both necessary and achievable by the same decision-tree
argument. The first `d` with `R(d,e)≥f` is exactly `D(e,f)`.

Build capacities for increasing `d` and fill each answer cell only as
its capacity is first reached. Capacities can safely saturate at F:
larger values are indistinguishable to every legal query, and the update
is monotone. There are at most F passes because one egg covers d floors,
and every table cell is written once. This gives `O(EF)` preprocessing,
`O(EF)` storage and `O(1)` per query. Capped summands are at most F,
so each addition is at most `2F+1=2001`, safe in the native integer types.

Only the old Python source is currently called optimized under the 30%
rule: CPython 0.078 s / 812 KB versus the simpler PyPy source's
0.265 s / 2916 KB, saving 70.6% time and 72.2% memory. This is a different
algorithm, kept under its existing `dp` name. The old Java is only 28.4%
faster and uses more memory, so it remains an algorithmic alternative;
C++/Go/Rust also fail the 30% admission comparison against their new
bases. They stay available without an optimized label. The new simple
Java already meets the rating goal.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1223_bruteforce_dp.cpp](1223_bruteforce_dp.cpp) | G++ 13.2 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.015 s | 152 KB | 11308226 |
| [1223_bruteforce_dp.go](1223_bruteforce_dp.go) | Go 1.14 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.031 s | 1208 KB | 11308230 |
| [1223_bruteforce_dp.java](1223_bruteforce_dp.java) | Java 1.8 | bruteforce, dp | O(EF^2 + Q) | AC | 0.109 s | 584 KB | 11308235 |
| [1223_bruteforce_dp.py](1223_bruteforce_dp.py) | PyPy 3.10 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.265 s | 2916 KB | 11308219 |
| [1223_bruteforce_dp.rs](1223_bruteforce_dp.rs) | Rust 1.75 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.015 s | 344 KB | 11308239 |

### Other algorithms (30% rule not met)

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1223_dp.cpp](1223_dp.cpp) | G++ 13.2 x64 | dp | O(EF + Q) | AC | 0.015 s | 172 KB | 11283700 |
| [1223_dp.go](1223_dp.go) | Go 1.14 x64 | dp | O(EF + Q) | AC | 0.031 s | 1216 KB | 11283701 |
| [1223_dp.java](1223_dp.java) | Java 1.8 | dp | O(EF + Q) | AC | 0.078 s | 668 KB | 11283703 |
| [1223_dp.rs](1223_dp.rs) | Rust 1.75 x64 | dp | O(EF + Q) | AC | 0.015 s | 376 KB | 11283704 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1223_dp.py](1223_dp.py) | Python 3.12 x64 | dp | O(EF + Q) | AC | 0.078 s | 812 KB | 11283702 |
| [1223_dp_optimized.go](1223_dp_optimized.go) \* | Go 1.14 x64 | dp | O(Σ Kᵢ·Dᵢ) | AC | 0.015 s | 828 KB | 11325045 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
