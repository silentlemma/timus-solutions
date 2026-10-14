# 1597. 屋顶上的切尔诺贝利之鹰（第 2 版）

[Timus 1597](https://acm.timus.ru/problem.aspx?space=1&num=1597) · 难度 1776 · binary_search

原题由 Sergey Vedernikov 准备。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

鸡蛋从不高于 E 的楼层扔下不会碎，高于 E 则会碎，未知的 E 满足 0 ≤ E ≤ n。有 k 个鸡蛋，没碎的可以再用，求最坏情况下确定 E
所需的最少扔蛋次数。最多 1000 组测试，k 和 n 不超过 10¹⁸，以 `0 0` 结束。这是
[第 1223 题](../../1200-1299/1223/README.zh.md) 的大数据版本。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

若干行 k 和 n，最后是 `0 0`。

## 输出

每组测试的最少扔蛋次数。

## 样例

### 样例 1

输入:

```
1 10
2 5
0 0
```

输出:

```
10
3
```

## 解法

把问题反过来：t 次扔蛋、k 个鸡蛋最多能确定多少层？第一次扔蛋把楼分成两部分：蛋碎了，下面的楼层还剩 t − 1 次和 k − 1 个蛋；
没碎，上面的楼层还剩 t − 1 次和 k 个蛋，所以 f(t, k) = f(t − 1, k − 1) + f(t − 1, k) + 1。
这个递推的解是 f(t, k) = C(t, 1) + C(t, 2) + … + C(t, k)。答案是使 f(t, k) ≥ n 的最小 t，f 随 t 增大，可以二分查找。

只有一个蛋时只能逐层扔，答案就是 n。有两个及以上的蛋时，f(t, 2) = t(t + 1)/2 在 t 小于 1.5·10⁹ 时就达到 10¹⁸，
所以在 t 不超过 U = 2·10⁹ 的范围内搜索。和按项累加，C(t, i) = C(t, i − 1)·(t − i + 1)/i，一旦超过 n 就停止，
这也覆盖了 k 极大的情况：各项增长极快，最多只需几十项。每组测试最多 31 步，每步约 60 项。

结果已在所有不超过 120 层、最多 8 个蛋的情形上与经典的按楼层和蛋数的动态规划对照。

注意事项：

- 乘积 C(t, i − 1)·(t − i + 1) 会溢出 64 位；C++、Go、Java 和 Rust 的解答把 C(t, i − 1) 写成 q·i + r，
  计算 q·(t − i + 1) + r·(t − i + 1)/i，结果精确，并在 q·(t − i + 1) 将超过 n 时立即放弃；
- 有 k ≥ 60 个蛋时答案就是对楼层的二分查找次数，即 n 的二进制位数，同一个循环就能给出；
- 一个蛋需要 n 次，可能超出搜索范围，所以先单独处理。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1597_binary_search.cpp](1597_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.015 s | 128 KB |
| [1597_binary_search.go](1597_binary_search.go) | Go 1.14 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.031 s | 1140 KB |
| [1597_binary_search.java](1597_binary_search.java) | Java 1.8 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.140 s | 892 KB |
| [1597_binary_search.py](1597_binary_search.py) | Python 3.12 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.140 s | 752 KB |
| [1597_binary_search.rs](1597_binary_search.rs) | Rust 1.75 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.046 s | 300 KB |
