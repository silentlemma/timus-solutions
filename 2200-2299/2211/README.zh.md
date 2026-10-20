# 2211. 统计边长为整数且面积为给定整数的三角形

[Timus 2211](https://acm.timus.ru/problem.aspx?space=1&num=2211) · 难度 1875 · number_theory

原题作者 Vadim Barinov，出自 2023 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计边长为整数、面积恰为 S 的三角形个数，边长多重集相同的三角形视为同一个。时间限制 0.5 秒，内存限制 256 MB。

## 输入

S（1 ≤ S ≤ 10⁹）。

## 输出

三角形的个数。

## 样例

### 样例 1

输入：

```
6
```

输出：

```
1
```

## 解法

海伦公式给出 S² = p(p − a)(p − b)(p − c)，其中 p 为半周长。边长和面积都是整数的三角形，周长总是偶数且面积能被 6 整除，所以 S 不被 6 整除时答案为 0。否则 x = p − a、y = p − b、z = p − c 都是正整数，三边为 y + z、x + z 和 x + y，并且

xyz(x + y + z) = S²。

不同的三角形对应 x ≤ y ≤ z 的解。x 和 y 都整除 S²，所以解法根据 S 的分解列出 S² 的所有因数。对每个满足 3x⁴ ≤ S² 的 x，候选的 y ≥ x 一直到满足 y²(x + 2y) ≤ S² / x 的最大者，这保证 z ≥ y，用二分查找得到。当 xy 整除 S² 时，z 是 z² + (x + y)z − S² / (xy) = 0 的正根，它必须是整数：判别式 (x + y)² + 4S² / (xy) 必须是奇偶性合适的完全平方数。

样例中 S² = 36 = 1 · 2 · 3 · 6，所以 x, y, z = 1, 2, 3，三边为 5、4、3。

工作量受限于 x 和 y 都较小的 S² 的因数对，对所有不超过 10⁹ 的 S 都足够快。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2211_number_theory.cpp](2211_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.031 s | 852 KB |
| [2211_number_theory.go](2211_number_theory.go) | Go 1.14 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.046 s | 2740 KB |
| [2211_number_theory.java](2211_number_theory.java) | Java 1.8 | number_theory | O(d(S²) log d(S²)) | AC | 0.250 s | 3296 KB |
| [2211_number_theory.py](2211_number_theory.py) | PyPy 3.10 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.500 s | 7688 KB |
| [2211_number_theory.rs](2211_number_theory.rs) | Rust 1.75 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.046 s | 892 KB |
