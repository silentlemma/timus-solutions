# 1186. 两个化学式所含原子是否相同

[Timus 1186](https://acm.timus.ru/problem.aspx?space=1&num=1186) · 难度 696 · strings

原题作者 Joseph Romanosky 和 Roman Elizarov，出自 2001–2002 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

化学式是用 `+` 分隔的若干序列，每个序列前面可以有倍数。序列是一串元素，每个
元素后面可以跟倍数；元素是一个化学符号（一个大写字母，后面可能跟一个小写字母）
或者用圆括号括起来的序列。给定一个左边和至多 10 个右边（每个至多 100 个字符），
判断每种化学元素在两边出现的总次数是否都相同。

时间限制：1 秒。内存限制：64 MB。

## 输入

左边，`N`，然后是 `N` 个右边。

## 输出

对每个右边，总数相同输出 `left==right`，否则输出 `left!=right`，两个化学式
都原样照抄。

## 样例

### 样例 1

输入：

```
C2H5OH+3O2+3(SiO2)
7
2CO2+3H2O+3SiO2
2C+6H+13O+3Si
99C2H5OH+3SiO2
3SiO4+C2H5OH
C2H5OH+3O2+3(SiO2)+Ge
3(Si(O)2)+2CO+3H2O+O2
2CO+3H2O+3O2+3Si
```

输出：

```
C2H5OH+3O2+3(SiO2)==2CO2+3H2O+3SiO2
C2H5OH+3O2+3(SiO2)==2C+6H+13O+3Si
C2H5OH+3O2+3(SiO2)!=99C2H5OH+3SiO2
C2H5OH+3O2+3(SiO2)==3SiO4+C2H5OH
C2H5OH+3O2+3(SiO2)!=C2H5OH+3O2+3(SiO2)+Ge
C2H5OH+3O2+3(SiO2)==3(Si(O)2)+2CO+3H2O+O2
C2H5OH+3O2+3(SiO2)!=2CO+3H2O+3O2+3Si
```

## 解法

统计每个化学式的原子数并比较。先按 `+` 分开（括号里不会有 `+`），在每一项中
读出前面的数，没有则为 1。然后用计数器栈扫描这一项，每个未闭合的括号对应一个
计数器：

- `(` 压入一个空计数器；
- `)` 弹出计数器，乘以括号后面的数，再加到下面的计数器上；
- 化学符号把它的倍数（默认 1）加到栈顶计数器上。

最底层的计数器乘以前面的数，就是这一项的贡献。每个化学式 `O(L)`，不计计数器上
的操作。

注意事项：

- `Co` 是一种元素，而 `CO` 是碳和氧，所以小写字母属于它前面的大写字母；
- 倍数可能含有 0，例如 `10`，尽管样例避开了与氧相像的数字 `0`；
- 没写倍数就是 1，无论在项前面，还是在元素或括号后面。

答案已在 300 个括号嵌套至多三层的随机测试（共 3000 个右边）上与另一份独立编写的
解答比对。

## 各语言说明

- 所有语言的解析方式相同，并比较各自的计数映射：Python 用 Counter，C++ 和
  Rust 用有序映射，Go 和 Java 用哈希表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1186_strings.cpp](1186_strings.cpp) | G++ 13.2 x64 | strings | O(L) per formula | AC | 0.015 s | 404 KB |
| [1186_strings.go](1186_strings.go) | Go 1.14 x64 | strings | O(L) per formula | AC | 0.015 s | 1288 KB |
| [1186_strings.java](1186_strings.java) | Java 1.8 | strings | O(L) per formula | AC | 0.187 s | 4096 KB |
| [1186_strings.py](1186_strings.py) | Python 3.12 x64 | strings | O(L) per formula | AC | 0.078 s | 524 KB |
| [1186_strings.rs](1186_strings.rs) | Rust 1.75 x64 | strings | O(L) per formula | AC | 0.031 s | 252 KB |
