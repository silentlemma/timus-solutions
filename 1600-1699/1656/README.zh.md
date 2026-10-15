# 1656. 远方王国的军队

[Timus 1656](https://acm.timus.ru/problem.aspx?space=1&num=1656) · 难度 206 · constructive

原题作者 Vladimir Yakovlev（创意来自 Magaz Asanov），出自 NEERC 2008 东部分区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 n² 名给定身高的士兵排成 n × n 的方阵，使每一行、每一列最高的人站在中间，从中间到两端身高都不增加。

## 输入

奇数 n（3 到 9），然后是 n² 个 170 到 200 的身高。

## 输出

方阵，n 行，每行 n 个身高。任何合法排列都被接受。

## 样例

### 样例 1

输入：

```
3
170
170
180
175
170
175
175
170
175
```

输出：

```
170 175 170
175 180 175
170 175 170
```

## 解法

按格子到中心行和中心列距离的二元组（较小者，较大者）给格子排序，把最高的士兵分给排名最靠前的格子。
在距中心为 a 的一行中，距离为 b 的格子排名在 b < a 时为 (b, a)，之后为 (a, b)：无论哪种情况排名都随 b
增大而增大，所以在中间两侧身高都向外不增加。列由对称性同理。排名相同的格子互为镜像，不会位于同一条线的
同一侧。`O(n² log n)`；Go 的稳定排序：`O(n² log² n)`。

易错点：

- “向两端不增加”允许身高相等（测试 02）；
- 合法排列很多，所以检查器验证规则和身高集合。

程序给出的方阵在 90 支随机军队上都能通过检查器。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1656_constructive.cpp](1656_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.015 s | 200 KB |
| [1656_constructive.go](1656_constructive.go) | Go 1.14 x64 | constructive | O(n² log² n) | AC | 0.031 s | 1152 KB |
| [1656_constructive.java](1656_constructive.java) | Java 1.8 | constructive | O(n² log n) | AC | 0.156 s | 4188 KB |
| [1656_constructive.py](1656_constructive.py) | Python 3.12 x64 | constructive | O(n² log n) | AC | 0.078 s | 448 KB |
| [1656_constructive.rs](1656_constructive.rs) | Rust 1.75 x64 | constructive | O(n² log n) | AC | 0.015 s | 240 KB |
