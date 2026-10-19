# 1900. Choosing Train Spans

[Timus 1900](https://acm.timus.ru/problem.aspx?space=1&num=1900) · difficulty 527 · dp

Original problem by Alex Samsonov, prepared by Alexander Fetisov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Stations 1 through n lie on a line. A nonnegative weight w(i,j) gives the
passengers traveling from i to j, where i < j. Choose exactly k distinct
spans between neighboring stations. A passenger is counted once if the
trip crosses any chosen span. Maximize the counted weight and print a
choice attaining it. Limits: 1 second and 64 MB.

## Input

First n and k, with 2 ≤ n ≤ 500 and 1 ≤ k < n. For each i = 1,…,n−1,
the next line contains w(i,i+1),…,w(i,n), each between 0 and 100.

## Output

Print the maximum weight, then k increasing span indices. Span i joins
stations i and i+1. Any optimal selection is accepted.

## Checking

The checker verifies k distinct increasing indices in range, recomputes
the covered weight, and compares it with the optimal objective. Different
optimal selections are allowed.

## Examples

```
4 1
5 0 6
5 3
5
```

```
14
3
```

## Solution

Cut the station sequence at each selected span. Exactly g = k+1 nonempty
groups remain. A passenger is missed precisely when both endpoints lie
in the same group. Thus minimize the total weight within the groups.

Let C(l,r) be the sum of w(i,j) for l ≤ i < j ≤ r. Build it in `O(n²)`:
process l downward and set C(l,r) = C(l+1,r) + Σ(j=l+1…r) w(l,j),
maintaining the latter sum while r increases.

Let D(t,r) be the least missed weight when stations 1,…,r form t groups.
The recurrence is D(t,r) = min over t−1 ≤ p < r of
D(t−1,p) + C(p+1,r). Initialize D(1,r) = C(1,r).
Retain the minimizing p for reconstruction. With g total groups, only
t ≤ r ≤ n−g+t is necessary: the remaining groups need a station each.

For a ≤ b ≤ c ≤ d, nonnegative weights give the Monge inequality
C(a,c) + C(b,d) ≤ C(a,d) + C(b,c). The difference between the right and
left sides is exactly the sum of w(i,j) with a ≤ i < b and c < j ≤ d.
Adding D(t−1,p) to each candidate row preserves this inequality. It
follows that the leftmost optimal split p is nondecreasing as r grows:
two crossing chosen minima can be uncrossed using the inequality; with
leftmost tie breaking a decrease is impossible.

Compute a DP layer by divide and conquer. Evaluate its middle endpoint
over the permitted split interval, then restrict the left recursion to
splits no larger than its optimum and the right recursion to splits no
smaller. Keep the first split on ties. Each layer costs `O(n log n)`.
Follow parent splits backward from (g,n); they are the selected spans.
Subtract the missed optimum from C(1,n).

Every selection corresponds to exactly one partition and conversely.
The recurrence examines every possible last group, so it computes the
minimum missed weight. Monotone optimization preserves the minimizing
candidate, hence reconstruction yields an optimal selection.

Time: `O(n² + kn log n)`. Space: `O(n² + kn)`, hence `O(n²)` since k < n.
All weights and DP values fit signed 32-bit integers: the total is at
most 100·500·499/2 = 12,475,000. Infinity is 10⁹.

The sample selects span 3: its trips have total 6+3+5=14.

Pitfalls:

- count a trip crossing several selected spans only once;
- keep every group nonempty;
- k selected spans create k+1 groups.

## Language notes

All five versions use the same optimized recurrence and leftmost ties.
Python stores costs and parents in packed integer arrays; Java uses
buffered input. Recursion depth is logarithmic in n.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1900_dp.cpp](1900_dp.cpp) | G++ 13.2 x64 | dp | O(n² + kn log n) | AC | 0.031 s | 3188 KB |
| [1900_dp.go](1900_dp.go) | Go 1.14 x64 | dp | O(n² + kn log n) | AC | 0.046 s | 10088 KB |
| [1900_dp.java](1900_dp.java) | Java 1.8 | dp | O(n² + kn log n) | AC | 0.125 s | 6548 KB |
| [1900_dp.py](1900_dp.py) | Python 3.12 x64 | dp | O(n² + kn log n) | AC | 0.250 s | 10272 KB |
| [1900_dp.rs](1900_dp.rs) | Rust 1.75 x64 | dp | O(n² + kn log n) | AC | 0.031 s | 4996 KB |
