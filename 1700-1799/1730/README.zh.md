# 1730. 人熊猪

[Timus 1730](https://acm.timus.ru/problem.aspx?space=1&num=1730) · 难度 1147 · constructive

原题作者 Fedor Fominykh（由 Ivan Burmistrov 准备），出自 2009 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两个生物杂交得到的生物中，每种动物的比例是两者比例的平均值。给定一个生物的动物组成及比例，写出产生它的谱系：
一列行，每行是一种动物或之前两行的杂交，最后一行是该生物本身，并且除最后一行外每行都参与某次杂交。不存在时输出 `No solution`。

## 输入

生物的名称：一到十个不同的动物名用连字符连接，不超过 200 个字符。然后是每种动物的比例，形如 a/b（1 ≤ a ≤ b ≤ 1500）；比例之和为 1。

## 输出

行数 n（1 ≤ n ≤ 10 000）和各行，或者 `No solution`。任何符合要求的谱系都可以。

## 样例

### 样例 1

输入：

```
man-bear-pig
1/2 1/4 1/4
```

输出：

```
7
man
pig
1 2
bear
man
4 5
3 6
```

### 样例 2

输入：

```
man
1/1
```

输出：

```
1
man
```

### 样例 3

输入：

```
man-bear-pig
1/3 1/3 1/3
```

输出：

```
No solution
```

## 解法

杂交时每个比例都是两个比例的平均值，所以由归纳法，任何谱系中任何比例的分母都是 2 的幂。若某个既约比例不是这样，则无解。

否则设 L 为最大的既约分母，不超过 1024。按顺序给每种动物分配 L 个等份叶子中属于它的那部分，在叶子上建一棵平衡二叉树：
每个内部结点杂交它的两半，于是每片叶子恰好贡献生物的 1/L。叶子全是同一种动物的子树就是这种动物本身，因此只占一行。
最多输出 2L − 1 ≤ 2047 行。`O(L)`。

样例 1 中 L = 4，叶子为 man、man、bear、pig。左半是纯 man，右半是 bear 与 pig 杂交，所以谱系为 man、bear、pig、2 3、1 4。

注意事项：

- 比例给出时未约分，例如 750/1500，必须先约分再看分母；
- 纯动物的谱系只有一行，没有任何杂交；
- 同一种动物可以出现在多行中。

检查程序用精确分数重放谱系，检查比例、行引用以及每个祖先都被使用。在 200 个随机数据上谱系都通过检查，
并且输出 `No solution` 的情况与一个独立的已通过实现完全一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1730_constructive.cpp](1730_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.015 s | 428 KB |
| [1730_constructive.go](1730_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.031 s | 1176 KB |
| [1730_constructive.java](1730_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.125 s | 1704 KB |
| [1730_constructive.py](1730_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.093 s | 504 KB |
| [1730_constructive.rs](1730_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.015 s | 244 KB |
