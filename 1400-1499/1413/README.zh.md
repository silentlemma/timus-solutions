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

## 评测方式

仓库测试按 |实际值-参考值| <= 0.0000000002·max(1,|参考值|) 比较数值记号，拒绝非有限值，并精确比较非数值记号。

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

`1413_simulation_optimized.java`. Java 保留键盘方向的整数计数，读 4096 字节块并在首个零处停止。每个坐标为 straight+diagonal/sqrt(2)。用 C/10^18 表示对角系数，C=707106781186547524=floor(10^18/sqrt(2))，再以整数运算输出十八位小数。将 C 拆成 707106781*10^9+186547524，保证乘积可用 long；floorDiv/floorMod 正确处理符号与近零借位。至多 10^6 步时系数误差小于 1e-12，低于 1e-10 要求，无 double 转换。系数是定义明确的数学常数，不是预存答案。按读入字节计时间 O(I)，辅助存储固定。保留简短浮点教学版。

精确源代码 Java 1.8 Accepted #11327528：0.093 s / 376 KB。2026-11-20 保存的编译器组比较：时间 3/49、内存 1/49。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11307336 为 0.109 s / 936 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1413_simulation_optimized.java`: 0.093 s / 376 KB; 保留教学基础版 `1413_simulation.java`: 0.093 s / 5804 KB.

优化的 Go 解法在一个可重复使用的 4 KB 缓冲区中统计按键，而不是把多达 10⁶ 次按键
一次全部读入内存：{1413_simulation_optimized.go}。

优化的 Python 解法按 8 KB 分块读取输入，并用 `bytes.count` 统计每块中的各个数
字，而不是把多达 10⁶ 次按键一次全部读入内存；第一个 0 之后的输入照常读取但不再计
数：{1413_simulation_optimized.py}。

优化的 Rust 解法在一个可重复使用的 4 KB 缓冲区中统计按键，而不是把多达 10⁶ 次按
键一次全部读入向量：{1413_simulation_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1413_simulation_optimized.go`: 时间降低 +0.00%; 内存降低 +68.46%; 基础版本: `1413_simulation.go`.

- `1413_simulation_optimized.py`: 时间降低 +16.13%; 内存降低 +82.94%; 基础版本: `1413_simulation.py`.

- `1413_simulation_optimized.rs`: 时间降低 +0.00%; 内存降低 +88.58%; 基础版本: `1413_simulation.rs`.

`1413_simulation_optimized.cpp`. 用可复用的 8 KB 缓冲区分块统计方向键，在首个零处停止计数。保留九个计数器，最后一次合并整数轴向与对角贡献，对角线系数为 sqrt(1/2)。时间 O(n)，额外空间 O(1)，不保存完整输入字符串。

与 `1413_simulation.cpp` 相比：时间 0.015 s → 0.015 s；内存 1832 KB → 92 KB。

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
| [1413_simulation_optimized.java](1413_simulation_optimized.java) \* | Java 1.8 | simulation | O(I) time; O(1) auxiliary space | AC | 0.093 s | 376 KB | 11327528 |
| [1413_simulation_optimized.py](1413_simulation_optimized.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 524 KB | 11307334 |
| [1413_simulation_optimized.rs](1413_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 244 KB | 11307332 |
| [1413_simulation_optimized.cpp](1413_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 92 KB | 11326635 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
