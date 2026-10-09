# 1067. A folder tree rebuilt from full paths

[Timus 1067](https://acm.timus.ru/problem.aspx?space=1&num=1067) · difficulty 363 · trees, sorting

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` different folder paths are given (`1 ≤ N ≤ 500`), each up to 80
characters long, with folder names separated by backslashes. A name has 1
to 8 characters: capital letters, digits and the special characters
``!#$%&'()-@^_`{}~``. Print the folder tree: every folder on its own line,
indented by one space per level, with the subfolders of each folder right
after it and the folders of every level in lexicographic order.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the paths.

## Output

The tree, one folder per line.

## Checking

The output must be equal to the expected text; only trailing whitespace at
the very end is ignored. The leading spaces are part of the answer.

## Examples

### Example 1

Input:

```
7
WINNT\SYSTEM32\CONFIG
GAMES
WINNT\DRIVERS
HOME
WIN\SOFT
GAMES\DRIVERS
WINNT\SYSTEM32\CERTSRV\CERTCO~1\X86
```

Output:

```
GAMES
 DRIVERS
HOME
WIN
 SOFT
WINNT
 DRIVERS
 SYSTEM32
  CERTSRV
   CERTCO~1
    X86
  CONFIG
```

## Solution

Put every path into a tree of folders: walk from the root along the names
of the path, creating the folders that are missing. Then a depth-first walk
prints each folder with as many spaces as its depth, visiting the
subfolders in sorted order. With a sorted map in every folder the order
comes for free. `O(L log N)` for the total length `L` of the paths.

Pitfalls:

- sorting the full paths as strings is not enough: the backslash sits in
  the middle of the code table, after the capital letters and digits but
  before `^`, `_`, `` ` ``, `{`, `}` and `~`, so `A!` would come between
  `A` and `A\X`; the names have to be compared level by level;
- a folder in the middle of a path may never be listed on its own, and
  equal names under different parents are different folders;
- the paths contain no spaces, so they can be read as whitespace-separated
  tokens, which also ignores any carriage returns.

The answers were checked by sorting every prefix of every path as a tuple
of names: a folder then comes right before its whole subtree.

## Language notes

- C++, Java and Rust keep the subfolders in a sorted map (`std::map`,
  `TreeMap`, `BTreeMap`); Go and Python keep a hash map and sort its keys
  when printing.
- All languages compare the names by character codes, which is the order
  the problem expects for these characters.
- Java splits a path with the regular expression `\\`, a single escaped
  backslash.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1067_trees_sorting.cpp](1067_trees_sorting.cpp) | G++ 13.2 x64 | trees, sorting | O(L log N) | AC | 0.015 s | 3472 KB |
| [1067_trees_sorting.go](1067_trees_sorting.go) | Go 1.14 x64 | trees, sorting | O(L log N) | AC | 0.015 s | 8376 KB |
| [1067_trees_sorting.java](1067_trees_sorting.java) | Java 1.8 | trees, sorting | O(L log N) | AC | 0.093 s | 7380 KB |
| [1067_trees_sorting.py](1067_trees_sorting.py) | Python 3.12 x64 | trees, sorting | O(L log N) | AC | 0.078 s | 6692 KB |
| [1067_trees_sorting.rs](1067_trees_sorting.rs) | Rust 1.75 x64 | trees, sorting | O(L log N) | AC | 0.031 s | 12116 KB |
