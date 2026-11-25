# 2146. Smallest circular period after at most k letter changes

[Timus 2146](https://acm.timus.ru/problem.aspx?space=1&num=2146) · difficulty 641 · strings

Original problem by Valentin Zuev, from the Ural Team Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A drum has n sectors in a circle, each with a lowercase letter. It has
period p when every sector matches the one p positions further around.
Change at most k letters so that the smallest period is as small as
possible, and print that period and the new drum. Any optimal drum is
accepted. The limits are 5 seconds and 256 MB.

## Input

n and k, 1 ≤ n ≤ 10⁵, 0 ≤ k ≤ n, then the n letters.

## Output

The smallest period and the drum after the changes.

## Checking

A checker verifies the period, the number of changes and that the
printed drum has exactly that smallest period.

## Examples

### Example 1

Input:

```
6 3
abcdef
```

Output:

```
3
abcabc
```

### Example 2

Input:

```
4 1
aaab
```

Output:

```
1
aaaa
```

### Example 3

Input:

```
4 0
aaab
```

Output:

```
4
aaab
```

## Solution

On a circle, periods p and n give the period gcd(p, n), so the smallest
period always divides n and only the divisors of n need to be tried. For
a divisor d the sectors split into d classes of positions with the same
remainder modulo d, and period d means each class has one letter. The
cheapest way keeps the most frequent letter of each class, so the
number of changes is n minus the sum of those frequencies.

The divisors are tried from the smallest, and the first one with at most
k changes is the answer, with every class filled with its most frequent
letter. That drum cannot have a smaller period d′: it would then be a
drum with period d′ at most k changes away, and d′ would have been
accepted first. Counting the letters takes O(n) per divisor, and n ≤ 10⁵
has at most 128 divisors.

In the first example period 3 keeps the classes "ad", "be" and "cf" at
one letter each with three changes, and periods 1 and 2 need more.

## Optimized solutions

The optimized C++ version counts one residue class at a time and reuses the alphabet counters. It rejects a divisor as soon as the accumulated edits exceed the budget. Only one period is stored, then repeated directly to the output. The metrics come from submission 11317091.

Go, Java and Rust also count one residue class at a time with a small alphabet table. Python takes strided byte slices and counts their letters with byte-string operations. The accepted submissions were 11317238, 11317242, 11317237 and 11317245, respectively.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11318161 · Java 1.8 №11318171.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2146_strings.cpp](2146_strings.cpp) | G++ 13.2 x64 | strings | O(n d(n)) | AC | 0.046 s | 10404 KB | 11318161 |
| [2146_strings.go](2146_strings.go) | Go 1.14 x64 | strings | O(n d(n)) | AC | 0.203 s | 51504 KB | 11322045 |
| [2146_strings.java](2146_strings.java) | Java 1.8 | strings | O(n d(n)) | AC | 0.156 s | 15172 KB | 11318171 |
| [2146_strings.py](2146_strings.py) | Python 3.12 x64 | strings | O(n d(n)) | AC | 1.375 s | 2528 KB | 11322046 |
| [2146_strings.rs](2146_strings.rs) | Rust 1.75 x64 | strings | O(n d(n)) | AC | 0.109 s | 20756 KB | 11322048 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2146_strings_optimized.cpp](2146_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n d(n)) | AC | 0.031 s | 264 KB | 11317091 |
| [2146_strings_optimized.go](2146_strings_optimized.go) | Go 1.14 x64 | strings | O(n d(n)) | AC | 0.031 s | 1360 KB | 11317238 |
| [2146_strings_optimized.java](2146_strings_optimized.java) | Java 1.8 | strings | O(n d(n)) | AC | 0.109 s | 680 KB | 11317242 |
| [2146_strings_optimized.py](2146_strings_optimized.py) | Python 3.12 x64 | strings | O(n d(n)) | AC | 1.046 s | 924 KB | 11317245 |
| [2146_strings_optimized.rs](2146_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(n d(n)) | AC | 0.031 s | 368 KB | 11317237 |

\* The saved comparison has no Go or Rust submissions from other authors with the same compiler. Python ranks second by time and first by memory and meets the memory improvement criterion.
