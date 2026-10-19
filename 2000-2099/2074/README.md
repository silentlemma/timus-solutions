# 2074. Group problems by their topic paths

[Timus 2074](https://acm.timus.ru/problem.aspx?space=1&num=2074) · difficulty 976 · implementation, sorting

Original problem by Mikhail Rubinchik.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A classifier of topics is a tree written as a list: each heading is an
id like `2.2.1.` followed by a topic name, and after it come zero or more
lines with the numbers of the problems of that topic. For every
mentioned problem print the topics it belongs to, each described by the
names on its path from the root joined with dots. Problems with exactly
the same set of topics are printed on one line. The limits are 2 seconds
and 256 MB.

## Input

The classifier, as in the example. There are at most 20 topics and at
most 20 distinct problem numbers from 1000 to 9999. A topic name is
1 to 20 lower-case letters and single spaces. Ids follow a depth-first
order, so a heading with k numbers is a child of the last heading with
k − 1 numbers.

## Output

Lines "numbers : topics": the problems of a group in increasing order
separated by ", ", then " : ", then the descriptions of their topics in
lexicographic order separated by ", ". The lines themselves are in
lexicographic order.

## Examples

### Example 1

Input:

```
1. graphs
1022
1065
2. geometry
1020
2.1. idea
1130
2.2. technique
1111 1065
1265
2.2.1. convex hull
1271
3. dynamic programming
1244
```

Output:

```
1020 : geometry
1022 : graphs
1065 : geometry.technique, graphs
1111, 1265 : geometry.technique
1130 : geometry.idea
1244 : dynamic programming
1271 : geometry.technique.convex hull
```

## Solution

The input is read line by line. A line whose first word ends with a dot
is a heading; the number of dots is its depth, so the stack of names is
cut to depth − 1 entries and the new name is pushed. The description of
the current topic is the stack joined with dots. Any other line holds
problem numbers, and each one gets the current description added to its
set. A problem belongs only to the topics that list it, not to their
ancestors: in the example 1065 is under graphs and geometry.technique
only.

Then the sorted set of each problem is joined into a key, problems with
equal keys are grouped, and each group gives a line of its sorted
numbers and the key. The lines are sorted as plain strings, where a
space comes before a dot and a dot before letters. With at most 20
topics and problems the work is tiny.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2074_implementation_sorting.cpp](2074_implementation_sorting.cpp) | G++ 13.2 x64 | implementation, sorting | O(1) | AC | 0.031 s | 808 KB |
| [2074_implementation_sorting.go](2074_implementation_sorting.go) | Go 1.14 x64 | implementation, sorting | O(1) | AC | 0.046 s | 1368 KB |
| [2074_implementation_sorting.java](2074_implementation_sorting.java) | Java 1.8 | implementation, sorting | O(1) | AC | 0.171 s | 4960 KB |
| [2074_implementation_sorting.py](2074_implementation_sorting.py) | Python 3.12 x64 | implementation, sorting | O(1) | AC | 0.109 s | 792 KB |
| [2074_implementation_sorting.rs](2074_implementation_sorting.rs) | Rust 1.75 x64 | implementation, sorting | O(1) | AC | 0.062 s | 796 KB |
