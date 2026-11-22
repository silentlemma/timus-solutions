# 1998. Completing ordered lifts despite interruptions

[Timus 1998](https://acm.timus.ru/problem.aspx?space=1&num=1998) · difficulty 378 · two_pointers

Original problem by Denis Dublennykh, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Objects have a fixed lifting order. Each ordinary second lifts the first
object not currently held. At a listed interruption second no object is
lifted; instead, release held objects in reverse lifting order until
their total released weight is strictly greater than `k`, or until none
remain. Find the first second when all `n` objects are held
simultaneously. Interruptions after completion have no effect.

Bounds: `1≤n,m≤100000`, `1≤k≤10^9`, weights `1≤w[i]≤10000`, and strictly
increasing interruption times between 1 and `10^9`. Time limit 0.5
seconds; memory 64 MB.

## Input

First `n m k`, then `n` weights in lifting order, then `m` interruption
times. Each weight and time is on its own line.

## Output

One integer: the completion time in seconds.

## Checking

Outputs are compared token by token.

## Examples

```
5 1 4
1
2
3
4
5
4
```

```
8
```

After seconds 1–3 the held weights are 1, 2, 3. At second 4 no lift
occurs. Releasing 3 alone does not exceed 4, so weight 2 must also be
released; the released total is 5. Weight 1 stays held, and seconds 5–8
restore the remaining four objects. Completion is at 8.

## Solution

The held objects always form a prefix of the fixed order: a lift extends
it by one and an interruption removes a suffix. Thus its length `h`
completely describes the physical state.

### Precompute every interruption

Let `P[h]` be the weight of the first `h` objects, with `P[0]=0`. Define
`retreat[h]` as the prefix length remaining after an interruption from
height `h`.

If `P[h]≤k`, all held objects fall, so `retreat[h]=0`. Otherwise the
stopping position is the largest `q<h` with `P[h]−P[q]>k`. It leaves the
fewest objects released while already exceeding the threshold. For
`q>0`, the next larger prefix would have released weight at most `k`.
Equivalently, the answer is the predecessor of the first prefix sum at
least `P[h]−k`, clipped to zero.

Because all weights are positive, `P` strictly increases, and this
predecessor never moves left as `h` increases. Maintain one pointer `q`,
initially zero. For each `h=1..n`, advance it while `q+1<h` and
`P[h]−P[q+1]>k`, then set `retreat[h]=q`. The current pointer remains
admissible when the threshold increases; the stopping test proves no
larger pointer is admissible. Before the total exceeds `k`, it stays
zero. Set `retreat[0]=0`.

The pointer advances at most `n` times across all heights, so all
interruption transitions take linear time to build. Testing `>k` is
essential: a total equal to `k` requires one more release if any held
object remains.

### Jump between events

Maintain the last processed interruption time `time` and the current
height `h`, initially both zero. Before the next interruption at `t`,
exactly `t−time−1` ordinary seconds are available. If they suffice to
lift the remaining `n−h` objects, return `time+n−h`; completion is
strictly before `t`.

Otherwise increase `h` by that number of ordinary seconds, replace it by
`retreat[h]`, and set `time=t`. No lift occurs at `t`. After the final
interruption return `time+n−h`.

Inductively each jump performs exactly the lifts of the literal process,
and the precomputed transition performs exactly its releases. A
completion check returns the first possible finishing second. If the
predicted completion would equal an interruption time, it is blocked and
must be processed as an interruption, not returned. Empty prefixes and
consecutive interruptions need no special simulation loop.

### Complexity and bounds

Time `O(n+m)` and memory `O(n+m)` including stored input, on all five
languages. Auxiliary tables use `O(n)`. Prefix sums are at most `10^9`;
completion is at most `max(t)+n≤1000100000`. Native ports use 64-bit
sums and times. A time gap is converted to an index only after checking
that it is smaller than the number of missing objects.

Release until the weight is strictly greater, not merely equal. The
interrupted second contributes no lift. Stop immediately once the whole
prefix is held and ignore later events. Do not simulate every second or
every fallen object: sparse times and repeated deep resets can represent
nearly a billion elementary actions. The release transition depends on
height, not on the number of interruptions already processed.

## Optimized solutions

`1998_two_pointers_optimized.java`. Keep the monotone two-pointer retreat table and the strict comparison with limit. Build prefix weights as the input arrives and consume interruption times one at a time; an early completion still ignores subsequent events. With at most 100000 weights of at most 10000, every prefix and prefix difference is at most 10^9, so int arrays suffice for prefixes and retreat indices. Times and limit remain long, and ordinary=event-time-1 is unchanged. A 4 KB byte parser replaces the generic reader; time O(N+M), storage O(N). The simple versions remain.

Compared with `1998_two_pointers.java`: time 0.125 s → 0.093 s; memory 3104 KB → 1152 KB.

The optimized C++ version keeps the two-pointer algorithm. While reading the weights, it maintains the weight of the current suffix and discards its first item whenever the remaining suffix still exceeds the threshold. The weights fit in 16 bits. Interruption times are processed as they arrive, and reading stops once the final lift is possible. The running time is O(n+m) and extra space is O(n). The Accepted run used 672 KB instead of 2740 KB, with the same 0.015 s runtime.

The retained accepted base implementations [1998_two_pointers.go](1998_two_pointers.go), [1998_two_pointers.py](1998_two_pointers.py), [1998_two_pointers.rs](1998_two_pointers.rs) also meet strict fast-set admission in the saved comparison: top ten or top 15% for the required metrics. They are reused without identical copies. Java uses the separate optimized source above; its teaching source remains. A star marks the separate language rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

Exact-source Accepted #11326586: 0.093 s / 1152 KB. In the saved Java 1.8 sample of 2026-11-20: time rank 1/40, memory rank 2/40. The asterisk still denotes the separate language rating target.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1998_two_pointers.cpp](1998_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n+m) | AC | 0.015 s | 2740 KB | 11292423 |
| [1998_two_pointers.go](1998_two_pointers.go) \* | Go 1.14 x64 | two_pointers | O(n+m) | AC | 0.125 s | 6872 KB | 11292424 |
| [1998_two_pointers.java](1998_two_pointers.java) \* | Java 1.8 | two_pointers | O(n+m) | AC | 0.125 s | 3104 KB | 11325563 |
| [1998_two_pointers.py](1998_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(n+m) | AC | 0.156 s | 27000 KB | 11292425 |
| [1998_two_pointers.rs](1998_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(n+m) | AC | 0.031 s | 6272 KB | 11292427 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1998_two_pointers_optimized.cpp](1998_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(n+m) | AC | 0.015 s | 672 KB | 11310347 |
| [1998_two_pointers_optimized.java](1998_two_pointers_optimized.java) \* | Java 1.8 | two_pointers | O(N+M) | AC | 0.093 s | 1152 KB | 11326586 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
