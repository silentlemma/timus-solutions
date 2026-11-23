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

## 优化解法

优化的 C++ 解法使用同样的名称集合。它逐个字符把每一行读入 30 个字符的缓冲区，而
不是用 `getline`，并预先按 `N` 个名称设定集合的大小：300 KB，而不是 512 KB，时间
不变。

按字节逐行读取并直接加入集合，保留名称里的空格。通过的提交 11324219 用时 0.078 秒、占用 456 KB；简单版用时 0.078 秒、占用 516 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1563_hashing_optimized.rs`. 保留原有算法及整数类型，直接转换十进制词元，避免通用字符串解析。负数按负值累积，因此最小有符号整数也不会在取绝对值时溢出。输入存储和算法复杂度不变。

Accepted #11328568 (Rust 1.75 x64): **0.031 s / 464 KB**. 历史对照: `1563_hashing.rs` (Rust 1.75 x64) — 0.046 s / 476 KB (#11287697).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1563_hashing.cpp](1563_hashing.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 512 KB | 11287691 |
| [1563_hashing.go](1563_hashing.go) | Go 1.14 x64 | hashing | O(N) | AC | 0.031 s | 1144 KB | 11287693 |
| [1563_hashing.java](1563_hashing.java) | Java 1.8 | hashing | O(N) | AC | 0.078 s | 660 KB | 11287696 |
| [1563_hashing.py](1563_hashing.py) | Python 3.12 x64 | hashing | O(N) | AC | 0.078 s | 516 KB | 11287695 |
| [1563_hashing.rs](1563_hashing.rs) | Rust 1.75 x64 | hashing | O(N) | AC | 0.046 s | 476 KB | 11287697 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1563_hashing_optimized.cpp](1563_hashing_optimized.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 300 KB | 11303620 |
| [1563_hashing_optimized.py](1563_hashing_optimized.py) | Python 3.12 x64 | hashing | O(N) | AC | 0.078 s | 456 KB | 11324219 |
| [1563_hashing_optimized.rs](1563_hashing_optimized.rs) | Rust 1.75 x64 | hashing | O(N) | AC | 0.031 s | 464 KB | 11328568 |
