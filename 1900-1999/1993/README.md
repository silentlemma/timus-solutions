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

`1993_parsing_optimized.rs`. Keep the three-role clause parser and optional prefix, including comma spacing and capitalizing only the first emitted byte. Lowercase one input byte vector; record role/prefix spans instead of allocating phrase strings and joining clause results. Emit spans directly. O(L) time and O(L) retained input storage; no change to the grammar.

Compared with `1993_parsing.rs`: time 0.046 s → 0.015 s; memory 224 KB → 80 KB.

`1993_parsing_optimized.java`. Keep object-subject-verb reordering, but record each phrase as start/end offsets into the original sentence instead of lowercasing the whole line, splitting clauses and copying substrings. Emit those slices directly, applying ASCII case conversion only as characters are written. Only the first output letter is capitalized; an optional conjunction stays before the second reordered clause and remains lowercase. Exact comma/space formatting is preserved. Time O(L); the input String still uses O(L) storage, while role offsets and output buffering are bounded. No whole-answer StringBuilder is retained.

Compared with `1993_parsing.java`: time 0.109 s → 0.078 s; memory 472 KB → 528 KB.

Retain the same role-based parsing proof. Compact C++/Go keep spans in one bounded ASCII input buffer instead of copying phrases or building stream/string objects. Scan over each complete bracketed group, recording object, subject and verb positions; an unbracketed word is the optional second-clause conjunction. Emit conjunction and the three roles in order, insert the original comma separator, lowercase all letters and capitalize only the first output letter. Groups are nonnested and roles unique, so every phrase is emitted exactly once with its internal word order unchanged. Python uses slices and existing text streams. With input length L<=100, both time and storage are O(L).

- `1993_parsing_optimized.cpp`: 0.015 s / 76 KB; base `1993_parsing.cpp`: 0.015 s / 388 KB; relative change: time -0.0%, memory -80.4%.
- `1993_parsing_optimized.go`: 0.015 s / 272 KB; base `1993_parsing.go`: 0.031 s / 1184 KB; relative change: time -51.6%, memory -77.0%.
- `1993_parsing_strings.py`: 0.156 s / 300 KB; base `1993_parsing.py`: 0.062 s / 504 KB; relative change: time +151.6%, memory -40.5%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1993_parsing_optimized.java`: time place 2/65, memory place 5/65 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1993_parsing_optimized.java](1993_parsing_optimized.java) \* | Java 1.8 | parsing | O(L) | AC | 0.078 s | 528 KB | 11325023 |
| [1993_parsing_optimized.rs](1993_parsing_optimized.rs) \* | Rust 1.75 x64 | parsing | O(L) time; O(L) space | AC | 0.015 s | 80 KB | 11325535 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
