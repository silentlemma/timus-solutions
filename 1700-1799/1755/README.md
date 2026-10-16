# 1755. Cake

[Timus 1755](https://acm.timus.ru/problem.aspx?space=1&num=1755) · difficulty 833 · greedy

Original problem by Vladislav Isenbaev, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cake holds n grams of cream and m grams of chocolate. Little Boy cuts
it into two pieces, any amounts of each, and Karlsson takes the piece he
likes more, leaving the choice to Little Boy on a tie. A piece with x
grams of cream and y of chocolate is worth a₁x + b₁y to Little Boy and
a₂x + b₂y to Karlsson. Find a cut that gives Little Boy the most.

## Input

a₁, b₁, a₂, b₂ (0 ≤ aᵢ, bᵢ ≤ 100), then n and m (0 ≤ n, m ≤ 1000).

## Output

The cream and chocolate of one of the two pieces, with an error of at
most 10⁻⁸. Any best cut is accepted.

## Examples

### Example 1

Input:

```
1 2 3 2
400 300
```

Output:

```
300.00000000 0.00000000
```

## Solution

Little Boy always ends up with a piece that Karlsson values at no more
than half of the whole cake, T/2 with T = a₂n + b₂m: if Karlsson likes
one piece more, he takes it, and on a tie both pieces are worth T/2 to
him. Any piece worth at most T/2 to Karlsson can be made Little Boy's
by cutting it off. So the task is to find the piece of greatest worth
a₁x + b₁y with a₂x + b₂y ≤ T/2, 0 ≤ x ≤ n and 0 ≤ y ≤ m.

That is a fractional knapsack with two goods: each gram of cream brings
a₁ and uses a₂ of the room T/2, each gram of chocolate brings b₁ and
uses b₂. Taking the good with the higher worth per room first, as much
as fits, and then the other, is best. Goods that use no room come
first, and comparing a₁·b₂ with b₁·a₂ keeps the order exact. `O(1)`.

In the example T/2 = 900. Chocolate brings 2 for 2 of room and cream 1
for 3, so all 300 grams of chocolate are taken, using 600, and then
100 grams of cream: a piece worth 700 to Little Boy. The program prints
this piece, 100 and 300; the example prints the other one, 300 and 0,
which is the same cut.

Pitfalls:

- the answer may name either piece, so the cut matters, not the piece;
- when Karlsson values nothing, Little Boy can take the whole cake;
- a tie is fine for Little Boy, so the piece may use the room exactly.

The cuts give Little Boy the same worth as an independent accepted
implementation, which tries the corners of the allowed region, on 600
random cakes, some with zero coefficients or with tastes that agree.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1755_greedy.cpp](1755_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 140 KB |
| [1755_greedy.go](1755_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1120 KB |
| [1755_greedy.java](1755_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.140 s | 1792 KB |
| [1755_greedy.py](1755_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 480 KB |
| [1755_greedy.rs](1755_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.046 s | 280 KB |
