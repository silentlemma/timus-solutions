# 1821. 冬季两项

[Timus 1821](https://acm.timus.ru/problem.aspx?space=1&num=1821) · 难度 178 · sorting

原题作者 Alexander Ipatov 和 Alexey Samsonov，出自 2011 年 3 月 19 日第十二届乌拉尔国立大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在间隔出发的比赛中，选手依次出发，间隔 30 秒。记分牌显示已到达终点的选手中用时最好的那一位。
按出发顺序给出选手及其比赛用时，列出所有曾出现在记分牌上的选手。

## 输入

n（1 ≤ n ≤ 100），然后 n 行：姓氏（至多 20 个英文字母，首字母大写）和用时 "mm:ss.d"。
没有两人同时到达终点，也没有两人用时相同。

## 输出

在到达终点时处于领先的选手人数，然后按字典序每行输出一个他们的姓氏。

## 样例

### 样例 1

输入：

```
6
Zaitseva 21:38.2
Hauswald 21:21.0
Boulygina 22:04.4
Henkel 22:06.1
Wilhelm 21:11.1
Jonsson 22:05.8
```

输出：

```
3
Hauswald
Wilhelm
Zaitseva
```

## 解法

以十分之一秒为单位。第 i 位选手（从 0 开始）在 300·i 出发，在 300·i 加上用时到达终点。
按到达终点的时刻对选手排序并重放比赛：若某选手的用时好于此前所有已到达者，就上记分牌。把收集到的姓氏排序后输出。`O(n log n)`。

在样例中，到达顺序为 Zaitseva (12982)、Hauswald (13110)、Boulygina (13844)、Wilhelm (13911)、Henkel (14161)、Jonsson (14758)（单位为十分之一秒）；最好用时在 Zaitseva、Hauswald 和 Wilhelm 处刷新。

注意事项：

- 到达顺序与出发顺序不同，所以要按到达时刻排序，而不是按用时；
- 记分牌显示的是目前最好的用时，而不是最早到达的人；
- 答案按姓氏排序，而不是按记分牌变化的顺序。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1821_sorting.cpp](1821_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 452 KB |
| [1821_sorting.go](1821_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.031 s | 1136 KB |
| [1821_sorting.java](1821_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3936 KB |
| [1821_sorting.py](1821_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 460 KB |
| [1821_sorting.rs](1821_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 228 KB |
