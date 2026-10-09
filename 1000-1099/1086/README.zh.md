# 1086. 第 n 个素数

[Timus 1086](https://acm.timus.ru/problem.aspx?space=1&num=1086) · 难度 106 · number_theory

原题为民间流传的题目，出自 2001 年 3 月 4 日斯维尔德洛夫斯克州第三届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 `k` 个数 `n`（`1 ≤ n ≤ 15000`）中的每一个，输出第 `n` 个素数。1 不是素数。

时间限制：2 秒。内存限制：64 MB。

## 输入

`k`，然后 `k` 行，每行一个 `n`。

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
- 询问的个数没有限制，所以素数只计算一次，而不是每次询问都算。

答案与用试除法逐个找出的素数做了核对。

## 各语言说明

- Python 在 `bytearray` 上用切片赋值划去倍数。
- C++、Go、Java 和 Rust 从 `p²` 开始划去倍数；C++ 和 Java 用 64 位计算它，以免溢出。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1086_number_theory.cpp](1086_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.031 s | 212 KB |
| [1086_number_theory.go](1086_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.001 s | 2308 KB |
| [1086_number_theory.java](1086_number_theory.java) | Java 1.8 | number_theory | O(L log log L) | AC | 0.093 s | 2132 KB |
| [1086_number_theory.py](1086_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 2764 KB |
| [1086_number_theory.rs](1086_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 1268 KB |
