# 1347. Blog

[Timus 1347](https://acm.timus.ru/problem.aspx?space=1&num=1347) · difficulty 1366 · parsing

Original problem by Den Raskovalov, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 100 bloggers each write a blog, and mark the people they read with
`<friend>name</friend>`. For every blogger, in the order of the input,
print three lists sorted alphabetically: the people the blogger
mentions, the bloggers who mention this blogger, and the people in both
lists. A blogger is never a friend of oneself. Names are case-sensitive
and made of Latin letters and `_`.

Time limit: 0.4 seconds. Memory limit: 64 MB.

## Input

N, then for each blog the name of its author on one line and the blog,
which starts with `<blog>` and ends with `</blog>`. A blog has up to
1000 lines of up to 255 characters, and the last line of the input may
have no line break.

## Output

For each blogger, the name and three lines starting with `1: `, `2: `
and `3: ` with the names separated by a comma and a space, and an empty
line between bloggers.

## Examples

### Example 1

Input:

```
3
xoposhiy
<blog>
Tomorrow I found <friend>_denplusplus_</friend> to
 be <b>smartest</b> blogger in the net.
Also I received interesting link from
 <friend>strange_human</friend>
</blog>
_denplusplus_
<blog>
Some shit about my work.
</blog>
strange_human
<blog>
<friend>xoposhiy</friend>
<friend>_denplusplus_</friend>
</blog>
```

Output:

```
xoposhiy
1: _denplusplus_, strange_human
2: strange_human
3: strange_human

_denplusplus_
1: 
2: strange_human, xoposhiy
3: 

strange_human
1: _denplusplus_, xoposhiy
2: xoposhiy
3: xoposhiy
```

## Solution

Read each blog from its name line up to the first line with `</blog>`,
which may be the same line as `<blog>`. Every `<friend>` up to the next
`</friend>` gives a name: whatever lies between, with any other tags
removed and spaces trimmed. The set of these names without the blogger
is list 1. List 2 for a blogger is the set of other bloggers whose
list 1 holds that name, and list 3 is the intersection. All lists are
sorted by character codes, so `_` comes after the capitals and before
the small letters. `O(L + N² log N)` for L characters.

Pitfalls:

- mentions of oneself do not count (test 02);
- a friend tag may hold spaces or other tags around the name (test 03);
- a whole blog may sit on one line (test 04);
- people without a blog can be friends but mention nobody (test 05);
- `Bob` and `bob` are different people, and a friend mentioned many
  times is listed once (test 06);
- an empty list is printed as `1: ` with the space.

## Language notes

- All five solutions read the whole input at once and search for the
  tags as plain text.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1347_parsing.cpp](1347_parsing.cpp) | G++ 13.2 x64 | parsing | O(L + N² log N) | AC | 0.015 s | 4996 KB |
| [1347_parsing.go](1347_parsing.go) | Go 1.14 x64 | parsing | O(L + N² log N) | AC | 0.031 s | 9156 KB |
| [1347_parsing.java](1347_parsing.java) | Java 1.8 | parsing | O(L + N² log N) | AC | 0.140 s | 16724 KB |
| [1347_parsing.py](1347_parsing.py) | Python 3.12 x64 | parsing | O(L + N² log N) | AC | 0.140 s | 5328 KB |
| [1347_parsing.rs](1347_parsing.rs) | Rust 1.75 x64 | parsing | O(L + N² log N) | AC | 0.015 s | 4076 KB |
