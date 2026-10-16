# 1818. 诚实的渔夫

[Timus 1818](https://acm.timus.ru/problem.aspx?space=1&num=1818) · 难度 1925 · number_theory

原题出自 Tavrida NU Akai Contest，2010 年 8 月彼得罗扎沃茨克夏季集训。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个渔夫依次分渔获。第 i 个醒来的人扔掉 aᵢ 条鱼，使剩下的鱼能平分成 n 份，拿走一份，留下另外 n − 1 份，并不知道别人已经拿过自己的一份。
已知所有 aᵢ，求最少可能的渔获，至少一条鱼。

## 输入

n（2 ≤ n ≤ 2000），然后是 a₁, …, aₙ（0 ≤ aᵢ ≤ n − 1）。

## 输出

最少的渔获。

## 样例

### 样例 1

输入：

```
2
1 1
```

输出：

```
3
```

### 样例 2

输入：

```
3
1 0 2
```

输出：

```
19
```

## 解法

若第 k 个渔夫找到 Fₖ 条鱼，条件是 Fₖ ≡ aₖ (mod n)，下一个人找到 Fₖ₊₁ = (Fₖ − aₖ)/n · (n − 1)。
一旦 Fₖ ≡ aₖ，由于 aₖ < n，Fₖ ≥ aₖ 自动成立。

渔获增加 t 会使 Fₖ 增加 t·((n − 1)/n)^(k−1)。当 t = s·nʲ 时，对前 j 个渔夫这是 n 的倍数，他们的条件保持不变，而第 j + 1 个渔夫多得 s·(n − 1)ʲ ≡ s·(−1)ʲ。
因此渔获可以按 n 进制逐位确定：第 j 步取 [0, n) 中唯一能满足第 j + 1 个渔夫的 s，渔获加上 s·nʲ，这个渔夫找到的鱼加上 s·(n − 1)ʲ，然后处理下一个渔夫。
可行的渔获恰好是模 nⁿ 的一个剩余类，所以答案就是这个剩余，若它为 0 则为 nⁿ。

数字会增长到大约 n·log₁₀ n ≈ 6600 位，所以所有解法都使用大整数：Go、Java 和 Python 用库，C++ 和 Rust 用一个以 10⁹ 为基的小类型，只包含这里需要的运算：乘加、减法、对小数的除法和取余。
`O(n² log n)` 次位运算。

对第二个样例：渔夫 1 需要 X ≡ 1 (mod 3)，所以 X = 1，渔夫 1 找到 1，给渔夫 2 留下 0，后者需要 0：可以，s = 0。
渔夫 3 也得到 0，但需要 2；X 加上 s·9 会让渔夫 3 多得 s·4 ≡ s，所以 s = 2，X = 19。

注意事项：

- 剩余为 0 意味着 nⁿ 条鱼，而不是 0：至少捕到了一条鱼；
- (n − 1)ʲ 模 n 在 1 和 −1 之间交替，所以奇数步上那一位要变号；
- 每个渔夫找到的鱼数必须精确保存，而不是模 n：除以 n 会把高位混进来。

答案在 n ≤ 5 时与暴力搜索一致，在 n 最大到 2000 的随机测试上与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1818_number_theory.cpp](1818_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^2 log n) | AC | 0.031 s | 1032 KB |
| [1818_number_theory.go](1818_number_theory.go) | Go 1.14 x64 | number_theory | O(n^2 log n) | AC | 0.046 s | 5716 KB |
| [1818_number_theory.java](1818_number_theory.java) | Java 1.8 | number_theory | O(n^2 log n) | AC | 0.250 s | 5244 KB |
| [1818_number_theory.py](1818_number_theory.py) | Python 3.12 x64 | number_theory | O(n^2 log n) | AC | 0.109 s | 2064 KB |
| [1818_number_theory.rs](1818_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^2 log n) | AC | 0.046 s | 320 KB |
