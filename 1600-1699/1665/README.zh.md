# 1665. 院长的金融金字塔

[Timus 1665](https://acm.timus.ru/problem.aspx?space=1&num=1665) · 难度 440 · number_theory

原题作者 Alex Samsonov，出自 2008 年 1 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

第 1 天晚上桌上有一份申请。之后每天申请数乘以一个整数因子，这个因子是 2 或大于 1 的奇数，每天可以不同。只有在
偶数日、且当天晚上桌上恰好有 N 份申请时才会付钱。对每个 N 判断这是否可能。

## 输入

T（1 ≤ T ≤ 100），然后是 T 个数 N（1 ≤ N ≤ 2²⁵ − 1）。

## 输出

对每个 N 输出 `YES` 或 `NO`。

## 样例

### 样例 1

输入：

```
4
4
7
6
30
```

输出：

```
NO
YES
NO
YES
```

## 解法

第 d 天的申请数是 d − 1 个因子的乘积，而 d 必须是偶数，所以问题是 N 能否写成奇数个因子的乘积，每个因子为 2 或
大于 1 的奇数。设 N = 2ᵃ · r，r 为奇数。只有因子 2 能提供 2，所以恰好有 a 个因子为 2，奇数因子的乘积为 r。

- 若 r = 1，因子恰有 a 个：a 为奇数时 `YES`（N = 1 是第 1 天，不会付钱）。
- 若 a 为偶数且 r > 1，a 个 2 加上 r 本身共 a + 1 个因子，是奇数个：`YES`。
- 若 a 为奇数，r 必须拆成偶数个大于 1 的奇数因子，这当且仅当 r 不是素数时可行（拆成两个，需要时更多）：r 为合数
  时 `YES`，r 为素数时 `NO`。

素性用奇数试除到 √r 来判断，最多约 2900 个除数。`O(T · √N)`。

易错点：

- N = 1 和 a 为偶数的 N = 2ᵃ 都是 `NO`；a 为奇数的 2ᵃ 是 `YES`（测试 02）；
- 奇数次幂的 2 乘以一个素数是 `NO`（样例中的 6，测试 03 中的 2²³ · 3）。

对不超过 3000 的每个 N，答案都与穷举所有因子序列的结果一致，也与一个独立的已通过实现一致。

## 优化解法

新 Go 保留因子数量奇偶性分类，为整批输入只筛一次奇素数。仅在因子 2 的指数为奇数时检查余数素性，因此已去掉至少一个 2，奇余数小于 2²⁴，平方根小于 R=4096。合数余数必有准备列表中的素因子。使用 p²≤余数，正确包含素数平方。纯二次幂提前处理，第一天的一份申请仍为 NO。筛表及 16 位素数列表占 O(R)，工作量 O(R log log R+T·π(R))。标准句柄代替 fmt。保留所有普通源码，其他四种语言合格基础版继续覆盖快速集合。

已通过评测的基础实现 [1665_number_theory.cpp](1665_number_theory.cpp), [1665_number_theory.java](1665_number_theory.java), [1665_number_theory.py](1665_number_theory.py), [1665_number_theory.rs](1665_number_theory.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1665_number_theory.cpp](1665_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 128 KB | 11288646 |
| [1665_number_theory.go](1665_number_theory.go) | Go 1.14 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 1084 KB | 11288647 |
| [1665_number_theory.java](1665_number_theory.java) | Java 1.8 | number_theory | O(T sqrt N) | AC | 0.125 s | 448 KB | 11288649 |
| [1665_number_theory.py](1665_number_theory.py) \* | Python 3.12 x64 | number_theory | O(T sqrt N) | AC | 0.093 s | 412 KB | 11288648 |
| [1665_number_theory.rs](1665_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T sqrt N) | AC | 0.031 s | 208 KB | 11288650 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1665_number_theory_optimized.go](1665_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(R log log R + T·π(R)) | AC | 0.015 s | 288 KB | 11315121 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
