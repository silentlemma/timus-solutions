# 1711. Code Names

[Timus 1711](https://acm.timus.ru/problem.aspx?space=1&num=1711) · difficulty 135 · greedy

Original problem by Alex Samsonov, prepared by Igor Chevdar, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n problems has three candidate code names, and the problems
of a set go in the alphabetical order of their names. Pick one name
per problem so that the problems come in a given order, or report that
no choice works.

## Input

n (1 ≤ n ≤ 16), then n lines with the three names of each problem:
lowercase Latin letters, at most 20 per name, all names distinct. The
last line is the required order, a permutation of 1 … n.

## Output

The chosen names in the required order, one per line, or IMPOSSIBLE.
Any valid choice is accepted.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The repository checker accepts IMPOSSIBLE exactly when the stored reference does. Otherwise it requires exactly n name tokens, each offered for the corresponding problem in the prescribed order, and strictly increasing names. Any valid choice is accepted; line breaks are not compared.

## Examples

### Example 1

Input:

```
11
cipher grille kamkohob
names codenames codes
newtests rejudge timus
size volume summit
watchmen braineater twosides
solution random yesorno
keywords subversion commands
bosses shooting shaitan
game strategy playgame
mnemonic palindromes bestname
eligibility rectangle rules
2 1 7 10 9 6 11 3 8 4 5
```

Output:

```
codenames
grille
keywords
mnemonic
playgame
random
rectangle
rejudge
shaitan
volume
watchmen
```

### Example 2

Input:

```
3
problems in the
first sample are
ordered not randomly
1 2 3
```

Output:

```
IMPOSSIBLE
```

## Acceptance update

Refreshed files: [1711_greedy_parsing_optimized.rs](1711_greedy_parsing_optimized.rs). Their new exact-source Accepted results are listed in the solution tables. Earlier comparison measurements and rankings for these files refer to preceding source snapshots and are retained as historical evidence. The cached audit confirms qualifying coverage in every available language. Teaching versions are retained for clarity; a source that also serves as the fast version must meet the performance criterion.

## Solution

Go along the required order and give each problem the least of its
names that comes after the previous chosen name. If none does, the
answer is IMPOSSIBLE.

This greedy choice is safe. Suppose some valid choice exists, and
compare it with the greedy one problem by problem. By induction the
greedy name is never later than the valid one: the valid name for the
next problem comes after the valid previous name, so also after the
greedy previous name. It is therefore a candidate, and the greedy pick
is at most it. So the greedy run never gets stuck. `O(n)` comparisons
of short strings.

Pitfalls:

- the names are compared as strings, so a prefix comes first: "code"
  before "codenames";
- the order line lists problem numbers by their place in the set, not
  the place of each problem;
- any valid answer is accepted, so the tests use a checker.

The checker verifies that every name belongs to its problem and that
the names increase. The answers match an independent accepted
implementation on 600 random sets.

## Optimized solutions

`1711_greedy_optimized.java`. Keep the same least-feasible-name greedy rule. Read ASCII bytes directly from the existing System.in stream, store the three names per item in one flat byte bank with separate lengths, and scan candidates instead of sorting String arrays. Compare only the common prefix and then the lengths, so proper prefixes remain ordered correctly. Buffer the complete answer in a byte array and use ordinary System.out.write plus flush; if a later item is impossible, discard the partial answer. With B input bytes and name length L<=20, time is O(B+nL) and auxiliary storage O(nL). Three additional runs of these exact source bytes returned (0.125 s, 384 KB), (0.093 s, 340 KB), and (0.125 s, 336 KB). The table uses the actual middle run: time and memory reductions are 33.57% and 34.11% against the retained Java baseline. The variation is shown explicitly; the selected 0.093 s is not paired with the third run's 336 KB.

Compared with `1711_greedy.java`: time 0.140 s → 0.093 s; memory 516 KB → 340 KB.

`1711_greedy_optimized.py`. Keep the greedy rule: choose the smallest of the three names strictly larger than the previous name. Scan the three byte strings directly instead of sorting every triple and constructing a filtered list; consume the order tokens without a separate integer-order list. Accumulate output in one bytearray, replacing it by IMPOSSIBLE if a later choice fails, so no partial answer escapes. Names are lowercase ASCII of length L<=20, making byte order identical to lexical order. With B input bytes, time O(B+nL), storage O(B+nL), not constant space. Flush before os._exit(0). The measured time improves from 0.093 to 0.062 seconds, while memory increases from 492 to 776 KB; admission is the time gain, not a memory saving.

Compared with `1711_greedy.py`: time 0.093 s → 0.062 s; memory 492 KB → 776 KB.

The optimized C++ solution reads with `scanf` into a fixed array of
16 × 3 names of 21 bytes each, enough for n ≤ 16 and 20 letters plus the
terminating zero, instead of a vector of vectors of `std::string` read
through `iostream`. Instead of sorting the three names of a problem, it
scans them with `strcmp` for the least one after the previous choice,
remembers only pointers to the chosen names, and prints them with
`puts`: {1711_greedy_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1711_greedy_optimized.cpp`: time reduction +51.61%; memory reduction
  +74.75%; base: `1711_greedy.cpp`.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1711_greedy_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328588 (Go 1.14 x64): **0.031 s / 976 KB**. Archived comparison: `1711_greedy.go` (Go 1.14 x64) — 0.062 s / 1148 KB (#11289207).


`1711_greedy_parsing_optimized.rs`. Use fixed stack storage for the allowed 16 records, three names per record and at most 20 bytes per name. Read names as bounded byte tokens, keep exact lexicographic min-above-previous selection and write the bounded answer once. No input, name or answer heap allocation is required.

This exact source has its own Accepted and meets the shared [rating criteria](../../RATING_CRITERIA.md). Time and memory below come from the same run; repeated runs can differ because of judge timing. Existing simple and distinct optimized implementations are preserved.

Accepted #11329353 (Rust 1.75 x64): **0.015 s / 60 KB**.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1711_greedy_optimized.py`: time place 1/21, memory place 20/21 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy.cpp](1711_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 396 KB | 11304067 |
| [1711_greedy.go](1711_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1148 KB | 11289207 |
| [1711_greedy.java](1711_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 516 KB | 11289209 |
| [1711_greedy.py](1711_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.093 s | 492 KB | 11304068 |
| [1711_greedy.rs](1711_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 236 KB | 11289213 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy_optimized.cpp](1711_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 100 KB | 11304441 |
| [1711_greedy_optimized.py](1711_greedy_optimized.py) | Python 3.12 x64 | greedy | O(B+nL) | AC | 0.062 s | 776 KB | 11325459 |
| [1711_greedy_optimized.java](1711_greedy_optimized.java) | Java 1.8 | greedy | O(B+nL) | AC | 0.093 s | 340 KB | 11325999 |
| [1711_greedy_optimized.go](1711_greedy_optimized.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 976 KB | 11328588 |
| [1711_greedy_parsing_optimized.rs](1711_greedy_parsing_optimized.rs) | Rust 1.75 x64 | greedy, parsing | O(n) | AC | 0.015 s | 56 KB | 11330236 |
