# 1098. 每数到第 1999 个就删去，最后剩下的字符

[Timus 1098](https://acm.timus.ru/problem.aspx?space=1&num=1098) · 难度 555 · math

原题作者 Stanislav Vasiliev，出自 1999 年第三届乌拉尔大学生团体程序设计锦标赛的练习赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

问题是去掉换行后的全部输入（1 到 30000 个字符；空格和标点都算）。从第一个字符开始数 `N − 1` 个字符，删去第 `N`
个，到结尾时回到开头继续数；然后从被删字符的下一个字符重新开始数，直到只剩一个字符，`N = 1999`。若剩下的是
`?`，输出 `Yes`；若是空格，输出 `No`；否则输出 `No comments`。

时间限制：1 秒。内存限制：64 MB。

## 输入

问题，可能分成多行。

## 输出

`Yes`、`No` 或 `No comments`。

## 评测方式

按行比较输出；行内按记号逐个比较。

## 样例

### 样例 1

输入：

```
Does the jury of this programming contest use the
algorithm described in this problem to answer my questions?
```

输出：

```
Yes
```

### 样例 2

输入：

```
At least, will anybody READ my question?
```

输出：

```
No
```

### 样例 3

输入：

```
This is
UNFAIR!
```

输出：

```
No comments
```

## 题解

这是约瑟夫问题。设 `J(m)` 为 `m` 个字符中最后剩下的那个相对于计数起点的位置。第一次删除后剩下 `m − 1` 个字符，
计数从往后 `N` 个位置处开始，所以 `J(m) = (J(m − 1) + N) mod m`，`J(1) = 0`。递推到问题的长度就得到这个位置，
只有那里的字符才重要。`O(L)`。

从字符串中一个一个地删除字符需要 `O(L²)`（`L = 30000`）：在编译型语言中也够快，但递推式完全避免了这一点。

注意事项：

- 除换行外的每个字符都要算，包括行尾和单词之间的空格，所以按原始字节读取输入，只去掉 `\n` 和 `\r`；
- 问题可能只有一个字符，这时答案就由它决定。

答案与一个从列表中逐个删去每第 1999 个字符的直接模拟做了核对。

## 各语言说明

- Rust 在 `2..=L` 上用折叠计算递推式。
- Java 和 C++ 逐字节读取输入，从而保留每一个空格。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1098_math.cpp](1098_math.cpp) | G++ 13.2 x64 | math | O(L) | AC | 0.001 s | 188 KB |
| [1098_math.go](1098_math.go) | Go 1.14 x64 | math | O(L) | AC | 0.015 s | 1300 KB |
| [1098_math.java](1098_math.java) | Java 1.8 | math | O(L) | AC | 0.093 s | 496 KB |
| [1098_math.py](1098_math.py) | Python 3.12 x64 | math | O(L) | AC | 0.062 s | 496 KB |
| [1098_math.rs](1098_math.rs) | Rust 1.75 x64 | math | O(L) | AC | 0.015 s | 236 KB |
