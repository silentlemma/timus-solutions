# 1800. Murphy's Law

[Timus 1800](https://acm.timus.ru/problem.aspx?space=1&num=1800) · difficulty 169 · math

Original problem by Alex Samsonov, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A toast, a thin segment of length l, is dropped butter side down from
height h, held level. It falls freely (g = 9.81 m/s²) and spins about
its centre at ω revolutions per minute in a vertical plane. Which side
touches the floor first? It is guaranteed not to touch while standing
upright.

## Input

l and h in centimetres and ω in revolutions per minute, whole numbers
from 1 to 1000.

## Output

"butter" or "bread".

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
10 400 15
```

Output:

```
butter
```

### Example 2

Input:

```
10 500 15
```

Output:

```
bread
```

## Solution

Convert lengths to metres and ω to radians per second. After t seconds
the centre is at h − g·t²/2 and the toast has turned by
ω·t, so its lower end is at gap(t) = h − g·t²/2 − (l/2)·|sin ωt|. The
answer depends only on the quarter turn in which gap first reaches
zero: in quarters 0 and 3 of a turn the butter faces down, in 1 and 2
the bread. So go through the quarters in order.

In an even quarter |sin ωt| grows, the lower end sinks faster than the
centre, and gap only decreases: the toast touches in it exactly when
gap ≤ 0 at its end. In an odd quarter the end rises back relative to
the centre, and gap may first fall, then rise, then fall again. Its
slope there is concave, since the third derivative is
(l/2)·ω³·cos ≤ 0. Find the peak of the slope by bisection on the
second derivative. If the slope at the peak is positive, a second
bisection finds where it turns positive, the local minimum of gap. The
quarter holds the first touch if that minimum or the value at its end
is at most zero. The centre reaches the floor within about 1.5
seconds, so there are at most about a hundred quarters. `O(ω)`.

In the first example the toast turns a quarter per second and lands
after about 0.9 s, at about 81°: butter. From 5 m it lands just past
90°: bread.

Pitfalls:

- the end of the toast may touch before the centre has fallen far: a
  long toast held low touches in the very first quarter (tests 05 and
  06, both butter);
- in an odd quarter gap is not monotone, so its value at the end of
  the quarter alone can miss a touch;
- the units: centimetres to metres, revolutions per minute to radians
  per second;
- the generators used by gen1, gen3 and gen4 must also enforce the
  no-upright-contact guarantee. With integer centimetres and speed r in
  rpm, upright first contact occurs exactly when
  (2h − l)·r² = 981·15²·n² for a positive odd integer n. Reject such
  draws using integer arithmetic; no side is specified for them.

The answers agree with an independent interval-subdivision oracle on
3000 random inputs (1500 small ones), 64 boundary inputs, all nine
stored tests and all five configured generator cases.

## Optimized solutions

`1800_math_optimized.java`. Keep the quarter-turn contact search and add an exact fast path when halfLength·omega²≤g. The lowest endpoint then descends monotonically: on odd quarters its derivative is at most (−g·pi/2+halfLength·omega²)/omega<0; on even quarters it is negative directly. Find the first nonpositive vertical and horizontal endpoints with square roots, correct the candidate indices by evaluating their heights, and choose the earlier quarter. The accepted contact/slope search with 60-step bisections remains the fallback; no output or floating-point precision is relaxed. Fast-path work is constant apart from boundary-index corrections; the fallback costs O(Q·60), with O(1) state. Read three values through 64 bytes, write and flush the complete answer, then call Runtime.getRuntime().halt(0). All 200000 comparisons with the previous accepted kernel matched, including 70212 fast-path cases. The current 0.093 s/512 KB pair is faster but uses more memory than the historical 0.125 s/376 KB pair; do not combine their metrics. Preserve the full-scan teaching implementation.

Exact-source Java 1.8 Accepted #11327885: 0.093 s / 512 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/32, memory 6/32. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11307242 was 0.125 s / 376 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1800_math_optimized.java`: 0.093 s / 512 KB; retained teaching base `1800_math.java`: 0.109 s / 1576 KB.

`1800_math_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327037 measures 0.078 s / 1008 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 2/255, memory rank 252/255. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11325886, 0.125 s / 412 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1800_math_optimized.py`. Keep the same gap/slope/curvature contact search and 60-step bisections. No endpoint can touch before t₀=sqrt(2·max(0,h−l/2)/g), because its vertical distance from the centre is at most l/2. Start one quarter before floor(t₀/quarter), retaining a safety interval for floating-point rounding, instead of searching every earlier quarter. Contact must occur by the next vertical maximum, so only nearby quarters remain; preserve interior-minimum tests and absolute-quarter butter/bread parity. No PyPy JIT-control import is needed. O(Q·60) work for the remaining Q quarters and constant state; keep the simple full scan.

Compared with `1800_math.py`: time 0.093 s → 0.125 s; memory 592 KB → 412 KB.

`1800_math_optimized.rs`. Keep the same quarter-turn contact search with gap, slope and curvature, including possible interior minima on odd quarters. Reduce the two bisections from 100 to 60 iterations: those searched positive intervals have endpoints within a factor of two, so 60 steps already reach f64 resolution. Read three bounded integer inputs without an input vector and write the unchanged butter/bread result directly. For Q quarters examined, O(Q·60) time and O(1) space; retain the original 100-step teaching version.

Compared with `1800_math.rs`: time 0.046 s → 0.031 s; memory 236 KB → 60 KB.

The optimized C++ solution reads the three numbers with `scanf` and
prints the side with `puts` instead of using `iostream`, whose runtime
is not needed here; the floating-point computation is exactly the same:
{1800_math_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1800_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +73.12%; base: `1800_math.cpp`.


`1800_math_parsing_optimized.go`. Locate the maximum gap slope analytically from its derivative in each odd quarter. Compute the inverse-sine offset once, eliminating the first100-step bisection per odd quarter. Keep the original contact-minimum bisection, quarter boundaries and side rule; complete integer inputs were checked against the archived algorithm. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

This exact source has its own Accepted and meets the shared [rating criteria](../../RATING_CRITERIA.md). Time and memory below come from the same run; repeated runs can differ because of judge timing. Existing simple and distinct optimized implementations are preserved.

Accepted #11329344 (Go 1.14 x64): **0.015 s / 836 KB**.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1800_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1800_math.cpp](1800_math.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 372 KB | 11304236 |
| [1800_math.go](1800_math.go) | Go 1.14 x64 | math | O(omega) | AC | 0.031 s | 1084 KB | 11289935 |
| [1800_math.java](1800_math.java) | Java 1.8 | math | O(omega) | AC | 0.109 s | 1576 KB | 11304238 |
| [1800_math.py](1800_math.py) | Python 3.12 x64 | math | O(omega) | AC | 0.093 s | 592 KB | 11289938 |
| [1800_math.rs](1800_math.rs) | Rust 1.75 x64 | math | O(omega) | AC | 0.046 s | 236 KB | 11304241 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1800_math_optimized.cpp](1800_math_optimized.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 100 KB | 11307243 |
| [1800_math_optimized.java](1800_math_optimized.java) | Java 1.8 | math | O(Q·60) fallback; O(1) state | AC | 0.093 s | 512 KB | 11327885 |
| [1800_math_optimized.rs](1800_math_optimized.rs) | Rust 1.75 x64 | math | O(Q·60) time; O(1) space | AC | 0.031 s | 60 KB | 11325533 |
| [1800_math_optimized.py](1800_math_optimized.py) | Python 3.12 x64 | math | O(Q·60) time; O(1) auxiliary state | AC | 0.078 s | 1008 KB | 11327037 |
| [1800_math_parsing_optimized.go](1800_math_parsing_optimized.go) | Go 1.14 x64 | math, parsing | O(omega) | AC | 0.015 s | 836 KB | 11329344 |
