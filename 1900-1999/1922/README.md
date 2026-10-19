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

## Language notes

All counts and indices fit ordinary integers. Every port retains original
indices while sorting thresholds. C++, Go, Java and Rust accumulate the
current prefix and copy it only at a valid size; Python extracts each
successful prefix. Stored teams must not be overwritten by later changes.
Buffered output keeps the potentially long listing efficient.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1922_sorting.cpp](1922_sorting.cpp) | G++ 13.2 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 1452 KB |
| [1922_sorting.go](1922_sorting.go) | Go 1.14 x64 | sorting | O(n*log(n) + R) | AC | 0.062 s | 5648 KB |
| [1922_sorting.java](1922_sorting.java) | Java 1.8 | sorting | O(n*log(n) + R) | AC | 0.140 s | 9488 KB |
| [1922_sorting.py](1922_sorting.py) | Python 3.12 x64 | sorting | O(n*log(n) + R) | AC | 0.093 s | 7764 KB |
| [1922_sorting.rs](1922_sorting.rs) | Rust 1.75 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 4040 KB |
