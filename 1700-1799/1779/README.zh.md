# 1779. 伟大的队伍

[Timus 1779](https://acm.timus.ru/problem.aspx?space=1&num=1779) · 难度 339 · constructive

原题作者 Ivan Burmistrov，出自第十五届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在 n 名学生上构造一个朋友关系图，使任意三名学生的朋友数不全相同；或报告不存在这样的图。

## 输入

n（3 ≤ n ≤ 200）。

## 输出

朋友对的数目和这些对；若没有合适的图，输出 −1。任何符合要求的图都可以。

## 样例

### 样例 1

输入：

```
4
```

输出：

```
2
1 3
3 4
```

## 解法

当 i + j > n 时连接学生 i 和 j。这样学生 i 与 n − i + 1、…、n 这 i 名学生为友，若他自己在其中（即 2i > n）则去掉自己。
所以 i ≤ n/2 时学生 i 有 i 个朋友，i > n/2 时有 i − 1 个：朋友数到中间为 1、2、…，之后继续递增，只有中间那个数被两名学生共有。
因此这样的图总是存在，从不输出 −1。`O(n²)`。

四名学生时得到 1–4、2–3、2–4、3–4，朋友数分别为 1、2、2、3，与样例的答案同样符合要求。

注意事项：

- n − 1 个朋友与 0 个朋友不能同时出现，所以 0 到 n − 1 的朋友数不可能全不相同，必有两名学生共用一个；
- 图可能很稠密，约 n²/4 对，所以输出很大；
- 答案不唯一，所以检查器自己统计朋友数。

对 3 到 200 的每个 n，这一构造都通过了检查器，一个独立的已通过实现也是如此。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1779_constructive.cpp](1779_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 292 KB |
| [1779_constructive.go](1779_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.015 s | 2140 KB |
| [1779_constructive.java](1779_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 2568 KB |
| [1779_constructive.py](1779_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.093 s | 1952 KB |
| [1779_constructive.rs](1779_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.015 s | 644 KB |
