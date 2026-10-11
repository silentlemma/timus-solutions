# 1319. 旅馆

[Timus 1319](https://acm.timus.ru/problem.aspx?space=1&num=1319) · 难度 39 · implementation

原题作者 Stanislav Vasiliev，出自 2004 年 3 月 11–16 日在叶卡捷琳堡举行的第八届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

旅馆的信件架是一个 N × N 的格子块（1 ≤ N ≤ 100），沿对角线编号：1 号在右上角，每条对角线从上往下编号，
各条对角线依次向左下角推进，左下角是 N²。输出编好号的表格。

时间限制：1 秒。内存限制：64 MB。

## 输入

整数 N。

## 输出

N 行，每行 N 个用空格分隔的数。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
4 2 1
7 5 3
9 8 6
```

## 解法

同一条对角线上的格子，列号 − 行号相同。让这个差从 N − 1 递减到 −(N − 1)，每条对角线内按行从上到下，
得到的正是编号顺序。`O(N²)`。

注意事项：

- 第一条对角线是右上角的单个格子，不是主对角线（测试 01）；
- N = 1 时只有一个格子，写 1（测试 02）。

## 各语言说明

- 五种解答都以同样的方式填表，最后输出。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1319_implementation.cpp](1319_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB |
| [1319_implementation.go](1319_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1188 KB |
| [1319_implementation.java](1319_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 2008 KB |
| [1319_implementation.py](1319_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 888 KB |
| [1319_implementation.rs](1319_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.001 s | 364 KB |
