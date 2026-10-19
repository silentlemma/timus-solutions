# 1832. 阿里郎表演

[Timus 1832](https://acm.timus.ru/problem.aspx?space=1&num=1832) · 难度 953 · constructive

原题作者 Victor Kamashev（由 Daniil Aizenshtein 准备），出自 2011 年 4 月第十五届乌拉尔竞技编程公开锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 名演员站成一排，分成 d 个圆圈舞，d 是 n 的一个未知真因子：第 j 个圆圈由演员 j, j + d, j + 2d, … 围成。
从 26 种颜色中为衬衫选色，使得无论 d 取何值，每个圆圈中相邻的演员颜色都不同；若做不到则报告不可能。

## 输入

n（2 ≤ n ≤ 300000）。

## 输出

n 个小写字母表示演员的颜色，或输出 "Impossible"。任何合法的着色都可以。

## 样例

### 样例 1

输入：

```
7
```

输出：

```
acacbdb
```

## 解法

演员从 0 开始编号。两名演员在某个 d 下相邻，当且仅当它们相距 d 或 n − d，其中 d 是 n 的真因子。

设 m 是不整除 n 的最小正整数。那么 m 也不整除任何真因子，所以按 x mod m 着色能区分任意两个相距 d 的演员。由于 lcm(1, …, 13) = 360360 超过 300000，m 至多为 13。

剩下的是跨越圆圈接口、相距 n − d 的对。设 p 是 n 的最小素因子，每个真因子都不超过 n/p，因此这些距离至少为 n − n/p。
把这一排分成前 n − n/p 名和后 n/p 名演员：由于 n/p ≤ n − n/p，两部分内部都没有这么长的距离。
两部分都按 x mod m 着色，第二部分使用另外 m 个字母。这样部分内部的对没问题，跨部分的对颜色永不相同。最多使用 2m ≤ 26 个字母，所以答案永远不是 "Impossible"。`O(n)`。

当 n = 7 时 m = 2，p = 7：前六名演员交替为 a 和 b，最后一名为 c，得到 abababc；样例答案是另一种合法着色。

注意事项：

- 圆圈是闭合的，所以相距 n − d 的演员也相邻；
- 当 d = n/2 时一个圆圈只有两名演员，这也是一对相邻者；
- 只按 x mod m 着色会在接口处出错：n = 7 时演员 0 和 6 会同色。

从 2 到 3000 的每个 n 以及许多大的 n（包括构造使用全部 26 个字母的情形）都对每个真因子做过检查。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1832_constructive.cpp](1832_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 476 KB |
| [1832_constructive.go](1832_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 2192 KB |
| [1832_constructive.java](1832_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 2708 KB |
| [1832_constructive.py](1832_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.140 s | 5448 KB |
| [1832_constructive.rs](1832_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 492 KB |
