# 1774. Barber of the Army of Mages

[Timus 1774](https://acm.timus.ru/problem.aspx?space=1&num=1774) · difficulty 515 · matching

Original problem by Magaz Asanov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n people each need two shaves, at two different whole minutes within
their stay: person i arrives at minute tᵢ and stays sᵢ minutes, so the
minutes tᵢ to tᵢ + sᵢ − 1 are allowed. At most k people can be shaved in
one minute. Decide whether everyone can be shaved and give the two
minutes for each.

## Input

n and k (1 ≤ n, k ≤ 100), then tᵢ and sᵢ for each person
(0 ≤ tᵢ ≤ 1000, 2 ≤ sᵢ ≤ 1000).

## Output

`No`, or `Yes` and for each person two minutes pᵢ < qᵢ. Any fitting
schedule is accepted.

## Examples

### Example 1

Input:

```
3 2
1 3
1 3
1 3
```

Output:

```
Yes
1 2
1 3
2 3
```

### Example 2

Input:

```
2 1
1 3
1 3
```

Output:

```
No
```

## Solution

This is a flow problem: each person sends 2 shaves, each minute takes
at most k, and a person can send at most one shave to each minute of
their stay. Minutes between two consecutive arrival or leaving times
see the same people, so they merge into blocks: a block of L minutes
takes at most k·L shaves, and at most min(L, 2) from one person. With
at most 2n + 1 blocks the network is small, and Dinic's algorithm finds
the maximum flow; everyone is shaved exactly when it is 2n.

Inside a block the shaves are dealt round its minutes in turn, the
shaves of each person one after the other. So two shaves of one person
in one block land on different minutes, as L ≥ 2 whenever a person
sends two there, and no minute gets more than k, since the block holds
at most k·L. The network has O(n²) edges and carries at most 2n
shaves, each found along a path in O(n²), so `O(n³)` in all.

In the first example the three people share minutes 1 to 3 with k = 2:
six shaves fill the six places, and dealing them round gives 1 2,
3 1, 2 3, that is, every pair of minutes once.

Pitfalls:

- the two shaves of one person must be at different minutes, which a
  plain count per block would miss;
- the last allowed minute is tᵢ + sᵢ − 1, not tᵢ + sᵢ;
- the schedule is not unique, so the checker tests the windows and the
  load of every minute.

The answers agree with a search over all pairs of minutes on 300 random
cases of up to 5 people and with an independent accepted
implementation, checked both ways, on 100 cases of up to 100 people.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1774_matching.cpp](1774_matching.cpp) | G++ 13.2 x64 | matching | O(n^3) | AC | 0.031 s | 580 KB |
| [1774_matching.go](1774_matching.go) | Go 1.14 x64 | matching | O(n^3) | AC | 0.031 s | 3476 KB |
| [1774_matching.java](1774_matching.java) | Java 1.8 | matching | O(n^3) | AC | 0.156 s | 3652 KB |
| [1774_matching.py](1774_matching.py) | Python 3.12 x64 | matching | O(n^3) | AC | 0.093 s | 4024 KB |
| [1774_matching.rs](1774_matching.rs) | Rust 1.75 x64 | matching | O(n^3) | AC | 0.046 s | 964 KB |
