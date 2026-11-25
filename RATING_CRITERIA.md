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
our_time <= max(reference_time * 1.15, displayed_tick_limit)
and, when our_memory >= 1024 KB:
our_memory <= reference_memory * 1.15
```

The allowed time regression is **15%, with a minimum allowance of one timer
tick**. Take the larger time limit; do not add a tick on top of the 15% limit.
The memory limit remains exactly 15%, with no tick allowance. All boundaries
are inclusive and calculated with decimal arithmetic.

For this policy, a timer tick is **1/64 s = 0.015625 s**. Reconstruct the
reference's integer tick count by rounding `reference_time / 0.015625` to the
nearest integer, with half values rounded up. Add one tick, then truncate
the resulting seconds to three decimal places to obtain `displayed_tick_limit`.
This accounts for displayed values such as 0.015, 0.031, 0.046 and 0.062 s;
simply adding 0.015 s would reject a legitimate neighboring displayed tick.
Times that do not align with this grid still retain the exact 15% alternative.
The configuration records the tick size, minimum allowance and display precision;
the audit records both candidate limits and the effective limit. This is a
comparison tolerance, not evidence that repeated runs execute equally fast.
The selected reference still needs an eligible time of at least 0.015 s.

| Reference time / memory | Our time / memory | Result |
| --- | --- | --- |
| 0.015 s / 252 KB | 0.031 s / 840 KB | Pass: one displayed tick; memory is excluded |
| 0.015 s / 252 KB | 0.046 s / 104 KB | Fail: two displayed ticks slower |
| 0.031 s / 500 KB | 0.046 s / 500 KB | Pass: one displayed tick |
| 0.125 s / 800 KB | 0.140 s / 1023 KB | Pass: within 15% |
| 0.125 s / 800 KB | 0.156 s / 1023 KB | Fail: exceeds both time limits |
| 0.100 s / 800 KB | 0.115 s / 1023 KB | Pass: only time is required |
| 0.100 s / 800 KB | 0.115 s / 1024 KB | Fail: memory exceeds 920 KB |
| 0.100 s / 2000 KB | 0.115 s / 2300 KB | Pass: both limits are met exactly |
| 0.100 s / 2000 KB | 0.115 s / 2301 KB | Fail: memory exceeds the limit |

With 11 or more exact-version rivals, use the ordinary ranking rules. With
zero exact-version rivals, this override cannot establish a reference; the
ordinary cohort and its documented fallback still apply. In particular,
CPython and PyPy are separate compiler/interpreter versions for the override.

## Explicit algorithm review when there are no rivals

A complete leaderboard with no eligible rivals in the language family, even
after the compiler fallback, cannot establish a numerical rank. An explicit
qualitative approval can nevertheless close that language position when:

- The exact candidate and its C++ reference both have verified Accepted source
  evidence and paired README measurements.
- The review assesses the algorithm, worst-case bounds and implementation
  against the problem constraints and the reference, and records its rationale.
- A durable decision ledger records the problem, language, filenames, compiler
  versions, Accepted IDs, SHA256 of both sources and the English Task/Input/Output
  and Checking sections, reviewer, date, review method and evidence provenance.

The reviewer must explicitly approve the decision. Model output alone cannot
create an approval. Model-assisted reviews must be identified as such and
include manual adjudication of flagged or invalid answers; they must not be
described as independent manual proofs of every source.

The private audit reports `pass_manual_review` separately from a numerical pass.
It retains `unknown_ranking_reference` as the numerical status and does not
invent a first place. Changed candidate/reference bytes, changed constraints,
different compiler or Accepted IDs, revoked approval, missing source evidence,
structural errors, incomplete tables or newly available eligible rivals prevent
this exception from applying. A known numerical failure cannot be overridden.

The ledger is durable audit input, not a disposable cache or model response.
Its contents and SHA256 are included in audit evidence. Ordinary offline audits
reuse it without contacting a model or the judge. This approval assesses the
algorithm; it is not a measured ranking claim or a reason to change README
asterisks automatically.

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
