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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1611_dp.cpp](1611_dp.cpp) | G++ 13.2 x64 | dp | O(n·(k + 1)) | AC | 0.015 s | 2428 KB |
| [1611_dp.go](1611_dp.go) | Go 1.14 x64 | dp | O(n·(k + 1)) | AC | 0.031 s | 6200 KB |
| [1611_dp.java](1611_dp.java) | Java 1.8 | dp | O(n·(k + 1)) | AC | 0.109 s | 2812 KB |
| [1611_dp.py](1611_dp.py) | Python 3.12 x64 | dp | O(n·(k + 1)) | AC | 0.328 s | 12976 KB |
| [1611_dp.rs](1611_dp.rs) | Rust 1.75 x64 | dp | O(n·(k + 1)) | AC | 0.015 s | 4524 KB |
