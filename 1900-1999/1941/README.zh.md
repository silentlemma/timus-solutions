# 1941. 统计多重集合相同的窗口

[Timus 1941](https://acm.timus.ru/problem.aspx?space=1&num=1941) · difficulty 432 · two_pointers

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov (prepared by Alex Samsonov).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每个字母由三个有序ASCII符号组成，每个码值在33至122之间，
共有90³=729000种字母。给定非空模式串m≤8000字母和非空文本
n≤500000字母，统计连续窗口中字母多重集合等于模式串的个数。
重复次数必须相同，字母内部符号顺序有意义，窗口允许重叠。
时限1秒，内存64 MB。

## 输入

第一行模式串，第二行文本。每个字母恰好三个相邻符号，字母之间
用空白分隔。第一行的边界决定模式长度，不单独给出m、n。

## 输出

一个整数：匹配窗口数。若m>n，输出0。

## 评测方式

比较一个整数标记，空白不影响结果。

## 样例

```
aaa bbb ccc
aaa aaa bbb ccc aaa zzz aaa bbb ccc
```

```
3
```

## 解法

将三元组(a,b,c)编码为((a−33)·90+(b−33))·90+(c−33)。各位在
0..89，得到0..728999的双射，不是哈希。建729000项有符号缺额
数组D，初值为模式频率；另建m个编码的环形缓冲区，missing=m。

每次输入新字母，若缓冲区满，先移除最旧的x：修改前D[x]≥0
则missing加一，再将D[x]加一。插入y时，修改前D[y]>0则missing
减一，再将D[y]减一。覆盖环形位置并循环前进。missing为零时
统计一个窗口；尚未插满m个时，不可能满足m个所需出现，故不会误计。

不变量为D[x]=模式次数[x]−当前窗口次数[x]，且missing等于所有
正缺额之和。移除恰在原D[x]≥0时增加缺额；插入恰在原D[y]>0时
填补缺额，更新保持不变量。满窗口两边总次数相等，所以没有正
缺额等价于全部缺额为零，也即多重集合相等。每个长度m窗口恰访问一次。

设U=729000，时间O(U+m+n)，计数核心空间O(U+m)。C++、Java流式
读文本；Python、Go、Rust保存输入，完整程序总空间O(U+m+n)。
答案至多max(0, n−m+1)≤500000，有符号32位足够。

一个字母是三元组，不是单个ASCII字符；三元组内部重排会改变字母。
集合不能代替多重次数。移除看≥0，插入看>0，均在修改前判断。
计入重叠及最后窗口，不移动整个缓冲区，也不在每步扫描全字母表。
当m>n时没有窗口（测试03），因此上界必须取与零的较大值。

## 各语言说明

缺额需有符号，过量字母产生负值。Python用紧凑signed int数组；
Go用int32与字节字段；Java直接解析三元组，不为每个字母分配String。
Rust只保存一次输入并迭代切片。不使用概率指纹或字典，比较完全精确。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1941_two_pointers.cpp](1941_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(U+m+n) | AC | 0.046 s | 2996 KB |
| [1941_two_pointers.go](1941_two_pointers.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.062 s | 21096 KB |
| [1941_two_pointers.java](1941_two_pointers.java) | Java 1.8 | two_pointers | O(U+m+n) | AC | 0.187 s | 3336 KB |
| [1941_two_pointers.py](1941_two_pointers.py) | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.734 s | 33664 KB |
| [1941_two_pointers.rs](1941_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 6000 KB |
