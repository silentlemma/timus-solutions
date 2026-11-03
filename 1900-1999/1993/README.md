# 1993. Reorder marked phrases and fix capitalization

[Timus 1993](https://acm.timus.ru/problem.aspx?space=1&num=1993) · difficulty 204 · parsing, strings

Original problem by Denis Dublennykh, prepared by Eugene Kurpilyansky.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Rearrange a marked sentence. Every simple clause contains exactly one
object in `{braces}`, one subject in `(round brackets)` and one verb
phrase in `[square brackets]`, in arbitrary order. Each marked phrase
contains one or more words. The sentence has one clause, or two
separated by one comma. An optional single-word conjunction immediately
after the comma is unmarked; it is the only possible word outside the
brackets.

Put each clause in object–subject–verb order, remove brackets and keep
every phrase's internal word order. Preserve the conjunction before the
second reordered clause. Only the first letter of the first output word
is uppercase; all other letters are lowercase, including after the
comma.

Input length is at most 100 characters. Words contain only Latin
letters. Initially only the first letter of the first input word is
uppercase. Brackets do not nest and occur at word boundaries. Words have
exactly one separating space, with no space before commas/closing
brackets or after opening brackets. Time limit: 1 second; memory limit:
64 MB.

## Input

One complete line containing the marked sentence.

## Output

One line with the reordered sentence. Use single spaces between words,
no space before the comma and one after it. Do not add punctuation.

## Checking

Output is compared character by character, allowing only the final line ending to differ.

- `1993_parsing_optimized.cpp` (G++ 13.2 x64): 102 repository cases; 112 additional source-bound comparisons.

- `1993_parsing_optimized.go` (Go 1.14 x64): 102 repository cases; 102 additional source-bound comparisons.

- `1993_parsing_strings.py` (PyPy 3.10 x64): 102 repository cases.

## Examples

Input:

```
(We) [are] {blind}, if (we) [could not see] {creation of this clone army}
```

Output:

```
Blind we are, if creation of this clone army we could not see
```

Input:

```
{Truly wonderful} (the mind of a child) [is]
```

Output:

```
Truly wonderful the mind of a child is
```

## Solution

First lowercase the whole input. This removes the old initial capital,
which may move into the middle of the result. Split at the comma; a
comma cannot occur inside a phrase because phrases contain only words.

Scan each clause from left to right. On `{`, `(` or `[`, find its
matching closing bracket, save the interior text in the corresponding
object, subject or verb slot, and advance beyond the group. On an
outside letter, read the unmarked conjunction. Skip spaces. Then join
the conjunction, if present, and the three slots in object–subject–verb
order. Join the clauses with `, ` and uppercase only the first character
of the final result.

Each group is nonnested, so the matching closing bracket ends exactly
that phrase. Its bracket type identifies its role uniquely; there is
exactly one slot of each role per clause. Saving the interior preserves
every word and its internal order. The scan skips entire groups, so the
only letters read outside them are precisely the optional conjunction.

Serialization emits each stored phrase once in the required order and
leaves the conjunction at the start of the second clause. The comma
still separates the same clauses. Lowercasing first and capitalizing
only the final first character ensures that the moved old first word
loses its capital when necessary and that the new first word gains one.
Thus the result has exactly the required words, order, punctuation and
case.

In the first example, the first object becomes the initial word and the
conjunction stays after the comma. In the second, the object is already
first, so its internal word order is unchanged.

## Optimized solutions

Retain the same role-based parsing proof. Compact C++/Go keep spans in one bounded ASCII input buffer instead of copying phrases or building stream/string objects. Scan over each complete bracketed group, recording object, subject and verb positions; an unbracketed word is the optional second-clause conjunction. Emit conjunction and the three roles in order, insert the original comma separator, lowercase all letters and capitalize only the first output letter. Groups are nonnested and roles unique, so every phrase is emitted exactly once with its internal word order unchanged. Python uses slices and existing text streams. With input length L<=100, both time and storage are O(L).

- `1993_parsing_optimized.cpp`: 0.015 s / 76 KB; base `1993_parsing.cpp`: 0.015 s / 388 KB; relative change: time -0.0%, memory -80.4%.
- `1993_parsing_optimized.go`: 0.015 s / 272 KB; base `1993_parsing.go`: 0.031 s / 1184 KB; relative change: time -51.6%, memory -77.0%.
- `1993_parsing_strings.py`: 0.156 s / 300 KB; base `1993_parsing.py`: 0.062 s / 504 KB; relative change: time +151.6%, memory -40.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1993_parsing.cpp`; covering source `1993_parsing_optimized.cpp`; time/memory places 1/1, other-author entries 63/63.

- Go: preferred teaching base `1993_parsing.go`; covering source `1993_parsing_optimized.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `1993_parsing.java`; covering source `1993_parsing.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1993_parsing.py`; covering source `1993_parsing_strings.py`; time/memory places 13/4, other-author entries 12/12.

- Rust: preferred teaching base `1993_parsing.rs`; covering source `1993_parsing.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1993_parsing.cpp](1993_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 388 KB | 11292395 |
| [1993_parsing.go](1993_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1184 KB | 11292397 |
| [1993_parsing.java](1993_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.109 s | 472 KB | 11309216 |
| [1993_parsing.py](1993_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.062 s | 504 KB | 11292399 |
| [1993_parsing.rs](1993_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 224 KB | 11292401 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1993_parsing_optimized.cpp](1993_parsing_optimized.cpp) | G++ 13.2 x64 | parsing | O(L) time and space | AC | 0.015 s | 76 KB | 11308436 |
| [1993_parsing_optimized.go](1993_parsing_optimized.go) | Go 1.14 x64 | parsing | O(L) time and space | AC | 0.015 s | 272 KB | 11309761 |
| [1993_parsing_strings.py](1993_parsing_strings.py) \* | PyPy 3.10 x64 | parsing, strings | O(L) time and space | AC | 0.156 s | 300 KB | 11309689 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
