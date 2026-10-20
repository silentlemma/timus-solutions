# 2149. 把 ASCII 鸽子转成整齐的图案

[Timus 2149](https://acm.timus.ru/problem.aspx?space=1&num=2149) · 难度 148 · implementation

原题作者 Kirill Borozdin，出自 2019 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 只鸽子排成一排（n 为偶数），每只朝左或朝右，用 ASCII 字符画出。当左半边朝一个方向、右半边朝另一个方向，或者偶数位置的鸽子朝一个方向、奇数位置的朝另一个方向时，这一排就是整齐的。求最少需要转身的鸽子数。时间限制 0.5 秒，内存限制 256 MB。

## 输入

n（2 ≤ n ≤ 100），然后是三行、每行 5n − 1 个字符的鸽子图：朝左的鸽子为 `<@..`、`.OO=`、`./\.`，朝右的为 `..@>`、`=OO.`、`./\.`，相邻鸽子之间用一列点隔开。

## 输出

最少的转身次数。

## 样例

### 样例 1

输入：

```
8
..@>.<@...<@.....@>...@>...@>.<@...<@..
=OO...OO=..OO=.=OO..=OO..=OO...OO=..OO=
./\.../\.../\.../\.../\.../\.../\.../\.
```

输出：

```
4
```

### 样例 2

输入：

```
4
..@>...@>.<@.....@>
=OO..=OO...OO=.=OO.
./\.../\.../\.../\.
```

输出：

```
1
```

## 解法

只需要第一行：第 i 只鸽子朝左当且仅当位置 5i 上的字符是 `<`。整齐的图案共有四种，分成两对互为相反的图案。统计与"左半边朝左、右半边朝右"不同的鸽子数；与之相反的图案恰好在其余鸽子上不同，所以需要 n 减去这个数。"偶数位置朝左、奇数位置朝右"同理。答案是这四个数中的最小值，用时 O(n)。

第二个样例中只有第一只鸽子破坏了交替，所以转一只就够了。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2149_implementation.cpp](2149_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 400 KB |
| [2149_implementation.go](2149_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1100 KB |
| [2149_implementation.java](2149_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1612 KB |
| [2149_implementation.py](2149_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 412 KB |
| [2149_implementation.rs](2149_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 240 KB |
