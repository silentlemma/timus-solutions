# 1352. 梅森素数

[Timus 1352](https://acm.timus.ru/problem.aspx?space=1&num=1352) · 难度 132 · number_theory

原题作者 Vladimir Yakovlev，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

梅森素数是形如 2^p − 1 的素数。给出 T 个询问，每个询问一个数 N ≤ 38，输出按从小到大顺序第 N 个梅森素数的
指数 p。

时间限制：1 秒。内存限制：64 MB。

## 输入

T，然后是 T 行，每行一个 N。

## 输出

T 行，每行一个指数。

## 样例

### 样例 1

输入：

```
13
18
32
24
21
19
34
27
33
20
30
28
29
22
```

输出：

```
3217
756839
19937
9689
4253
1257787
44497
859433
4423
132049
86243
110503
9941
```

## 解法

没有程序能在一秒内找到这些素数：第 38 个指数是 6 972 593，即使检验一个这么大的数也需要巨大的计算量。前 38 个
梅森素数的顺序早已确定，所以解答把它们的指数列表存为常量表，每个询问直接按下标查表。`O(T)`。

注意事项：

- N 从 1 开始计数：第一个梅森素数是 2² − 1 = 3，指数为 2（测试 03）；
- 所有指数都能放进 32 位整数。

前 22 项通过对 10 000 以内所有素数指数运行 Lucas–Lehmer 检验得到验证；其余各项取自公开的列表，并与样例及题面
中提到的数值一致。

## 各语言说明

- Python 把表存成一个按空格切分的字符串，因此输出答案时无需再转换回数字。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 128 KB |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1084 KB |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.078 s | 444 KB |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.062 s | 324 KB |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.001 s | 216 KB |
