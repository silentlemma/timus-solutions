# 1713. Key Substrings

[Timus 1713](https://acm.timus.ru/problem.aspx?space=1&num=1713) · difficulty 633 · strings

Original problem by Dmitry Ivankov (idea by Alexander Mironenko), from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A key of a command is a substring of it that is not a substring of any
other command. For each of n commands find a shortest key.

## Input

n (2 ≤ n ≤ 1000), then n commands: lowercase Latin letters, 1 to 100
of them. No command is a substring of another.

## Output

A shortest key of each command, in the input order. Any shortest key
is accepted.

## Examples

### Example 1

Input:

```
3
abcm
acm
bcd
```

Output:

```
ab
ac
d
```

## Solution

A substring that starts at position p of a command lies in another
command exactly when it is a prefix of some suffix of that other
command. So at p the shortest key is one letter longer than the
longest common prefix with any suffix of another command, if it fits
before the end of the command.

Sort all suffixes of all commands, at most 10⁵ of them. In sorted
order the common prefix of two suffixes is the minimum of the common
prefixes of neighbours between them. So the largest common prefix with
another command's suffix is reached at the nearest such suffix above
or below. Two sweeps find it. Going down, the running value restarts
at the neighbour's common prefix when the neighbour belongs to another
command, and otherwise takes the minimum with it. Going up works the
same way. The best start of each command then gives its key.
`O(L log L · ℓ)` for L letters in all and commands of length ℓ.

Pitfalls:

- the whole command is always a key, as no command is inside
  another, so every command gets an answer;
- a substring that repeats within its own command can still be a key:
  only other commands count;
- any shortest key is accepted, so the tests use a checker.

The checker verifies that each key belongs to its command, to no other
one, and has the least length. The lengths match an independent
accepted implementation on 200 small random sets and on large ones.

## Optimized solutions

Go packs each suffix position into 32 bits and stores common-prefix lengths in byte arrays. Submission 11317316 used 1728 KB compared with 10568 KB for the simple version.

Rust packs each suffix position into 32 bits and stores common-prefix lengths in byte arrays. Submission 11317319 used 800 KB compared with 5644 KB for the simple version.

Java packs each suffix position into 32 bits and stores common-prefix lengths in byte arrays. Submission 11317320 used 2000 KB compared with 20308 KB for the simple version.

Python packs each suffix and its position into one integer. Each lowercase letter takes five bits. Zero padding puts a shorter suffix first when it is a prefix of another. After discarding the position bits, the highest differing bit identifies the first unequal letter. Python 3.12 x64, submission 11319668. Time 0.546 → 0.328 s, memory 20160 → 12324 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321951 · Python 3.12 x64 №11321948 · Rust 1.75 x64 №11321950 · Go 1.14 x64 №11322285 · Java 1.8 №11322286.

C++ stores suffix positions in 32-bit integers and prefix lengths in bytes. G++ 13.2 x64, submission 11322344. Time 0.062 → 0.062 s, memory 1908 → 676 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1713_strings.cpp](1713_strings.cpp) | G++ 13.2 x64 | strings | O(L log L · ℓ) | AC | 0.062 s | 1908 KB | 11321951 |
| [1713_strings.go](1713_strings.go) | Go 1.14 x64 | strings | O(L log L · ℓ) | AC | 0.14 s | 10568 KB | 11322285 |
| [1713_strings.java](1713_strings.java) | Java 1.8 | strings | O(L log L · ℓ) | AC | 0.296 s | 20308 KB | 11322286 |
| [1713_strings.py](1713_strings.py) | Python 3.12 x64 | strings | O(L log L · ℓ) | AC | 0.546 s | 20160 KB | 11321948 |
| [1713_strings.rs](1713_strings.rs) | Rust 1.75 x64 | strings | O(L log L · ℓ) | AC | 0.078 s | 5644 KB | 11321950 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1713_strings_optimized.go](1713_strings_optimized.go) \* | Go 1.14 x64 | strings | O(L log L · ℓ) | AC | 0.078 s | 1728 KB | 11317316 |
| [1713_strings_optimized.rs](1713_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(L log L · ℓ) | AC | 0.046 s | 800 KB | 11317319 |
| [1713_strings_optimized.java](1713_strings_optimized.java) | Java 1.8 | strings | O(L log L · ℓ) | AC | 0.281 s | 2000 KB | 11317320 |
| [1713_strings_optimized.py](1713_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L log L · ℓ) | AC | 0.328 s | 12324 KB | 11319668 |
| [1713_strings_optimized.cpp](1713_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(L log L · ℓ) | AC | 0.062 s | 676 KB | 11322344 |

\* The Go rating target remains open. The Rust rating target remains open. The saved Python rating has no comparable submissions from other authors.
