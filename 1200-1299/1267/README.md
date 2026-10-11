# 1267. Yekaterinburg subway

[Timus 1267](https://acm.timus.ru/problem.aspx?space=1&num=1267) · difficulty 1706 · dp

Original problem by Leonid Volkov (prepared by Leonid Volkov and Alexander Somov), from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A subway line has N stations (1 ≤ N ≤ 16) with whole-minute travel
times between neighbours (each up to 10⁵, possibly 0). Trains leave
station 1 towards N every P minutes starting at minute A, and station N
towards 1 every P minutes starting at minute B (1 ≤ P ≤ 10⁵,
0 ≤ A, B ≤ P).
Stops are instant. A tourist starts at station S, gets on any train, and
must get off at every other station to inspect it, which with boarding
takes 59 seconds, so the next train taken from a station leaves at least
a minute after the arrival. Finally the tourist returns to S. Find the
shortest time from the first boarding to the final arrival at S.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N − 1 travel times, then S, then P, A and B.

## Output

The shortest duration in minutes.

## Examples

### Example 1

Input:

```
3
5 7
2
4 0 1
```

Output:

```
28
```

## Solution

Three observations shrink the problem.

- The start time is free, and once the first trains have reached the
  far ends the timetable repeats with period P. Starting a whole number
  of periods later uses the same trains at the same relative times, so
  every train can be taken to run forever: towards N it passes station
  i at times congruent to (A + pos(i)) mod P, towards 1 to
  (B + pos(N) − pos(i)) mod P.
- Being at a station earlier is never worse: one can wait for any later
  train. So for each set of inspected stations and current station only
  the earliest arrival time matters.
- Getting off at a station already inspected never helps. Riding on
  from there in the same direction is no better than staying on board,
  and the train back in the other direction passes the previous station
  later than the moment the tourist left it, so waiting there would have
  caught it.

For both directions of the first train, a DP over (inspected set,
station) keeps the earliest arrival. From each state, take the first
train each way leaving at least a minute after the arrival and ride to
any uninspected station on its way. Once every station is inspected,
add the wait and ride straight back to S. With n = N this is
`O(2ⁿ · n²)`.

Pitfalls:

- the tourist cannot leave on the train that brought them: the next
  departure is at least one minute later;
- travel times may be 0, putting several stations at the same place
  (tests 05, 09);
- a ride may pass uninspected stations without stopping;
- with N = 1 the answer is 0 (test 02).

The DP was compared on 400 small cases (N ≤ 6, short gaps and periods)
with a search over the real timetable, including the first trains, any
starting train and getting off at inspected stations.

## Language notes

- All languages run the same DP over a flat array of 2ⁿ · n arrival
  times.
- CPython needs about 1.3 s on the largest tests, over the limit, so the
  Python solution is submitted under PyPy 3.10.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1267_dp.cpp](1267_dp.cpp) | G++ 13.2 x64 | dp | O(2ⁿ · n²) | AC | 0.093 s | 7948 KB |
| [1267_dp.go](1267_dp.go) | Go 1.14 x64 | dp | O(2ⁿ · n²) | AC | 0.109 s | 10036 KB |
| [1267_dp.java](1267_dp.java) | Java 1.8 | dp | O(2ⁿ · n²) | AC | 0.218 s | 8768 KB |
| [1267_dp.py](1267_dp.py) | PyPy 3.10 x64 | dp | O(2ⁿ · n²) | AC | 0.312 s | 27088 KB |
| [1267_dp.rs](1267_dp.rs) | Rust 1.75 x64 | dp | O(2ⁿ · n²) | AC | 0.062 s | 8284 KB |
