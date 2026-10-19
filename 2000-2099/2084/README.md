# 2084. Order tasks that pay down a debt

[Timus 2084](https://acm.timus.ru/problem.aspx?space=1&num=2084) · difficulty 3114 · dp, sorting

Original problem by Nikita Burlakov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A debt starts at X. Each of N tasks first lowers the debt by aᵢ (not
below zero) and then earns max(0, bᵢ − D), where D is the debt at that
moment. Find the order of the tasks with the greatest total and output
it. The limits are 2 seconds and 256 MB.

## Input

X and N, 0 ≤ X ≤ 100, 1 ≤ N ≤ 200, then a₁ … a_N (0 to 100) and
b₁ … b_N (0 to 10⁶).

## Output

The greatest total, then an order of the tasks that earns it. Any such
order is accepted.

## Checking

A checker compares the total and replays the printed order.

## Examples

### Example 1

Input:

```
5 3
0 1 5
5 1 0
```

Output:

```
6
3 2 1
```

### Example 2

Input:

```
4 4
3 0 1 2
7 8 2 3
```

Output:

```
19
1 4 3 2
```

## Solution

The debt never exceeds X, so a task with b > X always earns b − X more
than the same task with b = X; that part is added at the end, and
afterwards every b is at most X. Write rᵢ for the total repair done up
to and including task i. Then the debt is X − min(X, rᵢ), and the task
earns max(0, min(X, rᵢ) − (X − bᵢ)).

Look at a best order and call the tasks that earn nothing given up.
Moving them to the front only raises the repair seen by the others, so
the given up tasks can go first. Every other task then earns
min(X, rᵢ) − (X − bᵢ), and the sum of the second parts does not depend
on the order. The first parts form the prefix sums of the repairs capped at X,
which are largest at every position when the tasks go by a descending.
Conversely, for any set of given up tasks this order earns at least the
formula, since a real task never earns less than zero. So the answer is
the best value of the formula over all sets of given up tasks.

Sort the tasks by a ascending. With the kept tasks in descending order
after the given up ones, task k sees the given up tasks before it in the
sorted list plus every task from k on. So a DP over the sorted list
keeps s, the repair of the given up tasks so far (capped at X, since
larger values change nothing): a kept task earns
min(X, s + suffix_k) − (X − b_k), a given up task adds its a to s. The
stored choices give the order: given up tasks first, then the kept ones
by a descending. The DP takes O(N · (X + 1)), plus sorting.

In the first example the third task repairs all 5 units first, then the
second and the first earn 1 and 5: 6 in total.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2084_dp.cpp](2084_dp.cpp) | G++ 13.2 x64 | dp | O(N log N + N X) | AC | 0.015 s | 268 KB |
| [2084_dp.go](2084_dp.go) | Go 1.14 x64 | dp | O(N log² N + N X) | AC | 0.031 s | 1740 KB |
| [2084_dp.java](2084_dp.java) | Java 1.8 | dp | O(N log N + N X) | AC | 0.156 s | 4360 KB |
| [2084_dp.py](2084_dp.py) | Python 3.12 x64 | dp | O(N log N + N X) | AC | 0.125 s | 1988 KB |
| [2084_dp.rs](2084_dp.rs) | Rust 1.75 x64 | dp | O(N log N + N X) | AC | 0.046 s | 480 KB |
