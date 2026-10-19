# 1895. Steaks on Board

[Timus 1895](https://acm.timus.ru/problem.aspx?space=1&num=1895) · difficulty 2082 · dp

Original problem by Alex Samsonov, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Schedule n orders on equipment that can process at most k orders at
once. Each order needs two separate, uninterrupted one-minute steps;
there may be a pause between them. Order i must finish by time tᵢ
and cannot start before max(0, tᵢ − x).

All step starts must be nonnegative integers. Minimize the number of
minutes during which any step is running, and construct a schedule.
Idle gaps do not count toward this objective. The limits are 1 second
and 64 MB.

## Input

The first line contains x and k, with 2 ≤ x ≤ 1000 and 1 ≤ k ≤ 50.
The second line contains n, with 1 ≤ n ≤ 50. The third line contains
t₁, …, tₙ in nondecreasing order, with 2 ≤ tᵢ ≤ 1000.

## Output

If no schedule exists, print `-1`. Otherwise print the minimum number
of active minutes, then n pairs of step-start times in input order.
For order i, the pair aᵢ, bᵢ must satisfy
max(0, tᵢ − x) ≤ aᵢ < bᵢ and bᵢ + 1 ≤ tᵢ. At most k steps may start
at any one minute. Any optimal schedule is accepted.

## Checking

A checker verifies the windows, the order of each pair, capacity, and
that the reported active-minute count equals the number of distinct
start times. That count must also equal the optimum; a valid but
nonoptimal schedule is rejected.

## Examples

### Example 1

Input:

```
10 2
3
2 16 25
```

Output:

```
5
0 1
11 15
15 17
```

### Example 2

Input:

```
10 2
4
7 8 9 10
```

Output:

```
4
3 6
4 5
3 6
4 5
```

### Example 3

Input:

```
2 1
2
2 2
```

Output:

```
-1
```

## Solution

Write rᵢ = max(0, tᵢ − x). Both releases rᵢ and deadlines tᵢ are
nondecreasing. We may assume that first steps occur in order of order
index, and second steps do too. To see this, sort all first-step starts
a₁ ≤ … ≤ aₙ and all second-step starts b₁ ≤ … ≤ bₙ separately and
assign the i-th of each to order i. Sorted releases imply aᵢ ≥ rᵢ,
and sorted deadlines imply bᵢ + 1 ≤ tᵢ. Among the first i second steps,
their i original first steps all occur before bᵢ, so aᵢ < bᵢ.
The reassignment preserves the number of steps at every minute.

Use dynamic programming by the number c of active minutes. For a
state (c, i, j), store the earliest last active start time after i
first steps and j second steps. Initially (0, 0, 0) has time −1.
Keeping only the earliest time is sufficient: a prefix that ends
earlier can replay any continuation of a later prefix with the same
counts, without violating windows or capacity.

Choose p new first steps, with 0 ≤ p ≤ min(k, n − i). Use the remaining
capacity for q = min(k − p, i − j) old second steps. Skip p + q = 0.
Only already-started orders may get their second step, so none receives
both steps in one minute. The earliest new start is the previous time
plus 1, also raised to rᵢ₊ₚ when p > 0. If q > 0, its completion must
be no later than tⱼ₊₁, the earliest deadline among those second steps.
Update (c + 1, i + p, j + q) with the minimum resulting time.

Taking the maximum q is safe. Any unused capacity can finish more
old orders now; delete their second steps from the future schedule.
Those orders finish earlier, while every other operation keeps its
time. Thus smaller q cannot produce a better continuation.

Discard a state if its next unfinished order has too little time left.
After a last start at s, an order whose first step is done cannot finish
before s + 2; one not yet started cannot finish before s + 3. These
are necessary bounds and do not exclude a feasible schedule.

The first layer reaching (n, n) gives the minimum active time. Save
predecessors and their chosen minutes to reconstruct both starts for
each order. If no layer through 2n reaches the goal, print −1:
any schedule has at most 2n occupied minutes.

There are `O(n³)` states across all layers and at most k + 1 transitions
per state. Time is `O(n³k)` and reconstruction storage is `O(n³)`.

In the first example, order 1 forces minutes 0 and 1. The windows of
orders 2 and 3 share only minute 15, so these two orders require at
least three more occupied minutes.
The output uses exactly five. In the second example, eight steps and
capacity 2 require at least four minutes, achieved by 3, 4, 5 and 6.
In the third, only minutes 0 and 1 are allowed, but four steps cannot
fit at capacity 1.

Pitfalls:

- a step starting at tᵢ finishes too late;
- the two steps of one order need distinct minutes;
- clamp negative release times at zero;
- minimize occupied minutes, not the span between the first and last;
- filling older slots greedily may prevent a better reassignment later.

Exhaustive search with a flow check confirms the optimum on 408 small
cases, and 19 tricky schedules test the checker.

## Language notes

Every version encodes `(i, j)` as `i·(n+1)+j` and visits only the
active states of a layer. The time layers and predecessor layers are
retained for reconstruction.

Python stores both in signed-short arrays, `array("h")`: an encoded state
is at most `51²−1 = 2600`, and the time sentinel is at most 1001, so the
stored values, including −1, fit. The compiled versions use native
integer arrays or vectors; Java reads through a buffered `StreamTokenizer`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1895_dp.cpp](1895_dp.cpp) | G++ 13.2 x64 | dp | O(n³ k) | AC | 0.015 s | 2168 KB |
| [1895_dp.go](1895_dp.go) | Go 1.14 x64 | dp | O(n³ k) | AC | 0.031 s | 6248 KB |
| [1895_dp.java](1895_dp.java) | Java 1.8 | dp | O(n³ k) | AC | 0.125 s | 3568 KB |
| [1895_dp.py](1895_dp.py) | Python 3.12 x64 | dp | O(n³ k) | AC | 0.156 s | 1632 KB |
| [1895_dp.rs](1895_dp.rs) | Rust 1.75 x64 | dp | O(n³ k) | AC | 0.031 s | 3168 KB |
