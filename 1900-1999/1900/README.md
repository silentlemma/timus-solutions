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

The teaching C++ version fills the partition table directly. For t groups ending at station r, it tries every last split p from t−1 to r−1 and adds the internal cost of [p+1,r] to the previous entry. Storing the chosen p lets us recover the spans backward. The input matrix is converted in place to internal costs, processing its rows from bottom to top. The time is O(kn²) and space O(n²). Even with k=n−1, there are only binom(n+1,3) candidate splits, at most 20,833,250 for n≤500.

## Optimized solutions

Go and CPython retain the same Monge divide-and-conquer partition DP. Store only intervals left≤right in one uint32 triangle grouped by right endpoint, at zero-based index right(right+1)/2+left. Initially place passenger weights there, then process left endpoints decreasingly. A running sum of that left station’s original weights plus the already-built interval below converts the same array to within-block unhappy costs. Candidates for a fixed DP end are contiguous in this layout. Put D = n − k. After reserving stations for the remaining nonempty blocks, the DP stores D end positions per layer and reads the position ending at n in the final layer. Keep two D-entry rows and kD uint16 parent cuts. This preserves the original monotone split ranges and reconstruction, including ties. The maximum unhappy total is 100 · 500 · 499 / 2 = 12,475,000, which fits uint32. A cut is at most 499 and fits uint16. At n = 500 the cost triangle uses 501,000 bytes and the parent table uses at most 125,000 bytes. Both stream numeric input. Python uses typed arrays and Go uses typed slices. Time is O(n² + kD log(D + 1)) and space is O(n² + kD). C++, Java and Rust reuse their admitted bases.

The accepted Python 3.12 x64 run takes 0.343 s versus 0.250 s for the base and uses 1 508 KB versus 10272 KB.

The accepted base implementations [1900_dp.cpp](1900_dp.cpp), [1900_dp.java](1900_dp.java), [1900_dp.rs](1900_dp.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

All five versions use the same optimized recurrence and leftmost ties.
Python stores costs and parents in packed integer arrays; Java uses
buffered input. Recursion depth is logarithmic in n.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1900_dp.cpp](1900_dp.cpp) | G++ 13.2 x64 | dp | O(n² + kn log n) | AC | 0.031 s | 3188 KB | 11291199 |
| [1900_dp.go](1900_dp.go) | Go 1.14 x64 | dp | O(n² + kn log n) | AC | 0.046 s | 10088 KB | 11291203 |
| [1900_dp.java](1900_dp.java) | Java 1.8 | dp | O(n² + kn log n) | AC | 0.125 s | 6548 KB | 11291210 |
| [1900_dp.py](1900_dp.py) | Python 3.12 x64 | dp | O(n² + kn log n) | AC | 0.250 s | 10272 KB | 11291207 |
| [1900_dp.rs](1900_dp.rs) | Rust 1.75 x64 | dp | O(n² + kn log n) | AC | 0.031 s | 4996 KB | 11291212 |
| [1900_dp_bruteforce.cpp](1900_dp_bruteforce.cpp) | G++ 13.2 x64 | dp, bruteforce | O(kn²) | AC | 0.046 s | 3156 KB | 11315871 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1900_dp_optimized.go](1900_dp_optimized.go) \* | Go 1.14 x64 | dp | O(n² + kD log(D + 1)) | AC | 0.046 s | 1580 KB | 11315676 |
| [1900_dp_optimized.py](1900_dp_optimized.py) \* | Python 3.12 x64 | dp | O(n² + kD log(D + 1)) | AC | 0.343 s | 1508 KB | 11315679 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
