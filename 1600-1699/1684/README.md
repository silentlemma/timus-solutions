# 1684. Jack's Last Word

[Timus 1684](https://acm.timus.ru/problem.aspx?space=1&num=1684) · difficulty 266 · strings

Original problem by Dmitry Ivankov, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a word and a second word, split the second word into pieces that
are each a nonempty prefix of the first, or report that it cannot be
done.

## Input

The two words, one per line, nonempty, lowercase Latin letters, each at
most 75000 long.

## Output

No and, on the next line, the pieces separated by spaces, if a split
exists; otherwise Yes. Any valid split is accepted.

## Examples

### Example 1

Input:

```
abracadabra
abrabracada
```

Output:

```
No
abr abracad a
```

### Example 2

Input:

```
abracadabra
arbadacarba
```

Output:

```
Yes
```

## Solution

Let z[p] be the length of the longest prefix of the first word that
starts at position p of the second one: the Z-function of
word + "#" + last gives all of them in linear time. From a cut at p the
next piece may end at any of p + 1, …, p + z[p], since every shorter
prefix also fits. So the reachable cuts always form a whole range
0, …, reach: sweep p from 0 while p ≤ reach and extend reach to
p + z[p]. Each newly covered cut q remembers the p that covered it,
and walking these links back from the end gives the pieces.

If the sweep stops before the end of the second word, the answer is
Yes. `O(m + n)` for words of lengths m and n.

Pitfalls:

- taking the longest prefix every time can fail: for aab and aaab the
  greedy aa leaves ab, while a + aab works (test 06);
- the answer words are inverted: No means a split exists;
- the output line holds up to 75000 pieces, so build it at once.

The checker verifies the verdict against an independent accepted
implementation, and that the pieces are prefixes that spell the word.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1684_strings.cpp](1684_strings.cpp) | G++ 13.2 x64 | strings | O(m + n) | AC | 0.031 s | 6108 KB |
| [1684_strings.go](1684_strings.go) | Go 1.14 x64 | strings | O(m + n) | AC | 0.031 s | 7368 KB |
| [1684_strings.java](1684_strings.java) | Java 1.8 | strings | O(m + n) | AC | 0.140 s | 8584 KB |
| [1684_strings.py](1684_strings.py) | Python 3.12 x64 | strings | O(m + n) | AC | 0.265 s | 7024 KB |
| [1684_strings.rs](1684_strings.rs) | Rust 1.75 x64 | strings | O(m + n) | AC | 0.062 s | 5168 KB |
