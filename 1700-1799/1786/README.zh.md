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

枚举名字六个字母的所有放置位置。一个字母大小写不对要 5，字母本身不对再加 5，所以两方面都不对的字母要 10。在每个位置把六个代价相加，取最小的和。`O(n)`。

样例中最佳位置是 "xander"：x 需要换字母并改成大写，花 10，e → r 和 r → o 各花 5，共 20。

注意事项：

- 字母不对且大小写也不对时，两笔费用都要付；
- 名字可以从第一个字母开始，也可以在最后一个字母结束。

在 150 个随机文本上（随机字母、名字的损坏副本以及只由名字字母组成的文本），答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 384 KB |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1616 KB |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 428 KB |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB |
