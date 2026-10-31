# 1413. 火星跳跃车

[Timus 1413](https://acm.timus.ru/problem.aspx?space=1&num=1413) · 难度 180 · simulation

原题作者 Stanislav Vasiliev，出自 2005 年 10 月 29 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一辆探测车用数字小键盘控制：1 到 9 中除 5 以外的每个键，使它朝该键相对中心键 5
的方向跳恰好一米（8 向北，6 向东，9 向东北，依此类推），5 表示采集土样，0 表示
自毁。给出不超过 10⁶ 次按键，输出探测车的最终位置：第一次按下 0 时所在的点，
若没有按 0，则是最后一次按键之后的位置。答案是向东和向北的位移，绝对或相对误差不超过
10⁻¹⁰。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

按键的数字序列。

## 输出

X 和 Y，向东和向北的位移。

## 样例

### 样例 1

输入:

```
1236987412369870234567890123456789
```

输出:

```
1.0000000000 0.0000000000
```

## 解法

统计第一个 0 之前每个键被按下的次数。直线跳使一条坐标轴变化整整一米，斜跳使两条
坐标轴各变化 1/√2，所以每条轴上的终点为（直线跳之和）+（斜跳之和）/ √2，由整数
和计算。计数避免了每次跳跃时的舍入，但最终的浮点乘法、加法及保留十位小数的输出
仍会舍入；绝对误差可能略大于 10⁻¹⁰。`O(n)`。

注意事项：

- 第一个 0 之后的按键必须忽略（测试 01、05、gen2）；
- 斜跳的长度是一米，不是 √2（测试 04）；
- 斜跳的坐标是无理数，因此计数并不能使最终坐标完全精确（测试 04）；
- 每个字符都调用一次慢速输入来读取一百万个字符，可能占去 0.5 秒中的很大一部分，
  所以各解法一次读入整个记号、整行或全部输入。

## 优化解法

优化的 Go 解法在一个可重复使用的 4 KB 缓冲区中统计按键，而不是把多达 10⁶ 次按键
一次全部读入内存：{1413_simulation_optimized.go}。

优化的 Java 解法直接按 `BufferedInputStream` 的字节统计按键，并在第一个 0 处停
止，而不是用 `BufferedReader` 把输入解码成长达一百万个字符的 `String` 行：
{1413_simulation_optimized.java}。

优化的 Python 解法按 8 KB 分块读取输入，并用 `bytes.count` 统计每块中的各个数
字，而不是把多达 10⁶ 次按键一次全部读入内存；第一个 0 之后的输入照常读取但不再计
数：{1413_simulation_optimized.py}。

优化的 Rust 解法在一个可重复使用的 4 KB 缓冲区中统计按键，而不是把多达 10⁶ 次按
键一次全部读入向量：{1413_simulation_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1413_simulation_optimized.go`: 时间降低 +0.00%; 内存降低 +68.46%; 基础版本: `1413_simulation.go`.

- `1413_simulation_optimized.java`: 时间降低 -17.20%; 内存降低 +83.87%; 基础版本: `1413_simulation.java`.

- `1413_simulation_optimized.py`: 时间降低 +16.13%; 内存降低 +82.94%; 基础版本: `1413_simulation.py`.

- `1413_simulation_optimized.rs`: 时间降低 +0.00%; 内存降低 +88.58%; 基础版本: `1413_simulation.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1413_simulation.cpp](1413_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 1832 KB | 11307301 |
| [1413_simulation.go](1413_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 3196 KB | 11286093 |
| [1413_simulation.java](1413_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.093 s | 5804 KB | 11307330 |
| [1413_simulation.py](1413_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 3072 KB | 11286094 |
| [1413_simulation.rs](1413_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB | 11286097 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1413_simulation_optimized.go](1413_simulation_optimized.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 1008 KB | 11307331 |
| [1413_simulation_optimized.java](1413_simulation_optimized.java) \* | Java 1.8 | simulation | O(n) | AC | 0.109 s | 936 KB | 11307336 |
| [1413_simulation_optimized.py](1413_simulation_optimized.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 524 KB | 11307334 |
| [1413_simulation_optimized.rs](1413_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 244 KB | 11307332 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
