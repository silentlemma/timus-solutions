# 1945. 用质因数指数给乘法家族染色

[Timus 1945](https://acm.timus.ru/problem.aspx?space=1&num=1945) · difficulty 3183 · number_theory

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定互异正整数及g个厅。若存在正整数p和不同出生序号1≤i,j≤g，
使a=p·i、b=p·j，则a,b可能是兄弟，必须分到不同厅。即使p或其他
家族成员不在输入，也要保证所有可能关系均安全。求任意合法分配。
时限1秒，内存64 MB。

## 输入

n、g满足1≤n≤50000、2≤g≤5，随后n个互异整数a₁,…,a_n，范围
1..10^9。输出须按输入顺序对应。

## 输出

Yes及n个1..g的整数厅号；不可能时输出No。大小写严格，任何合法
分配都接受。下文证明全部合法输入都有解。

## 评测方式

检查器检验所有在某个父亲下可能成为兄弟的数对，接受任何合法的分配。根据下面的构造，在给定限制内 `No` 永远不正确。

## 样例

```
5 2
1
2
3
4
6
```

```
Yes
1
2
1
1
2
```

## 解法

令v_p(a)为质数p的指数，取w₃=min(g−1,3)，定义
F(a)=v₂(a)+w₃·v₃(a)+4·v₅(a)模g，厅号为F(a)+1。
反复除以2、3、5求这三个指数，无需其他质因子。小乘数完整表：

| g | w₃=min(g−1,3) | F(1),…,F(g) modulo g |
|---:|---:|---|
| 2 | 1 | 0, 1 |
| 3 | 2 | 0, 1, 2 |
| 4 | 3 | 0, 1, 3, 2 |
| 5 | 3 | 0, 1, 3, 2, 4 |

取F(2)=1迫使F(4)=2。g=3时令F(3)=2，g=4或5时令F(3)=3。
g=5剩下的余数由F(5)=4填补。较小g不约束用不到的乘数，故v₅
系数保持相同。每行恰有所有余数各一次。

质因数指数可加：v_q(p·i)=v_q(p)+v_q(i)，所以
F(p·i)=F(p)+F(i)模g。加同一F(p)不改变每行余数的互异性。
故完整可能家族p,2p,…,gp分入g个不同厅，输入中的任意子集也
安全。这证明所有合法输入可行，程序总输出Yes。这里只用循环
加法，即使g=4为合数也成立，不要求模数为质数。

时间O(n log A)，A=max a_i≤10^9，每个数成功除法最多29次，另有
三次失败整除检查。单个颜色辅助空间O(1)。完整缓冲程序至多
O(n)空间，C++、Go以有限缓冲流式处理输入输出。累加值≤4·29，
有符号32位足够。

可能兄弟比值不一定为整数：g≥3时4、6共有父亲2。3、4在g=3时
可同厅，g=4则不可。父亲不必出现在队列中。w₃随g变化，余数
需加一，保持输入顺序及Yes/No大小写。答案可与样例不同。

## 各语言说明

仅整数运算，每行一个厅。Java、Rust构建输出，Python保存输入
和结果。只除2、3、5，无需到sqrt(A)的完整分解、一般图染色或
搜索无解输入。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1945_number_theory.cpp](1945_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log A) | AC | 0.031 s | 436 KB |
| [1945_number_theory.go](1945_number_theory.go) | Go 1.14 x64 | number_theory | O(n log A) | AC | 0.109 s | 2740 KB |
| [1945_number_theory.java](1945_number_theory.java) | Java 1.8 | number_theory | O(n log A) | AC | 0.125 s | 3760 KB |
| [1945_number_theory.py](1945_number_theory.py) | Python 3.12 x64 | number_theory | O(n log A) | AC | 0.187 s | 7052 KB |
| [1945_number_theory.rs](1945_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log A) | AC | 0.031 s | 2148 KB |
