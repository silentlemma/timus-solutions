# 1567. 短信垃圾广告

[Timus 1567](https://acm.timus.ru/problem.aspx?space=1&num=1567) · 难度 41 · implementation

原题作者 Denis Musin，出自 2007 年 10 月 6 日第十二届乌拉尔国立大学程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Petya 在没有联想输入的手机上输入一条不超过 1000 个字符的广告语，每按一次键收一卢布。一个字符的费用等于
它在所在按键上的位置：

| 按键 | 字符 |
|-----|------------|
| 1 | a b c |
| 2 | d e f |
| 3 | g h i |
| 4 | j k l |
| 5 | m n o |
| 6 | p q r |
| 7 | s t u |
| 8 | v w x |
| 9 | y z |
| 0 | . , ! |
| # | 空格 |

广告语由小写单词、空格、逗号、句点和感叹号组成。输出它的价格。

时间限制：1 秒。内存限制：64 MB。

## 输入

一行广告语。

## 输出

按键次数。

## 样例

### 样例 1

输入:

```
pokupaite gvozdi tolko v kompanii gvozdederov i tovarischi!
```

输出:

```
114
```

## 解法

用一张表把每个字符映射到它在按键上的位置（从 1 起算），答案就是整行之和。要整行读入，因为空格也要按一次
键。`O(n)`。

注意事项：

- 9 键上只有 y 和 z，所以 z 花费 2（测试 03）；
- 空格是 # 键上的单独字符，每个按一次，两个空格相连时也是如此（测试 05）；
- 按单词读入会丢掉空格。

## 优化解法

优化的 C++ 解法把按键转换成一张 256 项的表，给出每个字节需要的按键次数，因此每个
字符只需查一次表，而不是在所有按键中查找；它用 `getchar` 代替 `getline` 读取这一
行：100 KB，而不是 376 KB，时间不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1567_implementation.cpp](1567_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 376 KB | 11287740 |
| [1567_implementation.go](1567_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1048 KB | 11287743 |
| [1567_implementation.java](1567_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 424 KB | 11287747 |
| [1567_implementation.py](1567_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 380 KB | 11287745 |
| [1567_implementation.rs](1567_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 224 KB | 11287750 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1567_implementation_optimized.cpp](1567_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 100 KB | 11303623 |
