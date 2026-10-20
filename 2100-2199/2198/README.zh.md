# 2198. N 个顶点的所有有序有根树的高度总和

[Timus 2198](https://acm.timus.ru/problem.aspx?space=1&num=2198) · 难度 1368 · math, combinatorics

原题作者 Vadim Barinov，出自 2024 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

求所有 N 个顶点的有序有根树的高度之和，对 10⁹ + 7 取模。时间限制 1 秒，内存限制 256 MB。

## 输入

N（1 ≤ N ≤ 400）。

## 输出

和对 10⁹ + 7 取模。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
3
```

## 解法

绕着一棵有 e = N − 1 条边的有序树走一圈，每条边向下、向上各走一次，得到一条 2e 步的 Dyck 路径；这是一个双射，树的高度就是路径的最高层。总高度等于对 h ≥ 1 求到达第 h 层的路径数之和。

停留在第 0 层到第 h − 1 层之间的路径，可以通过关于 −1 和 h 两条直线的反射来计数，得到周期为 w = h + 1 的二项式系数交错和。用全部路径数减去它并重新整理，到达第 h 层的 Dyck 路径数为

对 k ≥ 1 求和 C(2e, e + kw − 1) − 2 C(2e, e + kw) + C(2e, e + kw + 1)，

且只有 kw ≤ e + 1 的项非零。所以答案是对宽度 w = 2 … e + 1 及其倍数的二重和，约 e ln e 项，二项式系数 C(2e, j) 用模逆元一次算好。

样例中 3 个顶点的两棵树是高度为 2 的路径和根带两片叶子、高度为 1 的树，所以答案为 3。

复杂度 O(N log N)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2198_math_combinatorics.cpp](2198_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(N log N) | AC | 0.015 s | 188 KB |
| [2198_math_combinatorics.go](2198_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(N log N) | AC | 0.031 s | 880 KB |
| [2198_math_combinatorics.java](2198_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(N log N) | AC | 0.140 s | 216 KB |
| [2198_math_combinatorics.py](2198_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(N log N) | AC | 0.078 s | 272 KB |
| [2198_math_combinatorics.rs](2198_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(N log N) | AC | 0.031 s | 24 KB |
