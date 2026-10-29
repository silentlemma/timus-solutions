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

## 优化解法

优化解法（C++、Java）用 `getchar` 和 `System.in.read` 把七个位当作单个字符读入，
而不是用 `iostream` 和 `Scanner`，并逐个字符（C++）或作为一个字节数组（Java）输
出答案。对单个改动的枚举不变。C++ 为 84 KB，而不是 396 KB，时间不变。Java 为
0.109 s，而不是 0.156 s；380 KB，而不是 1604 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1792_implementation.cpp](1792_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 396 KB | 11303512 |
| [1792_implementation.go](1792_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1168 KB | 11289857 |
| [1792_implementation.java](1792_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1604 KB | 11303513 |
| [1792_implementation.py](1792_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 464 KB | 11303514 |
| [1792_implementation.rs](1792_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11303515 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1792_implementation_optimized.cpp](1792_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 84 KB | 11303639 |
| [1792_implementation_optimized.java](1792_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303516 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
