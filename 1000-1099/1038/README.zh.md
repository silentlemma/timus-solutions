# 1038. 统计大小写错误

[Timus 1038](https://acm.timus.ru/problem.aspx?space=1&num=1038) · 难度 487 · implementation

原题作者 Alexander Galperin，出自 2000 年 10 月第五届乌拉尔国立大学团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一段不超过 10000 个字符的文本由拉丁字母、数字、标点 `. , ; : - ! ?` 和空白字符组成。单词是极长的连续字母
串；任何其他字符（包括换行符）都会结束单词。句子以 `.`、`?` 或 `!` 结束；文本开头也开始一个句子。统计两类
错误：

- 句子的第一个字母是小写；
- 大写字母不是所在单词的第一个字母（每个这样的字母算一个错误）。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

文本，可能有多行。

## 输出

错误的个数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
This sentence iz correkt! -It Has,No mista;.Kes et oll.
But there are two BIG mistakes in this one!
and here is one more.
```

输出：

```
3
```

### 样例 2

输入：

```
hello. World? yes!
OK, fine.
```

输出：

```
3
```

## 题解

对字符扫描一遍，维护两个标志：

- `new_sentence`——从文本开头或上一个 `.`、`?`、`!` 以来还没有出现过字母；
- `in_word`——前一个字符是字母。

遇到字母时：若为小写且 `new_sentence` 为真，是第一类错误；若为大写且 `in_word` 为真，是第二类错误。然后清除
`new_sentence`、设置 `in_word`。其他字符清除 `in_word`，句末符号设置 `new_sentence`。长度为 `L` 的文本
`O(L)`。

注意事项：

- 句子的第一个字母不一定在句子最开头：前面可能有数字、空格或其他标点（`2nd place.` 在 `n` 处有错误）；
- 数字不是字母，所以 `3Rd` 中的单词是以大写字母开头的 `Rd`，没有错误；
- 整个输入都是文本：要读到结尾，包括换行符。

## 各语言说明

- 各语言都整体读入输入（逐字节或作为一个字符串），并执行同样的双标志扫描。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1038_implementation.cpp](1038_implementation.cpp) | G++ 13.2 x64 | implementation | O(L) | AC | 0.015 s | 108 KB |
| [1038_implementation.go](1038_implementation.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.031 s | 1052 KB |
| [1038_implementation.java](1038_implementation.java) | Java 1.8 | implementation | O(L) | AC | 0.109 s | 392 KB |
| [1038_implementation.py](1038_implementation.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.109 s | 364 KB |
| [1038_implementation.rs](1038_implementation.rs) | Rust 1.75 x64 | implementation | O(L) | AC | 0.031 s | 252 KB |
