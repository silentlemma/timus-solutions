# 1375. 不随大流

[Timus 1375](https://acm.timus.ru/problem.aspx?space=1&num=1375) · 难度 541 · number_theory

原题作者 Den Raskovalov，出自 2005 年 4 月 19–24 日在叶卡捷琳堡举行的第九届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定素数 p ≤ 10⁶ 和 0 ≤ k ≤ p − 1，输出任意一对 0 到 p − 1 之间的 x、y，使 x² + y² ≡ k (mod p)；若不存在则输出
`NO SOLUTION`。

时间限制：1 秒。内存限制：64 MB。

## 输入

k 和 p。

## 输出

x 和 y，或 `NO SOLUTION`。

## 样例

### 样例 1

输入：

```
1 3
```

输出：

```
0 2
```

## 解法

对奇素数 p，平方数模 p 取 (p + 1) / 2 个不同的值，k − x² 也取同样多个值。p 个数中的两个各含 (p + 1) / 2 个值的集合
必然相交，所以总有 x² 与 y² 之和为 k：答案总是存在，永远不会输出 `NO SOLUTION`。p = 2 时，任何 k 都等于 0² + 0² 或
1² + 0²。

求解时，先为每个平方数记下一个平方根：对 0 到 p − 1 的 y，把 y 记为 y² mod p 的根。然后依次尝试 x = 0, 1, 2, …，
直到 k − x² mod p 有根为止。大约一半的值是平方数，所以几乎立刻就能结束。`O(p)`。

注意事项：

- k = 0 时答案是 0 0（测试 07）；
- k − x² 要取模 p 的非负值；
- y² 可接近 10¹²，超出 32 位整数。

对 300 以内的所有素数和所有 k 检查过答案，测试由接受任意一对答案的检查程序评判。

## 各语言说明

- 五种解答都把平方根表存放在一个长度为 p 的数组中。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1375_number_theory.cpp](1375_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p) | AC | 0.031 s | 3656 KB |
| [1375_number_theory.go](1375_number_theory.go) | Go 1.14 x64 | number_theory | O(p) | AC | 0.062 s | 9624 KB |
| [1375_number_theory.java](1375_number_theory.java) | Java 1.8 | number_theory | O(p) | AC | 0.156 s | 5172 KB |
| [1375_number_theory.py](1375_number_theory.py) | Python 3.12 x64 | number_theory | O(p) | AC | 0.359 s | 23992 KB |
| [1375_number_theory.rs](1375_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p) | AC | 0.046 s | 7892 KB |
