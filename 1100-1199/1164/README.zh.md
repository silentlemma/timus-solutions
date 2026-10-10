# 1164. 找出填字游戏中所有单词后剩下哪些字母

[Timus 1164](https://acm.timus.ru/problem.aspx?space=1&num=1164) · 难度 206 · strings

原题作者 Alex Selivanov，出自 2001 年 ACM ICPC 东北欧区域赛北部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个 `N×M` 的大写字母网格（`2 ≤ N, M ≤ 10`）中藏着 `P ≤ 100` 个单词。每个
单词占据一条由边相邻格子组成的路径，任何格子都不属于两个单词，也不会在同一个
单词中出现两次。合法的摆放方式总是存在。按字母顺序输出没有被任何单词使用的
格子里的字母。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`、`M` 和 `P`，然后是网格的 `N` 行，再然后是 `P` 个单词。

## 输出

排好序的剩余字母，占一行。

## 样例

### 样例 1

输入：

```
3 3 2
EBG
GEE
EGE
BEG
GEE
```

输出：

```
EEG
```

## 解法

根本不需要找出单词的位置。任何摆放方式都会让每个单词的每个字母恰好占用一个
格子，所以无论怎样摆放，剩下的格子里都是网格的字母减去单词的字母（按重数计）。
统计网格中 26 个字母的个数，减去它们在单词中的个数，再把每个字母按剩余次数
输出。`O(N·M + 单词总长)`。

注意事项：

- 看起来似乎必须搜索，其实不用：摆放方式可能不唯一（例如样例），但剩余字母的
  多重集合总是唯一的；
- 如果单词覆盖了整个网格，答案是一个空行。

## 各语言说明

- 所有语言都按空白分隔的记号读取输入，所以换行无关紧要。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1164_strings.cpp](1164_strings.cpp) | G++ 13.2 x64 | strings | O(N·M + total word length) | AC | 0.015 s | 380 KB |
| [1164_strings.go](1164_strings.go) | Go 1.14 x64 | strings | O(N·M + total word length) | AC | 0.031 s | 1184 KB |
| [1164_strings.java](1164_strings.java) | Java 1.8 | strings | O(N·M + total word length) | AC | 0.109 s | 1640 KB |
| [1164_strings.py](1164_strings.py) | Python 3.12 x64 | strings | O(N·M + total word length) | AC | 0.078 s | 436 KB |
| [1164_strings.rs](1164_strings.rs) | Rust 1.75 x64 | strings | O(N·M + total word length) | AC | 0.015 s | 220 KB |
