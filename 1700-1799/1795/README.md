# 1795. Husband in a Shop

[Timus 1795](https://acm.timus.ru/problem.aspx?space=1&num=1795) · difficulty 254 · simulation

Original problem by Andrew Gein, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shop has m products in given amounts, and n husbands stand in line
before Mark, each wanting some amount of one product. At the counter,
which takes a minute, a husband buys his amount if there is enough, or
leaves if the product is absent or gone. If there is some but not
enough, he lets the next person ahead and calls home, standing second;
told to take the rest, he comes back and buys it all if the amount is
unchanged, leaves if nothing is left, and otherwise lets one more
person ahead and calls again. How many minutes pass before Mark reaches
the counter?

## Input

m (1 ≤ m ≤ 1000) lines "amount of name", then n (1 ≤ n ≤ 1000) lines in
the same form for the husbands, front of the line first. Amounts are
from 1 to 1000, names are up to 20 lowercase letters, and a husband may
want a product the shop does not sell.

## Output

The number of minutes.

## Examples

### Example 1

Input:

```
3
2 of sweets
4 of milk
1 of sausage
4
2 of milk
3 of sweets
3 of milk
1 of cheese
```

Output:

```
6
```

## Solution

Simulate the line. Each visit to the counter is a minute. Keep, for
every husband, the amount he was told at his last visit. A husband who
must call is put back into the line behind the next person; if there
is nobody left before Mark, Mark is next and the count stops there.
When he returns, the amount is compared with the one he was told: the
same means he takes it all, zero means he leaves, anything else means
another call. The line holds at most 1000 husbands and each call moves
the caller back by one place, so the simulation is quick. `O(n²)`.

In the example the first husband buys 2 of the 4 milk. The second
finds only 2 sweets and steps back behind the third, who finds only 2
milk and steps back too. Then both return to unchanged amounts and buy
them, and the last husband finds no cheese: 6 visits before Mark.

Pitfalls:

- a husband who returns to an unchanged amount buys all of it, even
  though it is less than he wanted;
- a husband who must call while last in line lets Mark ahead, so Mark
  is at the counter right after that minute;
- every visit counts as a minute, including the one that ends in a
  call.

The answers agree with an independent accepted implementation on 300
random cases, among them a single stock with rare buyers of everything
who call again after every small purchase.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1795_simulation.cpp](1795_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2) | AC | 0.031 s | 576 KB |
| [1795_simulation.go](1795_simulation.go) | Go 1.14 x64 | simulation | O(n^2) | AC | 0.046 s | 6376 KB |
| [1795_simulation.java](1795_simulation.java) | Java 1.8 | simulation | O(n^2) | AC | 0.125 s | 4680 KB |
| [1795_simulation.py](1795_simulation.py) | Python 3.12 x64 | simulation | O(n^2) | AC | 0.093 s | 1080 KB |
| [1795_simulation.rs](1795_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2) | AC | 0.031 s | 652 KB |
