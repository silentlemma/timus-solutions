# 1792. 汉明码

[Timus 1792](https://acm.timus.ru/problem.aspx?space=1&num=1792) · 难度 84 · implementation

原题作者 Sofia Tekhazheva（由 Olga Soboleva 准备），出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

四个相交的圆各写一个比特，三个花瓣（三个圆的公共部分）写的是覆盖它的各圆之和的奇偶性。按题面图中的顺序，花瓣 j 位于除圆 j 以外的所有圆中，
第四个圆覆盖全部三个花瓣。七个比特中至多有一个被改动。恢复一个正确的编码。

## 输入

七个比特：四个圆，然后三个花瓣。

## 输出

一个正确编码的七个比特，与输入至多有一处不同。

## 样例

### 样例 1

输入：

```
0 1 0 1 1 0 1
```

输出：

```
0 1 0 0 1 0 1
```

### 样例 2

输入：

```
1 1 1 1 1 1 1
```

输出：

```
1 1 1 1 1 1 1
```

## 解法

先检查原样的字：花瓣 j 必须等于除圆 j 以外各圆之和模 2。若不成立，就依次尝试改动七个比特中的每一个，保留第一个使字变正确的改动。
两个正确的字至少有三处不同，所以答案唯一。`O(1)`。

第一个样例中三个花瓣都不对，而只有第四个圆位于它们全部之下；把它从 1 改为 0 后，花瓣变为 1、0、1，与所写的一致。

注意事项：

- 被改动的比特可能就是某个花瓣，而不是圆；
- 字可能本来就是正确的，此时原样输出。

全部 128 种可能的输入都与一个独立的已通过实现给出相同的答案。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1792_implementation.cpp](1792_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 400 KB |
| [1792_implementation.go](1792_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1168 KB |
| [1792_implementation.java](1792_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1600 KB |
| [1792_implementation.py](1792_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 472 KB |
| [1792_implementation.rs](1792_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 220 KB |
