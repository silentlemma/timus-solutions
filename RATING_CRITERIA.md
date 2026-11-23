# Rating criteria

This file defines the rating policy for C++, Go, Java, Python/PyPy and Rust.
The same policy determines whether a language position meets its performance
goal and whether an optimized solution needs an asterisk in its README row.
There is no separate first-place requirement for any language.

## Evidence and retained versions

Performance measurements must come from one Accepted submission of the exact
source stored in the repository. Do not combine the fastest time of one run
with the lowest memory of another. A changed source needs its own Accepted
evidence, even if the change only affects formatting or comments.

Keep meaningful simple versions alongside distinct optimized versions.
A simple version that already meets the goal can close the language position;
there is no need to duplicate it under an `_optimized` filename. A problem is
fully verified only when every language offered by the judge has a qualifying
version with confirmed source evidence. Languages unavailable for that problem
are excluded.

## Metrics

- If **our submission uses less than 1024 KB**, compare **time only**.
- At **1024 KB or more**, compare both time and memory.
- Missing memory is unknown, never zero, and cannot activate the exception.
- Exclude rival submissions faster than **0.015 s (15 ms)** before counting
  rivals, selecting compiler cohorts or comparing either metric. Keep results
  exactly equal to 0.015 s. Excluded rows do not contribute memory measurements.
- Our time is still floored at 0.015 s for comparison. The older rival rows are
  excluded rather than raised to that floor.

The memory exception applies to both the usual ranking rules and the small
cohort comparison below. It depends on our submission's memory, not the
reference submission's memory.

## Usual ranking rules

A version qualifies when **either** condition holds for all required metrics:

1. Its shared rank is **at most 10**.
2. Its shared rank is within the **top 15%**.

For example, when both metrics are required, both must meet the top-ten rule,
or both must meet the top-15-percent rule. Passing a different rule for each
metric is insufficient.

Exclude all submissions by the archive's author before selecting rivals.
A shared rank is `1 + the number of strictly better rival results`. For a
cohort of `N` rival submissions, use `N + 1` as the denominator and
`ceil(0.15 * (N + 1))` as the top-15-percent rank limit. Equal results share a
rank; repeated runs by the archive's author cannot improve the comparison.

The ordinary cohort contains rival submissions on compiler versions currently
offered by the judge for the same language family. If there are no such rivals,
use all compiler versions of that language family and record the fallback for
review. Never silently mix another language into the comparison.

## Override for 1-10 rivals on the same compiler

If there are **1 through 10 rival submissions on the exact same compiler or
interpreter version as our submission**, replace the ranking rules above with
this comparison. A top-ten rank does not provide an alternative way to pass.

Sort eligible rival submissions by execution time, breaking equal-time ties
by smaller memory. Select one reference by its position in this ordered list:

| Eligible rivals on the exact version | Reference position |
| --- | --- |
| 1 | First |
| 2 | Second |
| 3-10 | Third |

The position is `min(3, rival_count)`, counting submissions even when their
times are tied. Take both reference measurements from that one submission.
This reduces dependence on one exceptional record. It does not guarantee a
literal top-three rank: many results may fit within the allowed 15% margin.

Our version qualifies only if:

```text
our_time <= reference_time * 1.15
and, when our_memory >= 1024 KB:
our_memory <= reference_memory * 1.15
```

The 15% boundary is inclusive and calculated without binary floating-point
rounding. There is no additional fixed-tick allowance. The selected reference
already has an eligible time of at least 0.015 s.

| Reference time / memory | Our time / memory | Result |
| --- | --- | --- |
| 0.100 s / 800 KB | 0.115 s / 1023 KB | Pass: only time is required |
| 0.100 s / 800 KB | 0.115 s / 1024 KB | Fail: memory exceeds 920 KB |
| 0.100 s / 2000 KB | 0.115 s / 2300 KB | Pass: both limits are met exactly |
| 0.100 s / 2000 KB | 0.115 s / 2301 KB | Fail: memory exceeds the limit |

With 11 or more exact-version rivals, use the ordinary ranking rules. With
zero exact-version rivals, this override cannot establish a reference; the
ordinary cohort and its documented fallback still apply. In particular,
CPython and PyPy are separate compiler/interpreter versions for the override.

## Unknown results and README asterisks

An incomplete leaderboard or a complete snapshot with no rivals cannot prove
that a version meets the goal. Missing reference measurements also leave the
small-cohort comparison unknown. Report these cases separately from a measured
failure. A missing source-to-Accepted binding is another independent evidence
gap; an existing Accepted verdict alone does not resolve it.

Mark an optimized solution that is known to miss the goal with an escaped
asterisk immediately after its link:

```markdown
| [1000_math_optimized.cpp](1000_math_optimized.cpp) \* | ... |

\* Accepted; the rating target is not yet met. This version may be optimized further.
```

Keep the marker and translated explanation consistent across all four README
languages. Remove the marker when the version meets the goal. An unknown
rating does not justify automatically adding or removing a marker. Asterisks
describe performance goals, not correctness or the availability of source
evidence. Retained simple versions are not marked as optimization targets.

## Policy maintenance

The private audit configuration implements this policy and uses saved rating
snapshots and Accepted receipts. Credentials, caches and reports stay outside
this public repository. Update this document, the executable configuration and
their boundary tests together when the policy changes.

The previous top-30-percent and 30-percent base-improvement admission rules,
and the separate first-place targets for some languages, are not part of this
profile. A trial comparison against the fastest rival for every cohort size
does not replace this policy unless explicitly adopted.
