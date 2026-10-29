# 1910. 和最大的连续三项

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · implementation

原题作者 Denis Dublennykh，比赛 NEERC 2012, Eastern subregional contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定正数序列，找出和最大的连续三个元素。输出该和以及中间元素从一开始
的下标。保证取得最大和的三元组唯一。时间限制 1 秒，内存限制 64 MB。

## 输入

先给 n，3≤n≤1000，再给 n 个整数 aᵢ，1≤aᵢ≤10⁶。
空格或换行均可作为分隔符。

## 输出

最大和，以及中间元素从一开始的下标。

## 评测方式

两个精确整数，按标记比较。

## 样例

```
6
1 4 4 4 1 1
```

```
12 3
```

## 解法

把第二节到倒数第二节依次当作三节中间的一节：把它和两个邻居相加，记下最大的和
以及它的编号。题目保证最优的三节唯一，所以用严格比较即可。`O(n)`；和不超过
3·10⁶，32 位整数放得下。

注意事项：

- 答案是中间一节的编号，从 1 开始计数；
- n = 3 时只有一组三节。

## 优化解法

优化的 C++ 解法不保存各节：它用 `scanf` 逐个读入，只记住当前一节之前的两节，三节
之和只需要这些：128 KB，而不是 192 KB，时间不变。

优化的 Java 解法和 C++ 解法一样只保存当前段之前的两段，并手工解析输入，而不是使
用 `Scanner`：0.125 s，而不是 0.156 s；380 KB，而不是 2372 KB。

## 各语言说明

没有特别需要注意的地方。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1910_implementation.cpp](1910_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 192 KB | 11303319 |
| [1910_implementation.go](1910_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1108 KB | 11303324 |
| [1910_implementation.java](1910_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 2372 KB | 11303327 |
| [1910_implementation.py](1910_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.062 s | 452 KB | 11303331 |
| [1910_implementation.rs](1910_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 236 KB | 11303334 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1910_implementation_optimized.cpp](1910_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303648 |
| [1910_implementation_optimized.java](1910_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) | AC | 0.125 s | 380 KB | 11303787 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
