# 1048. 两个百万位数相加

[Timus 1048](https://acm.timus.ru/problem.aspx?space=1&num=1048) · 难度 200 · implementation

原题作者 Stanislav Vasiliev 和 Alexander Klepinin，出自 2000 年 3 月 25 日乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两个正整数各有 `N` 位（`1 ≤ N ≤ 10^6`，允许前导零），它们的和也不超过 `N` 位。数字按列给出：第 `i` 行是两个数
各自的第 `i` 位数字。输出恰好 `N` 位的和。

时间限制：2 秒。内存限制：16 MB。

## 输入

`N`，然后 `N` 行，每行两个用空格分开的数字。

## 输出

在一行中输出和的 `N` 位数字。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
4
0 4
4 2
6 8
3 7
```

输出：

```
4750
```

### 样例 2

输入：

```
3
0 0
4 5
5 5
```

输出：

```
100
```

## 题解

竖式加法：把每列的和（0 到 18）存进字节数组，然后从最后一列向第一列走，加上进位，保留 `t mod 10`，新进位为
`t div 10`。同一个 `N` 字节的数组直接变成答案的各位数字。时间 `O(N)`，内存 `N` 字节。

难点只在规模：约 4 MB 的输入，而内存限制是 16 MB。必须快速读入，并且不能为每一位保存对象或 4 字节整数。

注意事项：

- 和的前导零也要输出：输出恰好 `N` 位；
- 进位可能贯穿全部一百万位（`0999…9 + 000…1`）；
- 没有必要把数转换成大整数类型，而且在很多语言里这是平方复杂度的。

## 各语言说明

- **C++**、**Java**：用 `fread` / `DataInputStream` 做带缓冲的逐字节读入；**Go**：`bufio.Reader.ReadByte`；
  **Rust**：把全部输入读进一个字节向量。
- **Python**：全部输入是一个 `bytes` 对象；`translate` 删去空白字符，步长为 2 的切片分出两个数，进位循环写入
  `bytearray`。用 `int()` 转换会是平方复杂度的（而且 Python 3.12 默认拒绝超过 4300 位的字符串）。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1048_implementation.cpp](1048_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 1184 KB |
| [1048_implementation.go](1048_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.062 s | 1976 KB |
| [1048_implementation.java](1048_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.140 s | 2080 KB |
| [1048_implementation.py](1048_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.406 s | 10360 KB |
| [1048_implementation.rs](1048_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 10248 KB |
