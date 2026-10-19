# 1932. 四位标识符的距离分布

[Timus 1932](https://acm.timus.ru/problem.aspx?space=1&num=1932) · difficulty 961 · combinatorics

Original problem from Open Ural FU Championship 2012 | by Victor Vinogradov (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出互不相同的四字符十六进制标识符，统计恰好在一、二、三、四个
字符位置不同的无序对数。前导零占据实际位置。限制：1秒，64MB。

## 输入

首先 n，2≤n≤65536，随后 n 个互异的四字符字符串。
字符为0..9和小写a..f，0000是合法标识符。

## 输出

四个整数，按不同位置数递增排列。每个无序对恰好属于一个输出类别。

## 评测方式

精确比较四个整数记号。

## 样例

```
3
dead
beef
f00d
```

```
0 0 2 1
```

## 解法

对 k=1,2,3，令 S_k 为所有选定 k 个位置子集上投影相同的对数之和。
它有重数：若一对标识符有 r 个相同位置，就贡献 C(r,k)，每个合适
子集一次。由于标识符互异，不存在四个位置全相同的对。设 d_j 是
恰好 j 个位置不同的对数，则 S_3=d_1、S_2=3d_1+d_2、
S_1=3d_1+2d_2+d_3。因此 d_1=S_3，d_2=S_2−3d_1，
d_3=S_1−3d_1−2d_2，d_4=n(n−1)/2−d_1−d_2−d_3。
这些恒等式证明了恢复公式。

在线计算统计量。每个位置子集分别维护投影数字频数。新标识符到来时，
先把该键已有频数加入对应 S_k，再增加频数。每个匹配无序对仅在
后一个元素到来时计一次，故所得统计量准确。

需要四个大小16的单位置表、六个大小256的双位置表、四个大小4096
的三位置表，共17,984个计数器。不同位置子集用独立表。把标识符
解析为整数后仍提取固定四个半字节，因此保留前导零的位置含义。
投影键按原位置次序打包。

时间 O(14n+17984)，空间为17,984个频数加输入缓冲。四位与大小16
字母表固定时，时间 O(n)，频数工作空间 O(1)，含输入缓冲总空间 O(n)。

统计字符差异，不是二进制位：0000与000f只差一个位置。不同位置
子集不能共用表。S_k带二项式重数，并非至少k处相同的对数。
标识符互异是S_3=d_1的前提。先加旧频数再增加。答案顺序为1、2、
3、4个不同位置；解析整数时仍须保持固定四位的前导零语义。

## 各语言说明

累加使用有符号64位，先提升类型再乘 n(n−1)。n=65536时乘积
4,294,901,760在除以2之前已超出有符号32位；总对数2,147,450,880。
频数本身32位足够，单、双、三位置表分别至多4096、256、16。
C++、Go、Java、Rust使用宽累加器，Python使用精确整数。
Java缓冲读取十进制数量及十六进制代码。C++读取n后仅将输入流
设为十六进制，输出仍为十进制。Python选择CPython。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1932_combinatorics.cpp](1932_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.046 s | 720 KB |
| [1932_combinatorics.go](1932_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 3184 KB |
| [1932_combinatorics.java](1932_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.140 s | 4948 KB |
| [1932_combinatorics.py](1932_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.359 s | 4844 KB |
| [1932_combinatorics.rs](1932_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.046 s | 1332 KB |
