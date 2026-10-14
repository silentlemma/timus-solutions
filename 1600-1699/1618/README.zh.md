# 1618. Arrays Printing

[Timus 1618](https://acm.timus.ru/problem.aspx?space=1&num=1618) · 难度 4269 · combinatorics

原题出自 2008 年冬季彼得罗扎沃茨克集训的 SPbSU ITMO Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

形如 `new Object[a1][a2]…[an][0]` 的 Java 数组（n ≤ 100，a1 · … · an ≤ 512）
用 `Arrays.deepToString` 打印，得到字符串 S（最多 10⁵ 个字符）。数组元素是引用，
所以同一个数组对象可以出现在多个位置。两种配置相同，当且仅当在一种配置中任意两条
下标路径指向同一对象时，在另一种中也是如此。求打印结果为 S 的配置数，模 10007。

时间限制：2 秒。内存限制：64 MB。

## 输入

字符串 S。

## 输出

配置数模 10007。

## 样例

### 样例 1

输入：

```
[[], []]
```

输出：

```
2
```

### 样例 2

输入：

```
[[[[]]]]
```

输出：

```
1
```

### 样例 3

输入：

```
[[[]], [[]]]
```

输出：

```
3
```

## 解法

解析括号得到各维大小 a1、…、an。从底层往上数。m 个指向空数组的引用可以任意分组为
对象：这是集合划分，共 B(m) 种（贝尔数）。往上一层，m 个指向宽度为 w 的数组的引用先
被分成 k 个不同对象，有 S(m, k) 种方式（第二类斯特林数）；这 k 个对象共有 k · w 个指向
下一层的引用，它们独立配置：

f(m) = Σₖ S(m, k) · g(k · w)，

其中 g 是下一层的计数。不同的对象仍可以持有相同的引用，所以下一层不受约束。根是一个含
a1 个引用的数组，答案就是最上层的 f(a1)。m 不会超过 512 / w，也不会超过该深度的位置数，
所以计算量不超过 n · 512² / 2 次乘法。`O(n · 512²)`。

易错点：

- 单独的 `[]` 没有引用，恰有一种配置（测试 04）；
- 第一个样例中的两个数组可以是同一个对象，也可以不是：答案 2；
- 计数增长很快，从斯特林数表开始就取模 10007。

在 100 个随机形状上，答案与一个独立的已通过实现一致。

## 各语言说明

- Python 在 PyPy 下运行：CPython 在评测的第 6 个测试上超过 2 秒的限制。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1618_combinatorics.cpp](1618_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n · 512²) | AC | 0.015 s | 1212 KB |
| [1618_combinatorics.go](1618_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n · 512²) | AC | 0.031 s | 4348 KB |
| [1618_combinatorics.java](1618_combinatorics.java) | Java 1.8 | combinatorics | O(n · 512²) | AC | 0.156 s | 2872 KB |
| [1618_combinatorics.py](1618_combinatorics.py) | PyPy 3.10 x64 | combinatorics | O(n · 512²) | AC | 0.421 s | 6788 KB |
| [1618_combinatorics.rs](1618_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n · 512²) | AC | 0.031 s | 2468 KB |
