# 1086. 第 n 个素数

[Timus 1086](https://acm.timus.ru/problem.aspx?space=1&num=1086) · 难度 107 · number_theory

原题为民间流传的题目，出自 2001 年 3 月 4 日斯维尔德洛夫斯克州第三届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 `k` 个数 `n`（`1 ≤ n ≤ 15000`）中的每一个，输出第 `n` 个素数。1 不是素数。

时间限制：2 秒。内存限制：64 MB。

## 输入

`k`（`1 ≤ k ≤ 15000`），然后 `k` 行，每行一个 `n`。

## 输出

每个 `n` 对应的第 `n` 个素数，每行一个。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
4
3
2
5
7
```

输出：

```
5
3
11
17
```

## 题解

第 15000 个素数是 163 841，所以用埃拉托斯特尼筛法筛到这个数，就能列出所有可能被询问的素数，每次询问只是列表中
的一次下标访问。筛法 `O(L log log L)`，`L = 163 842`，每次询问 `O(1)`。

注意事项：

- 第一个素数是 2，不是 1；
- 筛的上界必须包含第 15000 个素数本身；可以用任何方法事先求出一次并写进程序；
- 询问最多有 15000 个，所以素数只计算一次，而不是每次询问都算。

答案与用试除法逐个找出的素数做了核对。

## 优化解法

优化的 Go 解法只筛奇数，筛子因此缩小一半；恰好 15000 个素数用 `uint32` 存储（它
们都小于 163 842，放得下），而不是不断增长的 `int` 切片；数字逐字节读入、用
`strconv` 输出，而不是用 `fmt`：{1086_number_theory_optimized.go}。

优化的 Java 解法只筛奇数，筛子因此缩小一半；素数数组恰好 15000 个元素，而不是
163 842 个；输入按 8 KB 分块手动解析，而不是用 `StreamTokenizer`；数字通过 8 KB
的字节缓冲区输出，而不是把全部输出攒在 `StringBuilder` 里：
{1086_number_theory_optimized.java}。

优化的 Python 解法只筛奇数，`bytearray` 因此缩小一半；素数存放在 32 位无符号整数
的 `array` 中（它们都小于 163 842，放得下），而不是 Python 整数的列表；询问逐行
读取，而不是一次性切分全部输入；答案每 1024 个一批输出：
{1086_number_theory_optimized.py}。

优化的 Rust 解法只筛奇数，筛子因此缩小一半；恰好 15000 个素数用 `u32` 存放在预先
分配容量的向量中（它们都小于 163 842，放得下），而不是不断增长的 `Vec<usize>`；
答案通过 `BufWriter` 写出，而不是为每个答案生成字符串再拼接：
{1086_number_theory_optimized.rs}。

优化的 C++ 版本保留相同的筛法，但只用压缩位数组记录奇数（约 10 KB）。有序素数表只保存 15000 个素数各自的低 16 位，共 30 KB。所有素数均小于 `3 × 2^16`；生成素数时计算两个边界下标，即可在回答时判断应加零个、一个还是两个 `2^16`。查询仍为常数时间，不使用预计算答案表。总时间为 `O(L log log L + k)`，空间为 `O(L + P)`，其中 `L` 为筛的上界，`P` 为素数个数。普通向量实现保留为基础版本。

与源代码对应的 Accepted 记录：基础版本 0.031 秒 / 212 KB；本版本 0.015 秒 / 148 KB（提交 11307512）。内存降低 30.19%；仅一个计时刻度的时间差不作为加速证据。已在更新后的排名中达到目标。

{1086_number_theory_optimized.cpp}.

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1086_number_theory_optimized.cpp`: 时间降低 +51.61%; 内存降低 +30.19%; 基础版本: `1086_number_theory.cpp`.

- `1086_number_theory_optimized.go`: 时间降低 +0.00%; 内存降低 +48.87%; 基础版本: `1086_number_theory.go`.

- `1086_number_theory_optimized.java`: 时间降低 +16.13%; 内存降低 +72.98%; 基础版本: `1086_number_theory.java`.

- `1086_number_theory_optimized.py`: 时间降低 +0.00%; 内存降低 +64.25%; 基础版本: `1086_number_theory.py`.

- `1086_number_theory_optimized.rs`: 时间降低 +0.00%; 内存降低 +50.79%; 基础版本: `1086_number_theory.rs`.

## 各语言说明

- Python 在 `bytearray` 上用切片赋值划去倍数。
- C++、Go、Java 和 Rust 从 `p²` 开始划去倍数；基础 C++ 版本和 Java 用 64 位计算它，以免溢出。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1086_number_theory.cpp](1086_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.031 s | 212 KB | 11279046 |
| [1086_number_theory.go](1086_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.001 s | 2308 KB | 11279049 |
| [1086_number_theory.java](1086_number_theory.java) | Java 1.8 | number_theory | O(L log log L) | AC | 0.093 s | 2132 KB | 11279053 |
| [1086_number_theory.py](1086_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 2764 KB | 11279050 |
| [1086_number_theory.rs](1086_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 1268 KB | 11279055 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1086_number_theory_optimized.cpp](1086_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.015 s | 148 KB | 11307512 |
| [1086_number_theory_optimized.go](1086_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.015 s | 1180 KB | 11304263 |
| [1086_number_theory_optimized.java](1086_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(L log log L) | AC | 0.078 s | 576 KB | 11304023 |
| [1086_number_theory_optimized.py](1086_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 988 KB | 11304024 |
| [1086_number_theory_optimized.rs](1086_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 624 KB | 11304043 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
