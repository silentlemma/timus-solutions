# 1922. Teams That Block Every Single Addition

[Timus 1922](https://acm.timus.ru/problem.aspx?space=1&num=1922) · difficulty 322 · sorting

Original problem by Grigoriy Nazarov, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n participants. Participant i accepts a team only if its total
size is at least aᵢ, including that participant. A nonempty team is
effective when every member accepts its size. An effective team is reliable
when adding any one outsider makes it ineffective. An effective team
containing everyone is also reliable. Enumerate all distinct reliable teams.
An empty team is never an answer. Limits: 1 second, 64 MB.

## Input

The first line contains n, 1≤n≤1000. The next n lines contain aᵢ,
1≤aᵢ≤1000. A threshold may exceed n. Original indices are 1 through n.

## Output

Print the number k of reliable teams. In each of the following k lines,
print a team size followed by the original indices of its members.
Teams and members may appear in any order. If none exist, print `0`
without a team description.

## Checking

A custom checker verifies nonempty distinct members, index bounds,
effectiveness, failure of every one-member addition, no repeated teams,
and completeness of the collection. Team order and member order are ignored;
the output need not match one canonical description.

## Examples

```
5
1
3
3
6
6
```

```
2
1 1
3 2 1 3
```

## Solution

Consider an effective team S of size s. Every old member has aᵢ≤s,
so the larger size s+1 cannot violate an old member's requirement.
Adding outsider j therefore succeeds exactly when aⱼ≤s+1.
Reliability is equivalent to every outsider having threshold greater than s+1.

Consequently every participant with aᵢ≤s must belong to S. A participant
with aᵢ=s+1 cannot be inside, because the team would be ineffective,
and cannot remain outside, because adding that participant would work.
Thus at most one reliable team has any given size: precisely the set
of participants whose thresholds are at most s, provided its size is s
and nobody has threshold s+1.

Sort pairs (threshold, original index). For each s=1..n, test:

```text
largest threshold in the first s pairs ≤ s;
and either s=n or the next threshold > s+1.
```

If both hold, output those first s original indices. The first condition
makes the prefix effective. The second blocks every outsider. Conversely,
the preceding argument forces every reliable team to be exactly such a
prefix, so none are missed or duplicated. Equal thresholds cannot be split
across a valid boundary, so their sorting order does not create extra teams.

For s=n, only effectiveness remains to be checked. A complete team is
not automatically effective when some thresholds exceed n.

Reliability is about adding one participant, not about being maximal among
all effective supersets. With thresholds 1,3,3, both the singleton and the
three-member team are reliable: neither threshold-3 outsider can join the
singleton alone, though both could join together.

Let R be the total number of member indices printed. Sorting and listing
take O(n log n+R) time and O(n+R) space in these buffered implementations.
The output can be quadratic: thresholds 2,2,4,4,…,1000,1000 produce
500 teams with 250,500 member indices. Listing them requires that work.

The outside comparison is strictly greater than s+1, not merely greater
than s. Inside thresholds may equal s. Exclude the empty team, allow zero
answers and preserve one-based input indices. Duplicates are distinct
participants, but do not create alternative reliable subsets of one size.
Do not replace the single-addition definition with global maximality,
or omit the output term R from complexity.

## Optimized solutions

`1922_sorting_optimized.java`. Keep reliable teams as qualifying sorted prefixes: the last member threshold is at most size, and the next outsider threshold, if any, must exceed size+1. Pack each threshold and original ID in one long and store only the qualifying prefix lengths. Emit members from the sorted order when needed instead of copying every prefix and keeping the complete output. Let Z be the number of emitted member IDs and S(N) the primitive-sort cost: total time O(N+S(N)+Z), usually O(N log N+Z), with O(N) storage even if Z is quadratic. The zero-team case emits only zero. Sorting ties still follow original IDs; any team/member order is valid.

Compared with `1922_sorting.java`: time 0.109 s → 0.125 s; memory 9 504 KB → 512 KB.

The C++, Go and Rust variants pack each threshold and original index into one integer. The index occupies the low ten bits, so sorting the packed integers sorts by threshold first. The boundary test stays the same. Store only the sizes of reliable teams, then print each sorted prefix directly. For R printed indices, the running time is O(n log n + R) and the memory usage is O(n).

The C++ revision keeps the same packed sort and qualifying-prefix test, with 16 KB input/output buffers. Its exact-source Accepted is 0.015 s / 152 KB; the teaching base is 0.015 s / 1452 KB. The C++ rating check uses the saved 20 November 2026 snapshot.

The accepted base implementations [1922_sorting.java](1922_sorting.java), [1922_sorting.py](1922_sorting.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

Earlier additions were compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1922_sorting_optimized.java`: time place 4/18, memory place 1/18 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1922_sorting.cpp](1922_sorting.cpp) | G++ 13.2 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 1452 KB | 11291505 |
| [1922_sorting.go](1922_sorting.go) | Go 1.14 x64 | sorting | O(n*log(n) + R) | AC | 0.062 s | 5648 KB | 11291507 |
| [1922_sorting.java](1922_sorting.java) \* | Java 1.8 | sorting | O(n*log(n) + R) | AC | 0.109 s | 9504 KB | 11325561 |
| [1922_sorting.py](1922_sorting.py) \* | Python 3.12 x64 | sorting | O(n*log(n) + R) | AC | 0.093 s | 7584 KB | 11325598 |
| [1922_sorting.rs](1922_sorting.rs) | Rust 1.75 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 4040 KB | 11291512 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1922_sorting_optimized.cpp](1922_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 152 KB | 11326637 |
| [1922_sorting_optimized.go](1922_sorting_optimized.go) \* | Go 1.14 x64 | sorting | O(n*log(n) + R) | AC | 0.031 s | 932 KB | 11310396 |
| [1922_sorting_optimized.rs](1922_sorting_optimized.rs) \* | Rust 1.75 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 216 KB | 11310393 |
| [1922_sorting_optimized.java](1922_sorting_optimized.java) \* | Java 1.8 | sorting | O(N+S(N)+Z) | AC | 0.125 s | 512 KB | 11325025 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
