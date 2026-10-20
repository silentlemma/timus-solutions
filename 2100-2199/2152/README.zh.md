# 2152. 修改 k 个包裹的一位数字来提高关税

[Timus 2152](https://acm.timus.ru/problem.aspx?space=1&num=2152) · 难度 1167 · greedy, sorting

原题作者 Ivan Sychev，出自 2020 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

包裹的重量每超出 mxw 一千克要付 a 个信用点，价格超出 mxp 的每个信用点要付 b%。n 个包裹中至多 k 个可以修改重量或价格的恰好一位数字。使总关税最大，并输出它以及每个包裹的新数据。任何最优的修改方案都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

n 和 k（1 ≤ n ≤ 2 · 10⁵，0 ≤ k ≤ n），然后是 mxw、mxp、a、b（1 ≤ mxw, mxp, a ≤ 10⁹，1 ≤ b ≤ 100），然后是各包裹的重量和价格，范围 1 到 10⁹。

## 输出

最大的总关税，然后是每个包裹的重量和价格。

## 评测方式

检查器以 10⁻⁹ 的相对误差核对总额，验证修改合法，并验证输出的数据给出该总额。

## 样例

### 样例 1

输入：

```
4 2
30 500 4 30
6 1100
60 90
9 990
91 420
```

输出：

```
3217.000000000
6 9100
60 90
9 990
91 920
```

## 解法

关税只会随重量和价格增大，所以一个包裹的最佳修改是让两个数之一尽可能大：把它第一个不是 9 的数位改成 9。比较对重量这样做和对价格这样做的收益，保留较好的；全是 9 的数无法再变大。

各包裹互不影响，所以排序后取 k 个最大的正收益。所有金额都以百分之一信用点为单位存成整数，因为整数信用点的 b% 至多有两位小数，所以总额是精确的。工作量 O(n log n)。

样例中价格 1100 变为 9100，420 变为 920，这是两个最大的收益。

## 各语言说明

- Python 在 PyPy 下运行：在 CPython 3.12 下它在第 9 个测试点超时（1.015 秒），而在 PyPy 3.10 下以 0.281 秒通过。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2152_greedy_sorting.cpp](2152_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(n log n) | AC | 0.140 s | 16016 KB |
| [2152_greedy_sorting.go](2152_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(n log n) | AC | 0.140 s | 23532 KB |
| [2152_greedy_sorting.java](2152_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(n log n) | AC | 0.281 s | 24904 KB |
| [2152_greedy_sorting.py](2152_greedy_sorting.py) | PyPy 3.10 x64 | greedy, sorting | O(n log n) | AC | 0.281 s | 18812 KB |
| [2152_greedy_sorting.rs](2152_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(n log n) | AC | 0.062 s | 19692 KB |
