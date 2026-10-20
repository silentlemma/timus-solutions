# 2130. 与已知整除回答一致的数

[Timus 2130](https://acm.timus.ru/problem.aspx?space=1&num=2130) · 难度 954 · math, number_theory

原题作者 Kirill Borozdin 和 Nikita Sivukhin（由 Vladimir Leskov 整理），出自 “迟到总比不到好”专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

隐藏的整数 x 在 1 到 10¹² 之间。n 次操作中的每一次告诉你 x 是否能被某个 dᵢ 整除。每次操作后，输出同一范围内与目前所有回答都一致的任意一个数，若不存在则输出 −1。任何这样的数都可接受。时间限制 2.5 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 10⁵），然后是 n 对 dᵢ, tᵢ，其中 1 ≤ dᵢ ≤ 10⁶；tᵢ = 1 表示"是"。

## 输出

每次操作后的一个合适的数或 −1。

## 评测方式

检查器对每次操作自行判断是否存在合适的数，并用当时的回答核对每个输出的数。

## 样例

### 样例 1

输入：

```
3
10 1
5 0
100500 0
```

输出：

```
100500
-1
-1
```

### 样例 2

输入：

```
6
2 1
5 0
3 1
1 1
5 1
100500 0
```

输出：

```
12
12
12
12
-1
-1
```

### 样例 3

输入：

```
6
1000000 1
999999 1
2 0
999998 1
999997 1
999996 1
```

输出：

```
999999000000
999999000000
-1
-1
-1
-1
```

## 解法

任何合法的数都是 L 的倍数，L 是回答为"是"的所有除数的最小公倍数。L 本身就是最好的候选：若存在合法的 x，则 L 整除 x，而回答为"否"的除数 d 不整除 x，因此也不整除 L。所以当 L ≤ 10¹² 且没有"否"的除数整除 L 时答案为 L，否则为 −1；一旦变成 −1 就一直是 −1，因为回答只会增加条件。

新的"否"除数只与当前的 L 检查一次。不改变 L 的"是"什么也不改变，而 L 的每次改变至少翻倍，所以 L 在超过 10¹² 之前至多改变约 40 次。只有这时才重新检查所有存下的"否"除数，总工作量保持 O(40 n)。

第二个样例中 2 和 3 给出 L = 6，但 5 是"否"的除数，之后对 5 的"是"使 L = 30 能被 5 整除，所以答案变为 −1；样例输出的 12 是 6 的另一个倍数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2130_math_number_theory.cpp](2130_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(n log X) | AC | 0.062 s | 1220 KB |
| [2130_math_number_theory.go](2130_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(n log X) | AC | 0.046 s | 7616 KB |
| [2130_math_number_theory.java](2130_math_number_theory.java) | Java 1.8 | math, number_theory | O(n log X) | AC | 0.125 s | 8892 KB |
| [2130_math_number_theory.py](2130_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(n log X) | AC | 0.343 s | 18092 KB |
| [2130_math_number_theory.rs](2130_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(n log X) | AC | 0.031 s | 4564 KB |
