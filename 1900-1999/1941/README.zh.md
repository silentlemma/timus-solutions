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

## 优化解法

`1941_two_pointers_optimized.py`. 保留精确 90 进制三元组编码和缺失次数滑窗不变量。729000 项差值及环形队列使用 Python 列表替代压缩 array 单元，避免每次更新的转换。文本经 16 KiB split 缓冲流式分词，不保留整段文本。更新前删除检查 deficit>=0，插入检查 deficit>0。时间 O(U+m+n)，状态 O(U+m) 加有界词缓冲，U=90^3。这是精确表示与输入输出权衡，并非哈希或新窗口算法；保留教学版。

精确源代码 PyPy 3.10 x64 Accepted #11326701：0.234 s / 17756 KB。2026-11-20 保存的当前 Python 语言族编译器比较：时间 2/16、内存 2/16，两项严格前十均通过。内存至少 1024 KB，故必须同时满足时间和内存。单独的两项第一语言目标未满足，保留星号。此前记录的优化 CPython 3.12 #11314998 为 0.89 s / 8604 KB。所选 PyPy 记录时间更低、内存更高；这是不同解释器的独立成对测量，并非纯算法加速或混合最小值。保留的简单 CPython 版当前 Accepted #11327563：0.781 s / 33640 KB。无需额外源代码副本或重复提交。

仅格式化后的自身 Accepted：`1941_two_pointers.py` #11327563。保留基础算法及其余源文件。

新 Go、Python、Rust 保留精确的 90 进制三元组编码及缺失次数不变量。Go、Rust 中模式与窗口频数在 0..m、m≤8000，用压缩有符号 16 位差值将 729000 项表降至 1458000 字节；其环形缓冲用 32 位精确编码。Go、Rust 用有界缓冲流式读入，总空间 O(U+m)。Python 以整数列表保存差值和环形队列，以更大存储换更快更新；文本词经有界 16 KiB 缓冲流式输入，状态 O(U+m) 加有界输入空间。修改前，删除检查 ≥0，插入检查 >0。第一换行仍区分模式与文本，包括 CRLF。保留全部简单版；C++、Java 复用合格基础版覆盖快速集合。

保留的 Accepted 基础版 [1941_two_pointers.cpp](1941_two_pointers.cpp), [1941_two_pointers.java](1941_two_pointers.java) 在保存比较中满足所需指标的严格前十或前 15% 收录，不增加相同优化副本。表为当前精确成对测量，星号表示单独语言目标。格式化不改算法，不将速度变化归功于格式化。

## 各语言说明

以下说明针对基础实现。

缺额需有符号，过量字母产生负值。Python用紧凑signed int数组；
Go用int32与字节字段；Java直接解析三元组，不为每个字母分配String。
Rust只保存一次输入并迭代切片。不使用概率指纹或字典，比较完全精确。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1941_two_pointers.cpp](1941_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(U+m+n) | AC | 0.046 s | 2996 KB | 11291874 |
| [1941_two_pointers.go](1941_two_pointers.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.062 s | 21096 KB | 11291875 |
| [1941_two_pointers.java](1941_two_pointers.java) \* | Java 1.8 | two_pointers | O(U+m+n) | AC | 0.187 s | 3336 KB | 11291879 |
| [1941_two_pointers.py](1941_two_pointers.py) | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.781 s | 33640 KB | 11327563 |
| [1941_two_pointers.rs](1941_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 6000 KB | 11291881 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1941_two_pointers_optimized.go](1941_two_pointers_optimized.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 1864 KB | 11315003 |
| [1941_two_pointers_optimized.py](1941_two_pointers_optimized.py) | PyPy 3.10 x64 | two_pointers | O(U+m+n) time; O(U+m) space plus bounded input | AC | 0.234 s | 17756 KB | 11326701 |
| [1941_two_pointers_optimized.rs](1941_two_pointers_optimized.rs) \* | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.015 s | 1364 KB | 11315010 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
