# 2212. 把 Q 次前缀和写成一次卷积

[Timus 2212](https://acm.timus.ru/problem.aspx?space=1&num=2212) · 难度 1009 · math, combinatorics

原题作者 Yackov Malin，出自 2024 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N 个数组成的数组连续 Q 次被替换为它的前缀和。输出结果对 998 244 353 取模。时间限制 2 秒，内存限制 256 MB。

## 输入

N 和 Q（2 ≤ N ≤ 10⁵，1 ≤ Q ≤ 10⁷），然后是取值 1 到 10⁸ 的数组。

## 输出

最终数组对 998 244 353 取模。

## 样例

### 样例 1

输入：

```
3 2
1 2 3
```

输出：

```
1 4 10
```

## 解法

一次前缀和把数组的生成函数乘以 1 / (1 − x)，所以 Q 次就是乘以 1 / (1 − x)^Q，其系数为 C(Q + k − 1, k)。答案是卷积

pᵢ = 对 j ≤ i 求和 C(Q + i − j − 1, i − j) · vⱼ。

这些系数可以依次得到：第 k 个等于前一个乘以 (Q + k − 1) / k，1 … N 的模逆元用常见的线性递推求出。

卷积用数论变换在模 998 244 353 下完成，这个模数正是为它选的。Python 则把两个序列打包成巨大的十进制数，每个元素占 22 位。乘积的每个精确系数都小于 10⁵ · 10⁸ · 10⁹，所以各槽位之间不会溢出，内置的十进制乘法内部就会做快速变换；然后对每个槽位取模 998 244 353。

样例中 Q = 2 给出系数 1、2、3，所以最后一个值为 3 · 1 + 2 · 2 + 1 · 3 = 10。

复杂度 O(N log N)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2212_math_combinatorics.cpp](2212_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(N log N) | AC | 0.093 s | 2180 KB |
| [2212_math_combinatorics.go](2212_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(N log N) | AC | 0.125 s | 9012 KB |
| [2212_math_combinatorics.java](2212_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(N log N) | AC | 0.500 s | 9564 KB |
| [2212_math_combinatorics.py](2212_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(N log N) | AC | 0.765 s | 31896 KB |
| [2212_math_combinatorics.rs](2212_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(N log N) | AC | 0.062 s | 8384 KB |
