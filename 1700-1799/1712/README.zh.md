# 1712. 密码格栅

[Timus 1712](https://acm.timus.ru/problem.aspx?space=1&num=1712) · 难度 86 · implementation

原题作者 Alex Samsonov，由 Alexander Ipatov 整理，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一张 4 × 4 的格栅上开了四个窗口。把它放在 4 × 4 的纸上会露出四个格子，按阅读顺序在其中写下 16 个字母密码的
接下来四个字母。然后把格栅顺时针转 90°，如此重复四次，每个格子恰好写入一个字母。
给定初始位置的格栅和写满的纸，还原密码。

## 输入

格栅的四行（X 表示窗口，. 表示纸），然后是纸的四行：大小写拉丁字母。

## 输出

16 个字母的密码。

## 样例

### 样例 1

输入：

```
....
X..X
.X..
...X
Pwoo
Khaa
smrs
odbk
```

输出：

```
KamkohobPassword
```

## 解法

重演书写过程。在四个位置中的每一个，按行、从左到右收集窗口下的字母，然后旋转格栅。
顺时针旋转把格子 (r, c) 移到 (c, 3 − r)，所以旋转后的格栅在 (r, c) 处的内容是旧格栅在 (3 − c, r) 处的内容。`O(1)`。

注意事项：

- 同一位置内的字母按窗口的阅读顺序排列，而不是按它们在上一个位置中被找到的顺序；
- 旋转方向是顺时针：反方向旋转会以不同顺序读取同样的格子（测试 04 的四个窗口都在一个角上）；
- 输入中没有空格，所以在任何语言中按单词读取都可行。

在 300 个随机的合法格栅上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1712_implementation.cpp](1712_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 352 KB |
| [1712_implementation.go](1712_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1076 KB |
| [1712_implementation.java](1712_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1568 KB |
| [1712_implementation.py](1712_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 484 KB |
| [1712_implementation.rs](1712_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB |
