# 1055. 二项式系数的不同素因子个数

[Timus 1055](https://acm.timus.ru/problem.aspx?space=1&num=1055) · 难度 422 · number_theory

原题出自雷宾斯克国立航空学院。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 `1 ≤ M < N ≤ 50000`，求能整除二项式系数 `C(N, M) = N! / (M! · (N − M)!)` 的不同素数的个数。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N` 和 `M`。

## 输出

`C(N, M)` 的不同素因子个数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
5 3
```

输出：

```
2
```

### 样例 2

输入：

```
10 5
```

输出：

```
3
```

## 题解

`C(N, M)` 有几万位，所以根本不去计算它。能整除它的只可能是不超过 `N` 的素数，而素数 `p` 在 `x!` 中的指数由
勒让德公式给出：

```text
e_p(x!) = ⌊x/p⌋ + ⌊x/p²⌋ + ⌊x/p³⌋ + …
```

所以 `p` 整除 `C(N, M)` 当且仅当 `e_p(N!) − e_p(M!) − e_p((N − M)!) > 0`。用埃拉托斯特尼筛法列出不超过 `N` 的
素数，每个素数需要 `O(log N)` 次除法：总计 `O(N log log N)`。

注意事项：

- 阶乘本身立刻就会溢出：只处理指数；
- 必须检查所有不超过 `N` 的素数，包括大于 `N / 2` 的；
- `M = N − 1` 时 `C = N`，其素因子就是 `N` 的素因子。

等价的判断是库默尔定理：`p` 整除 `C(N, M)` 当且仅当在 `p` 进制下计算 `M` 加 `N − M` 时产生进位。测试用它核对过，
`N ≤ 3000` 时还通过分解精确的系数核对过。

## 各语言说明

- 各语言都用同样的筛法；Python 用一次 `bytearray` 切片赋值标记一个素数的所有倍数。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1055_number_theory.cpp](1055_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 184 KB |
| [1055_number_theory.go](1055_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.015 s | 1112 KB |
| [1055_number_theory.java](1055_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.093 s | 1680 KB |
| [1055_number_theory.py](1055_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.078 s | 580 KB |
| [1055_number_theory.rs](1055_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.031 s | 268 KB |
