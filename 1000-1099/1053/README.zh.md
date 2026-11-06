# 1053. 锯木条直到只剩一根

[Timus 1053](https://acm.timus.ru/problem.aspx?space=1&num=1053) · 难度 344 · number_theory

原题出自雷宾斯克国立航空学院。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `N` 根木条（`1 ≤ N ≤ 1000`），长度为 1 到 `2^31 − 1` 的整数。只要还剩不止一根，就任取两根：若长度相等，扔掉
其中一根；否则从长的那根上锯下与短的一样长的一段并扔掉。输出最后一根的长度；若它取决于选择方式，输出
`IMPOSSIBLE`。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后 `N` 个长度，每行一个。

## 输出

最后一根木条的长度。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
3
2
3
4
```

输出：

```
1
```

### 样例 2

输入：

```
4
12
18
30
42
```

输出：

```
6
```

## 题解

两种操作都保持所有长度的最大公约数不变：`gcd(a, b) = gcd(a − b, b)`，而扔掉两根等长木条中的一根不改变公约数
的集合。过程最终只剩一根，而一个数的最大公约数就是它本身，所以无论怎样选择，最后一根总是初始长度的最大
公约数。答案永远不是 `IMPOSSIBLE`。`O(N log L)`。

这正是同时作用于多个数的减法形式的欧几里得算法。

注意事项：

- 长度可达 `2^31 − 1`，仍可用有符号 32 位整数表示；
- 只有一根木条时它本身就是答案；
- 对于 `2^31 − 1` 和 1 这样的长度，逐次模拟锯切太慢。

## 优化解法

Go 和 Rust 每读入一个长度就更新当前最大公约数。一旦变为一，答案不可能再变化，因此立即结束，无需继续读取剩余长度。输入有缓冲，直接输出最大公约数，辅助空间为常数。Go 直接访问标准句柄并完成部分写入。Rust 通过 C 运行库读写。

通过评测的 Rust 1.75 x64 版本耗时 0.031 秒，基础版为 0.015 秒，内存为 68 KB，基础版为 244 KB。

已通过评测的基础实现 [1053_number_theory.cpp](1053_number_theory.cpp), [1053_number_theory.java](1053_number_theory.java), [1053_number_theory.py](1053_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- 各语言都用欧几里得算法依次合并各长度。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1053_number_theory.cpp](1053_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log L) | AC | 0.015 s | 132 KB | 11278705 |
| [1053_number_theory.go](1053_number_theory.go) | Go 1.14 x64 | number_theory | O(N log L) | AC | 0.015 s | 1100 KB | 11278706 |
| [1053_number_theory.java](1053_number_theory.java) \* | Java 1.8 | number_theory | O(N log L) | AC | 0.093 s | 776 KB | 11278708 |
| [1053_number_theory.py](1053_number_theory.py) \* | Python 3.12 x64 | number_theory | O(N log L) | AC | 0.078 s | 488 KB | 11278707 |
| [1053_number_theory.rs](1053_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log L) | AC | 0.015 s | 244 KB | 11278709 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1053_number_theory_optimized.go](1053_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N log L) | AC | 0.015 s | 296 KB | 11311219 |
| [1053_number_theory_optimized.rs](1053_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(N log L) | AC | 0.031 s | 68 KB | 11311238 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
