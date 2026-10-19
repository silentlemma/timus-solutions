# 1893. A380

[Timus 1893](https://acm.timus.ru/problem.aspx?space=1&num=1893) · 难度 60 · implementation

原题作者 Denis Dublennykh，出自 NEERC 2011 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

根据排号和字母判断一个有效座位的位置。不同排号使用不同布局：

| 排号 | 按顺序排列的座位字母 | 过道位置 |
| --- | --- | --- |
| 1–2 | A B C D | A/B 之间及 C/D 之间 |
| 3–20 | A B C D E F | B/C 之间及 D/E 之间 |
| 21–65 | A B C D E F G H J K | C/D 之间及 G/H 之间 |

每排的第一个和最后一个座位靠窗。过道两侧的座位靠过道。若座位靠窗，
输出 `window`；否则若靠过道，输出 `aisle`；其余输出 `neither`。
靠窗的分类优先。

时间限制为 1 秒，内存限制为 64 MB。

## 输入

一个座位编号：先是排号，紧接着一个大写字母，例如 `3C`。
排号在 1 到 65 之间，字母保证在该排有效。经济舱各排省略字母 I。

## 输出

输出 `window`、`aisle` 或 `neither` 中的一个单词。

## 评测方式

输出按记号逐一比较。

## 样例

### 样例 1

输入：

```
3C
```

输出：

```
aisle
```

### 样例 2

输入：

```
64A
```

输出：

```
window
```

### 样例 3

输入：

```
21F
```

输出：

```
neither
```

## 解法

最后一个字符是座位字母，前面的数字是排号。选择三个排号区间之一，
按下表分类：

| 排号 | `window` | `aisle` | `neither` |
| --- | --- | --- | --- |
| 1–2 | A D | B C | 无 |
| 3–20 | A F | B C D E | 无 |
| 21–65 | A K | C D G H | B E F J |

这些集合直接来自每排两端及各过道的相邻座位。在第 1–2 排，A 和 D
既靠窗又靠过道；按靠窗优先的规则，得到上述分类。每个有效字母因此
都对应要求的结果。

检查次数和输入长度均为常数，因此时间和额外空间都是 `O(1)`。

样例中，第 3 排的 B 和 C 之间有过道，所以 `3C` 为 `aisle`。
`64A` 靠左侧窗户。`21F` 位于两条过道之间的中间座位块内部，不与
任何过道相邻，因此为 `neither`。

注意事项：

- 排号在 2/3 和 20/21 之间时布局改变；
- 最右侧靠窗字母依次为 D、F、K；
- 第 21–65 排没有座位 I；
- 先判断靠窗，尤其注意第 1–2 排的 A 和 D。

在全部 566 个有效座位上，答案与单独实现的座位布局模型一致。

## 各语言说明

五种实现都把最后一个 ASCII 字母之前的数字解析为排号，并使用同一套
固定大小的分类。Go 和 Rust 可以安全地按字节索引，因为合法输入只含
十进制数字和一个大写英文字母。

Java 用 `Scanner` 读取这个短记号。无需专门的快速输入或大整数类型；
成员检查仅涉及固定的座位字母集合。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1893_implementation.cpp](1893_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 348 KB |
| [1893_implementation.go](1893_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1104 KB |
| [1893_implementation.java](1893_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1580 KB |
| [1893_implementation.py](1893_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 468 KB |
| [1893_implementation.rs](1893_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB |
