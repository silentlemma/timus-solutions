# 1563. Bayan

[Timus 1563](https://acm.timus.ru/problem.aspx?space=1&num=1563) · 难度 54 · hashing

原题作者 Vladimir Yakovlev，出自 2007 年 10 月 6 日第十二届乌拉尔国立大学程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Angela 依次经过 N 家商店（N ≤ 1000），每到一家名字已经见过的商店就说一声“Bayan”。求 Angela 说了几次。
店名是由 1 到 30 个拉丁字母和空格组成的字符串，并且没有两个店名只在大小写上不同。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后每行一个店名。

## 输出

重复的商店的数目。

## 样例

### 样例 1

输入:

```
12
ESPRIT
Nice Connection
Camelot
Adilisik
Lady and Gentleman City
MEXX
Camelot
Sultanna Frantsuzova
Camaieu
MEXX
Axara
Camelot
```

输出:

```
3
```

## 解法

同名商店中第一家之后的每一家都是重复，所以答案是 N 减去不同店名的个数，用哈希集合统计。店名是整行，包括
空格，所以按整行读入，只去掉行尾。期望时间 `O(N)`。

注意事项：

- 店名中有空格，按单词读取会把它们拆开（测试 03、gen3）；
- 多一个或少一个空格就是另一个店名（测试 03）；
- 一个店名可能是另一个的前缀（测试 05）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1563_hashing.cpp](1563_hashing.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 512 KB |
| [1563_hashing.go](1563_hashing.go) | Go 1.14 x64 | hashing | O(N) | AC | 0.031 s | 1144 KB |
| [1563_hashing.java](1563_hashing.java) | Java 1.8 | hashing | O(N) | AC | 0.078 s | 660 KB |
| [1563_hashing.py](1563_hashing.py) | Python 3.12 x64 | hashing | O(N) | AC | 0.078 s | 516 KB |
| [1563_hashing.rs](1563_hashing.rs) | Rust 1.75 x64 | hashing | O(N) | AC | 0.046 s | 476 KB |
