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

The output is compared exactly, character by character; only the final
line break may differ.

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

## Language notes

Let `L≤100` be the input length. Scan positions advance past every
processed group; each phrase is copied once. Time and memory are `O(L)`.
There are at most six phrases, and no recursive or general
nested-bracket parser is needed.

Read the whole line, not one whitespace token. Keep multiword phrases
intact. Do not capitalize the second clause or every word, and do not
lose the old first word's lowercase conversion. Python and Go lowercase
the sentence directly; Java uses `Locale.ROOT`, C++ passes an unsigned
character to the case-conversion functions, and Rust uses ASCII
conversion and byte positions. These are safe because the allowed
alphabet is ASCII Latin letters, spaces and punctuation. A
regular-expression extractor is an alternative; the scanner needs only
the standard library.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1993_parsing.cpp](1993_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 388 KB |
| [1993_parsing.go](1993_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1184 KB |
| [1993_parsing.java](1993_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.093 s | 504 KB |
| [1993_parsing.py](1993_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.062 s | 504 KB |
| [1993_parsing.rs](1993_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 224 KB |
