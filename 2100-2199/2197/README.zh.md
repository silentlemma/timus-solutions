# 2197. 块覆盖下字符串的最短重复前缀

[Timus 2197](https://acm.timus.ru/problem.aspx?space=1&num=2197) · 难度 2200 · hashing, fenwick

原题作者 Konstantin Rychkov，出自 2024 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

长度为 N 的字符串 S 由它某个前缀的若干份拷贝打印而成，打印一次长度为 l 的前缀需要 l² 秒。共有 Q 次操作，每次用固定集合中的某个模式串 t_k 从位置 p 开始覆盖 S。输出初始字符串以及每次覆盖后的最少打印时间。时间限制 3 秒，内存限制 256 MB。

## 输入

N、M 和 Q（1 ≤ N ≤ 2 · 10⁵，0 ≤ M, Q ≤ 2 · 10⁵），然后是 S，然后是总长不超过 10⁶ 的 M 个模式串，然后是覆盖操作 p k。

## 输出

Q + 1 个时间。

## 样例

### 样例 1

输入：

```
4 3 3
abab
be
ebb
ee
3 1
1 2
2 3
```

输出：

```
8
16
16
4
```

## 解法

打印长度为 l 的前缀 N / l 次需要 N · l 秒，所以要找的是整除 N 且能生成 S 的最短长度 l。

整除 N 且能生成 S 的长度对 gcd 封闭，所以最短的那个整除其他所有的。从 l = N 开始，解法对 N 的每个质因数，只要更短的前缀仍能生成 S，就把 l 除以它；最后剩下的就是最短周期。长度为 c 的前缀能生成 S，当且仅当 S 的哈希等于该前缀重复 N / c 次的哈希，即几何级数 h(prefix) · (B^N − 1) / (B^c − 1)，乘开分母后比较。使用两个模数使碰撞可以忽略。

难点在于对一个会被长段覆盖的字符串求哈希。所有可能出现的文本，即 S 和全部模式串，被放进一个带前缀哈希的源串。当前的 S 是一列片段，每个片段指向源串中的一段，并保存已按其在 S 中位置平移过的哈希，按起始位置存放在树状数组中。一次覆盖在两端切开片段，删掉内部的片段，再为模式串加入一个片段，所以每次覆盖只产生常数个片段。前缀哈希是完整片段上的树状数组前缀和，加上从源串读出的最后一个片段的部分哈希。答案还按整个字符串的哈希缓存。

样例中 "abab" 的周期为 2，时间为 4 · 2 = 8；"eeee" 的周期为 1，时间为 4。

每次查询对 N 的每个质因数花费 O(log N)，覆盖操作对每个产生或删除的片段花费 O(log N)。

## 各语言说明

- Python 在 PyPy 下运行，以 2.593 秒通过（限制 3 秒）。它还会跳过副本数不能整除字符编码之和的周期，因为重复一个前缀也会重复这个和。在 CPython 3.12 下，这里最大的测试已经需要约 2.7 秒，因此不使用它。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2197_hashing_fenwick.cpp](2197_hashing_fenwick.cpp) | G++ 13.2 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.375 s | 32896 KB |
| [2197_hashing_fenwick.go](2197_hashing_fenwick.go) | Go 1.14 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.468 s | 65604 KB |
| [2197_hashing_fenwick.java](2197_hashing_fenwick.java) | Java 1.8 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 1.250 s | 71216 KB |
| [2197_hashing_fenwick.py](2197_hashing_fenwick.py) | PyPy 3.10 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 2.593 s | 94140 KB |
| [2197_hashing_fenwick.rs](2197_hashing_fenwick.rs) | Rust 1.75 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.328 s | 45500 KB |
