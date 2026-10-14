# 1524. Men in Black

[Timus 1524](https://acm.timus.ru/problem.aspx?space=1&num=1524) · difficulty 9705 · simulation

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Simulate an agency of at most 26 agents, each with a code letter and five
traits between 0 and 1: accuracy, walking speed, intelligence,
experience and driving skill. The agency also has cars (each of a type
with a minimal driving skill and a distance it can run before breaking)
and a list of monster kinds. Events come in time order: a new agent
joins (and takes the free letter nearest to the first letter of the
name, the smaller one on a tie), a car is bought, or a quest arrives: a
delivery, killing a monster, an investigation or negotiations at some
distance from the office.

A quest is done by one agent or a pair, on foot or by one car, there and
back. A pair walks at the slower speed and drives at the better skill;
its accuracy is the mean and its experience and intelligence combine as
1 − (1 − a)(1 − b). Killing takes evasiveness / accuracy, an
investigation minimal time / intelligence, negotiations minimal time /
experience, and each kind has its requirements on the traits. Every
stretch of time is rounded to a minute separately. A car that runs out
of distance breaks and the rest of the way is walked. A quest starts as
soon as somebody can do it, earlier quests first; the team that is
fastest wins, a single agent before a pair, then the smaller letters; a
car is taken only when it is strictly faster, then the smallest id.
After a quest each agent’s traits grow by the given formulas, and an
agent whose experience reaches the retirement level leaves.

Print every bought car, broken car, killed monster, finished quest,
tired agent, new agent and started quest with its time, in that order
within a minute and lexicographically by message within a kind.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

The agents, car types, cars and monster kinds, then the maximal walking
distance, maximal evasiveness, maximal monster experience and the
retirement experience, and then up to 2000 events.

## Output

Lines `dddd:hh:mm    message` as described above.

## Examples

### Example

Input:

```
1
James 0.8 0.7 0.75 0.5 0.85 J

1
0.4 100 mibLexus

2
mibLexus 0 pq123bu
mibLexus 12 ab891ah

1
0.2 0.3 18 100 cockroach

200 20 200 0.95

4
10 newagent Klint 0.9 0.8 0.5 0.7 0.86
20 quest run 48
30 newcar mibLexus 47 aa890bu
43 quest kill 100 cockroach
```

Output:

```
0000:00:10    New agent Klint got a letter K.
0000:00:20    Agent J started quest 1 using car pq123bu.
0000:00:30    MIB bought a car of class mibLexus.
0000:00:43    Agent K started quest 2 using car ab891ah.
0000:02:12    Agent J finished quest 1.
0000:02:25    Car ab891ah was broken.
0000:03:00    Agent K killed monster cockroach.
0000:05:05    Agent K finished quest 2.
```

## Solution

An event-driven simulation. When a quest starts, its whole course is
known: the moments when the car breaks, the monster is killed and the
quest ends, counted from the start. These moments go into a priority
queue ordered by time and then by kind (breaking, killing, finishing),
which is also the order of the messages in a minute.

At each moment due events are processed, then the outside event is
applied, and then the waiting quests are tried in the order
they came, again and again while one of them can start. For a quest,
every free agent and every pair of free agents is tried with no car and
with every free car; with a car there are five cases: it breaks on the
way there, on arrival, on the way back, exactly on return, or not at
all. The messages of a minute are sorted by kind and text before
printing.

Pitfalls:

- every stretch is rounded on its own: driving and the walk after a
  breakdown are two roundings, using `floor(t + 0.5 + 10⁻⁹)` so that
  0.5 is not lost to the binary representation;
- the requirements compare with ≥ and no tolerance (test 05);
- a car that is only as fast as walking is not taken; among equally
  fast eligible cars the smallest id wins (car ties: test 06);
- a pair is better only when strictly faster than every eligible free
  single agent;
- a car breaks exactly when its distance runs out, also on arrival or on
  return (test 04);
- a tired agent frees the letter at once (test 07);
- a later quest may start while an earlier one still waits for someone
  able to do it (test 03).

The output was compared with an independent accepted implementation on
the tests here and on 100 random agencies.

## Language notes

- Python runs under PyPy: the largest test here takes about 10 s with
  CPython and 1.7 s with PyPy. It also tries only the first eligible car,
  by id, among those that will not break on the trip, since they all
  take the same time.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1524_simulation.cpp](1524_simulation.cpp) | G++ 13.2 x64 | simulation | O(N²) | AC | 0.093 s | 696 KB |
| [1524_simulation.go](1524_simulation.go) | Go 1.14 x64 | simulation | O(N²) | AC | 0.093 s | 7912 KB |
| [1524_simulation.java](1524_simulation.java) | Java 1.8 | simulation | O(N²) | AC | 0.296 s | 8992 KB |
| [1524_simulation.py](1524_simulation.py) | PyPy 3.10 x64 | simulation | O(N²) | AC | 2.593 s | 17972 KB |
| [1524_simulation.rs](1524_simulation.rs) | Rust 1.75 x64 | simulation | O(N²) | AC | 0.093 s | 1576 KB |
