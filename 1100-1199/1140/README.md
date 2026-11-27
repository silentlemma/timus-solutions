# 1140. The shortest way back to the centre of a hexagonal grid after a walk

[Timus 1140](https://acm.timus.ru/problem.aspx?space=1&num=1140) · difficulty 383 · geometry

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bog is split into hexagonal cells, and three of the six directions
between neighbouring cells are named `X`, `Y` and `Z`, with `Y` lying
between `X` and `Z`. A student starts in the central cell and walks along
up to 32000 straight segments, each given as a direction and a nonzero
signed length; a negative length goes the opposite way. The student never
gets more than 100 cells away from the centre. Describe a route back to
the centre through the fewest cells, in the same format.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` (`1 ≤ n ≤ 32000`), then `n` lines with a direction letter and a signed length.

## Output

The number of segments `m ≥ 0` of the way back, then the segments.

## Checking

Any shortest route is accepted. The checker verifies the format, that the
route ends at the centre, and that its total length equals the hexagonal
distance from the last cell.

## Examples

### Example 1

Input:

```
4
Z -2
Y 3
Z 3
X -1
```

Output:

```
2
Y -2
Z -2
```

## Solution

On a hexagonal grid the middle direction is the sum of the other two: one
step along `Y` lands on the same cell as one step along `X` followed by
one along `Z`. So add up the lengths per direction and write the end of
the walk as `a·X + b·Z` with `a = X + Y` and `b = Z + Y`. A way back that
uses `m` steps along `Y` needs `a − m` along `X` and `b − m` along `Z`,
backwards, and has `|a − m| + |m| + |b − m|` steps. A sum of distances
from `m` to the points `a`, `0` and `b` is smallest at their median, so
take `m` as the median of `a`, `0` and `b` and print the nonzero parts of
`X −(a − m)`, `Y −m`, `Z −(b − m)`. `O(n)`.

The geometric state is three totals and at most three candidate return
segments: O(1) bounded numeric words in every version, with no recursion.
Simple C++/Go/Java read incrementally and retain only bounded buffers
and this state. Simple Python keeps the full input and split tokens,
Rust the full input String: O(I) additional bytes. Optimized Go/Rust
remove such full-input retention where present. Optimized Python
uses a 4096-byte chunk plus split pieces and the unfinished token,
O(4096+T) bytes for maximum token length T, rather than O(I). Reading
I bytes adds O(I) time to the O(n) geometric updates.

Pitfalls:

- when `a` and `b` have the same sign, part of the way goes along `Y`;
  when their signs differ, `m = 0` and `Y` is not used;
- segments of length zero are not allowed, so they are dropped, and the
  answer can be `0` segments;
- the input must contain at least one segment even when it ends at the
  centre (test 03); mode 1 of the generator uses a cancelling pair when
  a small requested size would otherwise produce an empty input route;
- several shortest routes may exist, any one is accepted.

The answers were checked by the checker on every test and on 1200 random
walks; the distance formula in the checker was compared with a
breadth-first search over all cells within 100 of the centre.

## Optimized solutions

Both native optimized versions keep the same median formula. Go
replaces map[string]int with a three-element integer array, sort.Ints
on three values with an explicit clamp, fmt.Fscan with Scanner/ScanWords
and strconv.Atoi, and fmt-formatted lines with a small byte output
buffer. Its base already accumulated only three totals. Rust replaces
read_to_string and generic token parsing with stdin.lock().bytes()
and a direct signed-number reader, plus a three-element array of i32
totals. Its base already computed the median by min/max; clamp is the
same constant-size operation, not a new geometric algorithm. Outputs
still omit zero lengths and both readable bases remain.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 188 KB versus 344 KB.

The exact-source cache confirms reused C++/Java by time only below
1 MiB. Simple Python at 0.125 s/776 KB fails its small-cohort time
reference; the separate 0.062 s/828 KB revision covers Python. Simple
Go passes both small-cohort metrics, optimized Go only time; both Rust
sources pass ordinary time ranks below 1 MiB. Shared
[rating criteria](../../RATING_CRITERIA.md) apply. Retain all teaching
files unstarred, without duplicate optimized copies.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1140_geometry_implementation_optimized.py`. Replace full text read/
split with os.read chunks, carrying only an unfinished token between
chunks. It still accumulates three direction totals in a dictionary,
then derives the two axes and sorts (a,0,b) for the median, as the
base does. It does not accumulate the two axes directly. Byte keys
and flushed os._exit after the complete output are implementation
changes; the geometry and simple file remain.

Accepted #11329035 (Python 3.12 x64): **0.062 s / 828 KB**. Archived comparison: `1140_geometry.py` (Python 3.12 x64) — 0.125 s / 776 KB (#11279441).

The current optimized Python revision only names the unchanged ASCII
space-byte threshold 32 used by chunk tokenization. The median
formula, numeric values, simple source and substantive comments remain.

## Language notes

These notes describe the simple implementations.

- All languages add up the lengths and take the same median.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1140_geometry.cpp](1140_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 188 KB | 11279439 |
| [1140_geometry.go](1140_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1348 KB | 11279440 |
| [1140_geometry.java](1140_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 828 KB | 11279442 |
| [1140_geometry.py](1140_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.125 s | 776 KB | 11279441 |
| [1140_geometry.rs](1140_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 344 KB | 11279443 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1140_geometry_optimized.go](1140_geometry_optimized.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 908 KB | 11311067 |
| [1140_geometry_optimized.rs](1140_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 188 KB | 11311072 |
| [1140_geometry_implementation_optimized.py](1140_geometry_implementation_optimized.py) | Python 3.12 x64 | geometry, implementation | O(n) | AC | 0.078 s | 796 KB | 11331074 |
