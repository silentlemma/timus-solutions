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

## Checking

Check that the reported pieces concatenate to the text and each is a prefix of the pattern; accept any valid decomposition and verify impossibility answers.

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

## Optimized solutions

The new algorithm uses prefix-function matching and a backward longest-suffix greedy, rather than the simple Z-function and forward reachable cuts. The dictionary consists of prefixes: extending the final piece leftwards can only truncate an earlier valid prefix, so choosing the longest possible last piece is safe. Record the matched length at each text endpoint, reconstruct cuts backwards and stream original slices. Packed links and lengths replace the combined Z buffer and copied output pieces.

- `1684_greedy_strings.cpp`: 0.015 s / 836 KB; base `1684_strings.cpp`: 0.015 s / 6084 KB; relative change: time -0.0%, memory -86.3%.
- `1684_greedy_strings.go`: 0.015 s / 2068 KB; base `1684_strings.go`: 0.031 s / 7368 KB; relative change: time -51.6%, memory -71.9%.
- `1684_greedy_strings.java`: 0.109 s / 1248 KB; base `1684_strings.java`: 0.140 s / 8584 KB; relative change: time -22.1%, memory -85.5%.
- `1684_greedy_strings.py`: 0.156 s / 1692 KB; base `1684_strings.py`: 0.250 s / 7360 KB; relative change: time -37.6%, memory -77.0%.
- `1684_greedy_strings.rs`: 0.015 s / 1288 KB; base `1684_strings.rs`: 0.031 s / 4176 KB; relative change: time -51.6%, memory -69.2%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1684_strings.cpp`; covering source `1684_greedy_strings.cpp`; time/memory places 1/1, other-author entries 67/67.

- Go: preferred teaching base `1684_strings.go`; covering source `1684_strings.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1684_strings.java`; covering source `1684_greedy_strings.java`; time/memory places 1/1, other-author entries 6/6.

- Python/PyPy: preferred teaching base `1684_strings.py`; covering source `1684_greedy_strings.py`; time/memory places 6/1, other-author entries 30/30.

- Rust: preferred teaching base `1684_strings.rs`; covering source `1684_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1684_strings.cpp](1684_strings.cpp) | G++ 13.2 x64 | strings | O(m + n) | AC | 0.015 s | 6084 KB | 11308841 |
| [1684_strings.go](1684_strings.go) | Go 1.14 x64 | strings | O(m + n) | AC | 0.031 s | 7368 KB | 11288854 |
| [1684_strings.java](1684_strings.java) | Java 1.8 | strings | O(m + n) | AC | 0.140 s | 8584 KB | 11288857 |
| [1684_strings.py](1684_strings.py) | Python 3.12 x64 | strings | O(m + n) | AC | 0.250 s | 7360 KB | 11309202 |
| [1684_strings.rs](1684_strings.rs) | Rust 1.75 x64 | strings | O(m + n) | AC | 0.031 s | 4176 KB | 11309203 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1684_greedy_strings.cpp](1684_greedy_strings.cpp) | G++ 13.2 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 836 KB | 11309270 |
| [1684_greedy_strings.go](1684_greedy_strings.go) | Go 1.14 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 2068 KB | 11309272 |
| [1684_greedy_strings.java](1684_greedy_strings.java) | Java 1.8 | greedy, strings | O(pattern length + text length) | AC | 0.109 s | 1248 KB | 11309271 |
| [1684_greedy_strings.py](1684_greedy_strings.py) \* | Python 3.12 x64 | greedy, strings | O(pattern length + text length) | AC | 0.156 s | 1692 KB | 11309268 |
| [1684_greedy_strings.rs](1684_greedy_strings.rs) | Rust 1.75 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 1288 KB | 11309273 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
