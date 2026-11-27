# 1098. The last character left by counting out every 1999th

[Timus 1098](https://acm.timus.ru/problem.aspx?space=1&num=1098) · difficulty 557 · math

Original problem by Stanislav Vasiliev, from the trial round of the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The question is the whole input with the line breaks removed (at least
one and at most 30000 characters; spaces and punctuation count). Starting
from the first character, count `N − 1` characters and delete the `N`-th,
going round to the beginning when the end is reached; then count again
from the character after the deleted one, until one character is left,
with `N = 1999`. Print `Yes` if it is `?`, `No` if it is a space, and
`No comments` otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The question, possibly on several lines.

## Output

`Yes`, `No` or `No comments`.

## Checking

The output is compared line by line; within a line, token by token.

## Examples

### Example 1

Input:

```
Does the jury of this programming contest use the
algorithm described in this problem to answer my questions?
```

Output:

```
Yes
```

### Example 2

Input:

```
At least, will anybody READ my question?
```

Output:

```
No
```

### Example 3

Input:

```
This is
UNFAIR!
```

Output:

```
No comments
```

## Solution

This is the Josephus problem. Let `J(m)` be the position, counted from
where the counting starts, of the last one left among `m` characters.
After the first deletion `m − 1` characters remain and the counting
starts `N` places further on, so `J(m) = (J(m − 1) + N) mod m` with
`J(1) = 0`. One pass up to the length of the question gives the position,
and only the character there matters. `O(L)`.

Let L be the length after removing line endings and I the raw bytes
read, including those endings. Recurrence arithmetic uses O(1) state
and O(L) time. Simple C++/Java retain O(L) text; simple Go/Python/Rust
can retain O(I+L) raw/filtered storage. Thus full reading plus recurrence
takes O(I+L), even when many line endings are removed. Optimized Python
keeps O(I+L) transient byte strings. Go/Rust bitsets reserve two arrays
of ceil(MAX_LENGTH/8) bytes each, with MAX_LENGTH=30000, plus bounded I/O.

The five simple 1098_math sources now clarify only the Josephus index
origin: zero-based from the original counting start, with the modulo
translation after deletion. Their table IDs and paired measurements
belong to the preceding comment revisions: C++ #11321759, Go #11322213,
Java #11321761, Python #11322214 and Rust #11322215. Algorithms,
all meaningful simple implementations and comments are preserved.

Deleting characters one by one from a string would cost `O(L²)` with
`L = 30000`: fast enough in a compiled language, but the recurrence
avoids it altogether.

Pitfalls:

- every character except the line breaks counts, including spaces at the
  ends of lines and between words, so the input is read as raw bytes and
  only `\n` and `\r` are dropped;
- the question may consist of a single character, and then that
  character determines the answer.

The answers were checked against a direct simulation that deletes every
1999th character from a list.

## Language notes

- Rust folds the recurrence over `2..=L`.
- Java and C++ read the input byte by byte, which keeps every space.

## Optimized solutions

The Python variant removes carriage returns and line feeds with two byte-string operations.
The filtered string gives both the length for the Josephus recurrence and the final byte, so
the code no longer scans the input again in Python. Submission 11316943 used 348 KB versus
500 KB for the base version and took 0.078 s versus 0.078 s.

Go stores question marks and spaces in separate bit sets and skips line endings during input. The Josephus recurrence gives the final position, whose two bits determine the answer. Submission 11317592 took 0.015 s and used 900 KB, compared with 0.015 s and 1304 KB for the simple version.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321759 · Go 1.14 x64 №11322213 · Java 1.8 №11321761 · Python 3.12 x64 №11322214 · Rust 1.75 x64 №11322215.

Rust stores two bitsets for question marks and spaces and resumes the Josephus recurrence from a precomputed checkpoint. Rust 1.75 x64, submission 11323266. Time 0.015 → 0.015 s, memory 224 → 56 KB.

Rust still scans all I raw bytes. STRIDE=128 checkpoints reduce only
the recurrence tail to at most 127 updates, so total runtime is
O(I+STRIDE), not O(N) in the fixed deletion step N=1999. The compile-time
checkpoint construction takes O(MAX_LENGTH) work and stores
O(MAX_LENGTH/STRIDE) u16 values, separate from the two classification
bitsets. Input scanning remains linear despite this recurrence shortcut.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1098_math.cpp](1098_math.cpp) | G++ 13.2 x64 | math | O(I + L) time | AC | 0.015 s | 176 KB | 11331154 |
| [1098_math.go](1098_math.go) | Go 1.14 x64 | math | O(I + L) time | AC | 0.031 s | 1304 KB | 11331035 |
| [1098_math.java](1098_math.java) | Java 1.8 | math | O(I + L) time | AC | 0.093 s | 484 KB | 11331057 |
| [1098_math.py](1098_math.py) | Python 3.12 x64 | math | O(I + L) time | AC | 0.093 s | 328 KB | 11331090 |
| [1098_math.rs](1098_math.rs) | Rust 1.75 x64 | math | O(I + L) time | AC | 0.015 s | 224 KB | 11331132 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1098_math_optimized.py](1098_math_optimized.py) | Python 3.12 x64 | math | O(I + L) time | AC | 0.078 s | 348 KB | 11316943 |
| [1098_math_optimized.go](1098_math_optimized.go) | Go 1.14 x64 | math | O(I + L) time | AC | 0.015 s | 900 KB | 11317592 |
| [1098_math_optimized.rs](1098_math_optimized.rs) | Rust 1.75 x64 | math | O(I + STRIDE) time | AC | 0.015 s | 56 KB | 11323266 |
