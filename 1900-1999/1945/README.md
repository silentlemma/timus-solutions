# 1945. Coloring Multiplicative Families with Valuations

[Timus 1945](https://acm.timus.ru/problem.aspx?space=1&num=1945) · difficulty 3183 · number_theory

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given distinct positive integers and g halls, assign each integer a hall.
Two values a,b may belong to the same family if a=p·i and b=p·j for
some positive integer p and distinct birth ordinals 1≤i,j≤g. Such values
must go to different halls for every possible p, even when p or the
other family members are absent from the input. Find any valid assignment.
Limits: 1 second, 64 MB.

## Input

n and g, with 1≤n≤50000 and 2≤g≤5, followed by n pairwise distinct
integers a₁,…,a_n in 1..10^9. Preserve their input order in the answer.

## Output

Yes followed by n integer hall numbers in 1..g, one for each input value;
or No if impossible. Capitalization is exact. Any valid hall assignment
is accepted. The proof below establishes that every valid input is feasible.

## Checking

A checker verifies every pair of values that could be brothers for some
parent and accepts any valid assignment. By the construction below, `No`
is never correct within the limits.

## Examples

```
5 2
1
2
3
4
6
```

```
Yes
1
2
1
1
2
```

## Solution

Let v_p(a) be the exponent of prime p in a. Choose w₃=min(g−1,3) and
define F(a)=v₂(a)+w₃·v₃(a)+4·v₅(a), taken modulo g. Assign hall F(a)+1.
Compute just these three exponents by repeated division; residual prime
factors are irrelevant. The complete small-multiplier calculation is:

| g | w₃=min(g−1,3) | F(1),…,F(g) modulo g |
|---:|---:|---|
| 2 | 1 | 0, 1 |
| 3 | 2 | 0, 1, 2 |
| 4 | 3 | 0, 1, 3, 2 |
| 5 | 3 | 0, 1, 3, 2, 4 |

Why these weights? Set F(2)=1, which forces F(4)=2. For g=3 use
F(3)=2; for g=4 or 5 use F(3)=3. At g=5 the remaining residue is filled
by F(5)=4. Smaller g does not constrain the unused multipliers, so the
same coefficient of v₅ works throughout. Each table row contains every
residue exactly once.

Prime valuations are additive: v_q(p·i)=v_q(p)+v_q(i). Therefore
F(p·i)=F(p)+F(i) modulo g for every parent p. Adding the same residue
F(p) preserves all the distinct residues in a table row. Consequently
the full possible family p,2p,…,gp uses all g halls distinctly, and
any subset present in the input also satisfies the requirement.
This proves feasibility for every valid input, so the programs always
print Yes. The argument uses cyclic addition, including composite g=4;
it does not assume g is prime.

O(n log A) time for A=max a_i≤10^9: at most 29 successful divisions
per value, followed by three failed divisibility tests. A scalar color
needs O(1) auxiliary space. Complete buffered programs use at most O(n)
space; C++ and Go stream both values and labels with bounded buffers.
The accumulator is at most 4·29, so ordinary signed 32-bit integers suffice.

Possible brothers need not have an integer ratio: 4 and 6 share parent 2
when g≥3. Conversely, the pair 3,4 can share a hall at g=3 but not g=4.
The parent need not occur in the queue. Use g-dependent w₃, add one to
the residue, preserve input order, and match Yes/No capitalization.
An answer may differ from the sample while remaining valid.

## Language notes

All versions use integer arithmetic only and print one hall per line.
Java and Rust build the output; Python keeps input and result lists.
Repeated division by 2, 3 and 5 suffices; trial division through sqrt(A),
general graph coloring and searching for an impossible instance are unnecessary.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1945_number_theory.cpp](1945_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log A) | AC | 0.031 s | 436 KB |
| [1945_number_theory.go](1945_number_theory.go) | Go 1.14 x64 | number_theory | O(n log A) | AC | 0.109 s | 2740 KB |
| [1945_number_theory.java](1945_number_theory.java) | Java 1.8 | number_theory | O(n log A) | AC | 0.125 s | 3760 KB |
| [1945_number_theory.py](1945_number_theory.py) | Python 3.12 x64 | number_theory | O(n log A) | AC | 0.187 s | 7052 KB |
| [1945_number_theory.rs](1945_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log A) | AC | 0.031 s | 2148 KB |
