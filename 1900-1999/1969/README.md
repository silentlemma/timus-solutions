# 1969. Reconstructing Repeated Tram Schedules

[Timus 1969](https://acm.timus.ru/problem.aspx?space=1&num=1969) · difficulty 2809 · constructive

Original problem from the Open Ural FU Personal Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Identical trams move at constant speed between endpoints A and B without
stopping at either endpoint. Each starts at A and makes the same positive
number k of complete round trips, finally stopping at A. An observer lies
strictly between A and B. Travel times a from A to the observer and b from
the observer to B are positive integer seconds, shared by all trams.

The first tram departs at D. Departures are distinct and increasing, and
every tram departs strictly before the first tram returns to A for the
first time. All trips finish by 23:59:59 of the same day. Given D and all
distinct observed passage times in increasing order, recover any schedule
consistent with them. Limits: 1 second, 64 MB.

## Input

The first line is D in HH:MM:SS format. Every remaining line, until EOF,
is one observed passage in the same format. There is no count line.
The number n of passages is even, 2≤n≤5000. They are distinct, sorted,
at most 23:59:58, and the first is strictly after D. A solution exists.

## Output

Print one line per tram, ordered by departure. Each line lists every
endpoint visit, beginning with departure from A, alternating B and A,
and ending with the final arrival at A: 2k+1 HH:MM:SS values. All trams
use the same k and the same one-way duration a+b. Any valid answer is accepted.

## Checking

A checker simulates the printed schedule and verifies the conditions of
the statement and the exact multiset of passages; any valid schedule is
accepted.

## Examples

```
08:00:00
08:07:30
08:38:30
08:44:49
08:51:32
08:53:30
09:15:49
09:22:32
09:24:30
09:30:49
09:37:32
10:01:49
10:08:32
```

```
08:00:00 08:23:00 08:46:00 09:09:00 09:32:00
08:37:19 09:00:19 09:23:19 09:46:19 10:09:19
08:44:02 09:07:02 09:30:02 09:53:02 10:16:02
```

## Solution

Convert times to seconds. Write T for the sorted observations, P=2(a+b)
for a round-trip period and τ=P/2 for one-way travel.

### Enumerate the first return past the observer

The earliest observation belongs to the first tram on its outward leg,
so a=T[0]−D is known. That tram first passes the observer on its return
at D+P−a. If this is T[j], then P=T[j]−D+a. Before this return, every
observation is an initial outward passage: no later tram can return sooner.
Thus j is at most the number R of trams, and R≤n/2. Try j=1,…,n/2,
including the final index. Reject odd P and P≤2a, which would give b≤0.

### Determine k without a second search

Let d be the latest departure. The final observation is d+kP−a, and
D≤d<D+P. Consequently

k=floor((T[n−1]−D+a)/P).

Reject k=0 or n not divisible by 2k. The number of trams is R=n/(2k).
This floor identity depends on the strict departure window.

### Recover departures greedily

For a candidate P, scan T from left to right, skipping used observations.
The earliest unused t must be the first outward passage of a remaining
tram: every other passage of that tram is later. Its departure is forced
to be t−a and must be less than D+P. The tram must account for

t+rP and t+(P−2a)+rP, for r=0,…,k−1.

Require every such value to be present and unused, then mark it. Reject
the candidate on a missing time, collision, invalid departure or incorrect
number of trams. Accept when all observations belong to exactly R trams.
Use a membership array or set and generation-stamped marks so that failed
candidates do not require clearing the entire day-sized array.

### Correctness and cost

The true P occurs in the enumerated range and yields the true k by the
floor identity. Inductively, after complete trams are removed, the earliest
remaining passage forces the next true departure. Hence the true candidate
cannot fail. Conversely, a successful candidate partitions every input
observation into exactly the simulated legs, obeys all endpoint conditions
and uses a,b>0. Its latest final arrival is T[n−1]+a, within the day by
the input guarantee. Therefore every returned schedule is valid.

At most n/2 candidates each scan or mark O(n) observations. With S=86400,
time is `O(n²+S)` and memory is `O(n+S)`; all arithmetic fits signed 32 bits.

In the example a=450 seconds, P=2760 and τ=1380. There are k=2 round
trips and R=3 departures, at 08:00:00, 08:37:19 and 08:44:02. Adding τ
repeatedly produces the five endpoint times on each line. Alternating
observer offsets 450 and 930 seconds reconstructs all twelve observations.

Read observations through EOF, not as an explicit count. Different valid
periods and round-trip counts can explain the same input, so do not compare
answers token by token. Include candidate index n/2. The latest departure
must be strictly less than D+P, not equal. Reset marks logically for every
candidate and check target bounds before array indexing. Endpoint visits
of different trams may coincide; observed passages may not.

## Language notes

All five versions use the same reconstruction. Python uses a set for presence
and a list of generation marks. C++, Go, Java 8 and Rust use indexed arrays.
Java appends two-digit fields directly rather than repeatedly invoking a
general formatter. Each program preserves one output line per tram.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1969_constructive.cpp](1969_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2+86400) | AC | 0.015 s | 804 KB |
| [1969_constructive.go](1969_constructive.go) | Go 1.14 x64 | constructive | O(n^2+86400) | AC | 0.046 s | 2752 KB |
| [1969_constructive.java](1969_constructive.java) | Java 1.8 | constructive | O(n^2+86400) | AC | 0.187 s | 5808 KB |
| [1969_constructive.py](1969_constructive.py) | Python 3.12 x64 | constructive | O(n^2+86400) | AC | 0.093 s | 2540 KB |
| [1969_constructive.rs](1969_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2+86400) | AC | 0.015 s | 716 KB |
