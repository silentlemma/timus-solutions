# 1440. 训练日程

[Timus 1440](https://acm.timus.ru/problem.aspx?space=1&num=1440) · 难度 669 · bruteforce

原题作者 Ekaterina Vasilyeva（构思与题面）和 Stanislav Vasiliev（程序），出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

格兰芬多魁地奇球队在一周中固定的几天训练，例如每个星期五和星期日。训练可以从 9
月 2 日开始，一直到第一场比赛的前一天；比赛日期在 9 月 2 日到 12 月 24 日之间。
训练次数必须在 A 到 B 之间（1 ≤ A ≤ B ≤ 200）。已知 9 月 1 日是星期几以及比赛
日期，选出一组星期几使训练次数满足要求，或者报告不存在。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

9 月 1 日是星期几（英文），比赛日期，格式为 "Month Day"，然后是 A 和 B。

## 输出

"Impossible"，或者选出的星期几的个数，后面每行一个名字，顺序任意。任何满足要求
的集合都被接受。

## 样例

### 样例 1

输入:

```
Thursday
September 10
9 20
```

输出:

```
Impossible
```

### 样例 2

输入:

```
Tuesday
October 7
12 14
```

输出:

```
Impossible
```

### 样例 3

输入:

```
Friday
October 4
12 14
```

输出:

```
3
Monday
Wednesday
Saturday
```

## 解法

先统计每个星期几上有多少个训练日：从 9 月 2 日到比赛前一天逐日走一遍（最多 113
天），给每天对应的星期几加一。一组星期几给出它们计数之和，而非空的组合只有 127
个，所以全部尝试，输出第一个和在 A 与 B 之间的组合。设比赛前有 D 天，复杂度
`O(D + 2⁷ · 7)`。

注意事项：

- 比赛在 9 月 2 日时没有任何训练日（测试 04）；
- 圣诞节前永远放不下 200 次训练（测试 05）；
- 有时只有一组可行，或者需要全部七天（测试 06、09、10、13）；
- 各月长度不同：9 月 30 日和 10 月 1 日是相邻的两天（测试 11、12）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1440_bruteforce.cpp](1440_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.015 s | 404 KB |
| [1440_bruteforce.go](1440_bruteforce.go) | Go 1.14 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.031 s | 1164 KB |
| [1440_bruteforce.java](1440_bruteforce.java) | Java 1.8 | bruteforce | O(D + 2^7 · 7) | AC | 0.109 s | 1708 KB |
| [1440_bruteforce.py](1440_bruteforce.py) | Python 3.12 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.078 s | 428 KB |
| [1440_bruteforce.rs](1440_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.031 s | 220 KB |
