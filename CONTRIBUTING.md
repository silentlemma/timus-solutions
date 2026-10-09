# How the repository is organised

This document describes how problems, write-ups, solutions and tests are laid
out and which rules they follow. Every problem in the repository follows it.

## Layout

```
README.md                         overview and the list of problem ranges
1000-1099/README.md               the problems of the range: titles, tags, languages
1000-1099/1005/README.md          write-up in English
1000-1099/1005/README.ru.md       the same in Russian, Chinese and Spanish
1000-1099/1005/README.zh.md
1000-1099/1005/README.es.md
1000-1099/1005/1005_<approach>.<ext>   solutions
1000-1099/1005/tests/             own tests (see "Tests")
run_tests.py                      test runner (see "Running the tests")
```

Problems are grouped by hundreds, so that no folder holds more entries than
GitHub can list. The folder of a problem appears when it has a write-up and at
least one accepted solution. Problem numbers are the Timus problem numbers.

## Write-ups

The English write-up is written first; the other languages are translations of
it. A write-up never reproduces the text, the story or the characters of the
original statement: it describes the algorithmic task in its own words and
links to the original problem.

```markdown
# NNNN. <Own short title>

[Timus NNNN](<link>) · difficulty <Timus rating> · <tags>

Original problem from <contest> | by <author>.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task
Given ... Find ... — precise, with all constraints (strict / non-strict
inequalities, value ranges, sizes), time limit and memory limit.

## Input
## Output

## Checking
Token by token | line by line | absolute/relative error ≤ ε | any valid
answer, and what the checker verifies.

## Examples
The tests marked `"example": true` in tests.json, in the same order: for each,
the input and the output as fenced code blocks, with the exact file contents.

## Solution
Idea, algorithm, why it is correct (sketch), complexity, pitfalls.
Alternative approaches in a line each, if any.

## Language notes
What differs between languages: e.g. "the greedy passes in C++ and Go but
needs the O(n log n) version in Python", "Java 8 needs fast input".

## Solutions
Table: file · language · approach · complexity · verdict · time · memory.
```

Fenced code blocks without a language tag are reserved for the examples: the
plain blocks of a write-up are exactly the inputs and outputs of its examples.
Any other code in a write-up carries a language tag (` ```cpp `, ` ```text `,
...). The "Checking" section states the same rule as `judging` in tests.json.

A write-up is **self-sufficient**: a reader who has only the write-up (and not
the original statement) can solve the problem.

The range page (`1000-1099/README.md`) and the list in the main README are
generated from the write-ups; they are not edited by hand.

## Solutions

### Languages

| Extension | Timus compiler | Notes |
|-----------|----------------|-------|
| `.cpp` | G++ 13.2 x64 | |
| `.go` | Go 1.14 x64 | no generics, no `min`/`max` builtins |
| `.py` | Python 3.12 x64 or PyPy 3.10 x64 | the same source; the table of solutions says which one was accepted |
| `.java` | Java 1.8 | Java 8 only; exactly one public class, `public class Main` (the runner compiles the file as `Main.java`) |
| `.rs` | Rust 1.75 x64 | standard library only; mind the stack size for deep recursion |

### File names

`NNNN_<approach>.<ext>`, where `<approach>` is one or more tags from the list
below joined with `_`, e.g. `1589_astar_bidirectional.cpp`, `1005_dp.go`. Two
solutions of a problem in the same language differ in the approach part of the
name. The suffix is present even when a problem has a single approach.

Every file is a complete program: it reads standard input and writes standard
output, exactly as submitted to the judge.

### Code style

- **Comments** explain what is not obvious: one comment is at most 3 lines; no
  commented-out code; English only. The full explanation belongs to the
  write-up.
- **Line length**: at most 100 characters, code and comments alike.
- **No problem number** in the code: not in identifiers, literals or strings.
- **No magic numbers**: limits, moduli and other constants of the problem are
  named constants; bare literals are fine only for trivial values (`0`, `1`,
  `2`, `-1`, `10`, ...).
- **No hardcoding**: the code never special-cases particular inputs, such as
  values from the examples or the tests.
- **Formatting**: the standard formatter of the language (`gofmt`,
  `clang-format` with the repository's `.clang-format`, `ruff format`,
  `rustfmt`).
- **Warnings**: the code builds without warnings with the judge's compiler.

### Tags

Tags name approaches; they appear in file names and in the write-ups. Use these
only, and extend the list here when a new one is needed.

`adhoc`, `astar`, `backtracking`, `bfs`, `bidirectional`, `binary_search`,
`bitmask`, `bruteforce`, `combinatorics`, `constructive`, `dfs`, `dijkstra`,
`dp`, `dsu`, `fenwick`, `flow`, `games`, `geometry`, `graphs`, `greedy`,
`hashing`, `implementation`, `interactive`, `math`, `matching`, `matrix`,
`meet_in_middle`, `number_theory`, `parsing`, `prefix_sums`, `probability`,
`segment_tree`, `shortest_paths`, `simulation`, `sorting`, `sqrt_decomposition`,
`strings`, `suffix_structures`, `ternary_search`, `trees`, `two_pointers`.

