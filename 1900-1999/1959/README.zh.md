# 1959. 用重叠窗口众数恢复符号

[Timus 1959](https://acm.timus.ru/problem.aspx?space=1&num=1959) · difficulty 1062 · two_pointers

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Bulat Zaynullin).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

文本 s 长 n，模式 p 长 m<n。对每个长 m 的连续文本子串，计算与 p 的
汉明距离，再求和；汉明距离是不同位置数。至多一个序列含未知符号，
也可能都完整。恢复未知处使总和最小，已知符号不得改变。限制：1 秒、64 MB。

## 输入

先给 n，1≤n≤100000，及 n 个文本整数；再给 m，1≤m<n，及 m 个模式整数。
两条件合起来要求 n≥2。数值范围 0…100000，正数为符号 ID，零为未知。
两个序列不会同时含零。

## 输出

第一行恢复后的文本，第二行恢复后的模式。所有 ID 在 1…100000，保留已知
位置。任意最优恢复均可，不输出距离。

## 评测方式

检查器确认已知符号保持不变，并且每个恢复的符号都是其比较对象中出现最多的符号之一；根据下面的论证，任何这样的选择都是最优的，所以并列时任选其一。

## 样例

```
5
1 2 3 1 2
3
1 2 0
```

```
1 2 3 1 2
1 2 1
```

## 解法

### 独立选择

因为仅一侧有未知，每个未知符号的所有比较对象都是固定已知值。已知对
已知的贡献是常数。若某未知处参与 t 次比较，填 v 的贡献为 t−frequency(v)。
选择其比较对象的任意众数即可。未知处互不影响，局部最小之和即全局最小。
每个比较窗口非空且只含正 ID，所以总有合法最优符号。

设 g=n−m，下标从零开始。模式位置 j 比较文本 s[j…j+g]，窗口宽 g+1。
j 右移时删除旧左端、加入新右端。

文本位置 i 与满足 i=j+offset、0≤offset≤g、0≤j<m 的模式位置比较，
故窗口为 p[max(0,i−g)…min(m−1,i)]，两端均单调右移。逐个 i：若 i<m
加入 p[i]，若 i>g 删除 p[i−g−1]，然后若 s[i]=0 就取众数。窗口先增长，
可能滑动或停留，最后缩小。完整的对侧序列保持不变。

### 常数时间众数

保存 frequency[v]。频率 f>0 的符号组成侵入式双向链表，使用 previous[v]、
following[v] 和 head[f]；零仅作空链接，零频符号不入表。另保存最大非空频率
maximum。

更新时从旧链表移除符号，频率加减一，正频率则插入新链表头。新频率更大
则提高 maximum，否则在当前表空时递减。一次合法更新使最大频率最多减一：
删除后原符号仍以 f−1 留下，除非 f=1。因此更新和查询均 O(1)。
head[maximum] 即合法众数。

模式未知时，表头容量到 g+1；文本未知时用 m，因为先加右端再删左端，
中间窗口可能比最终滑动宽度临时大一。

时间、空间 O(n+m+σ)，σ 为最大输入 ID，σ≤100000。端点更新 O(n+m)，
数组直接索引。不能取全局众数、漏掉闭区间宽度 g+1、把零加入计数、修改
已知符号，或只考虑最佳一次对齐。独立性必须依赖只损坏一侧的保证。

程序不计算数值目标。单个计数适合 32 位整数，但总比较对数可达
2,500,050,000，超过 2³¹−1；验证总距离时用宽整数。

## 各语言说明

C++、Go 1.14、Java 8、Rust 1.75 使用原生数组/向量，Java 无逐符号对象。
Rust 仅用标准库。Python 使用索引列表，CPython 有资源余量。两侧都无零
时直接返回输入，不构建计数器。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1959_two_pointers.cpp](1959_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n+m+sigma) | AC | 0.046 s | 2300 KB |
| [1959_two_pointers.go](1959_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n+m+sigma) | AC | 0.171 s | 7228 KB |
| [1959_two_pointers.java](1959_two_pointers.java) | Java 1.8 | two_pointers | O(n+m+sigma) | AC | 0.171 s | 10212 KB |
| [1959_two_pointers.py](1959_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n+m+sigma) | AC | 0.453 s | 17424 KB |
| [1959_two_pointers.rs](1959_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n+m+sigma) | AC | 0.046 s | 6792 KB |
