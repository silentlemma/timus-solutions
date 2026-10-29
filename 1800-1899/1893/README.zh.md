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

行号是最后一个字符之前的数字，座位是最后一个字母。飞机有三种排布，每种排布决定
哪些座位靠窗、哪些靠过道：

| 排 | `window` | `aisle` | `neither` |
| --- | --- | --- | --- |
| 1–2 | A D | B C | 无 |
| 3–20 | A F | B C D E | 无 |
| 21–65 | A K | C D G H | B E F J |

在第 1–2 排，A 和 D 既靠窗又靠过道；靠窗优先，所以它们是 `window`。`O(1)`。

注意事项：

- 排布在第 2 排和第 20 排之后改变；
- 第 21–65 排没有座位 I。

## 优化解法

优化的 C++ 解法用 `scanf("%d%c")` 读入座位、用 `puts` 输出，而不是使用
`iostream` 和 `std::string`：120 KB，而不是 348 KB。座位排布不变。

优化的 Java 解法逐字节读取座位：数字组成排号，下一个字节是字母，而不是读入字符串：
0.109 s，而不是 0.156 s；380 KB，而不是 1580 KB。

## 各语言说明

没有特别需要注意的地方。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1893_implementation.cpp](1893_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 348 KB | 11291153 |
| [1893_implementation.go](1893_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1104 KB | 11291155 |
| [1893_implementation.java](1893_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1580 KB | 11291159 |
| [1893_implementation.py](1893_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 468 KB | 11291157 |
| [1893_implementation.rs](1893_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11291163 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1893_implementation_optimized.cpp](1893_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB | 11303647 |
| [1893_implementation_optimized.java](1893_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303785 |
