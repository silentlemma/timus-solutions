# 1543. 舞蹈革命

[Timus 1543](https://acm.timus.ru/problem.aspx?space=1&num=1543) · 难度 2151 · simulation

原题作者 Denis Musin，出自 2007 年 4 月 21 日在叶卡捷琳堡举行的第十一届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一首歌是一串节拍，每拍要么为空（N），要么要求按 U、D、L、R 中的一个键。在 Easy、Medium、
Hard 难度下一拍分别持续 1000、500、250 毫秒（Diff = 1、2、3）。根据玩家的按键记录，按每个
非空节拍（称为一步）内的第一次按键评分：

- 没有按键：Boo；按错键：Miss；
- 在该拍开始后不到 40% 的时间内按对：Perfect，不到 70%：Great，否则 Good。

同一拍内第一次之后的按键以及空拍中的按键都不计。然后计算：

- 舞蹈得分：第 n 步得 p·n·⌊B / S⌋，Perfect 时 p = 10，Great 时 5，其余为 0，B = 10⁶·Diff，
  S = N(N + 1)/2，N 为步数；
- 连击奖励：在由 Perfect、Great、Good 组成的连续段中，第 c 步 Perfect 得 55·c，Great 得
  33·c，Good 得 0；Boo 和 Miss 中断连击；
- 等级奖励，依据舞点（Perfect +2，Great +1，Good 0，Boo −4，Miss −5）：只要舞点曾低于零就
  为 0，否则全部为 Perfect 得 10⁷，全部为 Perfect 或 Great 得 10⁶，其余按舞点不低于最大可能
  值 2N 的 80%、64%、50% 或更低分别得 10⁵、10⁴、10³ 或 100。

时间限制：1 秒。内存限制：64 MB。

## 输入

歌曲长度（m:ss）和难度，节拍串，然后是若干行"时间 按键"，时间为从开始起的毫秒数。

## 输出

五个计数、一行 20 个短横线和四个分数，格式同样例。

## 样例

### 样例 1

输入:

```
0:30 Easy
NNNNNLNNRNUNNUNNNDDDNNUNNNNRNU
5201 L
8475 R
8735 L
10000 U
13200 U
17284 D
18355 D
19124 D
22222 U
27543 R
29923 U
```

输出:

```
Perfect: 7
Great: 2
Good: 1
Boo: 0
Miss: 0
--------------------
Stage Score: 7181495
Combo Bonus: 2233
Dance Level Bonus: 100000
Total Score: 7283728
```

## 解法

第 i 拍覆盖时间 [i·T, (i + 1)·T)，T 为周期。把按键按时间排序，用一个指针扫描：每拍开始前
跳过早于其开始的按键；若指针处的按键早于该拍结束，它就是该拍的第一次按键。阈值用整数比较：10·elapsed < 4·T 与 10·elapsed < 7·T，比例也一样：100·舞点 ≥ 80·2N 等。
不需要歌曲长度：节拍已经给出。分数可用 64 位整数存放。L 拍、P 次按键时为 `O(L + P log P)`。

题面有多种读法。以下几点遵循题面；前两点也在评测网站的讨论区得到确认，第三点是我们对"不低于
80%"的理解：

- 一拍包含其开始时刻，不包含结束时刻；
- 只要舞点一度低于零，等级奖励就是 0，即使最终结果不错（测试 03）；
- 比例精确比较：6 分中得 4 分低于 80%（4.8），所以测试 02 得 10⁴ 而不是 10⁵。

注意事项：

- 恰好在一拍的 40% 和 70% 处按下分别是 Great 和 Good（测试 06）；
- 第一次按错就是 Miss，即使随后按对（测试 07）；
- 紧挨在一步之前的空拍中的按键不算作该步（测试 07）；
- Good 延长连击但不增加连击奖励（测试 gen3）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1543_simulation.cpp](1543_simulation.cpp) | G++ 13.2 x64 | simulation | O(L + P log P) | AC | 0.031 s | 528 KB |
| [1543_simulation.go](1543_simulation.go) | Go 1.14 x64 | simulation | O(L + P log P) | AC | 0.031 s | 1776 KB |
| [1543_simulation.java](1543_simulation.java) | Java 1.8 | simulation | O(L + P log P) | AC | 0.171 s | 4360 KB |
| [1543_simulation.py](1543_simulation.py) | Python 3.12 x64 | simulation | O(L + P log P) | AC | 0.078 s | 1676 KB |
| [1543_simulation.rs](1543_simulation.rs) | Rust 1.75 x64 | simulation | O(L + P log P) | AC | 0.015 s | 644 KB |
