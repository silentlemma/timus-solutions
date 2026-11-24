# 1611. Decimation

[Timus 1611](https://acm.timus.ru/problem.aspx?space=1&num=1611) · difficulty 698 · dp

Original problem by Alexander Ipatov (idea by Stanislav Vasiliev), from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n ≤ 10000 conductors stand in a line, each good (`1`) or bad (`0`); every
person whose place is a multiple of 10 is fined. Up to k ≤ 50 friends
of the conductors can be put into the line anywhere before the fines.
Minimise the number of fined friends plus fined good conductors, and
print it with the places of the friends in the new line. Any best line
is accepted.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n and k, then the line as a string of `0` and `1`.

## Output

The least number of such fines, then m and the m places of the friends.

## Examples

### Example 1

Input:

```
10 2
0000000001
```

Output:

```
0
2 5 12
```

### Example 2

Input:

```
10 2
1111111111
```

Output:

```
1
0
```

## Solution

Build the new line from the front. After i conductors and j friends the
next person stands at place i + j + 1, whoever it is. So cost[i][j], the
least number of fines so far, has two moves: a friend steps in and is
fined when that place is a multiple of 10, or conductor i + 1 steps in
and adds a fine only if good and on such a place. Friends after the last
conductor could only be fined, so they are never needed. The answer is
the best cost[n][j] over j ≤ k, and walking the table back gives the
places of the friends: `O(n·(k + 1))`.

The tests use a checker that rebuilds the line from the printed places
and counts its fines. The numbers were checked against trying every set
of friend places on short lines.

Pitfalls:

- a friend shifts every conductor behind it by one place, so one friend
  in front can save all good conductors at once (test 05), and a second
  friend may only add a fine;
- friends themselves are fined on tenth places, and the longer line can
  reach a new tenth place (test 08);
- the answer is not unique: the first example's answer puts two
  friends, but one at the front is just as good.

## Optimized solutions

Update the dynamic program only at positions divisible by ten, where a fine can occur. A monotone queue selects the cheapest previous state among feasible friend counts, and one byte per state records how to reconstruct the lineup.

Python submission 11317970 took 0.093 s and used 848 KB. The simple version took 0.375 s and used 13328 KB.

Go submission 11317975 took 0.015 s and used 1248 KB. The simple version took 0.031 s and used 6184 KB.

Java submission 11317985 took 0.093 s and used 660 KB. The simple version took 0.125 s and used 2792 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321890 · Go 1.14 x64 №11322096 · Rust 1.75 x64 №11321891 · Java 1.8 №11322098 · Python 3.12 x64 №11322099.

The packed version keeps one row of costs and one bit per state to reconstruct the placement. Rust 1.75 x64, submission 11322342. Time 0.046 → 0.046 s, memory 4520 → 224 KB.

The packed version keeps one row of costs and one bit per state to reconstruct the placement. G++ 13.2 x64, submission 11322343. Time 0.015 → 0.015 s, memory 2412 → 204 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1611_dp.cpp](1611_dp.cpp) | G++ 13.2 x64 | dp | O(n·(k + 1)) | AC | 0.015 s | 2412 KB | 11321890 |
| [1611_dp.go](1611_dp.go) | Go 1.14 x64 | dp | O(n·(k + 1)) | AC | 0.031 s | 6184 KB | 11322096 |
| [1611_dp.java](1611_dp.java) | Java 1.8 | dp | O(n·(k + 1)) | AC | 0.125 s | 2792 KB | 11322098 |
| [1611_dp.py](1611_dp.py) | Python 3.12 x64 | dp | O(n·(k + 1)) | AC | 0.375 s | 13328 KB | 11322099 |
| [1611_dp.rs](1611_dp.rs) | Rust 1.75 x64 | dp | O(n·(k + 1)) | AC | 0.046 s | 4520 KB | 11321891 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1611_dp_optimized.py](1611_dp_optimized.py) | Python 3.12 x64 | dp | O((n + k)·(k + 1)) | AC | 0.093 s | 848 KB | 11317970 |
| [1611_dp_optimized.go](1611_dp_optimized.go) | Go 1.14 x64 | dp | O((n + k)·(k + 1)) | AC | 0.015 s | 1248 KB | 11317975 |
| [1611_dp_optimized.java](1611_dp_optimized.java) | Java 1.8 | dp | O((n + k)·(k + 1)) | AC | 0.093 s | 660 KB | 11317985 |
| [1611_dp_optimized.rs](1611_dp_optimized.rs) | Rust 1.75 x64 | dp | O(n·(k + 1)) | AC | 0.046 s | 224 KB | 11322342 |
| [1611_dp_optimized.cpp](1611_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n·(k + 1)) | AC | 0.015 s | 204 KB | 11322343 |
