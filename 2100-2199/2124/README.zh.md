# 2124. 区间乘法下区间生成子群的阶

[Timus 2124](https://acm.timus.ru/problem.aspx?space=1&num=2124) · 难度 1303 · number_theory, segment_tree

原题作者 Alexey Danilyuk，出自 2018 年夏季彼得罗扎沃茨克集训营 t.me/umnik_team 专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在模素数 p 的乘法群中进行运算。一个由 n 个剩余组成的数组有 q 个询问：把 [l, r] 中每个元素乘以 x，或者输出由 [l, r] 中元素生成的子群的阶。时间限制 4 秒，内存限制 256 MB。

## 输入

p、n 和 q（2 ≤ p < 10⁹ 为素数，1 ≤ n, q ≤ 10⁵），数组（1 ≤ aᵢ < p），以及询问 "1 l r x" 和 "2 l r"，其中 1 ≤ l ≤ r ≤ n，1 ≤ x < p。

## 输出

每个第二类询问的答案。

## 样例

### 样例 1

输入：

```
17 3 7
10 16 2
2 2 3
2 1 2
2 2 2
1 1 2 3
2 1 1
2 3 3
2 1 3
```

输出：

```
8
16
2
4
8
16
```

## 解法

该群是阶为 m = p − 1 的循环群。对生成元 g，元素 gᵉ 生成指数为 gcd(e, m) 的子群，而一个集合生成的子群，其指数是各元素指数的最大公约数；阶等于 m 除以这个指数。单个元素 a 的指数为 m / ord(a)，ord(a) 由 m 的素因子求出：从 m 开始，只要 a 的（当前阶 / q）次幂仍为 1，就除以素数 q。不需要离散对数。

区间乘法会改变很多元素，所以改为存储比值 bᵢ = aᵢ / aᵢ₋₁（b₁ = a₁）。把 [l, r] 乘以 x 就是把 b_l 乘以 x、把 b_{r+1} 乘以 x⁻¹，两次单点修改。元素 a_l, a_{l+1}, …, a_r 与 a_l, b_{l+1}, …, b_r 生成同一个子群，因为两个集合可以互相表示。于是：

- 线段树维护各比值指数的最大公约数，给出 b_{l+1} … b_r 上的最大公约数；
- 树状数组维护边界修改的乘数；其前缀乘积乘以初始 a_l，便得到当前 a_l。

询问时求出 a_l 的指数，与线段树结果取最大公约数，输出 m 除以它。C++、Go、Java 和 Rust 每次修改或询问需要 O(log n) 次树操作，以及求阶和逆元的 O(log² p) 次模运算。试除分解需要 O(sqrt p)，初始比值的指数需要 O(n log² p)。逆元由费马小定理求得。

Python 的备用分支延迟计算比值的指数，并在每个节点缓存与已检查除数的最大公约数投影。因此单次询问可能访问 O(n) 个节点，不能套用其他版本的单次询问界限。两次失效之间，缓存的已检查除数按整除关系至多增长 O(log p) 次。每次修改使 O(log n) 个节点失效，而计算未缓存投影需要 O(log² p)，从而得到表中的保守总摊还界限。S 表示 Python 搜索原根和建立对数表的开销，备用分支中 S = 0。

易错点：测试 11 覆盖素数幂（p = 257），测试 13 覆盖八个不同素因子；选择 Python 分支时两种情形都要考虑。这并不保证延迟询问总是对数时间：当 p = 999999503、n = 100000 且所有元素均为 1 时，首个询问 `2 1 100000` 正确输出 1，但会完成 O(n) 的延迟树计算。

样例中 p = 17，m = 16。元素 16 = −1 的阶为 2，而 10 和 16 一起生成阶为 16 的子群，即整个群。

## 各语言说明

- 当每个素数幂分量都能放入一个表，或拆为两个数位且各表不超过 min(65536, n + q) 项时，Python 使用离散对数。互素分量可以共用一个表，再通过中国剩余定理合并对数。此时区间乘法变为指数坐标中的加法，使用维护 gcd 的线段树和加法树状数组。否则使用上述延迟计算比值指数的备用分支。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2124_number_theory_segment_tree.cpp](2124_number_theory_segment_tree.cpp) | G++ 13.2 x64 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 1.015 s | 4244 KB |
| [2124_number_theory_segment_tree.go](2124_number_theory_segment_tree.go) | Go 1.14 x64 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 1.156 s | 14484 KB |
| [2124_number_theory_segment_tree.java](2124_number_theory_segment_tree.java) | Java 1.8 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 1.593 s | 7364 KB |
| [2124_number_theory_segment_tree.py](2124_number_theory_segment_tree.py) | PyPy 3.10 x64 | number_theory, segment_tree | O(sqrt p + S + (n + q log(n + 1)) log^3 p) | AC | 2.046 s | 51480 KB |
| [2124_number_theory_segment_tree.rs](2124_number_theory_segment_tree.rs) | Rust 1.75 x64 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 0.765 s | 10952 KB |
