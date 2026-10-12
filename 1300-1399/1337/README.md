# 1337. Bureaucracy

[Timus 1337](https://acm.timus.ru/problem.aspx?space=1&num=1337) · difficulty 1532 · graphs

Original problem by Anatoly Uglov and Evgeny Krokhalev, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 100 officials each issue one kind of document and receive visitors
on one day of a week of L ≤ 100 days; several officials may share a day.
Getting a document takes the whole day, so at most one document is
fetched per day, and it is given only to someone who already holds a
certain set of other documents. Today is day K of the week, and today
can be used as well. Given the documents in hand and the ones wanted,
find the least number of days after today needed to get them all, and
the documents in the order they are fetched, or print `No Solution`.
Any order is accepted when several are equally fast.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and L; the reception day of each official; N lists of the documents
each one needs, each ending with 0; K; the list of documents in hand,
ending with 0; the list of wanted documents, ending with 0.

## Output

The number of days, then the documents in the order they are fetched,
or `No Solution`.

## Examples

### Example 1

Input:

```
2 7
1 2
0
1 0
1
1 0
2 0
```

Output:

```
1
2
```

## Solution

First find what must be fetched: the wanted documents not in hand and,
behind each of them, the papers it needs that are not in hand, and so
on. A paper already in hand ends the search, since nothing it needed
matters any more. If these documents need each other in a cycle, none
of the cycle can ever be the first, and the answer is `No Solution`; a
topological sort finds out.

Number the days from today, which is day 0. A plan is an order of the
documents: each is fetched on the first free day of its official that
comes after its papers. On a day when some document can be fetched,
fetching one never hurts, since moving that document's later fetch to
this day only frees a day. So the only choice is which of the documents
ready on the first usable day to take, and all of them belong to
officials of that weekday. When no two officials share a day the plan
is forced; otherwise taking the document with the longest chain of
waiting behind it is a good guess but not always right (test 11).

The answer is found by branch and bound over this choice:

- the longest-chain rule gives a first plan and is rerun from every node
  of the search to improve the best plan found;
- a node is cut by a lower bound: the earliest day of each remaining
  document follows from its papers, and for each weekday the k
  documents that cannot come before day r take k such days from r on,
  while the last of them still has its shortest chain of waiting ahead;
- a set of documents in hand that was already reached by the same or an
  earlier day is not searched again.

The search is exponential in the worst case. On random cases with 100
officials sharing a week of a few days it usually ends within a fraction
of a second, but rare cases take far longer. The results were checked
against a dynamic programming over all subsets of the documents to fetch
on 1000 random cases with up to 14 documents and shared days.

Pitfalls:

- several officials may receive on the same day while only one document
  can be fetched, so the order matters (test 09);
- today is day 0 and can be used: a document whose official receives
  today takes 0 days (test 04);
- if everything wanted is in hand, the answer is 0 and an empty line
  (tests 02 and 06);
- a cycle among needed papers can be broken by a paper already in hand
  (test 07), and only a cycle among the documents still to fetch makes
  the task impossible (test 03).

## Language notes

- The set of documents in hand is a Python integer, two 64-bit words in
  C++, Go and Rust, and a list of two longs in Java, used as a map key.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1337_graphs.cpp](1337_graphs.cpp) | G++ 13.2 x64 | graphs | exponential | AC | 0.015 s | 300 KB |
| [1337_graphs.go](1337_graphs.go) | Go 1.14 x64 | graphs | exponential | AC | 0.031 s | 1780 KB |
| [1337_graphs.java](1337_graphs.java) | Java 1.8 | graphs | exponential | AC | 0.187 s | 4100 KB |
| [1337_graphs.py](1337_graphs.py) | Python 3.12 x64 | graphs | exponential | AC | 0.109 s | 1216 KB |
| [1337_graphs.rs](1337_graphs.rs) | Rust 1.75 x64 | graphs | exponential | AC | 0.046 s | 580 KB |
