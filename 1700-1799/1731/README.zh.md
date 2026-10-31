# 1731. 莳萝

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · 难度 106 · constructive

原题作者 Eugene Kurpilyansky（由 Sofia Tekhazheva 准备），出自 2009 年乌拉尔地区程序设计团队竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

为 n 箱第一种莳萝和 m 箱第二种莳萝选定质量——互不相同、不超过 10⁹ 的正整数——使得无法给两位邻居各送一箱每种莳萝且总质量相等。

## 输入

n 和 m（2 ≤ n, m ≤ 50）。

## 输出

一行 n 个第一种的质量，下一行 m 个第二种的质量。任何符合要求的质量都可以。

## 样例

### 样例 1

输入：

```
2 3
```

输出：

```
1 2
5 10 12
```

## 解法

两份礼物 a + b 和 a′ + b′ 没有共同的箱子；而有共同箱子的两个和本来就不同，因为所有质量互不相同。
所以条件就是全部 n·m 个和 a_i + b_j 互不相同。

取 a_i = i（i = 1..n），b_j = (j + 1)·n + 1（j = 0..m − 1）。于是 a_i + b_j = (j + 1)·n + 1 + i，
由于 i 取遍 1..n，这个和同时确定 i 和 j，就像 n 进制数确定末位和其余部分一样。所有质量互不相同，最大不到 3000。`O(n + m)`。

对样例得到 1 2 和 3 5 7，各和为 4、6、8、5、7、9。

注意事项：

- 答案总是存在，所以永远不输出 "It is a lie!"；
- 第二种不能与第一种的质量重复，所以从大于 n 开始。

检查程序验证数量、范围、互不相同以及所有和都不同。

## 优化解法

优化的 C++ 解法用 `scanf` 而不是 `std::cin` 读取 n 和 m，因此程序完全不引入
`iostream`；质量的输出方式不变：{1731_constructive_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐位读取 n 和 m，而不是创建 `Scanner`——后者的
初始化比程序其余部分都费时；输出的构造方式不变：
{1731_constructive_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1731_constructive_optimized.cpp`: 时间降低 +0.00%; 内存降低 +67.02%; 基础版本: `1731_constructive.cpp`.

- `1731_constructive_optimized.java`: 时间降低 +45.61%; 内存降低 +76.20%; 基础版本: `1731_constructive.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1731_constructive.go](1731_constructive.go).
- [1731_constructive.rs](1731_constructive.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 376 KB | 11304041 |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB | 11289416 |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB | 11289419 |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB | 11289417 |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.046 s | 220 KB | 11304042 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive_optimized.cpp](1731_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 124 KB | 11304262 |
| [1731_constructive_optimized.java](1731_constructive_optimized.java) | Java 1.8 | constructive | O(n + m) | AC | 0.093 s | 376 KB | 11304040 |
