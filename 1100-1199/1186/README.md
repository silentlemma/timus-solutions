# 1186. Do two chemical formulas contain the same atoms?

[Timus 1186](https://acm.timus.ru/problem.aspx?space=1&num=1186) · difficulty 697 · strings

Original problem by Joseph Romanosky and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A formula is a `+`-separated list of sequences, each with an optional
leading multiplier. A sequence is a run of elements, each optionally
followed by a multiplier; an element is a chemical symbol (a capital
letter, maybe followed by a small letter) or a sequence in round
brackets. For a left side and up to 10 right sides of at most 100
characters each, say whether every chemical element occurs the same total
number of times on both sides.

Explicit multipliers are integers at least 2; an omitted multiplier is 1.
In each complete formula, the total count of any individual element is at most 10000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The left side, `N`, then `N` right sides.

## Output

For each right side, `left==right` if the totals match and `left!=right`
otherwise, with both formulas copied exactly.

## Examples

### Example 1

Input:

```
C2H5OH+3O2+3(SiO2)
7
2CO2+3H2O+3SiO2
2C+6H+13O+3Si
99C2H5OH+3SiO2
3SiO4+C2H5OH
C2H5OH+3O2+3(SiO2)+Ge
3(Si(O)2)+2CO+3H2O+O2
2CO+3H2O+3O2+3Si
```

Output:

```
C2H5OH+3O2+3(SiO2)==2CO2+3H2O+3SiO2
C2H5OH+3O2+3(SiO2)==2C+6H+13O+3Si
C2H5OH+3O2+3(SiO2)!=99C2H5OH+3SiO2
C2H5OH+3O2+3(SiO2)==3SiO4+C2H5OH
C2H5OH+3O2+3(SiO2)!=C2H5OH+3O2+3(SiO2)+Ge
C2H5OH+3O2+3(SiO2)==3(Si(O)2)+2CO+3H2O+O2
C2H5OH+3O2+3(SiO2)!=2CO+3H2O+3O2+3Si
```

## Solution

Count the atoms of each formula and compare the counts. Split at `+`
(brackets never contain one), and in each term read the leading number,
1 if absent. Then scan the term with a stack of counters, one per open
bracket:

- `(` pushes an empty counter;
- `)` pops the counter, multiplies it by the number after the bracket and
  adds it to the counter below;
- a symbol adds its multiplier, 1 by default, to the top counter.

The bottom counter, times the leading number, is the term's share.
`O(L)` per formula, apart from the work on the counters.

Pitfalls:

- `Co` is one element, while `CO` is carbon and oxygen, so a small letter
  belongs to the capital before it;
- multipliers can contain zeros, like `10`, even though the examples
  avoid the digit `0` as it looks like oxygen;
- a missing multiplier means 1, both before a term and after an element
  or a bracket.

The answers were compared with a separately written solution on 300
random tests with brackets up to three levels deep, 3000 right sides in
all.

## Language notes

- All languages parse the same way and compare their counting maps:
  counters in Python, ordered maps in C++ and Rust, hash maps in Go and
  Java.

## Optimized solutions

Read each term backwards so the group multiplier is known before reaching its elements. Count elements by a numeric symbol code.

Java submission 11317912 took 0.093 s and used 420 KB. The simple version took 0.156 s and used 4148 KB.

Python scans each formula from right to left. It reads a group's multiplier before its elements and adds their counts directly to one dictionary. In the saved ranking it shares third place by time and first by memory. The measured memory exceeds that of the simple version. Python 3.12 x64, submission 11317903. Time 0.078 → 0.078 s, memory 532 → 588 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321888 · Go 1.14 x64 №11321889 · Java 1.8 №11322193 · Python 3.12 x64 №11322194 · Rust 1.75 x64 №11322195.

Rust scans each formula backward so the multiplier of a group is known before its atoms are counted. Rust 1.75 x64, submission 11323410. Time 0.031 → 0.015 s, memory 248 → 52 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1186_strings.cpp](1186_strings.cpp) | G++ 13.2 x64 | strings | O(L) per formula | AC | 0.001 s | 392 KB | 11321888 |
| [1186_strings.go](1186_strings.go) | Go 1.14 x64 | strings | O(L) per formula | AC | 0.015 s | 1264 KB | 11321889 |
| [1186_strings.java](1186_strings.java) | Java 1.8 | strings | O(L) per formula | AC | 0.156 s | 4148 KB | 11322193 |
| [1186_strings.py](1186_strings.py) | Python 3.12 x64 | strings | O(L) per formula | AC | 0.078 s | 532 KB | 11322194 |
| [1186_strings.rs](1186_strings.rs) | Rust 1.75 x64 | strings | O(L) per formula | AC | 0.031 s | 248 KB | 11322195 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1186_strings_optimized.java](1186_strings_optimized.java) | Java 1.8 | strings | O(L) per formula | AC | 0.093 s | 420 KB | 11317912 |
| [1186_strings_optimized.py](1186_strings_optimized.py) | Python 3.12 x64 | strings | O(L) per formula | AC | 0.078 s | 588 KB | 11317903 |
| [1186_strings_optimized.rs](1186_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(L) per formula | AC | 0.015 s | 52 KB | 11323410 |

\* The marked versions have room to improve in the ratings.
