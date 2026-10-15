# 1673. 考试资格

[Timus 1673](https://acm.timus.ru/problem.aspx?space=1&num=1673) · 难度 1220 · number_theory

原题作者 Igor Chevdar，出自 2008 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 位老师上 N² 次实验课：老师 t 上编号为 t、N + t、2N + t、… 的课。N 名学生中的学生 j 恰好去编号为 j 的倍数
的课；学生若去过每位老师的至少一次课，就获得考试资格。恰有 K 名学生获得资格；输出最小可能的 N，若不存在则输出 0。

## 输入

K（1 ≤ K ≤ 2·10⁹）。

## 输出

最小的 N，或 0。

## 样例

### 样例 1

输入：

```
8
```

输出：

```
15
```

### 样例 2

输入：

```
3
```

输出：

```
0
```

## 解法

老师 t 上的是编号模 N 余 t 的课。学生 j 去 j、2j、…、Nj，它们模 N 取遍 gcd(j, N) 的所有倍数；这恰好是全部余数
当且仅当 gcd(j, N) = 1。所以 K = φ(N)（欧拉函数），问题就是求满足 φ(N) = K 的最小 N。

设 N = p₁^e₁ ⋯ p_r^e_r，则 φ(N) = ∏ (pᵢ − 1) pᵢ^(eᵢ − 1)。每个 pᵢ − 1 都整除 K，所以只需尝试形如 d + 1 的素数，
其中 d 是 K 的因数。K ≤ 2·10⁹ 至多有 1536 个因数；每个 d + 1 用以 2、3、5、7 为底的 Miller–Rabin 检验，在
3.2·10⁹ 以下是精确的。

记忆化搜索按递增顺序使用候选素数：least(rest, i) 是从第 i 个素数起各素数幂的乘积中、欧拉函数等于 rest 的最小值。
对从 i 起每个满足 (p − 1) | rest 的素数 p，依次尝试 p¹、p²、…（只要幂还能整除剩余部分），对剩余部分用更靠后的素数
递归，并保留最小的乘积。每个状态是 K 的一个因数加一个素数下标，答案为 least(K, 0)。对 D 个因数和 P 个候选素数，
至多 `O(D · P²)` 步，实际远少于此。

易错点：

- K = 1 时 N = 1：只有一位老师和一次课时，唯一的学生获得资格（测试 03）；
- 大于 1 的奇数 K 永远不是欧拉函数值（测试 02），某些偶数也不是，最小的是 14（测试 08）；
- 答案可能超过 2³¹：φ(2 500 015 625) = 2·10⁹（测试 06）。

对所有不超过 300 的 K 以及不超过 3000 的每第七个 K，答案与欧拉函数筛法找到的最小 N 一致；对大的 K，与一个独立的
已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1673_number_theory.cpp](1673_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(D P^2) | AC | 0.062 s | 1848 KB |
| [1673_number_theory.go](1673_number_theory.go) | Go 1.14 x64 | number_theory | O(D P^2) | AC | 0.078 s | 5620 KB |
| [1673_number_theory.java](1673_number_theory.java) | Java 1.8 | number_theory | O(D P^2) | AC | 0.203 s | 8080 KB |
| [1673_number_theory.py](1673_number_theory.py) | Python 3.12 x64 | number_theory | O(D P^2) | AC | 0.375 s | 5048 KB |
| [1673_number_theory.rs](1673_number_theory.rs) | Rust 1.75 x64 | number_theory | O(D P^2) | AC | 0.046 s | 3292 KB |
