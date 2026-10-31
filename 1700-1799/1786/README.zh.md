# 1786. 桑德罗传记

[Timus 1786](https://acm.timus.ru/problem.aspx?space=1&num=1786) · 难度 110 · strings

原题作者 Olga Soboleva，出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一段由拉丁字母组成的文本需要修改，使其中出现单词 "Sandro"。把一个字母换成同样大小写的另一个字母需要 5 枚金币，改变一个字母的大小写也需要 5 枚。求最小花费。

## 输入

文本，长度为 6 到 200 个字母。

## 输出

最少的金币数。

## 样例

### 样例 1

输入：

```
MyNameIsAlexander
```

输出：

```
20
```

## 解法

枚举名字六个字母的所有放置位置。一个字母大小写不对要 5，字母本身不对再加 5，所以两方面都不对的字母要 10。在每个位置把六个代价相加，取最小的和。扫描本身需要 `O(n)` 时间，但 Python 在每个位置复制后缀 `text[start:]`，因此该实现的时间复杂度为 `O(n^2)`。所有实现计入输入字符串后的空间复杂度均为 `O(n)`；输入长度最多只有 200。

样例中最佳位置是 "xander"：x 需要换字母并改成大写，花 10，e → r 和 r → o 各花 5，共 20。

注意事项：

- 字母不对且大小写也不对时，两笔费用都要付；
- 测试 03 的 `sANDRO` 中，六个字母的大小写全部错误，因此花费为 30；
- 名字可以从第一个字母开始，也可以在最后一个字母结束。

在 2,000 个随机短文本、592 个定向用例、全部 8 个已有测试和 64 个生成用例上，Python 的答案与基于合法操作图的独立参考程序一致。

## 优化解法

优化的 C++ 解法用 `scanf` 把文本读入 201 字节的缓冲区（足够容纳 200 个字母和结尾
的零），而不是使用 `std::cin` 和 `std::string`；由于文本只含拉丁字母，它通过与
`'Z'` 比较来判断大小写，通过加上 `'a' − 'A'` 转成小写，而不是调用 `isupper` 和
`tolower`：{1786_strings_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐字符读取文本，而不是创建 `Scanner`；由于文
本只含拉丁字母，它通过与 `'Z'` 比较来判断大小写，通过加上 `'a' − 'A'` 转成小写，
而不是调用 `Character.isUpperCase` 和 `Character.toLowerCase`：
{1786_strings_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1786_strings_optimized.cpp`: 时间降低 +0.00%; 内存降低 +68.42%; 基础版本: `1786_strings.cpp`.

- `1786_strings_optimized.java`: 时间降低 +28.44%; 内存降低 +75.13%; 基础版本: `1786_strings.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1786_strings.go](1786_strings.go).
- [1786_strings.rs](1786_strings.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 380 KB | 11304047 |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB | 11289804 |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1576 KB | 11304048 |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.109 s | 408 KB | 11304049 |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB | 11289809 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings_optimized.cpp](1786_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 120 KB | 11304276 |
| [1786_strings_optimized.java](1786_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.078 s | 392 KB | 11304277 |
