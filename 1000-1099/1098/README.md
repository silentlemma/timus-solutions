# 1098. The last character left by counting out every 1999th

[Timus 1098](https://acm.timus.ru/problem.aspx?space=1&num=1098) · difficulty 555 · math

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

Deleting characters one by one from a string would cost `O(L²)` with
`L = 30000`: fast enough in a compiled language, but the recurrence
avoids it altogether.

Pitfalls:

- every character except the line breaks counts, including spaces at the
  ends of lines and between words, so the input is read as raw bytes and
  only `\n` and `\r` are dropped;
- the question may consist of a single character, and then that
  character is the answer.

The answers were checked against a direct simulation that deletes every
1999th character from a list.

## Language notes

- Rust folds the recurrence over `2..=L`.
- Java and C++ read the input byte by byte, which keeps every space.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1098_math.cpp](1098_math.cpp) | G++ 13.2 x64 | math | O(L) | AC | 0.001 s | 188 KB |
| [1098_math.go](1098_math.go) | Go 1.14 x64 | math | O(L) | AC | 0.015 s | 1300 KB |
| [1098_math.java](1098_math.java) | Java 1.8 | math | O(L) | AC | 0.093 s | 496 KB |
| [1098_math.py](1098_math.py) | Python 3.12 x64 | math | O(L) | AC | 0.062 s | 496 KB |
| [1098_math.rs](1098_math.rs) | Rust 1.75 x64 | math | O(L) | AC | 0.015 s | 236 KB |
