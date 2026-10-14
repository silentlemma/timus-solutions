# 1606. Slalom

[Timus 1606](https://acm.timus.ru/problem.aspx?space=1&num=1606) · difficulty 713 · greedy

Original problem by Alexander Toropov, prepared by Alexander Ipatov, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Up to 50000 flags stand on a slope, all with different x and different
y. Petya skis down from the start line y = 100000 to the finish line
y = 0 along a broken line whose corners are flags, always going down,
and must change direction left/right at every flag touched; flags can
also be passed straight through without touching. Touch as many flags
as possible and print them in order. Any best list is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then the coordinates of the flags.

## Output

The number of flags, then their numbers in the order touched.

## Examples

### Example 1

Input:

```
5
5 2
6 5
1 1
4 3
2 4
```

Output:

```
4
2 5 4 3
```

### Example 2

Input:

```
4
1 6
3 4
5 2
4 1
```

Output:

```
3
1 3 4
```

## Solution

The skier always goes down, so the touched flags come in order of
falling y. Sorted that way, their x coordinates must zigzag: each step
goes the other way sideways from the step before. The start and the
finish lines can be reached at any point, so the first and the last
step impose nothing. The task is the longest zigzag subsequence of the
x coordinates.

Split the sorted sequence into maximal runs in which x only grows or
only falls. Taking the first flag, the flag where each run turns and the
last flag gives a zigzag with one flag more than there are runs, and no
zigzag can be longer, since each of its steps needs a run of its own.
After sorting this is a single pass: `O(n log n)`.

The tests use a checker that accepts any list of the right length that
goes down and turns at every flag. The length was checked against an
exhaustive search over all subsets of up to 8 flags.

Pitfalls:

- the answer is not unique: in the first example x = 4 or x = 5 can be
  the third flag, and the output may differ from the example;
- a single flag is a valid descent with one touch (test 03);
- if x only grows down the slope, at most two flags can
  be touched (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1606_greedy.cpp](1606_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.062 s | 1388 KB |
| [1606_greedy.go](1606_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.078 s | 7300 KB |
| [1606_greedy.java](1606_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.171 s | 7232 KB |
| [1606_greedy.py](1606_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.187 s | 18416 KB |
| [1606_greedy.rs](1606_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 6028 KB |
