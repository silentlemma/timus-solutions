# 1575. 叶卡捷琳堡地铁 2

[Timus 1575](https://acm.timus.ru/problem.aspx?space=1&num=1575) · 难度 863 · bfs

原题作者 Alexander Ipatov，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

题面给出一张未来地铁图：8 条线上共 70 个车站，其中一条是环线，某些车站可在 2 到 4 条线之间换乘。相邻车站之间
行驶需要一分钟，换乘和等车不花时间。回答至多 4900 个问题：从一个车站到另一个车站最少需要几分钟。

时间限制：1 秒。内存限制：64 MB。

## 输入

问题个数，然后每行两个车站名。

## 输出

每个问题输出一个分钟数。

## 样例

### 样例 1

输入:

```
6
Prospekt_Kosmonavtov Geologicheskaya
Shevchenko Vilonovskaya
Koltsovo Zelyony_ostrov
Teatralnaya Kamennye_palatki
China_town Italyanskaya
1905_year_square 1905_year_square
```

输出:

```
6
3
11
3
9
0
```

## 解法

真正的工作只是从图片上抄下地铁图。每条线按顺序写下各站，环线还要把最后一站连回第一站。换乘站画成两个或更多
并排的小圆，有时中间还有一小段线，但它是同一个车站：八条线恰好提到 70 个车站，所以每个小圆都属于某个有名字
的站。例如 Teatralnaya 连接浅蓝线、蓝线和黄线，1905_year_square 连接四条线。

换乘免费，所以答案就是车站图中最短路径上的区间数，从每个车站各做一次广度优先搜索即可求出。
`O(70 · 边数 + 问题数)`。地铁图是独立从图片上抄下的，全部 4900 个有序站对的答案都与一个独立程序一致。

注意事项：

- 有两个车站在图上的写法与输入不同：`Prospekt Kosmonavtov` 和 `Kamennye palatki` 在图上带空格并换行，输入中
  则用下划线；
- 环线是由 12 个车站组成的环；
- 问题可能是从一个车站到它自己（0）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1575_bfs.cpp](1575_bfs.cpp) | G++ 13.2 x64 | bfs | O(V E + Q) | AC | 0.015 s | 408 KB |
| [1575_bfs.go](1575_bfs.go) | Go 1.14 x64 | bfs | O(V E + Q) | AC | 0.031 s | 2400 KB |
| [1575_bfs.java](1575_bfs.java) | Java 1.8 | bfs | O(V E + Q) | AC | 0.171 s | 6332 KB |
| [1575_bfs.py](1575_bfs.py) | Python 3.12 x64 | bfs | O(V E + Q) | AC | 0.109 s | 1532 KB |
| [1575_bfs.rs](1575_bfs.rs) | Rust 1.75 x64 | bfs | O(V E + Q) | AC | 0.046 s | 836 KB |
