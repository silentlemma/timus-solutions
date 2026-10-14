# 1602. 电梯

[Timus 1602](https://acm.timus.ru/problem.aspx?space=1&num=1602) · 难度 454 · implementation

原题作者 Vladimir Yakovlev，出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Petya 在摩天楼的顶层第 n 层，想去一楼。电梯此刻在第 k 层，正下行去一楼；到一楼后要停 15 秒才能上行。
电梯每层用 v 秒，Petya 跑一层用 u 秒（0.1 < v < u < 100，最多两位小数），进电梯要 5 秒。Petya 应该走到哪一层，
才能最快到达一楼？若有多个同样好的楼层，选步行最少的那个。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

n、k、u 和 v。

## 输出

楼层。

## 样例

### 样例 1

输入:

```
50 49 4.8 0.2
```

输出:

```
45
```

## 解法

逐个尝试每一层 f。一路走到底（f = 1）需要 (n − 1)·u。否则 Petya 走到第 f 层时呼叫电梯，此时为 (n − f)·u。
电梯最早在 (k − 1)·v + 15 时离开一楼，所以它在两者中较晚的时刻开始上行，上升 f − 1 层，等待 5 秒让人进入，
再下降 f − 1 层。总时间最小者胜出，时间相同时选较高的楼层，即步行更少：`O(n)`。

样例确定了题意：电梯只有在第 f 层被呼叫后才开始上行。若它停够后立即上行，样例中第 44 层会比第 45 层更好。

结果已在 3500 个随机输入和容易出现平局的输入上与独立实现对照。

注意事项：

- u 和 v 有两位小数，确实会出现精确平局（测试 09，第 3 层和第 4 层）；以百分之一秒为单位时所有时间都是精确的整数，
  不需要比较浮点数；
- 一路走到底也是一种选择，在矮楼里常常是最优的（测试 02）；
- 平局时选较高的楼层，所以比较时遇到相同总时间要保留后面的楼层。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1602_implementation.cpp](1602_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 416 KB |
| [1602_implementation.go](1602_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1096 KB |
| [1602_implementation.java](1602_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1680 KB |
| [1602_implementation.py](1602_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 464 KB |
| [1602_implementation.rs](1602_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 236 KB |
