# 1590. 培根密码

[Timus 1590](https://acm.timus.ru/problem.aspx?space=1&num=1590) · 难度 187 · strings

原题作者 Alexey Zhevak，出自 2007 年 10 月 27 日在叶卡捷琳堡举行的 ACM ICPC 2007–2008 NEERC 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一个由小写拉丁字母组成、长度不超过 5000 的字符串，求其不同非空子串的个数。

时间限制：2 秒。内存限制：64 MB。

## 输入

字符串。

## 输出

不同子串的个数。

## 样例

### 样例 1

输入:

```
aaba
```

输出:

```
8
```

## 解法

建立字符串的后缀自动机。每个状态对应结束位置集合相同的那些子串；它们的长度从 len(link) + 1 到 len，所以该状态包含
len − len(link) 个不同子串，且每个子串只属于一个状态。答案就是除初始状态外所有状态的 len − len(link) 之和。
自动机的状态数少于 2n，构建的时间和内存为 `O(n·26)`。结果已在短字符串上与用集合收集所有子串的做法对照。

注意事项：

- 5000 个随机字母的字符串约有 1250 万个不同子串，64 MB 内存不可能把它们都存下来；
- 分裂状态时，克隆状态要继承旧状态的全部转移和后缀链接。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1590_strings.cpp](1590_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1428 KB |
| [1590_strings.go](1590_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2328 KB |
| [1590_strings.java](1590_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 2412 KB |
| [1590_strings.py](1590_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 3132 KB |
| [1590_strings.rs](1590_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 2272 KB |
