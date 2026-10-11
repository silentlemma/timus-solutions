# 1213. 把蟑螂赶进气闸最少要开几次隔板

[Timus 1213](https://acm.timus.ru/problem.aspx?space=1&num=1213) · 难度 171 · graphs

原题作者 Evgeny Krokhalev，出自 2002 年 10 月 USU Open Collegiate Programming Contest（Junior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

货舱最多有 30 个隔舱，由隔板相连，每个隔舱里都满是蟑螂。向一个隔舱放毒气并打开
它的一块隔板，所有蟑螂都会跑到相邻的隔舱。每个隔舱都与气闸相通。求把所有蟑螂都
赶进气闸最少要打开几次隔板。

时间限制：1 秒。内存限制：64 MB。

## 输入

气闸的名字，然后每行一块隔板，写作用 `-` 连接的两个隔舱名，最后一行是 `#`。名字
最多 20 个字母和数字，区分大小写。

## 输出

最少的打开次数。

## 样例

### 样例 1

输入：

```
Gateway
Machinery-Gateway
Machinery-Control
Control-Central
Control-Engine
Central-Engine
Storage-Gateway
Storage-Waste
Central-Waste
#
```

输出：

```
6
```

## 解法

除气闸外，每个隔舱一开始都有蟑螂，最后必须为空，而隔舱只有在打开它自己的某块隔板
时才会变空，所以每个隔舱至少要打开一次。这也足够了：取一棵能从每个隔舱通到气闸的
隔板树，从最远的隔舱开始向气闸方向依次清空，每个隔舱都通过通往气闸路上的那块隔板。
答案就是不同隔舱名的个数减一。`P` 为隔板数时为 `O(P log P)`。

注意事项：

- `Engine` 和 `engine` 是不同的隔舱；
- 气闸可能根本没有列出隔板，这时答案是 0；
- 隔板的布局无关紧要，只有隔舱的数量有关。

答案已在 100 个随机货舱上与另一份独立解答比对。

## 各语言说明

- 所有语言都把名字收集到集合中，输出集合大小减一。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1213_graphs.cpp](1213_graphs.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 392 KB |
| [1213_graphs.go](1213_graphs.go) | Go 1.14 x64 | graphs | O(P log P) | AC | 0.015 s | 1064 KB |
| [1213_graphs.java](1213_graphs.java) | Java 1.8 | graphs | O(P log P) | AC | 0.109 s | 1876 KB |
| [1213_graphs.py](1213_graphs.py) | Python 3.12 x64 | graphs | O(P log P) | AC | 0.078 s | 384 KB |
| [1213_graphs.rs](1213_graphs.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.062 s | 416 KB |
