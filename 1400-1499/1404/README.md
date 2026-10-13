# 1404. Easy to Hack!

[Timus 1404](https://acm.timus.ru/problem.aspx?space=1&num=1404) · difficulty 80 · implementation

Original problem by Vladimir Yakovlev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A word of at most 100 lowercase letters is encrypted like this: the
letters become numbers 0 to 25, 5 is added to the first number, each
following number gets the new value of the one before it added, and all
values are taken modulo 26 and turned back into letters. Given the
encrypted word, print the original one.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The encrypted word.

## Output

The original word.

## Examples

### Example 1

Input:

```
xbduyr
```

Output:

```
secret
```

## Solution

The k-th encrypted value is the (k − 1)-th one plus the k-th letter,
and taking everything modulo 26 changes nothing in that relation. So
each letter is the difference of its code and the code before it,
modulo 26, with 5 standing before the first code. `O(n)`.

Pitfalls:

- the difference can be negative, so it is brought back into 0 … 25
  (test 02, where a turns into v and back);
- the sums of the encryption grow past 25 before the modulo, but the
  codes in the input are already reduced, which is all that is needed.

The tests were made by encrypting words and are judged by exact
comparison.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1404_implementation.cpp](1404_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 360 KB |
| [1404_implementation.go](1404_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1068 KB |
| [1404_implementation.java](1404_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 1612 KB |
| [1404_implementation.py](1404_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 352 KB |
| [1404_implementation.rs](1404_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 208 KB |
