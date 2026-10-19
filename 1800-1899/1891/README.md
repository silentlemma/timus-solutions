# 1891. Language Ocean

[Timus 1891](https://acm.timus.ru/problem.aspx?space=1&num=1891) · difficulty 711 · parsing

Original problem by Alex Samsonov, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Type-check a sequence of variable declarations. The available types are
`int`, `real` and `string`. Each declaration initializes a new variable
with a function call; its declared type is either one of these types or
`auto`, which takes the function's return type.

Functions can share a name. A call selects a function by its name and
the ordered list of argument types, including the number of arguments.
Arguments must be variables declared on earlier lines. Types must match
exactly: there are no implicit conversions. Function and variable names
belong to separate namespaces, so they may coincide.

Find the first erroneous declaration. Within that line, check errors
in this priority order:

- `Double declaration`: the variable name has already been declared;
- `Unknown variable`: at least one argument is not yet declared;
- `No such function`: no function has the required name and argument types;
- `Invalid initialization`: an explicit declared type differs from the return type.

If the whole program is valid, list the inferred types of its `auto`
variables in declaration order. The limits are 1 second and 64 MB.

## Input

First comes f, the number of function headers, with 1 ≤ f ≤ 100.
Each of the next f lines has the form `name(type, ..., type) : type`;
the parameter list may be empty. Two headers never have both the same
name and the same ordered parameter types.

Then comes n, the number of declarations, with 1 ≤ n ≤ 100. Each of
the next n lines has the form `type variable = name(argument, ..., argument)`;
here `type` may also be `auto`, and arguments are variable names.
Every header and call has at most 10 arguments.

Names have 1 to 20 letters. Variable names contain only lowercase
English letters; function names may also contain uppercase English
letters and are case-sensitive. The words `int`, `real`, `string` and
`auto` cannot be names. Spacing follows the examples; the input has
valid syntax, so only the listed semantic errors need checking.

## Output

On an error, print `Error on line k: message`, using the declaration's
1-based line number and the exact error message above. Print no inferred
types in this case, even for earlier valid lines.

Otherwise print `name : type` for each `auto` variable in declaration
order. If there are no `auto` declarations, the output is empty.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
2
ReadInt() : int
IntToReal(int) : real
3
auto a = ReadInt()
auto b = IntToReal(a)
int c = ReadInt()
```

Output:

```
a : int
b : real
```

### Example 2

Input:

```
1
ReadInt() : int
2
int x = ReadInt()
int x = ReadInt()
```

Output:

```
Error on line 2: Double declaration
```

### Example 3

Input:

```
3
ReadInt() : int
ReadReal() : real
SumRealInt(real, int) : real
4
auto x = ReadInt()
auto y = ReadReal()
real z = SumRealInt(y, x)
real q = SumRealInt(x, y)
```

Output:

```
Error on line 4: No such function
```

## Solution

Parse function headers into a map from a signature to a return type.
A signature consists of the function name and the ordered sequence
of parameter types; an empty sequence represents a parameterless
function. Keep another map from declared variable names to their types.
The punctuation separates fields and cannot occur inside a name.

Process declarations in order. First check whether the new variable
already exists. Only then look up every argument; any missing argument
produces `Unknown variable` before function resolution is attempted.
Use the argument types to construct the signature and look it up in the
function map. If found, compare its return type with an explicit type,
or use it as the inferred type for `auto`.

Insert the new variable only after all checks succeed. For `auto`,
also append its name and inferred type to an output list. Print that
list only after the entire program succeeds; if a later line fails,
print only its error.

Before each line, the variable map contains exactly the types established
by earlier valid declarations. Therefore argument lookup uses precisely
the allowed variables. Signature lookup implements the exact overload
rule, and the explicit return-type comparison implements initialization.
Checking these steps in the required order gives the highest-priority
error on the earliest erroneous line.

Let L be the total input length. With hash maps, parsing, signature
construction and lookup take `O(L)` expected time, with `O(L)` memory.

In the first example, `a` becomes `int` and `b` becomes `real`; the
explicit declaration of `c` is omitted from the output. The second
example redeclares `x` on declaration line 2. In the third example,
`SumRealInt(y, x)` matches `(real, int)`, but `(int, real)` on line 4
does not. Although `x` and `y` were inferred earlier, their types must
not be printed because the program contains an error.

Pitfalls:

- preserve argument order and distinguish function-name case;
- a missing function does not take priority over an unknown argument;
- check redeclaration before examining the right-hand side;
- the new variable cannot refer to itself before it is declared;
- `auto` becomes a concrete type and never appears in a call signature;
- do not convert `int` to `real` implicitly;
- zero-argument functions and empty successful output are both valid.

The answers agree with a separate interpreter of the rules on 237 cases
covering valid programs and all four kinds of errors.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1891_parsing.cpp](1891_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 516 KB |
| [1891_parsing.go](1891_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1180 KB |
| [1891_parsing.java](1891_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.109 s | 1288 KB |
| [1891_parsing.py](1891_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 644 KB |
| [1891_parsing.rs](1891_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.062 s | 492 KB |
