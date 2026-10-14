# 1512. 齐尼姆

[Timus 1512](https://acm.timus.ru/problem.aspx?space=1&num=1512) · 难度 885 · constructive

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在 N × N 的棋盘上放 N 个皇后（4 ≤ N ≤ 100000），使任意两个不在同一行、同一列或同一
条对角线上。

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

每个皇后的列号和行号，每行一个皇后，顺序任意。任何合法的摆法都可以。

## 样例

### 样例 1

输入:

```
8
```

输出:

```
1 5
2 1
3 8
4 4
5 2
6 7
7 3
8 6
```

## 解法

这么大的规模搜索没有希望，但有已知的显式摆法。对 N mod 6 ≠ 2 的偶数 N，把第
i ≤ N/2 列的皇后放在第 2i 行，第 N/2 + i 列的皇后放在第 2i − 1 行：左半边的每个皇后
与右半边的任何皇后都不在同一对角线上，而每一半内部行号随列号每次增加 2，所以也不会
共对角线。N mod 6 = 2 的偶数 N 不能这样做；改为令 s = (2(i − 1) + N/2 − 1) mod N，
把第 i 列放在第 1 + s 行、第 N + 1 − i 列放在第 N − s 行。两种摆法都不占用主对角线，
所以奇数 N 取 N − 1 的摆法，再在角上 (N, N) 加一个皇后。已对 4 到 3000 的所有 N 以
及最大的几个 N 做过检查。`O(N)`。

注意事项：

- 简单的“先偶后奇”摆法恰好在 N mod 6 = 2 时失效，比如样例中的 N = 8（测试 01、
  05、gen2、gen7）；
- 奇数 N 需要 N − 1 的摆法空出角落（测试 03、06、gen3、gen6）；
- 正确的摆法很多，所以测试使用检查程序（所有测试）；
- 100000 行输出最好在一个缓冲区里拼好（gen5）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1512_constructive.cpp](1512_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.031 s | 3232 KB |
| [1512_constructive.go](1512_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 4076 KB |
| [1512_constructive.java](1512_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 7808 KB |
| [1512_constructive.py](1512_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.140 s | 13344 KB |
| [1512_constructive.rs](1512_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 3960 KB |
