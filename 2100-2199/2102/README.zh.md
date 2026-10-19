# 2102. 恰好二十个质因子

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · 难度 147 · number_theory

原题作者 Vladimir Leskov，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

判断 n 的质因数分解中指数之和是否恰好为 20，即 n 是否恰好是 20 个（计重数）质数之积。时间限制 2 秒，内存限制 64 MB。

## 输入

n（1 ≤ n ≤ 10¹⁸）。

## 输出

`Yes` 或 `No`。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
No
```

### 样例 2

输入：

```
1048576
```

输出：

```
Yes
```

### 样例 3

输入：

```
10000000000
```

输出：

```
Yes
```

## 解法

用从 2 到 B = 2·10⁶ 的每个 d 去除 n（当 d² ≤ n 时），统计除掉的质因子数。若循环因 d² 超过剩余部分而停止，剩下的是 1 或质数，贡献 0 或 1。否则剩余部分至少为 B² = 4·10¹²，因此已除掉的部分至多 10¹⁸ / B²，小于 2¹⁸，即目前不到 18 个因子；剩余部分没有小于 B 的因子且至多 10¹⁸ < B³，所以至多再贡献两个。总数不可能达到 20，答案为 No。时间复杂度为 O(min(sqrt n, B))。

第三个样例中 10¹⁰ = 2¹⁰ · 5¹⁰ 有 20 个质因子。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 124 KB |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.156 s | 1636 KB |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.484 s | 428 KB |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB |
