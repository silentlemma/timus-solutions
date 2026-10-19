# 1940. 统计没有小真因子的年份

[Timus 1940](https://acm.timus.ru/problem.aspx?space=1&num=1940) · difficulty 835 · number_theory

Original problem from Open Ural FU Championship 2012 | by Ksenia Karpova (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

检查编号为A+1至A+B的B个年份，包含末年。对编号n依次尝试
2,3,…,n−1作为除数，每次花一分钟。找到因子或用完k分钟即停止。
没有找到因子就认为该年为质数年，即使n实际为合数；若真因子
候选提前用尽，也通过。求通过的年份数。时限1秒，内存64 MB。

## 输入

三个整数A,B,k，2≤A,B≤10^9，1≤k≤300。最大年份2·10^9。
空白分隔，允许换行。

## 输出

一个0到B之间的整数，表示区间(A,A+B]内通过的年份数。

## 评测方式

按一个整数标记比较，空白不影响结果。

## 样例

```
23 7 3
```

```
2
```

## 解法

k分钟内最后可试的除数是y=k+1。合数除数无须单独考虑，
因为更小的质因子已试过。记不超过y的质数为p₁,…,p_s。

令φ(x,t)表示[1,x]中不被前t个质数整除的整数个数，包含1。
递推式为φ(x,t)=φ(x,t−1)−φ(⌊x/p_t⌋,t−1)。被删去的倍数
与除以p_t后仍通过前t−1个质数检查的商一一对应。缓存(x,t)，
两个区间端点共用缓存。

但质数n≤y不能被自身拒绝，因为只试到n−1。将它们补回：

answer = φ(A+B,s)−φ(A,s) + π(min(A+B,y))−π(min(A,y))。

其余被删除的合数都有不超过y的真质因子，故没有其他例外。
数字1在两个前缀相减时抵消；左端不含，右端包含。

取b=min(s,6)个小质数作递归基底，乘积W≤30030。预计算一个
周期中每个前缀的存活数，φ(x,b)由完整周期与余数前缀O(1)求出。

更高层中φ(0,t)=0；若1≤x<p_t，仅1存活。若p_t≤x<p_t²，
存活合数的两个最小质因子都必须大于p_t，乘积会超过x，所以
φ(x,t)=1+π(x)−t。筛到L=301²并求质数个数前缀，足以回答
这些查询。其余状态用递推。每步t减一，基底及剪枝由此归纳
证明整个计数正确。

设N=A+B，s=π(k+1)≤62，b≤6，W≤30030，L=301²。对每个端点X，
⌊X/d⌋只有O(√N)个不同值，嵌套向下取整除法仍属于这种形式。
缓存状态O(s√N)。期望时间O(L log log L+bW+s√N)，空间
O(L+W+s√N)，递归深度≤s。筛和周期都小，没有与B等长的循环或数组。

从A+1开始，包含A+B，除数试到k+1。没有小因子的合数也通过，
例如k=3时的25。不能用质数本身将其删除。新增的除数为合数时
答案可能不变。无须逐年扫描十亿年份，也无须无剪枝的全部子集容斥。

## 各语言说明

端点和计数均能放入有符号32位：N≤2·10^9，答案≤10^9。
将x左移六位并拼接t的缓存键必须用64位。C++、Go、Rust使用
标准哈希表；Java用可增长的原始类型开放寻址表，避免装箱对象。
Python整数不限位宽，周期前缀用unsigned short数组。全部只用
标准库，输出整数和末尾换行。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1940_number_theory.cpp](1940_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 3596 KB |
| [1940_number_theory.go](1940_number_theory.go) | Go 1.14 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 8528 KB |
| [1940_number_theory.java](1940_number_theory.java) | Java 1.8 | number_theory | O(s sqrt(N)) | AC | 0.140 s | 6668 KB |
| [1940_number_theory.py](1940_number_theory.py) | Python 3.12 x64 | number_theory | O(s sqrt(N)) | AC | 0.171 s | 8424 KB |
| [1940_number_theory.rs](1940_number_theory.rs) | Rust 1.75 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 5564 KB |
