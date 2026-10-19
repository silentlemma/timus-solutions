# 1889. Airport Announcements

[Timus 1889](https://acm.timus.ru/problem.aspx?space=1&num=1889) · difficulty 308 · bruteforce

Original problem by Denis Dublennykh, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Igor heard n phrases of an announcement and knows the language of some
of them; the others are "unknown". The announcement was read in several
languages, each at most once and with the same number of phrases in
each. In how many languages could it have been read? List every
possibility in increasing order, or print "Igor is wrong." if there is
none.

## Input

n (2 ≤ n ≤ 1000), then n lines with a language name (4 to 20 lowercase
letters) or "unknown"; at least one phrase is known.

## Output

All possible numbers of languages in increasing order, or
"Igor is wrong.".

## Examples

### Example 1

Input:

```
6
english
unknown
unknown
unknown
german
unknown
```

Output:

```
2 3 6
```

### Example 2

Input:

```
4
english
french
unknown
english
```

Output:

```
Igor is wrong.
```

### Example 3

Input:

```
3
zulu
zulu
zulu
```

Output:

```
1
```

## Solution

If the announcement was read in k languages, k divides n and the
phrases fall into k consecutive blocks of n/k, one block per language.
For every divisor k check two things. The known phrases of a block must
all be in one language. No language may appear in two different blocks.
Blocks without known phrases can take any new language. Hash sets give
expected `O(n·d(n))`; C++'s ordered set gives `O(n·d(n)·log n)`.

In the first example one block would hold both English and German, so 1
fails. For 2 the blocks are "english ? ?" and "? german ?", for 3 they
are pairs with English first and German in the third, and 6 is always
possible here: the answer is 2 3 6.

Pitfalls:

- the same language in two blocks breaks k, as in the third example
  for 3 languages;
- a block of only unknown phrases is fine;
- the output line is "Igor is wrong." with the dot.

The answers agree with an independent accepted implementation on 125
random announcements.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1889_bruteforce.cpp](1889_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n d(n) log n) | AC | 0.015 s | 532 KB |
| [1889_bruteforce.go](1889_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n d(n)) | AC | 0.031 s | 1236 KB |
| [1889_bruteforce.java](1889_bruteforce.java) | Java 1.8 | bruteforce | O(n d(n)) | AC | 0.125 s | 684 KB |
| [1889_bruteforce.py](1889_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n d(n)) | AC | 0.093 s | 476 KB |
| [1889_bruteforce.rs](1889_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n d(n)) | AC | 0.015 s | 452 KB |
