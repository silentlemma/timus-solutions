# 1731. 莳萝

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · 难度 105 · constructive

原题作者 Eugene Kurpilyansky（由 Sofia Tekhazheva 准备），出自 2009 年乌拉尔地区中学生程序设计竞赛。

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

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 380 KB |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.015 s | 224 KB |
