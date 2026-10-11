# 1300. Taxes

[Timus 1300](https://acm.timus.ru/problem.aspx?space=1&num=1300) · difficulty 2895 · binary_search

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tax scale has limits N1 < … < Nm and rates S1, …, Sm+1 percent: an
income K pays S1 % of the part up to N1, S2 % of the part between N1
and N2, and so on, and Sm+1 % of the part above Nm. Call this T(K).

On top of a salary R every employer pays a regional bonus of L % of R,
and the bonus is taxed on its own: the employer withholds
T(R) + T(L % · R) and pays out R − T(R) + L % · R − T(L % · R). All
these amounts are rounded to cents.

A citizen worked for up to 30 employers, and only the amounts paid out
are known. Print how much more tax is owed for the whole year, that is,
the tax on the total salary and on the total bonus minus what the
employers have already withheld.

Time limit: 1 second. Memory limit: 64 MB.

## Input

L; then lines `N S`, ended by a line `0 S` with the top rate; then
the amounts paid out, one per line, ended by −1. The rates are whole
percents from 0 to 99; the amounts and limits are positive, have at
most two decimals and are at most 10⁹. There are at most 20 limits.

## Output

The difference, with two decimals.

## Examples

### Example 1

Input:

```
15         
12000000 12
24000000 20
36000000 25
48000000 30
0        35
12000000   
12000000   
-1
```

Output:

```
937233.19
```

## Solution

Everything is computed in whole cents, so no rounding error can build
up. A percentage of an amount is rounded half up to a cent, and T(K)
adds up the brackets exactly before rounding once.

The hard part is going back from an amount paid out to the salary.
Call net(R) the amount paid for a salary R. One more cent of salary
raises the tax by at most one cent (all rates are below 100 %), and the
bonus and its tax behave the same way, so net(R) never decreases as R
grows. A binary search therefore finds the salary for an amount: first
double an upper bound until its net exceeds the amount, then halve the
interval about 45 times.

Several salaries can give the same net amount, since a cent of salary
can be eaten by a cent of tax. The solutions take the largest salary
whose net does not exceed the amount. Then, with the salaries Ri
known:

answer = T(ΣRi) + T(L % · ΣRi) − Σ(T(Ri) + T(L % · Ri)).

`O(J · m · log V)` for J employers and amounts up to V.

Pitfalls:

- the answer can be negative: the scale need not rise, and with a
  falling scale the citizen gets money back (test 08); rounding alone
  can give −0.02 (test 07);
- with rates of 99 % the salary behind an amount of 10⁹ is about 50
  times larger, so 64-bit cents are needed (test 07);
- amounts may have one decimal or none, and lines may end in spaces
  (tests 01 and 06);
- the bonus goes on its own scale, not on top of the salary (test 04).

The search was checked against a plain scan over all salaries on 150
small random inputs.

## Language notes

- All languages parse the amounts by hand into whole cents.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1300_binary_search.cpp](1300_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(J * m * log V) | AC | 0.015 s | 400 KB |
| [1300_binary_search.go](1300_binary_search.go) | Go 1.14 x64 | binary_search | O(J * m * log V) | AC | 0.031 s | 1032 KB |
| [1300_binary_search.java](1300_binary_search.java) | Java 1.8 | binary_search | O(J * m * log V) | AC | 0.093 s | 988 KB |
| [1300_binary_search.py](1300_binary_search.py) | Python 3.12 x64 | binary_search | O(J * m * log V) | AC | 0.078 s | 736 KB |
| [1300_binary_search.rs](1300_binary_search.rs) | Rust 1.75 x64 | binary_search | O(J * m * log V) | AC | 0.015 s | 260 KB |
