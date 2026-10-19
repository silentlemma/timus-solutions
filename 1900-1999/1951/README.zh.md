# 1951. 统计相容的复数根

[Timus 1951](https://acm.timus.ru/problem.aspx?space=1&num=1951) · difficulty 1787 · number_theory

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Olga Soboleva).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计同时满足 xⁿ=A=a+bi 和 xᵐ=C=c+di 的复数 x，其中 i²=−1。
四个系数都是整数，两个右侧复数非零，指数为正。限制：1 秒、64 MB。

## 输入

第一行 a,b,n，第二行 c,d,m。
−10¹⁸≤a,b,c,d≤10¹⁸，包含端点；1≤n,m≤100。
a,b 至少一个非零，c,d 也至少一个非零。

## 输出

一个整数，表示公共复数根的数量。

## 评测方式

按记号逐个比较输出。

## 样例

```
0 1 2
1 0 2
```

```
0
```

```
1 0 2
1 0 4
```

```
2
```

## 解法

设 g=gcd(n,m)、p=n/g、q=m/g，则 gcd(p,q)=1。若 A^q=C^p，答案
为 g，否则为零。必要性由两个方程分别升至 q、p 次方得到。充分性：
取整数 u,v 使 up+vq=1，令 Y=A^u C^v。A,C 非零，所以负指数有定义。
相容条件推出 Y^p=A、Y^q=C。因此 x^g=Y 的所有根均满足原方程，
每个公共根反过来满足 x^g=A^u C^v。非零 Y 恰有 g 个不同的 g 次根，
得出计数结论。

通过模运算准确比较两个高斯整数幂。筛出 L=10000 以内的质数，取
不小于 5000 的前 K=510 个。区间内共有 560 个质数，所选从 5003
到 9521。规范化两坐标，二进制快速幂，再对每个模数比较两坐标。
任一不同则返回零，全部相同则返回 g。

这不是概率哈希。Z^e 的任一坐标绝对值至多
(|Re Z|+|Im Z|)^e。输入两坐标绝对值之和 ≤2·10¹⁸<2⁶¹，且 p,q≤100，
所以 A^q 与 C^p 的每个坐标差 D 满足
|D|<2·(2·10¹⁸)^100<2⁶¹⁰¹。每个所选质数 >4096=2¹²，乘积
P>2^(510·12)=2⁶¹²⁰>|D|。同余说明每个不同质数都整除 D，因此
P 整除 D；在 |D|<P 的范围只有零符合。两坐标都为零就准确相等。
正确性来自完整整数大小界，而非碰撞概率。

复数对的模乘为 (r₁r₂−i₁i₂, r₁i₂+i₁r₂)，随后分别取模。这是环
同态；高斯剩余环不必是域，因为没有使用除法或模逆。

O(L log log L + K log E) 时间、O(L) 空间，E=max(n,m)、L=10000、
K=510。筛只构造一次。把由范围固定的 L,K 视为常数，比较本身是
O(log E) 时间和固定存储。

指数必须先除 g：仅 Aᵐ=Cⁿ 可能并无公共根。两坐标、相位、负数都
重要。浮点模长或角度不能证明相等。少量质数不足以代替完整乘积界，
也不能假设高斯剩余环一定为域。两个右侧非零是证明的前提。

## 各语言说明

原生语言以有符号 64 位读入系数。乘法前将负余数规范到 0..prime−1。
规范后中间值绝对值小于 2·9999²<2³¹−1，但实现仍统一用 64 位。
不要直接相乘 10¹⁸ 的原始系数。只需标准库；Python/C++/Go/Java
缓存一份模数，Rust 构造一次列表并传入比较函数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1951_number_theory.cpp](1951_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(n,m)) | AC | 0.015 s | 412 KB |
| [1951_number_theory.go](1951_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(n,m)) | AC | 0.046 s | 1096 KB |
| [1951_number_theory.java](1951_number_theory.java) | Java 1.8 | number_theory | O(log max(n,m)) | AC | 0.156 s | 708 KB |
| [1951_number_theory.py](1951_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(n,m)) | AC | 0.093 s | 688 KB |
| [1951_number_theory.rs](1951_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(n,m)) | AC | 0.046 s | 244 KB |
