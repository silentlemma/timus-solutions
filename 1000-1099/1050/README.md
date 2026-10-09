# 1050. Turning straight quotes into TeX quotes

[Timus 1050](https://acm.timus.ru/problem.aspx?space=1&num=1050) · difficulty 1442 · parsing

Original problem by Alexander Galperin, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A TeX source of at most 250 lines (at most 80 characters each) ends with
the command `\endinput`. Copy it exactly, except for the double quotes
`"` (code 34):

- within a paragraph, the quotes are replaced in turn by ``` `` ```
  (opening) and `''` (closing);
- an opening quote without a closing one in the same paragraph is deleted;
- `\"` is the umlaut command (as in `\"e`) and stays as it is.

A paragraph ends at an empty line (or several) and at the command `\par`.
Commands start with `\` and end at the first character that is not a Latin
letter. The text may contain bytes above 127, and the last line may have
no line break.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The text, ending with `\endinput`.

## Output

The converted text.

## Checking

The output must be equal to the expected text; only trailing whitespace at
the very end is ignored. The tests store the text in UTF-8 and give it to
the solutions in cp1251, a single-byte encoding with Cyrillic letters.

## Examples

### Example 1

Input:

```
There is no "q in this sentence. \par 
"Talk child," said the unicorn. 

She s\"aid, "\thinspace `Enough!', he said." 
\endinput
```

Output:

```
There is no q in this sentence. \par 
``Talk child,'' said the unicorn. 

She s\"aid, ``\thinspace `Enough!', he said.'' 
\endinput
```

### Example 2

Input:

```
Он сказал: "Привет!" и ушёл, "не закрыв цитату.
   
"Новый абзац" с умлаутом \"o.
\endinput
```

Output:

```
Он сказал: ``Привет!'' и ушёл, не закрыв цитату.
   
``Новый абзац'' с умлаутом \"o.
\endinput
```

## Solution

One pass over the bytes, remembering the positions of the quotes of the
current paragraph:

- `\` followed by `"` is the umlaut: skip both. Otherwise read the Latin
  letters after `\`; if they are exactly `par`, the paragraph ends
  (`\parbox` does not end it);
- `"` is added to the list of the paragraph;
- at a line break, look at the next line: if it holds only spaces, tabs
  and other whitespace and ends with a line break of its own, the
  paragraph ends.

When a paragraph ends, an odd last quote is marked for deletion and the
others alternate between opening and closing. After the last paragraph,
the bytes are copied with the marked quotes replaced. `O(L)` for a text of
`L` bytes.

Pitfalls:

- a quote can only be decided at the end of its paragraph, so the output
  is written after the scan;
- a "blank" line may contain spaces or tabs;
- `\par` must be a whole command: `\parbox` and `\partial` are not
  paragraph ends, while `\par"x` is;
- the text is bytes, not UTF-8: letters above 127 pass through unchanged,
  and a missing final line break must stay missing;
- the tests avoid a doubled backslash `\\` directly before `"` or before
  letters, where TeX and a simple scan can disagree.

## Language notes

- All languages read the whole input as bytes and write bytes: Java does
  not use a `Reader` with a charset, Python uses `sys.stdin.buffer`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1050_parsing.cpp](1050_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 260 KB |
| [1050_parsing.go](1050_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.015 s | 1888 KB |
| [1050_parsing.java](1050_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.093 s | 1348 KB |
| [1050_parsing.py](1050_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 2356 KB |
| [1050_parsing.rs](1050_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.015 s | 536 KB |
