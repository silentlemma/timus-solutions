# 1129. Painting doors green on one side and orange on the other so that every room is balanced

[Timus 1129](https://acm.timus.ru/problem.aspx?space=1&num=1129) · difficulty 378 · graphs

Original problem by Magaz Asanov, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A building has `N ≤ 100` rooms joined by doors; two rooms may share
several doors. Every door is painted green on one side and orange on the
other. Paint the doors so that in every room the numbers of green and
orange door sides differ by at most one. Print `Impossible` if this
cannot be done.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines: the number of doors of a room, then the numbers of
the rooms they lead to, in increasing order.

## Output

`N` lines: the colours of the doors of each room in the input order, `G`
for green and `Y` for orange, or the word `Impossible`.

## Checking

Any valid colouring is accepted. The checker verifies that every room gets
one colour per listed door, that each room is balanced within one, and
that for every pair of rooms the doors between them are green on exactly
one side. The doors between the same two rooms look alike, so it counts
green marks per pair instead of matching single doors.

## Examples

### Example 1

Input:

```
5
3 2 3 4
3 1 3 5
4 1 2 4 5
3 1 3 5
3 2 3 4
```

Output:

```
G Y G
Y G Y
G Y Y G
Y G G
G Y Y
```

## Solution

Think of the rooms as vertices and the doors as edges. The code replaces
each pair of parallel doors by a loop in each room. Painting a door
green in room `u` and orange in room `v` is the same as directing the edge
from `u` to `v`, so the task asks for an orientation where every vertex has
out-degree and in-degree differing by at most one. Such an orientation
always exists. Add a dummy vertex joined by one extra edge to each vertex
of odd degree; there is an even number of those, so now every degree is
even. Each connected part then has an Euler circuit, and walking it
leaves every vertex exactly as often as it enters. Direct each edge the
way the walk goes and drop the extra edges: a vertex loses at most one
edge, so its two counts differ by at most one. For `D` doors, expected
`O(N + D)` with hash maps, `O(N + D log D)` with the C++ ordered map.

The five simple sources and optimized Rust pair consecutive mentions
for each unordered room pair in row-scan order, not the k-th mentions
from opposite rooms. For multiplicity m between distinct rooms, this
creates floor(m/2) loops in each room and, if m is odd, one connecting
edge. Every loop paints two slots G/Y and is locally balanced. The
remaining connecting edge balances the odd remainder. Each room keeps
its original number of slots; between two rooms exactly m of the 2m
slots are green, which is the checker condition. Parallel doors have
no individual identity, so this artificial pairing is sufficient.
Self-door mentions pair within the same row. Optimized Java instead
pairs the opposite endpoint halves explicitly; optimized C++/Python
cancel even multiplicities and orient only the residual graph.

Pitfalls:

- `Impossible` is never the answer;
- a door appears in the rows of both its rooms; mentions for each room
  pair are paired consecutively in scan order. Doors between the same
  rooms are interchangeable;
- the circuit is walked with an explicit stack and a pointer to the next
  unused edge of each vertex, so every edge is looked at a constant number
  of times;
- rooms without doors print an empty line.

The answers were checked by the checker on every test and on random
buildings with many doors repeated between the same rooms.

## Optimized solutions

`1129_graphs_optimized.py`. Keep exact cancellation of opposite parallel-door pairs and Euler orientation of the residual graph after joining odd rooms to a dummy room. Since each room’s neighbours are sorted, itertools.groupby counts equal runs in native code. Python now keeps residual neighbours as integer bitsets, removes the lowest available edge by XOR and expands colors from original multiplicities; self-door pairs remain balanced. The output is not fingerprinted. With N rooms, D door mentions and B=ceil(N/w) integer limbs: O(D+N²B) work and O(N²+max row degree) storage, including per-row input/output. At the stated N<=100 bitsets have only a few limbs. Teaching graph implementations remain. Here w is the number of bits in a Python big-integer limb.

Exact-source CPython 3.12 Accepted #11327005: 0.078 s / 752 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 1/83, memory rank 1/83. Below 1024 KB, strict admission uses time only.

- `1129_graphs_optimized.py`: 0.078 s / 752 KB; retained teaching base `1129_graphs.py` (Python 3.12 x64): 0.078 s / 2560 KB; time change +0.0%; memory change -70.6%.

`1129_graphs_optimized.java`. Keep Euler-walk orientation after virtually connecting odd-degree rooms to a dummy room. Flatten all D door-side mentions with room offsets, original positions and mate indices. Sort packed (unordered-room-pair,original-slot) long keys: parallel doors pair the two endpoint halves in slot order, and self-door mentions pair consecutively. N<=100 keeps the room-pair key below 10000, separate from the low 32-bit slot. Real edges set opposite G/Y colors; virtual edges only balance parity and are not printed. A primitive stack and byte colors replace boxed adjacency, hash queues and the full output builder. Storage O(N+D). Let S(D) be the primitive sort cost: the remaining pairing/walk/output work is O(N+D); Java 8 sorting is typically O(D log D), with a conservative O(D²) worst-case allowance rather than a claimed strict logarithmic guarantee.

Compared with `1129_graphs.java`: time 0.156 s → 0.109 s; memory 3876 KB → 832 KB.

C++ and Python count the doors for each pair of rooms. Opposite orientations for each pair of parallel doors cancel in both rooms, so the residual graph has at most one real edge per room pair. After adding dummy edges it has even degrees. Follow unused edges until each walk closes and orient them as visited. C++ scans its adjacency matrix with monotone cursors; Python traverses residual integer bitsets as described above. Both expand original multiplicities in input order.

The preceding exact-source cache confirms simple Go by both applicable
small-cohort metrics. It does not admit simple Rust: 1172 KB requires
a memory comparison, which fails; the 884 KB optimized Rust receipt
qualifies by time only. Simple C++/Java/Python also fail their required
metrics; their optimized variants qualify by time only below 1 MiB.
Keep all teaching versions without target stars; current admission
uses the shared criteria rather than a separate language target.

The current five simple sources and optimized Rust have corrected
explanatory pairing comments; optimized Rust also names its unchanged
32-byte inline-token capacity. Table submission IDs and measurements
belong to the preceding source bytes.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1129_graphs_parsing_optimized.rs`. Preserve the scan-order pairing,
dummy-room parity correction and Euler orientation above, not a greedy
partition. Release waiting queues before graph traversal and store
colours as bytes. A 4096-byte native input buffer, inline short tokens
and direct integer conversion replace the full input String; parsed
rows, edge endpoints, adjacency, Euler state, colours and complete
output still use O(N+D) storage. This is bounded raw input, not a
streaming graph algorithm; time remains expected O(N+D).

Accepted #11329034 (Rust 1.75 x64): **0.015 s / 884 KB**. Archived comparison: `1129_graphs.rs` (Rust 1.75 x64) — 0.015 s / 1172 KB (#11279366).

## Language notes

The 18 November 2026 notes describe a historical snapshot. Current
comparisons discard rival times below 0.015 s before cohort selection,
while our own smaller times are floored only for comparison. Paired
Accepted measurements remain raw. Use the shared current policy.

`1129_graphs_optimized.java`: time place 1/23, memory place 1/23 in this comparable sample. Historical snapshot of 18 November 2026.

Current admission uses the shared [rating criteria](../../RATING_CRITERIA.md):
ordinary top-ten/top-15% comparisons or the exact-compiler small-cohort
reference when applicable, with time only below 1 MiB. A 30% gain and a
separate first-place language target are not admission criteria. Keep
meaningful teaching versions without optimization-target stars.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1129_graphs.cpp](1129_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2080 KB | 11331143 |
| [1129_graphs.go](1129_graphs.go) | Go 1.14 x64 | graphs | O(N + D) expected | AC | 0.031 s | 2416 KB | 11331023 |
| [1129_graphs.java](1129_graphs.java) | Java 1.8 | graphs | O(N + D) expected | AC | 0.171 s | 3884 KB | 11331050 |
| [1129_graphs.py](1129_graphs.py) | Python 3.12 x64 | graphs | O(N + D) expected | AC | 0.078 s | 2596 KB | 11331073 |
| [1129_graphs.rs](1129_graphs.rs) | Rust 1.75 x64 | graphs | O(N + D) expected | AC | 0.015 s | 1148 KB | 11331116 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1129_graphs_optimized.cpp](1129_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N² + D) | AC | 0.015 s | 160 KB | 11310449 |
| [1129_graphs_optimized.py](1129_graphs_optimized.py) | Python 3.12 x64 | graphs | O(D+N² ceil(N/w)) time; O(N²+max row degree) space | AC | 0.078 s | 752 KB | 11327005 |
| [1129_graphs_optimized.java](1129_graphs_optimized.java) | Java 1.8 | graphs | O(N+D+S(D)) | AC | 0.109 s | 832 KB | 11325013 |
| [1129_graphs_parsing_optimized.rs](1129_graphs_parsing_optimized.rs) | Rust 1.75 x64 | graphs, parsing | O(N + D) expected | AC | 0.046 s | 892 KB | 11331117 |
