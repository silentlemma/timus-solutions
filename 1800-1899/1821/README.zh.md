# 1821. 冬季两项

[Timus 1821](https://acm.timus.ru/problem.aspx?space=1&num=1821) · 难度 178 · sorting

原题作者 Alexander Ipatov 和 Alexey Samsonov，出自 2011 年 3 月 19 日第十二届乌拉尔国立大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在间隔出发的比赛中，选手依次出发，间隔 30 秒。记分牌显示已到达终点的选手中用时最好的那一位。
按出发顺序给出选手及其比赛用时，列出所有曾出现在记分牌上的选手。

## 输入

n（1 ≤ n ≤ 100），然后 n 行：非空姓氏（至多 20 个英文字母，首字母大写，其余小写）和用时 "mm:ss.d"。
所有姓氏互不相同。没有两人同时到达终点，也没有两人用时相同。

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
- 比较到达时刻时要加上出发偏移：测试 06 中，Late 在 6000 个十分之一秒时到达，Early 在 6601 时到达，因此只有 Late 领先；
- 答案按姓氏排序，而不是按记分牌变化的顺序。

## 优化解法

优化的 C++ 解法用一次 `scanf` 读入每名滑雪者，同时在 `:` 和 `.` 处拆开时间，而不
是用 `iostream` 和 `stoi` 转换的子串，并把滑雪者存在 100 条记录的静态数组中，每
条记录的名字占 21 字节（因为 `n ≤ 100`，姓氏最多 20 个字母，这已足够），而不是存
放 `std::string` 的元组向量。领先榜保存指向名字的指针，用 `strcmp` 排序：
{1821_sorting_optimized.cpp}。

优化的 Java 解法用 `BufferedReader` 和 `StringTokenizer` 读取各行（后者顺便在
`:` 和 `.` 处拆开时间），而不是用 `Scanner` 和子串，并对实现 `Comparable` 的记录
数组排序，而不是用 lambda 比较器对装箱的 `Integer` 下标排序：
{1821_sorting_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1821_sorting_optimized.cpp`: 时间降低 +0.00%; 内存降低 +73.21%; 基础版本: `1821_sorting.cpp`.

- `1821_sorting_optimized.java`: 时间降低 +30.13%; 内存降低 +83.13%; 基础版本: `1821_sorting.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1821_sorting.go](1821_sorting.go).
- [1821_sorting.rs](1821_sorting.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1821_sorting.cpp](1821_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 448 KB | 11304255 |
| [1821_sorting.go](1821_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.031 s | 1136 KB | 11290261 |
| [1821_sorting.java](1821_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3936 KB | 11290273 |
| [1821_sorting.py](1821_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 460 KB | 11290266 |
| [1821_sorting.rs](1821_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 228 KB | 11290275 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1821_sorting_optimized.cpp](1821_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 120 KB | 11307289 |
| [1821_sorting_optimized.java](1821_sorting_optimized.java) | Java 1.8 | sorting | O(n log n) | AC | 0.109 s | 664 KB | 11307294 |
