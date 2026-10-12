# 1350. Canteen

[Timus 1350](https://acm.timus.ru/problem.aspx?space=1&num=1350) · difficulty 389 · implementation

Original problem by Pavel Egorov, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A menu has N ≤ 100 products, and the meal of the day is made of M
different ones of them, nobody knows which. K + 1 ≤ 101 students eat it;
for each the products that are dangerous for them are known. The first
student ate and was fine. For each of the other K students print `YES`
if the meal is surely harmless for them, `NO` if it surely holds
something dangerous for them, and `MAYBE` if both can be.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and the N product names, then K, then K + 1 blocks: a count and that
many dangerous products, the first block for the first student. The
input ends with M.

## Output

K lines with `YES`, `NO` or `MAYBE`.

## Examples

### Example 1

Input:

```
7
Rafinad
Kefir
Pastila
Smetana
Chokolade
Kljukva
Imbir
3
3
Rafinad
Kefir
Imbir
1
Rafinad
3
Kefir
Kljukva
Smetana
2
Imbir
Smetana
3
```

Output:

```
YES
NO
MAYBE
```

## Solution

Since the first student was fine, none of that student's dangerous
products is in the meal: the meal is some M products of the rest, the
safe set S. For another student with dangerous products D:

- if M = 0, or no product of S is in D, every possible meal is harmless:
  `YES`;
- if fewer than M products of S are outside D, every meal of M products
  must take one from D: `NO`;
- otherwise a meal can avoid D and another can include it: `MAYBE`.

`O(N · K)` with sets.

Pitfalls:

- with M = 0 nothing is eaten and everyone is fine (test 02);
- names are case-sensitive: `Milk` and `milk` are two products (test 04);
- dangerous products outside S do not matter, since they cannot be in
  the meal.

The answers were compared with trying every possible meal on 400 random
canteens of up to 6 products.

## Language notes

- All five solutions count the products of S inside and outside D.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1350_implementation.cpp](1350_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·K) | AC | 0.062 s | 1344 KB |
| [1350_implementation.go](1350_implementation.go) | Go 1.14 x64 | implementation | O(N·K) | AC | 0.031 s | 2156 KB |
| [1350_implementation.java](1350_implementation.java) | Java 1.8 | implementation | O(N·K) | AC | 0.140 s | 6524 KB |
| [1350_implementation.py](1350_implementation.py) | Python 3.12 x64 | implementation | O(N·K) | AC | 0.078 s | 2240 KB |
| [1350_implementation.rs](1350_implementation.rs) | Rust 1.75 x64 | implementation | O(N·K) | AC | 0.015 s | 1560 KB |
