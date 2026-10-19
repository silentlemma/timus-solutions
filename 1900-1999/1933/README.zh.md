# 1933. 奇数人数的循环配对矩阵

[Timus 1933](https://acm.timus.ru/problem.aspx?space=1&num=1933) · difficulty 408 · constructive

Original problem from Open Ural FU Championship 2012 | by Alexander Ipatov (prepared by Oleg Dolgorukov).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有R=2n+1名参与者与R轮。每轮安排n对互不相交的搭档，剩下一名担任
负责人。每对搭档不能重复，每人恰好负责一次。构造对称矩阵，记录
每对搭档在哪一轮合作。限制：1秒，64MB。

## 输入

一个整数n，1≤n≤100。

## 输出

R行，每行R个0..R整数。对角线为零，非对角项(i,j)表示成员i、j
配对的轮号1..R。总配对名额nR=C(R,2)，不允许重复就意味着每对
恰好合作一次。任何满足全部条件的安排都正确。

## 评测方式

checker.py读取R²个整数，检查对角线、范围、对称性、每轮n对无重复
参与者的搭档、每轮恰好一名负责人以及所有负责人不同。不同的合法
安排，包括轮号重排与成员重排，都被接受。

## 样例

```
1
```

```
0 1 2
1 0 3
2 3 0
```

## 解法

行列使用从零开始的i、j。对角线填0，其余填
A[i][j]=((i+j+R−1) mod R)+1。加R保证各语言中表达式非负。
对称性与轮号范围显然满足。

固定成员i，让j遍历全部R个编号，公式恰好给出每个轮号一次。
排除j=i后，真实搭档的轮号互不相同，仅缺少
L_i=((2i+R−1) mod R)+1。R为奇数，因此模R乘以2可逆，所有
缺失轮号L_i互不相同，即使R是合数也成立。故每轮恰好一人不配对，
其余每人出现一次，由对称性组成n对。不配对者负责；每人缺少一轮，
且缺失轮次各异，所以每人恰好负责一次。每个无序搭档只获一个矩阵
标签，不会重复。由此证明全部要求。

时间O(n²)，与输出项数一致。实现保存完整矩阵，含输出缓冲总空间O(n²)。

只需R为奇数，无需素数。零只应在对角线，搭档轮号在两个对称位置
相同。每轮一名负责人还不够，还要每人负责一次。轮号或成员重排
会改变矩阵却保持正确性，应检查结构属性而非与保存的矩阵逐字比较。

## 各语言说明

R≤201，轮号≤201，i+j+R−1≤600，普通整数足够。C++使用向量矩阵与
关闭同步的流；Go使用缓冲输出；Java、Rust构建输出字符串；Python
逐行连接数值。每个程序输出R行且无行尾空格。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1933_constructive.cpp](1933_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 492 KB |
| [1933_constructive.go](1933_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 1836 KB |
| [1933_constructive.java](1933_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.125 s | 2592 KB |
| [1933_constructive.py](1933_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.109 s | 744 KB |
| [1933_constructive.rs](1933_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 640 KB |
