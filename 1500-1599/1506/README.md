# 1506. Columns of Numbers

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · difficulty 138 · implementation

Original problem by Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Print N numbers from 0 to 999 (1 ≤ N ≤ 100) in K columns (1 ≤ K ≤ N)
with as few rows as possible. All columns have the same height except
the last, which may be shorter. The numbers fill the first column top
to bottom, then the second, and so on. Each number is right-aligned in
a field of 4 characters, and no line has trailing spaces.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K, then the N numbers.

## Output

The table.

## Examples

### Example 1

Input:

```
7 3
1 2 30 40 50 600 700
```

Output:

```
   1  40 700
   2  50
  30 600
```

## Solution

The fewest rows are H = ⌈N / K⌉. Column c holds the numbers with
indices c·H to c·H + H − 1, so row r consists of the numbers c·H + r
that exist, for c = 0, 1, …; they stop at the first column that has run
out, which can only be the last one. Print each in a field of 4 and end
the row there. `O(N)`.

Pitfalls:

- the numbers go down the columns, not along the rows (test 01);
- every number takes 4 characters, the first one too, so each line
  starts with spaces (test 01);
- when the last column is shorter, the lower rows end one number
  earlier, without trailing spaces (test 06);
- K = N gives a single row and K = 1 a single column (tests 03, 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB |
