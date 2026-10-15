# 1718. Rejudge

[Timus 1718](https://acm.timus.ru/problem.aspx?space=1&num=1718) · difficulty 307 · implementation

Original problem by Alexander Ipatov, prepared by Alex Samsonov, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A problem had seven tests. Ten new tests were added after them, then
test 6 was removed, and all earlier solutions are rejudged. Each
author whose list of changed verdicts is not empty gets a letter.
Given the old verdicts, find the least and the greatest possible
number of letters.

## Input

n (1 ≤ n ≤ 1000), then n lines with an author's name and an old
verdict: AC, CE, or ML X, TL X or WA X with 1 ≤ X ≤ 7. A verdict with
test X passed tests 1 … X − 1 and failed test X. Verdicts that differ
only in X are different.

## Output

The least and the greatest number of authors who get letters.

## Examples

### Example 1

Input:

```
5
[SPbSU_ITMO]_WiNGeR TL 6
Milanin_(TNU) WA 6
Vladimir_Yakovlev_(USU) AC
Sandro_(USU) WA 1
Sandro_(USU) ML 3
```

Output:

```
0 3
```

## Solution

After the change, tests 1 … 5 stay, old test 7 becomes test 6, and the
new tests are 7 … 16. Each old verdict either surely changes, may
change, or surely stays:

- CE and failures on tests 1 … 5 stay, as the same tests come first;
- a failure on test 7 must change: that test is now number 6, so at
  best the verdict reads 6 instead of 7;
- AC may change, as a new test can fail, and a failure on test 6 may
  change, as that test is gone and the run continues to old test 7.
  If the run fails old test 7 the same way, the verdict stays the
  same, since that test is now number 6.

So the least number of letters is the number of authors with a failure
on test 7. The greatest adds those with an AC or a failure on test 6.
Names are counted in sets. `O(n)`.

Pitfalls:

- an author counts once, however many solutions change;
- a failure on old test 6 can keep exactly the same verdict, so it does
  not force a letter;
- names hold brackets and parentheses, but no spaces, so reading words
  works.

The answers match an independent accepted implementation on 600 random
cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1718_implementation.cpp](1718_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 596 KB |
| [1718_implementation.go](1718_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1344 KB |
| [1718_implementation.java](1718_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.078 s | 1140 KB |
| [1718_implementation.py](1718_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 724 KB |
| [1718_implementation.rs](1718_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 532 KB |