### Verdicts

- A solution is published once the judge **accepts** it; the table of solutions
  shows the compiler, time and memory of that run.
- A solution that **exceeds the time or memory limit** may be kept as an
  exception, when it is a meaningful correct approach that does not fit the
  limits (e.g. a 256 KB memory limit that a language runtime cannot meet). The
  table marks it `TLE` / `MLE` with the failed test and a note. It passed only
  the tests before that one and is not claimed to be correct on the others.
- Solutions with **wrong answer, runtime error or compilation error** are never
  kept.

## Tests

`tests/` in the folder of a problem holds tests of our own, not copied from the
original statement: hand-made cases, edge cases and, when useful, generated
large cases. They are a quick check, not a replacement for the judge, whose
hidden tests are much stronger.

### Files

- `<name>.in` / `<name>.out`: input and expected output, byte for byte. Text
  files with LF line endings and a final newline, at most 64 KB each; anything
  larger is generated. Outputs have no trailing spaces; inputs may have them,
  to test how solutions handle whitespace.
- All test files are UTF-8. When the judge gives the input in a single-byte
  legacy encoding (e.g. cp437 box-drawing characters), the tests still store
  it in UTF-8, so that it is readable here, and `input_encoding` in tests.json
  names the encoding: the runner converts the inputs before running the
  solutions and the checker.
- `tests.json`: how outputs are compared and the list of tests.
- `checker.py`: required when `judging` is `checker`.
- `gen.py`: required when some test is generated.

### tests.json

```json
{
  "judging": "tokens",
  "reference": "1000_math.cpp",
  "cases": [
    { "name": "01", "example": true, "note": "basic case" },
    { "name": "04", "note": "the sum does not fit in 32 bits" },
    { "name": "big1", "generator": "1 200000", "note": "maximal size, random" }
  ]
}
```

| Field | Meaning |
|-------|---------|
| `judging` | how an output is compared with the expected one (below) |
| `reference` | the solution that produces expected outputs of generated tests; required if any test is generated |
| `input_encoding` | optional: the encoding the solutions receive the inputs in, e.g. `cp437` |
| `cases[].name` | file name without extension |
| `cases[].example` | shown in the "Examples" section of the write-ups |
| `cases[].note` | what the test checks; required |
| `cases[].generator` | arguments of `gen.py`; the test has no files, its input is generated |

### Judging modes

| Mode | Comparison |
|------|------------|
| `tokens` | the outputs are equal as sequences of whitespace-separated tokens (default) |
| `lines` | the outputs have the same lines, each compared as a sequence of tokens |
| `exact` | the outputs are equal byte for byte, ignoring trailing whitespace at the end |
| `float:<eps>` | tokens; numeric tokens may differ by absolute or relative error ≤ `eps` |
| `checker` | `checker.py` decides (problems with several valid answers) |

### Checker

```
python checker.py <input file> <expected output file> <output file>
```

Exit code 0 means accepted, 1 means wrong answer; a short reason is printed to
standard output. The checker uses only the Python standard library. The stored
`.out` files must pass their own checker.

### Generator

```
python gen.py <arguments from tests.json>
```

Prints one test input to standard output. It is deterministic: the same
arguments always give the same input (seeded randomness only). The expected
output is produced by the `reference` solution when the tests are run.

## Running the tests

Requirements: [Docker](https://www.docker.com) and Python 3.8+.

```bash
python run_tests.py 1000                 # all solutions of problem 1000
python run_tests.py 1000 --only .py      # solutions whose file name contains ".py"
python run_tests.py 1000 --pypy          # Python solutions under PyPy instead of CPython
```

Every solution is built and run in the official Docker image of the language
version the judge uses, with warnings treated as errors:

| Language | Image | Build |
|----------|-------|-------|
| C++ | `gcc:13.2` | `g++ -O2 -Wall -Wextra -Werror` |
| Go | `golang:1.14` | `go vet`, `go build` |
| Python | `python:3.12-slim` (or `pypy:3.10-slim`) | — |
| Java | `eclipse-temurin:8-jdk` | `javac -Xlint:all -Werror` |
| Rust | `rust:1.75-slim` | `rustc -O --edition 2021 -D warnings` |

Generators and checkers run in `python:3.12-slim`.

## Commits

One problem per commit, in increasing order of problem numbers. A commit adds
the write-ups, solutions and tests of one problem and updates the generated
lists.

```
NNNN: <title>

A paragraph about the solution: algorithm, key ideas, complexity.

A paragraph about the solutions: languages and approaches.
```

## Licenses

- Code (solutions, tests, `run_tests.py`) is licensed under the MIT License
  ([LICENSE](LICENSE)).
- Write-ups (`README*.md` of the problems) are licensed under CC BY 4.0
  ([LICENSE-TEXTS.md](LICENSE-TEXTS.md)).
- Problems are taken from Timus Online Judge; each write-up links to the
  original problem. The original statements are not included.
