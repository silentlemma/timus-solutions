# 1861. Graveyard in Deyja

[Timus 1861](https://acm.timus.ru/problem.aspx?space=1&num=1861) · difficulty 1004 · dp

Original problem by Mikhail Rubinchik, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An inscription of n characters is partly worn away: a "?" stands for a
letter that cannot be read. Restoring the worn letters in the best way,
how many times at most can a given name of m letters occur in the
inscription? Occurrences may overlap, and letters of different case
differ.

## Input

The inscription (letters and "?") and the name (letters),
1 ≤ m ≤ n ≤ 1000.

## Output

The largest possible number of occurrences.

## Examples

### Example 1

Input:

```
R?la?dDefe?tedHi?Br?t?erArc?i??ld
Archibald
```

Output:

```
1
```

### Example 2

Input:

```
Arch?????rchibaldIronfist
Archibald
```

Output:

```
1
```

## Solution

Choose positions where copies of the name start. A copy fits at j when
every letter of the name falls on the same letter or on a "?". Two
copies d < m apart overlap and agree exactly when d is a period of the
name, that is, when the name shifted by d matches itself; copies m or
more apart never meet.

A set of copies is consistent as soon as every copy agrees with the
next one. For three copies j₁ < j₂ < j₃, every position shared by the
first and the third lies inside the second as well, so agreement
passes along the chain. Hence a DP over the last copy: best[j] is one
more than the largest of best[k] for k ≤ j − m and of best[j − d] for
the periods d of the name. The periods come from the prefix function:
they are m − b for the borders b of the name. With at most m periods and
n − m + 1 positions the DP takes at most m(n − m) ≤ n²/4 steps. The
Python solution finds the fitting positions as one AND of shifted bit
masks, one mask per letter. `O(n·m)`.

In the second example copies fit at positions 0 and 8, but 8 is not a
period of "Archibald", so only one of them can be written.

Pitfalls:

- consistency of neighbouring copies is enough; there is no need to
  track the restored letters themselves;
- a "?" may become any letter, also one absent from the name;
- "A" and "a" are different letters.

The answers agree with trying every restoration on four hundred short
inscriptions and with an independent accepted implementation on the
large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1861_dp.cpp](1861_dp.cpp) | G++ 13.2 x64 | dp | O(n m) | AC | 0.015 s | 400 KB |
| [1861_dp.go](1861_dp.go) | Go 1.14 x64 | dp | O(n m) | AC | 0.031 s | 1112 KB |
| [1861_dp.java](1861_dp.java) | Java 1.8 | dp | O(n m) | AC | 0.125 s | 628 KB |
| [1861_dp.py](1861_dp.py) | Python 3.12 x64 | dp | O(n m) | AC | 0.109 s | 576 KB |
| [1861_dp.rs](1861_dp.rs) | Rust 1.75 x64 | dp | O(n m) | AC | 0.046 s | 240 KB |
