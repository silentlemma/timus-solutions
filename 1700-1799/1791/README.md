# 1791. Uncle Styopa and Buses

[Timus 1791](https://acm.timus.ru/problem.aspx?space=1&num=1791) · difficulty 1471 · greedy

Original problem by Eugene Kurpilyansky, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A one-lane stretch of road is shared by buses in both directions, one
bus at a time, and each bus needs exactly one minute to pass. Bus i
arrives at minute tᵢ and may spend at most pᵢ minutes on the stretch,
waiting included. Buses of one direction must pass in their order of
arrival. Decide whether every bus can be on time.

## Input

n (1 ≤ n ≤ 100000), then n pairs tᵢ pᵢ for one direction; then m
(1 ≤ m ≤ 100000) and m pairs for the other. All numbers are from 1 to
10⁸, and each direction is listed in order of arrival.

## Output

"YES" if all buses can be on time, otherwise "NO".

## Examples

### Example 1

Input:

```
2
1 1
1 2
1
2 2
```

Output:

```
YES
```

### Example 2

Input:

```
2
1 1
1 2
1
2 1
```

Output:

```
NO
```

## Solution

Bus i must enter during one of the minutes tᵢ … tᵢ + pᵢ − 1, and only
one bus enters per minute. On one side a bus must enter before the next
one, so its last minute is at most the next bus's last minute minus
one; one pass from the back lowers the last minutes accordingly. Then
go through the minutes: of the two front buses that have already
arrived, send the one whose last minute is earlier; if none has
arrived, jump to the next arrival. If a bus is sent after its last
minute, the answer is NO. Sending the most urgent waiting bus is never
worse, since swapping it with a later one keeps both on time. The
answer is YES if all buses get through. `O(n + m)`.

In the first example the first bus enters at minute 1, the second at
2 and the bus from the other side at 3, the last minute it may use. In
the second example that bus must enter by minute 2, but so must the
second bus, and minute 1 is taken by the first one.

Pitfalls:

- a hurried bus behind a patient one on the same side makes the
  patient one hurry too, which the backward pass takes care of;
- the times reach 10⁸, so the clock must jump over idle periods instead
  of counting every minute;
- waiting counts towards pᵢ, so a bus that arrives at tᵢ must enter no
  later than tᵢ + pᵢ − 1.

The answers agree with a search over every merge of the two queues on
400 small random cases, and with an independent accepted
implementation on large cases: plans with spare minutes, full plans
with one bus a minute short, and random times.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1791_greedy.cpp](1791_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.281 s | 2872 KB |
| [1791_greedy.go](1791_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.078 s | 6852 KB |
| [1791_greedy.java](1791_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 3560 KB |
| [1791_greedy.py](1791_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.562 s | 46212 KB |
| [1791_greedy.rs](1791_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.031 s | 8328 KB |
