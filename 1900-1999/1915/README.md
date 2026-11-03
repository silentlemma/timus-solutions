# 1915. Titan Ruins: Reconstruction of Bygones

[Timus 1915](https://acm.timus.ru/problem.aspx?space=1&num=1915) · difficulty 228 · simulation

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Start with an empty stack. A positive operation pushes a value; −1 removes
and reports the top value; 0 puts a complete copy of the current stack
above it, preserving bottom-to-top order. Report all removed values.
Every removal is guaranteed to find a nonempty stack. The physical stack
may become exponentially larger than the operation count.
Limits: 2 seconds, 128 MB.

## Input

n, 1≤n≤1 000 000, followed by n lines, each containing one integer x.
It is either −1, 0, or a coin value in [1,1 000 000 000].

## Output

One removed value per line, in chronological order. If there are no
removals, the output is empty.

## Checking

Compare the integer output tokens exactly, including their order.

## Examples

```
8
3
4
0
-1
-1
-1
-1
1
```

```
4
3
4
3
```

## Solution

Read the operation list and count its P removals. At each step let r be
the number of removals still to come. Retain only the top min(h,r) values,
where h is the true, possibly enormous stack height. No later operation
can expose a deeper value without spending more than r removals.
If P=0 there is nothing to output. Once r reaches zero, later operations
are irrelevant.

Store the retained stack in a circular array of fixed capacity P, with
logical bottom b and stored size s. Positions wrap modulo P. Its logical
capacity is the shrinking r, which can be smaller than the physical P.

A push appends its value. If s=r, discard the stored bottom first, then
append at the new logical end. A removal reports the last stored element
and decrements both s and r.

For duplication, keep the existing top untouched. If s=r, it already
contains every future-observable value, so do nothing. Otherwise the
whole true stack is currently known and has size s. The copy adds below
the retained top at most q=min(s,r−s) values: exactly the last q values
of the old stack. Prepend that suffix in the circular array. The new
bottom is (b−q) mod P; the copied suffix begins at (b+s−q) mod P.
The destination occupies unused array positions and cannot overwrite
the source. A zero-size stack or a full logical capacity gives q=0.

### Correctness

Maintain that the stored sequence is precisely the last min(h,r) values
of the true stack. A push needs only the old top r−1 values and the new
value, so dropping the old bottom when full is valid. A removal changes
the desired depth to min(h−1,r−1), exactly the previous stored depth
minus one, and therefore reports the true top. During duplication, if
h≥r the desired top r values do not change. If h<r, the true stack is
fully stored; its doubled sequence ends with the old stack, preceded
by exactly the suffix described above. Thus every operation preserves
the invariant and every printed value is correct.

### Amortized bound

Each removal decreases s by one. An ordinary push increases it by one;
a full push has net zero effect. A duplication increases it by its copied
suffix length q. Initially s=0, and after the last removal r=s=0.
Consequently the total number of copied values equals P minus the number
of size-increasing pushes, and is at most P. Copy storms therefore do
not cause repeated large work. Time is `O(n)` and memory is `O(n)`:
the operation list and fixed ring each use at most n entries.

In the example [3,4] becomes [3,4,3,4]. Four removals give 4,3,4,3;
the last push has no effect on the output.

Duplication preserves order: it does not reverse the stack. Prepend a
suffix below the retained top, never append a prefix above it. The logical
capacity shrinks only on removal. When r<P, a full push must drop the
bottom and append at the logical end, rather than simply overwrite the
old bottom slot. Handle copying an empty stack and an experiment without
output. Do not materialize exponential copies or shift a full array.

## Optimized solutions

Retain only the top part of the coin stack that can affect the remaining removals, using the proven shrinking-ring invariant. Popped coins are emitted in bounded blocks instead of being copied into a complete answer array. Conditional wrap replaces hot remainder operations. The bound counts all copied elements over the entire execution, not separately for each command. The chosen Python version uses the interpreter recorded in its Accepted row.

- `1915_simulation_optimized.cpp`: 0.062 s / 7492 KB; base `1915_simulation.cpp`: 0.187 s / 11640 KB; relative change: time -66.8%, memory -35.6%.
- `1915_simulation_optimized.go`: 0.078 s / 9548 KB; base `1915_simulation.go`: 0.093 s / 21804 KB; relative change: time -16.1%, memory -56.2%.
- `1915_simulation_optimized.java`: 0.250 s / 8448 KB; base `1915_simulation.java`: 0.390 s / 12292 KB; relative change: time -35.9%, memory -31.3%.
- `1915_simulation_optimized.py`: 0.359 s / 37668 KB; base `1915_simulation.py`: 0.515 s / 16716 KB; relative change: time -30.3%, memory +125.3%.
- `1915_simulation_optimized.rs`: 0.062 s / 7856 KB; base `1915_simulation.rs`: 0.046 s / 16904 KB; relative change: time +34.8%, memory -53.5%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1915_simulation.cpp`; covering source `1915_simulation_optimized.cpp`; time/memory places 4/9, other-author entries 45/45.

- Go: preferred teaching base `1915_simulation.go`; covering source `1915_simulation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1915_simulation.java`; covering source `1915_simulation_optimized.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1915_simulation.py`; covering source `1915_simulation_optimized.py`; time/memory places 1/1, other-author entries 2/2.

- Rust: preferred teaching base `1915_simulation.rs`; covering source `1915_simulation.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1915_simulation.cpp](1915_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.187 s | 11640 KB | 11291421 |
| [1915_simulation.go](1915_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.093 s | 21804 KB | 11291424 |
| [1915_simulation.java](1915_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.390 s | 12292 KB | 11309214 |
| [1915_simulation.py](1915_simulation.py) | PyPy 3.10 x64 | simulation | O(n) | AC | 0.515 s | 16716 KB | 11291425 |
| [1915_simulation.rs](1915_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 16904 KB | 11291432 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1915_simulation_optimized.cpp](1915_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N+P) | AC | 0.062 s | 7492 KB | 11308596 |
| [1915_simulation_optimized.go](1915_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N+P) | AC | 0.078 s | 9548 KB | 11308605 |
| [1915_simulation_optimized.java](1915_simulation_optimized.java) | Java 1.8 | simulation | O(N+P) | AC | 0.250 s | 8448 KB | 11308601 |
| [1915_simulation_optimized.py](1915_simulation_optimized.py) | PyPy 3.10 x64 | simulation | O(N+P) | AC | 0.359 s | 37668 KB | 11309401 |
| [1915_simulation_optimized.rs](1915_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N+P) | AC | 0.062 s | 7856 KB | 11308602 |
