# 1102. 把一行拆成奇怪对话中的单词

[Timus 1102](https://acm.timus.ru/problem.aspx?space=1&num=1102) · 难度 176 · strings

原题作者 Katya Ovechkina，出自 2001 年 5 月 Tetrahedron Team Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对话是由单词 `out`、`output`、`puton`、`in`、`input` 和 `one` 组成、不带空格写在一起的任意序列。对 `N` 行
（`N ≤ 1000`，小写拉丁字母，总共 `4 · 10^6` 个字母）中的每一行，若它是对话则输出 `YES`，否则输出 `NO`。

时间限制：1 秒。内存限制：16 MB。

## 输入

`N`，然后 `N` 行。

## 输出

每行对应 `YES` 或 `NO`。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
6
puton
inonputin
oneputonininputoutoutput
oneininputwooutoutput
outpu
utput
```

输出：

```
YES
NO
YES
NO
NO
NO
```

## 题解

从前往后读，这些单词重叠得很麻烦：`out` 是 `output` 的开头，`in` 是 `input` 的开头，而 `output` + `one` 读起来像
`out` + `puton` + `e`。倒过来读，它们变成 `tuo`、`tuptuo`、`notup`、`ni`、`tupni` 和 `eno`，其中没有一个是另一个
的开头。所以在每个位置最多只有一个单词在那里结束，从行尾开始一个一个地贪心切下单词，要么切完整行，要么证明不存在
拆分。`L` 个字母需要 `O(L)`。

注意事项：

- 从前往后、总是取最长单词的贪心是错误的：`outputon` 是 `out` + `puton`，但先取 `output` 就会剩下 `on`；
- 行很长而内存限制只有 16 MB，所以要避免复制整个输入。

答案与按前缀从前往后的动态规划做了核对，覆盖所有不超过三个单词的对话、几乎是对话的串以及随机破坏过的行。

## 各语言说明

- Python 用正则表达式 `(?:tuo|tuptuo|notup|ni|tupni|eno)*+` 匹配倒过来的行；占有量词 `*+` 不保存可回溯的状态，
  由于拆分唯一，这样做是安全的。
- Java 逐字节读取输入，只保留最后六个字母并在其上做从前往后的动态规划，因为四百万个字母的一行作为 `String`
  放不进 16 MB。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1102_strings.cpp](1102_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.156 s | 5768 KB |
| [1102_strings.go](1102_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.078 s | 11448 KB |
| [1102_strings.java](1102_strings.java) | Java 1.8 | strings | O(L) | AC | 0.421 s | 476 KB |
| [1102_strings.py](1102_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.140 s | 8328 KB |
| [1102_strings.rs](1102_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 7760 KB |
