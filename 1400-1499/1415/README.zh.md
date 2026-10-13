# 1415. 移动生活

[Timus 1415](https://acm.timus.ru/problem.aspx?space=1&num=1415) · 难度 8920 · geometry, simulation

原题作者 Evgeny Krokhalev，出自 2005 年 10 月 29 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 个基站（N ≤ 100）位于整点上；基站 c 有阈值距离 R_c 和名字。信号功率与距离成反
比，手机指示灯在 R_c 以内为紫色，此后每损失 2 dB 功率下降一种颜色（靛、蓝、绿、
黄、橙、红），再远则保持红色。手机沿由 M ≤ 1000 条线段组成的折线移动。开机时选
择功率最大的基站，相同时选名字较小的；之后一直使用该基站，直到指示灯变红；红色
期间，只要出现信号不是红色的基站，就切换到其中功率最大的。输出开机、切换小区和
颜色变化的记录；即使手机在同一时刻立即切换，也要记下变红的那一行。

时间限制：2 秒。内存限制：64 MB。

## 输入

N，然后 N 行 X Y R 名字，然后 M，然后 M 条线段 X1 Y1 X2 Y2。

## 输出

记录。

## 样例

### 样例 1

输入:

```
4
0 0 1 Romashka
0 10 1 Lutik
10 10 2 Znaika
10 0 1 Children
2
5 5 -5 -5
-5 -5 5 5
```

输出:

```
Power on. CELL_ID:Znaika, SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
Signal changed. SIGNAL_LEVEL:RED
Cell changed. CELL_ID:Romashka, SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:BLUE
Signal changed. SIGNAL_LEVEL:INDIGO
Signal changed. SIGNAL_LEVEL:VIOLET
Signal changed. SIGNAL_LEVEL:INDIGO
Signal changed. SIGNAL_LEVEL:BLUE
Signal changed. SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
```

## 解法

功率与 R / d 成正比，所以损失为 10·log₁₀(d / R) dB，颜色在半径为 R·10^(k/5)
（k = 0..5）的圆上变化：第一个圆内为紫色，最后一个圆（半径 10·R）外为红色。

在线段 p(t) = s + t·(e − s) 上，到某基站的距离等于某个半径的时刻是关于 t 的二次
方程的根。只有两类时刻重要：当前基站穿过它的六个圆中的任意一个，以及任意基站穿
过它的红色圆（只有这时才会有基站变红或不再是红色）。把这些时刻排序，相差小于
10⁻⁹ 的合并为一组，在每组之后、到下一个时刻之间的中点查看状态：

- 如果手机不是红色，记录当前基站的新颜色；如果现在变成红色，则此处不是红色的所
  有基站都是候选；
- 如果手机原来是红色，候选是本组中不再是红色的基站。

候选中功率最大者胜出：在该时刻本身比较 R / d，并带相对容差，使同时到达红色圆的
基站视为相等，由较小的名字决定。如果胜出的是当前基站，只记录颜色；否则是切换小
区，新基站的颜色取该时刻之后、到它自己的下一个圆之前的值，并为新基站重建时刻列
表。`O(M·N·log N)`。

注意事项：

- 只要信号不是红色，手机就留在弱基站上，即使旁边有强得多的基站（测试 04、10）；
- 当前基站从红色恢复是颜色变化，不是切换小区（测试 02、03）；
- 多个基站可能在同一时刻到达红色圆；功率相等时按字节比较选择较小的名字（测试
  04、08、09、gen3）；
- 手机开机时可能就是红色且没有可用基站，线段长度也可能为零（测试 06、07）；
- 论坛上有些输入的事件相差约 10⁻¹³，即使 long double 也无法排序；评测数据避开了
  这些情况。

## 各语言说明

- Python 在 PyPy 下运行：CPython 在评测的第 20 个测试上超过 2 秒的限制，PyPy 用 1.8 秒，接近限制，尽管这里的每个测试都远不到 0.5 秒。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1415_geometry.cpp](1415_geometry.cpp) | G++ 13.2 x64 | geometry | O(M*N*log N) | AC | 0.125 s | 8800 KB |
| [1415_geometry.go](1415_geometry.go) | Go 1.14 x64 | geometry | O(M*N*log N) | AC | 0.140 s | 6788 KB |
| [1415_geometry.java](1415_geometry.java) | Java 1.8 | geometry | O(M*N*log N) | AC | 0.359 s | 44480 KB |
| [1415_geometry.py](1415_geometry.py) | PyPy 3.10 x64 | geometry | O(M*N*log N) | AC | 1.796 s | 46860 KB |
| [1415_geometry.rs](1415_geometry.rs) | Rust 1.75 x64 | geometry | O(M*N*log N) | AC | 0.093 s | 10192 KB |
