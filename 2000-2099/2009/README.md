# 2009. Two Unit-Time Service Queues

[Timus 2009](https://acm.timus.ru/problem.aspx?space=1&num=2009) · difficulty 833 · simulation

Original problem by Alexey Kungurtsev, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Students arrive at two service queues, left and right. Service takes one
second per student and starts immediately when possible. Each arriving
student may join either tail or stand immediately behind a listed
acquaintance who is currently in that queue. Choose a position with the
fewest people ahead, preferring the right queue on a tie. Queues cannot
later be changed. Students of one group arrive at the same time but make
their choices sequentially in the given order. Completions at an arrival
time happen first, in both queues. Find each student's departure time
and chosen queue.

## Input

Integers `n m`, `5 ≤ n ≤ 1000`, `1 ≤ m ≤ n`. Students are numbered 1..n.
Each of the next `n` lines lists at most 100 other student IDs after
whom that student may stand, followed by 0. The permission is directed,
not necessarily mutual; the student's own ID is absent. Each group has a
line `t k` and a line of its `k` IDs in arrival order. Group times are
increasing integers `1 ≤ t ≤ 10^9`. Every student arrives exactly once.
Time limit 1 second, memory 64 MB.

## Output

Print `n` lines in student-ID order, each containing the departure time
and `left` or `right`. The unique numbers and words are compared token
by token.

## Checking

Outputs are compared token by token.

## Examples

```
5 1
0
0
0
0
1 0
1 5
1 2 3 4 5
```

```
2 right
2 left
4 right
3 left
3 right
```

After the first four arrivals the right queue is `[1,3]` and the left is
`[2,4]`. Student 5 can stand directly behind 1, giving right queue
`[1,5,3]`. All arrive at time 1, so each front departs at 2. Student 5
departs at 3 and student 3 at 4. Output remains in ID order.

## Solution

Store both queues as ordered arrays. For every student maintain a
current queue number, or −1 if not waiting, and a current zero-based
position. Keep the next front-completion time for each nonempty queue. A
stale position of a departed student is ignored through the queue-number
field.

Before processing a group at time `t`, advance both servers. If a
queue's next completion is `u≤t`, exactly `min(queue_length,t−u+1)` of
its current front students leave. Record their times `u,u+1,…`, mark
them absent, erase that prefix and update remaining positions. If a
queue remains, advance its next completion by the number served;
otherwise mark it idle. This handles gaps up to `10^9` arithmetically.

For an arrival, start with the two tail positions. For each listed
acquaintance currently waiting, offer the acquaintance's position plus
one in that queue. Take each queue's minimum. Choose left only when its
position is strictly smaller; otherwise choose right. Insert the student
and update the shifted suffix positions. If the queue was empty, its new
front finishes at `t+1`. After all groups, record the remaining
departures from each queue's next completion at one-second intervals.

Induct on arrival events. Initially arrays, membership and clocks
describe empty queues. During an arrival-free gap, the front completes
at the saved time and subsequent students at consecutive seconds in the
stored order. The served-prefix formula therefore performs exactly all
completions through `t`, including equality, and restores positions
before any new arrival.

All legal arrival positions are precisely the tails and the places
immediately behind currently present listed students. The computed
minima and right-queue tie rule select exactly the specified place. In a
nonempty queue, every such insertion position is at least one, so the
working front is never displaced and its completion clock is unchanged.
For an empty queue, service begins now and completes one second later.
Updating the inserted suffix preserves all membership and position facts
for the next student of the same group. Final draining is the same
arrival-free progression. Thus every output record is correct.

Let `F` be the total number of listed acquaintances, at most `100n`. At
most `n` insertions and `2m` service batches each shift or rerank at
most `n` positions; friend inspection totals `F`. Time `O(n²+F)`, memory
`O(n+F)` including input and output. No loop over the elapsed time is
needed. Every departure is at most `max_arrival+n≤1000001000`, within
signed 32-bit range.

## Language notes

Remove completed students before all arrivals at the same time, and
ignore both future and departed acquaintances. Permissions are directed.
Repeated arrivals behind one acquaintance go immediately behind that
person, before earlier followers, rather than forming a permanent group.
Ties choose right. An idle server's clock restarts at the new arrival,
and final records are indexed by student ID. All five ports use
iterative arrays or lists; Java uses buffered input and primitive friend
rows.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2009_simulation.cpp](2009_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2 + F) | AC | 0.015 s | 640 KB |
| [2009_simulation.go](2009_simulation.go) | Go 1.14 x64 | simulation | O(n^2 + F) | AC | 0.078 s | 5532 KB |
| [2009_simulation.java](2009_simulation.java) | Java 1.8 | simulation | O(n^2 + F) | AC | 0.140 s | 1684 KB |
| [2009_simulation.py](2009_simulation.py) | Python 3.12 x64 | simulation | O(n^2 + F) | AC | 0.109 s | 10744 KB |
| [2009_simulation.rs](2009_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2 + F) | AC | 0.046 s | 1780 KB |
