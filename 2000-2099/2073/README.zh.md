# 2073. 比赛记录汇总表

[Timus 2073](https://acm.timus.ru/problem.aspx?space=1&num=2073) · 难度 242 · implementation

原题作者 Kirill Borozdin（由 Kirill Borozdin 和 Alexey Danilyuk 整理），出自 2015 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出 n ≤ 100 场比赛的记录：由 1 到 30 个拉丁字母、数字和空格组成的名称，日期 DD.MM.YY，题目数 p ≤ 13 和提交数 s ≤ 100，然后 s 条提交，每条为题目字母和评测结果。用 `+`、`-`、`|` 画出表格：一行表头，每场比赛一行，包括补齐到 30 个字符的名称、日期（8 个字符）和 13 个标记，对应字母 A … M。若题目至少通过一次，标记为 `o`；提交过但从未通过为 `x`；比赛中有该题但未提交为 `.`；比赛中没有该题则为空格。时间限制 1 秒，内存限制 64 MB。

## 输入

n，然后对每场比赛给出名称行、日期行、“p s”行和 s 行“字母 结果”。结果是 `Accepted`、`Wrong Answer`、`Runtime Error`、`Time Limit Exceeded`、`Memory Limit Exceeded`、`Compilation Error` 之一。

## 输出

按样例格式输出表格，表头前、表头后和每场比赛后各有一条边框线。

## 样例

### 样例 1

输入：

```
2
Codeforces Gamma Round 512
29.02.16
5 4
A Accepted
B Accepted
C Accepted
E Accepted
URKOP
17.10.15
12 11
A Accepted
B Wrong Answer
B Time Limit Exceeded
J Accepted
B Accepted
J Time Limit Exceeded
J Accepted
F Accepted
E Runtime Error
H Accepted
E Runtime Error
```

输出：

```
+------------------------------+--------+-------------+
|Contest name                  |Date    |ABCDEFGHIJKLM|
+------------------------------+--------+-------------+
|Codeforces Gamma Round 512    |29.02.16|ooo.o        |
+------------------------------+--------+-------------+
|URKOP                         |17.10.15|oo..xo.o.o.. |
+------------------------------+--------+-------------+
```

## 解法

每场比赛先放 p 个点和 13 − p 个空格。结果为 `Accepted` 的提交把对应标记设为 `o`；其他结果在标记还不是 `o` 时设为 `x`。然后输出各行，名称用空格补齐到 30 个字符。整体与输入规模成线性。

名称中可能有空格，所以按行读入，并去掉行尾的空格和回车（名称不会以空格结尾）。标记保留末尾的空格：样例中第二行在边框前以 `.. ` 结尾。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2073_implementation.cpp](2073_implementation.cpp) | G++ 13.2 x64 | implementation | O(input) | AC | 0.015 s | 380 KB |
| [2073_implementation.go](2073_implementation.go) | Go 1.14 x64 | implementation | O(input) | AC | 0.015 s | 1832 KB |
| [2073_implementation.java](2073_implementation.java) | Java 1.8 | implementation | O(input) | AC | 0.078 s | 2308 KB |
| [2073_implementation.py](2073_implementation.py) | Python 3.12 x64 | implementation | O(input) | AC | 0.062 s | 1324 KB |
| [2073_implementation.rs](2073_implementation.rs) | Rust 1.75 x64 | implementation | O(input) | AC | 0.015 s | 748 KB |
