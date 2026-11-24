# 1158. Counting the sentences of length M that avoid every forbidden word

[Timus 1158](https://acm.timus.ru/problem.aspx?space=1&num=1158) · difficulty 500 · strings

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An alphabet has `N ≤ 50` letters, and a sentence is any string of exactly
`M ≤ 50` letters. `P ≤ 10` forbidden words of at most 10 letters are
given; a sentence is forbidden if it contains one of them as a substring.
Count the sentences that are not forbidden. Letters can be any characters
with codes above 32, including codes above 127.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, `M` and `P`, then the `N` letters on one line, then the `P` words.

## Output

The number of allowed sentences.

## Examples

### Example 1

Input:

```
3 3 3
QWE
QQ
WEE
Q
```

Output:

```
7
```

## Solution

Build the Aho–Corasick automaton of the forbidden words: a trie with
failure links, completed so that every state has a transition for every
letter. A state stands for the longest end of the text so far that is a
prefix of some word; it is bad if a word ends there, directly or through
its failure links. A sentence is allowed exactly when reading it never
enters a bad state.

So count paths: `ways[s]` is the number of allowed beginnings of the
current length that end in state `s`. Start with one empty beginning at
the root and apply `M` steps, each sending `ways[s]` along all `N`
transitions that do not enter a bad state. The answer is the sum over all
states. With `S ≤ 101` states, this takes `O(M·S·N)` additions, about 5000
per step.

Pitfalls:

- the count can reach `50⁵⁰ ≈ 8.9·10⁸⁴`, so big integers are needed;
- a word containing another word is bad already at the shorter one, which
  the failure links carry over;
- letters are arbitrary bytes, possibly above 127, so the input is read
  as bytes and not decoded as text;
- the same word may be given twice.

The answers were compared with listing every sentence on 200 small random
inputs; the tests store letters above 127 as Latin-1 characters in
UTF-8, and the runner hands them to the solutions as single bytes.

The teaching Python version stores each state as a proper prefix of a forbidden word. After appending a letter, discard the transition if a forbidden word is a suffix. Otherwise take the longest suffix among the stored prefixes, including the empty prefix. Any shorter prefix that can finish a word is already a suffix of the current state, so these direct checks give the same transitions as the failure links. With P forbidden words and maximum word length L, building the table takes O(SN(P+S)L) time. Counting uses O(MSN) additions.

## Optimized solutions

Go and Rust retain Aho–Corasick and exact counting. At most 1+10·10=101 states and 50 letters allow byte transition IDs and a fixed BFS queue. Propagate forbidden suffixes first, finish every failure transition, then group safe letters with the same destination into one edge with multiplicity. Two reused DP layers add count·multiplicity per edge. Each count is at most 50⁵⁰<10⁸⁵, so ten base-10⁹ limbs are exact; a limb product with multiplicity≤50 fits uint64. Zero counts and inherited forbidden suffixes are retained. Codes above 127 are read as alphabet bytes. Let W be the total length of the forbidden words, S the number of states, N the alphabet size, E the number of grouped edges and D≤10 the limb count. Building and grouping takes O(W+S(S+N)) time because each row scans the target counts. Clearing, checking and updating the DP layers takes O(M(S+E)D) time. Storage is O(SN+SD) with fixed I/O blocks. C++, Java and Python use their admitted bases.

The accepted base implementations [1158_strings.cpp](1158_strings.cpp), [1158_strings.java](1158_strings.java), [1158_strings.py](1158_strings.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

Original Go/Python/Java use arbitrary-precision integers; original C++/Rust use dynamic nine-digit limbs. New Go/Rust use two fixed ten-limb layers and byte automata, preserving raw Latin-1 alphabet bytes. No modular arithmetic or answer lookup is used.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1158_strings.cpp](1158_strings.cpp) | G++ 13.2 x64 | strings | O(M·S·N) | AC | 0.015 s | 472 KB | 11281469 |
| [1158_strings.go](1158_strings.go) | Go 1.14 x64 | strings | O(M·S·N) | AC | 0.031 s | 1684 KB | 11281489 |
| [1158_strings.java](1158_strings.java) \* | Java 1.8 | strings | O(M·S·N) | AC | 0.109 s | 5476 KB | 11281536 |
| [1158_strings.py](1158_strings.py) \* | Python 3.12 x64 | strings | O(M·S·N) | AC | 0.093 s | 768 KB | 11281520 |
| [1158_strings.rs](1158_strings.rs) | Rust 1.75 x64 | strings | O(M·S·N) | AC | 0.031 s | 340 KB | 11281554 |
| [1158_dp_strings.py](1158_dp_strings.py) | Python 3.12 x64 | dp, strings | O(SN(P+S)L + MSN) | AC | 0.156 s | 584 KB | 11315835 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1158_strings_optimized.go](1158_strings_optimized.go) | Go 1.14 x64 | strings | O(W + S(S+N) + M(S+E)D) | AC | 0.015 s | 812 KB | 11315420 |
| [1158_strings_optimized.rs](1158_strings_optimized.rs) | Rust 1.75 x64 | strings | O(W + S(S+N) + M(S+E)D) | AC | 0.031 s | 204 KB | 11315424 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
