# 1491. 不真实的故事

[Timus 1491](https://acm.timus.ru/problem.aspx?space=1&num=1491) · 难度 205 · prefix_sums

原题作者 Alexander Toropov，出自 2006 年 10 月 14 日第十三届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 名骑士（2 ≤ N ≤ 100000）编号 1 到 N。国王说出 a、b、c，编号从 a 到 b 的每名骑
士得到 c 枚金币；接着每名骑士再说出一组 a_i、b_i、c_i，效果相同
（1 ≤ a ≤ b ≤ N，1 ≤ c ≤ 10000）。输出每名骑士得到的金币数。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，国王的三元组，然后是骑士们的 N 个三元组。

## 输出

N 个总数，以空格分隔。

## 样例

### 样例 1

输入:

```
4
2 3 2
2 4 1
3 4 1
1 2 1
1 1 1
```

输出:

```
2 4 4 2
```

### 样例 2

输入:

```
7
1 7 1
2 3 4
3 5 3
1 2 1
5 7 4
2 4 10
3 4 2
1 6 3
```

输出:

```
5 19 23 19 11 8 5
```

## 解法

N + 1 次区间加法，每次长达 10⁵，逐个处理太慢。差分数组把给 a..b 的骑士各 c 枚金币
记为位置 a 加 c、位置 b + 1 减 c；然后对数组求前缀和，就得到每名骑士的总数。
`O(N)`。

注意事项：

- 国王的三元组也是一次赏赐，所以共有 N + 1 次（测试 01、02）；
- 总数可达 100001 · 10000 ≈ 10⁹，接近 32 位上限，所以用 64 位保存（gen2）；
- 关于骑士自身座位的条件对计算毫无影响（所有测试）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1491_prefix_sums.cpp](1491_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.187 s | 980 KB |
| [1491_prefix_sums.go](1491_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 4540 KB |
| [1491_prefix_sums.java](1491_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 8872 KB |
| [1491_prefix_sums.py](1491_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.328 s | 35944 KB |
| [1491_prefix_sums.rs](1491_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 9428 KB |
