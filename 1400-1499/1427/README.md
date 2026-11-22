# 1427. SMS

[Timus 1427](https://acm.timus.ru/problem.aspx?space=1&num=1427) · difficulty 364 · greedy

Original problem by Dmitry Kovalioff, Nikita Rybak and Ilya Grebnov, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of up to 100 000 characters (Latin letters, spaces, digits and
the marks . , ; : ! ? - ") is cut into consecutive SMS messages. A
message of only letters and spaces may be up to M characters long; any
other message only up to N (1 ≤ N ≤ M ≤ 10 000). Find the smallest
number of messages.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N and M, then the text on its own line.

## Output

The smallest number of messages.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
10 15
On the 11-th of February, 2006 the contest "Timus Top Coders: First Challenge" is held!
```

Output:

```
8
```

## Solution

Let run(i) be the number of letters and spaces starting at position i.
A message starting at i can end anywhere up to i + max(N, min(M,
run(i))). This farthest end never moves back as i grows (i + N and the
end of the run of letters both only grow), and with such a monotone
reach the greedy that always sends the longest possible message is
optimal: any other plan is at each step no farther ahead. The runs are
counted from the end of the text. `O(L)`.

Pitfalls:

- the text may start with spaces, so the second line must be read whole
  and not after skipping whitespace (test 04);
- digits do not count as letters (tests 03, 06);
- a message of letters may be shorter than N anyway; the long form only
  helps when the run is longer than N (test 05).

## Optimized solutions

`1427_greedy_optimized.cpp`. Keep the exact streaming longest-message greedy rule and ASCII letter/space classification. A 4 KiB fread buffer replaces one locked input call per byte. Discard only the header remainder and terminal CR/LF, preserving leading/trailing spaces and punctuation in the text. The current length/plain-text flag still determines whether the next byte starts a new message. Time O(L), fixed auxiliary storage; no complete text string is retained.

Exact-source Accepted #11326989: 0.015 s / 88 KB. Saved G++ 13.2 sample, 2026-11-20: time rank 1/67, memory rank 1/67. Teaching sources remain unchanged.

`1427_greedy_optimized.py`. Keep the same farthest-reach greedy message count and Unicode isalpha semantics. Instead of precomputing a length-L suffix-run array, scan only the letters/spaces consumed by the current message, up to the maximum length. Every scanned character is consumed before the next iteration, so total scanning is O(L). The UTF-8 text line itself is retained: O(L) input storage, with O(1) additional state. Strip only CR/LF, preserving meaningful spaces and punctuation.

Compared with `1427_greedy.py`: time 0.093 s → 0.14 s; memory 4392 KB → 1 852 KB.

C++ and Go extend the current message while reading the text. Keep its length and whether every character so far is a letter or space. Once the next character would exceed the applicable limit, finish the current message and use that character to start the next. This implements the same longest-message rule in O(L) time with O(1) extra space.

The retained accepted base implementations [1427_greedy.go](1427_greedy.go), [1427_greedy.java](1427_greedy.java), [1427_greedy.rs](1427_greedy.rs) also meet strict fast-set admission in the saved comparison: top ten or top 15% for the required metrics. They are reused without identical copies; the other teaching sources remain. An asterisk denotes the separate language rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1427_greedy_optimized.py`: time place 4/11, memory place 5/11 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1427_greedy.cpp](1427_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 924 KB | 11286185 |
| [1427_greedy.go](1427_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 3196 KB | 11286186 |
| [1427_greedy.java](1427_greedy.java) \* | Java 1.8 | greedy | O(L) | AC | 0.093 s | 1612 KB | 11286188 |
| [1427_greedy.py](1427_greedy.py) \* | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 4392 KB | 11286187 |
| [1427_greedy.rs](1427_greedy.rs) \* | Rust 1.75 x64 | greedy | O(L) | AC | 0.031 s | 1252 KB | 11286189 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1427_greedy_optimized.cpp](1427_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.015 s | 88 KB | 11326989 |
| [1427_greedy_optimized.go](1427_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 912 KB | 11310457 |
| [1427_greedy_optimized.py](1427_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(L) time; O(L) input space | AC | 0.14 s | 1852 KB | 11325485 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
