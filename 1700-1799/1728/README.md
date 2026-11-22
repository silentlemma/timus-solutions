# 1728. Curse on Team.GOV

[Timus 1728](https://acm.timus.ru/problem.aspx?space=1&num=1728) · difficulty 524 · implementation

Original problem by Eugene Kurpilyansky (idea by Mikhail Rubinchik), from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Efremov and Kantorov pick a third member from a list of candidates. A
team's strength is the sum of its members' ratings. If the chosen team
has already played in some earlier tournament, Efremov stays away; if
the team without him has played too, it is disqualified. Choose the
candidate that gives the strongest team that plays, or report that
every choice is disqualified.

## Input

n (1 ≤ n ≤ 100) earlier teams, each as a size from 1 to 3 and the
surnames in alphabetical order; every team has Kantorov, and every team
of three has Efremov. Then the ratings of Efremov and Kantorov, m
(1 ≤ m ≤ 100) and m candidates with their ratings. Ratings are from 1
to 666.

## Output

`Win` and a candidate giving the strongest team, or `Fail`. Any best
candidate is accepted.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The checker applies the withdrawal and disqualification rules to every candidate. Accept Fail exactly when no candidate remains; otherwise require Win and a candidate attaining the maximum remaining team strength. Any optimal tie is valid.

## Examples

### Example 1

Input:

```
6
3 Efremov Kantorov Rubinchik
2 Efremov Kantorov
3 Efremov Kantorov Kokovin
3 Burmistrov Efremov Kantorov
3 Efremov Kantorov Pervukhin
2 Kantorov Pervukhin
100 10
6
Fominykh 200
Komarov 34
Pervukhin 250
Golubev 23
Soboleva 50
Gein 50
```

Output:

```
Win
Fominykh
```

### Example 2

Input:

```
2
3 Efremov Fominykh Kantorov
2 Fominykh Kantorov
99 666
1
Fominykh 100
```

Output:

```
Fail
```

## Solution

The preferred simpler C++, Go and Rust variants use two sets of third surnames. Every historical team contains Kantorov and every triple also contains Efremov, so a third surname uniquely identifies the only relevant pair or triple. Insert it into the full-team set for a triple or the pair set for a two-person team; singleton Kantorov and the Efremov/Kantorov pair are irrelevant to any candidate. For a candidate absent from the full set, Efremov joins and the strength is re+rk+r. If the full set contains it but the pair set does not, strength is rk+r; if both contain it, disqualify. Choose any candidate of maximum strength. Case-sensitive names and equality of the whole surname matter. Expected time O((n+m)L) for surname length L≤50; set storage O(nL). The original general approach sorts up to three surnames to make a canonical complete-lineup key, queries the triple, removes Efremov if repeated and then queries the pair. All five such original Accepted programs remain; Java/Python retain that approach as bases.

## Optimized solutions

`1728_implementation_optimized.java`. Keep the map of previous pair/triple participation and the maximum eligible team-strength scan. Reuse byte and character token scratch arrays for ASCII names, copying each into an immutable String; non-ASCII names retain UTF-8 decoding. Emit Win/Fail and the selected name as bytes. With I input bytes, U distinct retained names of T total characters and token scratch capacity L, expected time is O(I+N+M) and stored text/state is O(T+U+L). HashMap bounds are expected, not worst-case guarantees.

Exact-source Java 1.8 Accepted #11327746: 0.093 s / 508 KB. Saved 2026-11-20 compiler-cohort comparison: time 2/19, memory 3/19. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324823 was 0.125 s / 928 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1728_implementation_optimized.java`: 0.093 s / 508 KB; retained teaching base `1728_implementation.java`: 0.14 s / 2172 KB.

The fast Go version keeps the two surname sets and uses direct standard handles, fixed input and output buffers, and a 50-byte token buffer. Fast Rust reads names through standard C input and stores both team-size flags in one fixed open-addressed table. It compares the full names on collisions. The C++ surname sets also provide fast coverage. Java and Python reuse their admitted original programs. The older C++, Go and Rust programs that store canonical lineups are listed under Other Accepted approaches. A star marks a fast source below its language-specific rating target.

The accepted base implementations [1728_implementation.java](1728_implementation.java), [1728_implementation.py](1728_implementation.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1728_hashing.cpp](1728_hashing.cpp) | G++ 13.2 x64 | hashing | O((n + m)L) | AC | 0.015 s | 204 KB | 11315520 |
| [1728_hashing.go](1728_hashing.go) | Go 1.14 x64 | hashing | O((n + m)L) | AC | 0.031 s | 952 KB | 11315664 |
| [1728_implementation.java](1728_implementation.java) \* | Java 1.8 | implementation | O(n + m) | AC | 0.140 s | 2172 KB | 11289394 |
| [1728_implementation.py](1728_implementation.py) \* | Python 3.12 x64 | implementation | O(n + m) | AC | 0.109 s | 548 KB | 11289392 |
| [1728_hashing.rs](1728_hashing.rs) | Rust 1.75 x64 | hashing | O((n + m)L) | AC | 0.031 s | 420 KB | 11315666 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1728_implementation.cpp](1728_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m) log n) | AC | 0.015 s | 460 KB | 11325579 |
| [1728_implementation.go](1728_implementation.go) | Go 1.14 x64 | implementation | O(n + m) | AC | 0.031 s | 1156 KB | 11289390 |
| [1728_implementation.rs](1728_implementation.rs) | Rust 1.75 x64 | implementation | O(n + m) | AC | 0.046 s | 464 KB | 11289397 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1728_hashing_optimized.go](1728_hashing_optimized.go) \* | Go 1.14 x64 | hashing | O((n + m)L) | AC | 0.031 s | 320 KB | 11315884 |
| [1728_hashing_optimized.rs](1728_hashing_optimized.rs) \* | Rust 1.75 x64 | hashing | O((n + m)L) | AC | 0.031 s | 60 KB | 11315888 |
| [1728_implementation_optimized.java](1728_implementation_optimized.java) \* | Java 1.8 | implementation | Expected O(I+N+M); stored names and token scratch | AC | 0.093 s | 508 KB | 11327746 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
