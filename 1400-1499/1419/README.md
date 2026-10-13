# 1419. Maps of the Island Worlds

[Timus 1419](https://acm.timus.ru/problem.aspx?space=1&num=1419) · difficulty 1212 · graphs

Original problem by Alexander Klepinin, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A picture of M × N characters (both odd, from 1 to 99) has `O` at every
position with odd row and column (counting from 1) and `-`, `|`, `/`,
`\` or a space everywhere else. It is a real map of an island world if
the symbols are bridges between neighbouring islands, every island has
exactly three bridges, and the islands stay connected after any one
bridge is destroyed. Print "Island world" or "Just a picture".

This is the check behind [problem 1411](../1411/README.md).

Time limit: 1 second. Memory limit: 64 MB.

## Input

M and N, then N lines of M characters.

## Output

"Island world" or "Just a picture".

## Examples

### Example 1

Input:

```
15 9
O-O-O-O-O-O O-O
|\| |  \|/|/|/|
O-O O-O O O O O
 \ / /|  /  |/|
O-O O-O-O-O O-O
|\  |    / \  |
O-O O O-O-O O-O
|/ /| |\  |\ \|
O-O-O-O-O-O-O-O
```

Output:

```
Island world
```

### Example 2

Input:

```
5 3
O-O-O
|   |
O-O-O
```

Output:

```
Just a picture
```

## Solution

Read the lines as they are, since they may start with spaces. Every
symbol must fit its gap: `-` between two islands of a row, `|` between
two islands of a column, `\` or `/` in the middle of four islands; any
other symbol makes the picture fail. Each symbol adds an edge between
the two islands it joins. Then every island must have degree three, and
one depth-first search computes entry times and low links: the graph is
connected if the search reaches every island, and has no bridge if no
tree edge to a vertex v has low(v) > tin(parent). The search keeps its
own stack, since a path of 2500 islands is too deep for some languages'
call stacks. `O(MN)`.

Pitfalls:

- a symbol in the wrong kind of gap, such as `-` where only `|` can
  stand, is not a bridge (test 06);
- a map of degree-three islands can still fall apart into two pieces
  or hang on one bridge (tests 03, 07);
- a single island has no bridges at all (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1419_graphs.cpp](1419_graphs.cpp) | G++ 13.2 x64 | graphs | O(MN) | AC | 0.015 s | 572 KB |
| [1419_graphs.go](1419_graphs.go) | Go 1.14 x64 | graphs | O(MN) | AC | 0.031 s | 1796 KB |
| [1419_graphs.java](1419_graphs.java) | Java 1.8 | graphs | O(MN) | AC | 0.093 s | 1280 KB |
| [1419_graphs.py](1419_graphs.py) | Python 3.12 x64 | graphs | O(MN) | AC | 0.109 s | 1696 KB |
| [1419_graphs.rs](1419_graphs.rs) | Rust 1.75 x64 | graphs | O(MN) | AC | 0.031 s | 588 KB |
