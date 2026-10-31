# 1102. Splitting a line into the words of a strange dialogue

[Timus 1102](https://acm.timus.ru/problem.aspx?space=1&num=1102) · difficulty 176 · strings

Original problem by Katya Ovechkina, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dialogue is any sequence of the words `out`, `output`, `puton`, `in`,
`input` and `one`, written without spaces. For each of `N` lines
(`N ≤ 1000`, lowercase letters, `≤ 4 · 10^6` letters in all) print `YES` if
it is a dialogue and `NO` otherwise.

Time limit: 1 second. Memory limit: 16 MB.

## Input

`N` (`1 ≤ N ≤ 1000`), then `N` nonempty lines of lowercase Latin
letters.

## Output

`YES` or `NO` for each line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
puton
inonputin
oneputonininputoutoutput
oneininputwooutoutput
outpu
utput
```

Output:

```
YES
NO
YES
NO
NO
NO
```

## Solution

Read forwards, the words overlap badly: `out` starts `output`, `in`
starts `input`, and `output` + `one` reads like `out` + `puton` + `e`.
Read backwards, they become `tuo`, `tuptuo`, `notup`, `ni`, `tupni` and
`eno`, and none of these is the beginning of another. So at every point
at most one word can end there, and cutting the line greedily from its
end, one word at a time, either uses up the whole line or proves that no
split exists. `O(L)` for `L` letters.

Pitfalls:

- a forward greedy that always takes the longest word fails: `outputon`
  is `out` + `puton`, but taking `output` first leaves `on`;
- the lines are long and the memory limit is only 16 MB, so copies of the
  whole input must be avoided.

The answers were checked against a forward dynamic programming over
prefixes, on every dialogue of up to three words, on near misses and on
random spoiled lines.

## Optimized solutions

The optimized C++ solution recognises dialogues with a finite automaton
instead of cutting words from the end. The six words, 24 letters in all,
form a trie of at most 25 nodes, so a set of trie nodes fits in a 32-bit
mask. A state is the set of nodes reached by the words that are being
read, where the root also means that the prefix read so far splits into
whole words; the few such sets reachable from the root are found once at
the start and get a transition table. Each letter then costs one table
lookup, the line is never stored, and the answer is `YES` when the root
is in the set at the end of the line. Instead of reading a line of up to
four million letters into a `string` with `cin`, the input is read in
4 KB blocks: {1102_parsing.cpp}.

The optimized Go solution recognises dialogues with a finite automaton
instead of cutting words from the end. The six words, 24 letters in all,
form a trie of at most 25 nodes, so a set of trie nodes fits in a 32-bit
mask. A state is the set of nodes reached by the words that are being
read, where the root also means that the prefix read so far splits into
whole words; the few such sets reachable from the root are found once at
the start and get a transition table. Each letter then costs one table
lookup read straight from the buffered reader, the line is never stored
as a string, and the answer is `YES` when the root is in the set at the
end of the line: {1102_parsing.go}.

The optimized Java solution with dynamic programming reads the input
byte by byte from a buffered stream and goes forward along the line:
`good[i]` says whether the first `i` letters split into words, and it is
true when one of the six words ends at letter `i` and `good` holds just
before that word. A word has at most six letters, so only the last seven
letters and values are kept in a ring, and the line is never stored,
while the simple Java solution reads each line into an array of four
million characters: {1102_dp.java}.

The optimized Java solution with an automaton recognises dialogues with
a finite automaton instead of cutting words from the end. The six words,
24 letters in all, form a trie of at most 25 nodes, so a set of trie
nodes fits in a 32-bit mask. A state is the set of nodes reached by the
words that are being read, where the root also means that the prefix
read so far splits into whole words; the few such sets reachable from
the root are found once at the start and get a transition table. Each
byte, read from 4 KB blocks, then costs one table lookup, and the answer
is `YES` when the root is in the set at the end of the line. The line is
never stored, while the simple Java solution reads each line into an
array of four million characters: {1102_parsing.java}.

The optimized Rust solution recognises dialogues with a finite automaton
instead of cutting words from the end. The six words, 24 letters in all,
form a trie of at most 25 nodes, so a set of trie nodes fits in a 32-bit
mask. A state is the set of nodes reached by the words that are being
read, where the root also means that the prefix read so far splits into
whole words; the few such sets reachable from the root are found once at
the start and get a transition table. Each letter then costs one table
lookup made straight on the blocks of the input buffer, and the answer
is `YES` when the root is in the set at the end of the line. No line is
copied into a vector of its own: {1102_parsing.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1102_parsing.cpp`: time reduction +80.13%; memory reduction +97.50%;
  base: `1102_strings.cpp`.

- `1102_parsing.go`: time reduction +41.03%; memory reduction +90.39%;
  base: `1102_strings.go`.

- `1102_dp.java`: time reduction -68.40%; memory reduction +94.84%;
  base: `1102_strings.java`.

- `1102_parsing.java`: time reduction +50.00%; memory reduction +90.40%;
  base: `1102_strings.java`.

- `1102_parsing.rs`: time reduction -106.67%; memory reduction +94.23%;
  base: `1102_strings.rs`.

## Language notes

- Python matches the reversed line with the regular expression
  `(?:tuo|tuptuo|notup|ni|tupni|eno)*+`; the possessive `*+` keeps no
  states to backtrack to, which is safe because the split is unique.
- Java reads each line character by character into one `char` array
  sized for the four million letters of the whole input, 8 MB:
  `readLine` would also make temporary copies of a long line, and they
  do not fit in 16 MB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1102_strings.cpp](1102_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.156 s | 5768 KB | 11279162 |
| [1102_strings.go](1102_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.078 s | 11448 KB | 11279163 |
| [1102_strings.java](1102_strings.java) | Java 1.8 | strings | O(L) | AC | 0.250 s | 8372 KB | 11307280 |
| [1102_strings.py](1102_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.140 s | 8328 KB | 11279164 |
| [1102_strings.rs](1102_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 7760 KB | 11279166 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1102_parsing.cpp](1102_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.031 s | 144 KB | 11307270 |
| [1102_parsing.go](1102_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1100 KB | 11307275 |
| [1102_dp.java](1102_dp.java) \* | Java 1.8 | dp | O(L) | AC | 0.421 s | 432 KB | 11307279 |
| [1102_parsing.java](1102_parsing.java) \* | Java 1.8 | parsing | O(L) | AC | 0.125 s | 804 KB | 11307272 |
| [1102_parsing.rs](1102_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.031 s | 448 KB | 11307277 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
