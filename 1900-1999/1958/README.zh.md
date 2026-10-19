# 1958. 按元素值进行循环交换排序

[Timus 1958](https://acm.timus.ru/problem.aspx?space=1&num=1958) · difficulty 3577 · constructive

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Olga Soboleva (prepared by Denis Dublennykh).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

用以下操作把 1…n 的排列 p 排序：选择值 a，1≤a≤n，找到它当前的零基
位置 k，交换 p[k] 与 p[(k+a) mod n]。参数是元素值，不是下标。
输出不超过 10⁶ 次操作，或报告不可能。限制：1 秒、64 MB。

## 输入

先给 n，1≤n≤500，再给 n 个整数，恰为 1…n 的排列。

## 输出

若无法排序，输出 `Impossible`；否则先输出操作数 m，0≤m≤10⁶，随后
m 行依次给各次操作的参数。任何正确序列均可，不要求最少。下述构造证明
所有合法输入都能排序，因此程序从不输出 `Impossible`。

## 评测方式

检查器执行输出的操作，接受任何不超过限制且能把排列排好序的操作序列。

## 样例

```
5
1 3 5 2 4
```

```
3
4
3
3
```

## 解法

把最后的位置 n−1 当缓冲区。若其值 a<n，执行 a 将它与
(n−1+a) mod n=a−1 交换，a 直接就位。不断重复直到缓冲值为 n，称为清空。

一次清空中，每步固定一个新值，之后其他值 b 只指向不同的 b−1，
不会破坏已经固定的位置。因此至多 n−1 次调用后缓冲值变为 n。
先执行一次清空。

此时存在包含 n 的正确后缀。若全排列已正确则结束；否则找到值 1，
重复执行 1 直到它到最后。这是向右相邻交换，无环绕。再次清空并重复。

### 后缀为何增长

设一轮前 k…n−1 已正确，k>0，则 1 严格位于该后缀之前。把 1 推到最后
后，后缀所有值左移一格：k+1 位于 k−1，k+2 位于 k，…，n 位于 n−2。

接着清空时，只有固定 n−1 才能从 n−2 取出 n。n−1 又只能通过先固定
n−2 进入缓冲；反推得到必经 k,k+1,…,n−1 的链。清空中已固定的值不会
再被移走。因此不仅恢复旧后缀，还把 k 固定到 k−1，正确后缀至少增长一格。

每轮都前进，最终必然成功。初始清空最多 n−1 次，之后最多 n−1 轮，
每轮最多 n−1 次移动 1 和 n−1 次清空调用。因此

m≤(n−1)+2(n−1)²=(n−1)(2n−1)≤498501<10⁶。

n=1 或原本已排序时输出零。每个输出参数都是真实的一次操作，不是压缩指令。

含每轮查找 1 与输出的总时间 O(n²)。保存操作 O(n²) 空间，排列本身 O(n)。
不要混淆值 a 与下标 k，不要在取模公式中用一基位置。a=n 是合法空操作，
清空不会使用它。最终必须是 1…n，循环移位不算有序。

## 各语言说明

C++、Go、Rust 保存向量/切片。Java 8 按证明的容量分配原生 int 数组，
避免装箱。Python 保留整数引用并每 4096 次分块输出，避免巨大十进制字符串
列表。Rust 仅用标准库；原生版本普通整数足够。资源测试选择 CPython。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1958_constructive.cpp](1958_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 1416 KB |
| [1958_constructive.go](1958_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 7624 KB |
| [1958_constructive.java](1958_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 9216 KB |
| [1958_constructive.py](1958_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.234 s | 6288 KB |
| [1958_constructive.rs](1958_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.078 s | 4964 KB |
