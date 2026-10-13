# 1355. 再谈秃顶

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · 难度 212 · number_theory

原题作者 Aleksandr Bikbaev，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

酒馆用正整数编号，从酒馆 n 只能走到编号为 n 的倍数的酒馆。路线从酒馆 a 出发，必须到达酒馆 b，途中每个酒馆
（包括 a 和 b）都喝一杯麦酒。对 T ≤ 20 组 1 ≤ a, b ≤ 10⁹，输出最多能喝几杯，若到不了 b 则输出 0。

时间限制：1 秒。内存限制：64 MB。

## 输入

T，然后是 T 行，每行 a 和 b。

## 输出

T 行答案。

## 样例

### 样例 1

输入：

```
5
30 89
2 16
3 243
1 1
2 2
```

输出：

```
0
4
5
1
1
```

## 解法

路线上每个数都整除下一个数，所以只有 a 整除 b 时才能到达 b。此时每一步都把编号乘上一个大于 1 的因子，所有因子
的乘积为 q = b / a。要经过尽量多的酒馆，每个因子都应是素数，于是步数为 Ω(q)，即 q 按重数计的素因子个数。答案
是 1 + Ω(q)，把酒馆 a 本身也算上。

用试除法试到 √q ≤ 31 623 即可求出 Ω(q)。`O(T · √(b / a))`。

注意事项：

- a = b 时喝一杯，而不是零杯（样例）；
- b 小于 a 或不是 a 的倍数时答案为 0（测试 04）；
- T 可以为 0，此时不输出答案（测试 02）；
- q = 2²⁹ 的步数最多，共 30 杯（测试 03）。

## 各语言说明

- Python 先除尽 2，再只试奇数因子，在大素数上把循环次数减半。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB |
