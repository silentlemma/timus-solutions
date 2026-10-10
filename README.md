# Timus solutions

Solutions to the problems of [Timus Online Judge](https://acm.timus.ru), with
explanations written for people who learn algorithms.

For every problem there is:

- a **write-up** in English, Russian, Chinese and Spanish: the task in our own
  words, examples, the idea of the solution, why it works, its complexity and
  the usual pitfalls;
- **solutions** in C++, Go, Python, Java and Rust, each accepted by the Timus
  judge, sometimes with several approaches;
- **tests** of our own, with a runner that builds every solution with the
  compiler version the judge uses.

## Problems

<!-- index:start -->
| Range | Problems |
|-------|----------|
| [1000–1099](1000-1099/) | 100 problems |
| [1100–1199](1100-1199/) | 100 problems |
| [1200–1299](1200-1299/) | 5 problems |
<!-- index:end -->

Each folder `1000-1099/1005/` holds the write-ups (`README.md`,
`README.ru.md`, `README.zh.md`, `README.es.md`), the solutions
(`1005_dp.cpp`, `1005_dp.go`, ...) and the tests (`tests/`).

The best way to use this repository is to try a problem on Timus first, then
read the write-up, and only then the code.

## Running the tests

Requirements: [Docker](https://www.docker.com) and Python 3.8+.

```bash
python run_tests.py 1005                # every solution of problem 1005
python run_tests.py 1005 --only .py     # solutions whose file name contains ".py"
python run_tests.py 1005 --pypy         # Python solutions under PyPy
```

To check your own solution, put it into the problem folder under a name like
`1005_mine.cpp` and run the tests of that problem. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the details.

## How this repository is made

The write-ups, solutions and tests are written with Claude by Anthropic and
reviewed by a person. Every solution is submitted to Timus and published only
after it is accepted (rare exceptions are marked in the table of solutions).
The original problem statements are not reproduced: each write-up describes
the task in its own words and links to the original.

This project is not affiliated with Timus Online Judge.

## License

Code (solutions, tests, tools) is licensed under the [MIT License](LICENSE);
the write-ups under [CC BY 4.0](LICENSE-TEXTS.md).
