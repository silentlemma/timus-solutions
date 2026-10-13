# 1364. 抓住劳拉

[Timus 1364](https://acm.timus.ru/problem.aspx?space=1&num=1364) · 难度 957 · simulation

原题作者 Stanislav Vasiliev，出自 2005 年 4 月 19–24 日在叶卡捷琳堡举行的第九届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

墓地有 N 排、每排 M 座墓，2 ≤ N, M ≤ 100。Lara 的地道从墓 (1, 1) 开始向东挖：下一座墓完好就一直向前，遇到墙或已
被挖过的墓就右转。地道挖到 (rT, cT) 的宝藏为止。当 Lara 位于地道上的墓 (rL, cL) 时，警报留下 T ≤ 27 000 秒，沿
地道每秒能跑过一座墓。按挖掘顺序输出 Lara 来得及跑到的所有被挖过的墓。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是 rT 和 cT，然后是 rL 和 cL，最后是 T。

## 输出

能到达的墓，每行一对 `行 列`，按挖掘顺序。

## 样例

### 样例 1

输入：

```
5 4
4 3
2 2
5
```

输出：

```
5 2
5 1
4 1
3 1
2 1
2 2
2 3
3 3
4 3
```

## 解法

挖掘规则画出一条顺时针螺旋，地道终止于宝藏。模拟这个过程：在墓地四周放一圈“已挖”的格子代替墙，下一格已挖时就
右转。这样得到按挖掘顺序排列的墓，地道就是一条路径，两座墓之间的距离等于它们在列表中位置之差。

若 Lara 所在的墓位于第 p 位，宝藏位于第 q 位，答案就是第 max(0, p − T) 到第 min(q, p + T) 位。`O(N · M)`。

注意事项：

- 地道止于宝藏，宝藏之后无处可去（测试 06）；
- T 可能为 0，此时只剩 Lara 所在的那座墓（测试 02）；
- T 可能超过整条地道的长度，此时答案就是整条地道（测试 03 和生成测试 1）。

## 各语言说明

- 五种解答都用代替墙的外框构造同样的螺旋。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1364_simulation.cpp](1364_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.015 s | 300 KB |
| [1364_simulation.go](1364_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.015 s | 2096 KB |
| [1364_simulation.java](1364_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.093 s | 2068 KB |
| [1364_simulation.py](1364_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 1992 KB |
| [1364_simulation.rs](1364_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.015 s | 452 KB |
