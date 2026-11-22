# 1960. Distinct Palindromes in Every Prefix

[Timus 1960](https://acm.timus.ru/problem.aspx?space=1&num=1960) · difficulty 434 · strings

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Grigory Nazarov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every nonempty prefix of a word, count its distinct nonempty contiguous
substrings that are palindromes. Equal substring values count once even
if they occur many times. A palindrome equals its reversal.
Limits: 1 second, 64 MB.

## Input

One word of n lowercase English letters, 1≤n≤100000. There is no separate
length token.

## Output

n integers separated by spaces: the count for prefix lengths 1 through n.
The empty palindrome is excluded. Counts refer to distinct strings,
not occurrences or the length of a longest palindrome.

## Checking

Outputs are compared token by token.

## Examples

```
aba
```

```
1 2 3
```

## Solution

For the sample, `a` contains only `a`; `ab` contains `a,b`; `aba` adds `aba`. The prefix counts are therefore 1,2,3.

### At most one new palindrome

After appending c, every newly occurring substring ends at c. Let P be
the longest palindromic suffix of the new prefix. Any shorter palindromic
suffix Q is also a proper prefix of P, so Q already occurred ending before
c. Therefore only P can be new. Every append adds zero or one distinct
palindrome, and the total number is at most n.

### Palindromic tree

Use the standard eertree; see [Rubinchik–Shur, 2015](https://arxiv.org/abs/1506.04862).
A real node
represents one palindrome and stores its length, suffix link to the longest
proper palindromic suffix, and transitions by wrapping letters: Q→cQc.
Two artificial roots have lengths −1 and 0, indices 0 and 1. Both root
links lead to index 0. A length-one palindrome links to the empty root.
Each nonempty palindrome has a unique inner palindrome and wrapping letter,
so it has one unique incoming transition.

Keep last, the longest palindromic suffix before the next append. Follow
suffix links until the character preceding the candidate equals c.
For a root of length −1 that comparison is with the new character itself,
so the search always stops. The longest extendable candidate Q yields the
new longest suffix P=cQc. If its c-transition exists, reuse that node;
otherwise create one with length |Q|+2.

For a new length-one node set its link to the empty root. Otherwise start
at link[Q], search for the next extendable suffix in the same way, and
follow its existing c-transition. This is the longest proper palindromic
suffix of P. Its node already exists because it is a proper prefix of P
as well, hence occurred before this append. Set last to P's node and
output the number of real nodes, total_nodes−2.

### Correctness and complexity

Suffix links enumerate palindromic suffixes in decreasing length, so the
first extendable one gives exactly the longest new suffix. The node key
(inner palindrome, letter) uniquely identifies that palindrome. A missing
transition is equivalent to a new distinct value; all other suffix
palindromes are already known by the first lemma. Induction therefore
maintains exactly all distinct palindromes of every prefix.

Both suffix-link walks have linear total work. For the first walk, let
ℓ_old and ℓ_new be the old/new longest-suffix lengths. Each failed link
decreases length, and wrapping increases it by two, so the failed steps
are at most ℓ_old−ℓ_new+2. These bounds telescope over the whole word.
For the second walk, use q_old,q_new, the lengths of the longest proper
suffix of last. It starts at a length ≤q_old and ends at q_new−2; its
bound q_old−q_new+2 telescopes too. On appends without a new node, no second
walk occurs and q_new≤q_old+2 still holds.

Native versions use dense transitions over 26 letters: `O(26n)` time for
initialization and `O(26n)` memory, both `O(n)` for this fixed alphabet. Python
uses a sparse dictionary with the exact key parent*26+letter_code, so
expected `O(n)` time and `O(n)` memory. This is an injective integer key,
not a probabilistic substring fingerprint. There are at most n+2 nodes.

Do not count the two roots, add occurrence counts, omit even palindromes,
or assume every append increases the answer: `abca` ends with count 3.
Test the left boundary before indexing; Python negative indices would
otherwise silently access the wrong character. Long words require the
tree rather than enumerating their quadratic number of occurrences.

## Optimized solutions

The C++ revision keeps the sparse eertree, suffix links and child-list transitions. A fixed 16 KB output buffer writes the count for every prefix instead of printf per character. It still stores no answer vector; time is O(26n), linear for the fixed alphabet.

Exact-source Accepted (G++ 13.2 x64, #11326638: 0.031 s / 2164 KB); teaching base `1960_strings.cpp`: 0.031 s / 11464 KB. The previous optimized measurement was 0.046 s / 2160 KB. In the saved 20 November 2026 comparison, time place is 9/83, memory place 1/83; below 1 MiB the policy evaluates the time rank only.

The Java teaching source keeps its dense-transition eertree and changes only indentation. The formatting revalidation is its own Accepted #11327083: 0.14 s / 15240 KB. Those paired figures replace the former Java row; the algorithm is unchanged.

The new C++, Go and Rust eertrees retain lengths, suffix links and the two roots, but store only existing transitions. Every nonempty palindrome has one unique inner palindrome and wrapping letter, hence one incoming edge. Store that edge’s letter and next-sibling index in the child node itself, and a first-child index in the parent. Transition lookup scans at most 26 children. The original suffix-link argument is unchanged, so time is O(26n), linear for this alphabet. A node has four 32-bit fields and one byte instead of 26 native-index slots. Node identifiers are at most 100001; lengths range from −1 to 100000. Counts are emitted as prefixes are processed, without a separate answer vector. All dense simple versions remain; Java and Python reuse admitted bases in the fast set.

The accepted base implementations [1960_strings.java](1960_strings.java), [1960_strings.py](1960_strings.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

C++ uses arrays inside nodes. Go 1.14 and Rust 1.75 use native integer
indices; Java 8 uses one flat int transition array to avoid per-node
objects. Python uses bytes and sparse packed keys, keeping memory below
the limit. Rust uses only the standard library. CPython is selected by
resource measurements.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1960_strings.cpp](1960_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 11464 KB | 11292170 |
| [1960_strings.go](1960_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.062 s | 26104 KB | 11292171 |
| [1960_strings.java](1960_strings.java) | Java 1.8 | strings | O(n) | AC | 0.14 s | 15240 KB | 11327083 |
| [1960_strings.py](1960_strings.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.296 s | 23012 KB | 11292174 |
| [1960_strings.rs](1960_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 22956 KB | 11292176 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1960_strings_optimized.cpp](1960_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(26n) | AC | 0.031 s | 2164 KB | 11326638 |
| [1960_strings_optimized.go](1960_strings_optimized.go) \* | Go 1.14 x64 | strings | O(26n) | AC | 0.031 s | 2452 KB | 11315115 |
| [1960_strings_optimized.rs](1960_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(26n) | AC | 0.031 s | 2292 KB | 11315106 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
