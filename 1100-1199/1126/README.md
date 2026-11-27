# 1126. The maximum of every window of M consecutive readings

[Timus 1126](https://acm.timus.ru/problem.aspx?space=1&num=1126) · difficulty 92 · two_pointers

Original problem by Alexander Mironenko, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a window width `M` (`2 ≤ M ≤ 14000`) and `N` readings
(`M ≤ N ≤ 25000`, each from 0 to 100000) ending with `-1`, print the
maximum of readings `1..M`, then of `2..M+1`, and so on up to the last
full window.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`M`, then the readings one per line, then `-1`.

## Output

The `N − M + 1` window maxima, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
10
11
10
0
0
0
1
2
3
2
-1
```

Output:

```
11
11
10
0
1
2
3
3
```

## Solution

Keep a double-ended queue of indices whose values decrease from front to
back. A new reading first removes from the back every index whose value
is not larger than its own, since those can never increase the maximum
while the new one is in the window; then it joins the back. The front
leaves when it falls out of the window. The front of the queue is always
the maximum of the current window. Each index enters and leaves at most once, so
the whole pass is `O(N)`; recomputing every window would cost `O(N·M)`,
up to about 156 million steps.

All simple versions retain N readings. Their live deque needs O(M)
entries, but Go/Java allocate O(N) queue backing arrays with a moving
head; expired prefixes do not become O(M) storage. C++/Java/Python/Rust
retain P output bytes or answer values plus formatted output; Go
streams through a fixed writer. Python input parsing peaks with I
bytes/tokens plus its integer list and values slice; Rust retains its
I-byte input String. Total simple storage is O(N+I+P) where applicable.
Streaming optimized C++/Java/Rust and packed Python use O(M) queue
storage plus bounded input/output buffers. The optimized Go remains
O(N): it still stores all readings and an N-capacity index queue.

Pitfalls:

- the readings end with `-1`, not with a count;
- equal readings may all be dropped from the back except the newest one,
  which leaves the window last;
- with `M = N` there is a single window.

The answers were checked against the maximum of every window slice
computed directly, on every test.

## Optimized solutions

`1126_two_pointers_optimized.py`. Keep the monotone deque, but encode each entry as (value<<15)|index in one integer: N<=25000 makes 15 index bits sufficient. Integer ordering compares value first and then age, so an equal newer reading replaces the older one. Expire the head, remove dominated tails, and decode the maximum with >>15. Every reading enters and leaves at most once: O(N) amortized deque work, O(M) entries. A 4096-byte reader preserves partial tokens; output batches of 512 answers bound temporary storage. Raw writes and os._exit(0) inside main avoid normal teardown. The readable pair-based teaching source remains.

Current exact-source Python 3.12 Accepted #11327503: 0.093 s / 1452 KB.
Saved 2026-11-20 ranks 2/54 in both metrics are historical evidence;
the cached current-policy audit confirms both applicable metrics.
There is no separate first-place requirement, and the table row has
no asterisk. The source uses the shared [rating criteria](../../RATING_CRITERIA.md).

- `1126_two_pointers_optimized.py`: 0.093 s / 1452 KB; retained teaching base `1126_two_pointers.py`: 0.14 s / 3448 KB.

Historical earlier CPython revision #11326680 recorded 0.109 s /
2152 KB with saved time/memory ranks 6/54 and 4/54. Those measurements
and ranks belong to that revision, not current #11327503; no separate
Python first-place target applies.

Earlier Python revision #11303710 recorded 0.125 s / 668 KB. The
intermediate #11326680 pair (0.109 s / 2152 KB) differs by one displayed
timer tick; current #11327503 is 0.093 s / 1452 KB. These are three
separate runs/revisions. Keep each pair together and use current
source-bound admission, rather than describing all comparisons as one tick.

The optimized solutions (C++, Java) do not store the readings: each one
joins the deque together with its index as soon as it is read, and the
maximum of a full window is printed at once. C++ reads with `getchar`;
Java parses a byte buffer by hand, keeps the deque in a ring buffer of
`M` cells, since the window never holds more, and writes the numbers
through a byte buffer. C++: 224 KB instead of 776 KB, with the same
time; Java: 0.109 s instead of 0.156 s and 624 KB instead of 2332 KB.

Rust uses a 4-KB parser and emits answers through a bounded writer
instead of retaining input/output text. Its pair is 0.031 s / 332 KB
versus 0.046 s / 1192 KB for the base; the times are not equal.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1126_two_pointers_parsing_implementation_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Use an 8192-byte refillable input buffer instead of retaining the entire input. Tokens and partial/EOF reads retain their original meaning.

Optimized Go refills an 8192-byte raw-input buffer, but still collects
every reading in values and reserves an N-element queue. It improves
byte parsing and output conversion without streaming the window
algorithm itself; O(N) reading/queue storage remains.

Accepted #11328910 (Go 1.14 x64): **0.031 s / 2344 KB**. Archived comparison: `1126_two_pointers.go` (Go 1.14 x64) — 0.062 s / 2896 KB (#11279328).

The current optimized Go revision only names the unchanged 128-byte
inline token capacity. Window storage, parser values, simple source
and substantive comments remain unchanged.

## Language notes

- In the simple solutions, Go and Java keep the queue in an array with a
  moving head; C++, Rust and Python use their library deques.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB | 11279323 |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB | 11279328 |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB | 11279331 |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.14 s | 3448 KB | 11279329 |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB | 11279332 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1126_two_pointers_optimized.cpp](1126_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 224 KB | 11303561 |
| [1126_two_pointers_optimized.java](1126_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N) | AC | 0.109 s | 624 KB | 11303563 |
| [1126_two_pointers_optimized.py](1126_two_pointers_optimized.py) | Python 3.12 x64 | two_pointers | O(N) amortized; O(M) deque + bounded buffers | AC | 0.093 s | 1452 KB | 11327503 |
| [1126_two_pointers_optimized.rs](1126_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.031 s | 332 KB | 11303711 |
| [1126_two_pointers_parsing_implementation_optimized.go](1126_two_pointers_parsing_implementation_optimized.go) | Go 1.14 x64 | two_pointers, parsing, implementation | O(N) | AC | 0.031 s | 2356 KB | 11330993 |
