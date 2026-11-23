# 1783. Nuclear Arms Race

[Timus 1783](https://acm.timus.ru/problem.aspx?space=1&num=1783) · difficulty 473 · simulation

Original problem by Pavel Atnashev, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One country plans to hold exactly aᵢ warheads at the end of month i.
Its rival starts with none, and at the start of month i, knowing the
plans aᵢ, …, aᵢ₊ₘ₋₁, picks the smallest whole change xᵢ such that
changing its stock by xᵢ in each of the next m months would keep it at
or above the plan at the end of each of them. Only that month's change
is made; the next month the choice is made again. Print x₁, …, xₙ.

## Input

n and m (1 ≤ n ≤ 10000, 1 ≤ m ≤ 50), then a₁, …, aₙ₊ₘ₋₁
(0 ≤ aᵢ ≤ 10⁵).

## Output

x₁, …, xₙ.

## Examples

### Example 1

Input:

```
4 3
0 0 4 2 1 0
```

Output:

```
2 1 1 -1
```

## Solution

With stock s at the start of month i, after t months of the same change
x the stock is s + t·x, which must be at least aᵢ₊ₜ₋₁. So x is the
largest of ⌈(aᵢ₊ₜ₋₁ − s)/t⌉ over t = 1…m. The stock then grows by x and
the next month repeats. The rounding must be up also for negative
numbers, where plain integer division in many languages rounds towards
zero. `O(n·m)`.

In the example the first order must reach 4 within three months: 2.
With 2 in stock, the next plans 0, 4, 2 need ⌈2/2⌉ = 1; then with 3 the
plans 4, 2, 1 need 1; then with 4 the plans 2, 1, 0 allow −1.

Pitfalls:

- orders may be negative when the plans fall;
- ⌈−3/2⌉ is −1, not −2 and not 0, so the division must round up
  explicitly;
- only the first of the planned months is carried out each time.

The answers agree with an independent accepted implementation on 60
random cases, from a few months to 10000 months of random, wavy and
spiky plans.

## Optimized solutions

Formatting-only accepted revisions: `1783_simulation.java` #11327472, `1783_simulation.cpp` #11327473, `1783_simulation.py` #11327474, `1783_simulation.rs` #11327475. Each table row uses that exact file revision and its own paired time/memory; no performance improvement is attributed to formatting.

`1783_simulation_optimized.cpp`. Keep the exact maximum of signed ceilings over the same ring of at most 50 future plans. For each candidate delta/t, compute the division only if delta>best*t: for integer best this is equivalent to ceil(delta/t)>best, even for negative delta. Nonnegative division uses (delta+t-1)/t; negative division truncates toward zero. With plan and stock in 0..100000 and t<=50, best*t fits signed int. Fixed 16 KiB input/output buffers accompany the same O(nm) algorithm and O(m) plan storage.

Exact-source G++ 13.2 x64 Accepted #11326998: 0.015 s / 104 KB. Saved 2026-11-20 compiler comparison: time 1/43, memory 1/43; top-ten targets pass in both metrics, so no asterisk. Below 1024 KB, strict admission uses time only. Previous optimized run #11315303: 0.031 s / 88 KB. These are independent paired runs; the new recorded memory is higher. The retained teaching C++ source's own current Accepted #11327473 is 0.031 s / 264 KB; its algorithm is unchanged.

C++/Go keep exactly the original maximum of m signed ceilings, but stream future plans through a ring of at most50 integers. Initially read m plans; after each actual order replace the expired slot with the next plan and advance the head. The ring therefore contains precisely the current lookahead window. Walk it with a wrapped index rather than a remainder per item. Nonnegative deltas use (delta+t−1)/t; negative deltas use truncation toward zero, which is their ceiling. Plans and resulting stock stay between0 and100000, so signed32-bit arithmetic suffices. Time remains O(nm); plan storage drops from O(n+m) to O(m), with bounded I/O. All ordinary files remain; Java, Python and Rust reuse their admitted bases.

Retained accepted teaching sources [1783_simulation.java](1783_simulation.java), [1783_simulation.py](1783_simulation.py), [1783_simulation.rs](1783_simulation.rs) also meet the strict top-ten or top-15% criterion on the required metrics in the saved comparison. The current exact paired measurements are in the table, including the formatting-only revisions. Their algorithms are unchanged and no identical optimized copies are added. The asterisk denotes the separate language rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1783_implementation_parsing_optimized.rs`. Keep only the m-value lookahead in a ring. Scan its two contiguous parts in logical month order, then replace the oldest value with the next demand. Preserve exact ceiling division even for negative changes and stream orders directly, using O(m) storage instead of full input and answer vectors. Specialize direct output to the answer types actually used, avoiding generic formatting dispatch and temporary answer strings. Fixed text uses native writes; numeric writers handle the required signed or unsigned magnitudes exactly. Mathematical decisions and archived simple versions are preserved.

Accepted #11329204 (Rust 1.75 x64): **0.015 s / 72 KB**. Archived comparison: `1783_simulation.rs` (Rust 1.75 x64) — 0.031 s / 828 KB (#11327475).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1783_simulation.cpp](1783_simulation.cpp) | G++ 13.2 x64 | simulation | O(n m) | AC | 0.031 s | 264 KB | 11327473 |
| [1783_simulation.go](1783_simulation.go) | Go 1.14 x64 | simulation | O(n m) | AC | 0.031 s | 1384 KB | 11289783 |
| [1783_simulation.java](1783_simulation.java) | Java 1.8 | simulation | O(n m) | AC | 0.14 s | 2388 KB | 11327472 |
| [1783_simulation.py](1783_simulation.py) | Python 3.12 x64 | simulation | O(n m) | AC | 0.187 s | 2584 KB | 11327474 |
| [1783_simulation.rs](1783_simulation.rs) | Rust 1.75 x64 | simulation | O(n m) | AC | 0.031 s | 828 KB | 11327475 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1783_simulation_optimized.cpp](1783_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n·m) | AC | 0.015 s | 104 KB | 11326998 |
| [1783_simulation_optimized.go](1783_simulation_optimized.go) \* | Go 1.14 x64 | simulation | O(n·m) | AC | 0.031 s | 300 KB | 11315305 |
| [1783_implementation_parsing_optimized.rs](1783_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(nm) time; O(m) space + bounded I/O buffers | AC | 0.015 s | 72 KB | 11329204 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
