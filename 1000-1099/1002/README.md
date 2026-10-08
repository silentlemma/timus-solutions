# 1002. Spelling a number with the fewest words

[Timus 1002](https://acm.timus.ru/problem.aspx?space=1&num=1002) · difficulty 226 · dp, hashing

Original problem from the Central European Olympiad in Informatics 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every lowercase Latin letter stands for one digit:

| Digit | Letters |
|-------|---------|
| 1 | i j |
| 2 | a b c |
| 3 | d e f |
| 4 | g h |
| 5 | k l |
| 6 | m n |
| 7 | p r s |
| 8 | t u v |
| 9 | w x y |
| 0 | o q z |

A word spells the string of digits of its letters. Given a number (a string of
at most 100 digits) and a dictionary of `n ≤ 50 000` words, find a sequence of
dictionary words with the fewest words whose spellings, concatenated, give the
number. A word may be used any number of times.

The input holds several such tests; its total size is at most 300 KB.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Tests one after another. A test is a line with the number, a line with `n`,
and `n` lines with one word each (1 to 50 lowercase letters). A line `-1`
ends the input.

## Output

For every test, one line: the words of a shortest sequence separated by single
spaces, or `No solution.` if the number cannot be spelled.

## Checking

Any shortest sequence is accepted: the checker verifies that the words are in
the dictionary, that they spell the number, and that no shorter sequence
exists.

## Examples

### Example 1

Input:

```
8733
3
use
e
tree
12
2
ab
cd
-1
```

Output:

```
tree
No solution.
```

### Example 2

Input:

```
22
4
ac
ba
b
c
-1
```

Output:

```
ac
```

## Solution

Dynamic programming over prefixes of the number: `best[i]` is the fewest words
spelling the first `i` digits, `best[0] = 0`. From every reachable `i` try each
word that spells a substring starting at `i`, and remember the last word to
restore the answer.

Trying all `n` words at every position costs `O(100 · n · 50)` per test. It is
much faster to put the dictionary into a hash map from spelling to word: a word
is at most 50 letters long, so at each position only the substrings of length
1 to 50 have to be looked up. That is `O(100 · 50)` lookups per test plus
`O(total length of the words)` to build the map, fast in every language.

Pitfalls:

- several words may have the same spelling: keeping any one of them is enough;
- a word can be used many times;
- the output must be exactly `No solution.` when there is no answer.

## Language notes

- **C++**: `std::unordered_map<std::string, int>`; read with `cin` after
  `sync_with_stdio(false)`.
- **Go**: `map[string]int`, where `phone[i:i+l]` is a cheap substring.
- **Python**: the map is a `dict` and spellings come from `str.translate`; the
  lookup-based version is fast, while comparing every word at every position
  would be too slow.
- **Java**: `HashMap<String, Integer>` with `putIfAbsent`; input through
  `BufferedReader` and `StringTokenizer`.
- **Rust**: `HashMap<Vec<u8>, usize>` looked up with byte slices of the number.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1002_dp_hashing.cpp](1002_dp_hashing.cpp) | G++ 13.2 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.015 s | 2764 KB |
| [1002_dp_hashing.go](1002_dp_hashing.go) | Go 1.14 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.031 s | 3016 KB |
| [1002_dp_hashing.java](1002_dp_hashing.java) | Java 1.8 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.109 s | 7032 KB |
| [1002_dp_hashing.py](1002_dp_hashing.py) | Python 3.12 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.093 s | 5424 KB |
| [1002_dp_hashing.rs](1002_dp_hashing.rs) | Rust 1.75 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.031 s | 2540 KB |
