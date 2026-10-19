# 1937. 由两个循环字符串组成回文

[Timus 1937](https://acm.timus.ru/problem.aspx?space=1&num=1937) · difficulty 1217 · suffix_structures

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

分别选择两个字符串A、B的循环移位。将移位后的A接在移位后的B
之前，要求整个拼接等于其反转。找任意一对起点或判断不存在。
限制：1秒、64MB。

## 输入

两行小写拉丁字母，依次为长度n的A和长度m的B，1≤m<n≤100000。
从选定字符开始循环读取，保持原有字母顺序。

## 输出

无解输出No；否则输出Yes，下一行输出A、B中的两个起点，
均从1编号，分别在1..n、1..m内。任意使拼接回文的起点均可。

## 评测方式

检查器确认输出的两个循环移位确实构成回文；对于 `No`，它独立判断确实不存在这样的一对。任何合法的一对都被接受。

## 样例

```
cdedab
bac
```

```
Yes
5 3
```

```
aaaa
bbb
```

```
No
```

## 解法

使用零起始下标。把A的一个移位写为U V，其中|U|=m、|V|=L=n−m。
U V Brot为回文，当且仅当V为回文且Brot=reverse(U)。这样可把
中间条件与循环移位匹配分开，无需尝试全部n·m对。

令C=reverse(B)、P=C+C[:-1]。P中所有长度m的窗口恰好是C的
全部循环移位。构造P的后缀自动机，扫描A+A的前n+m−1个字符，
维护出现在P中的最长后缀。有对应转移就前进，否则沿后缀链接
退回，长度缩至该状态的最大长度，直到有转移。匹配至少m个
字符时，a=position−m+1对应的外部窗口U属于C的循环移位。
这些位置恰好覆盖A的全部n个起点。

每个自动机状态记录最大长度、后缀链接、转移及一个出现终点f。
追加字符时创建新状态，沿后缀链接补缺失转移。首个已有转移p→q
若满足len(q)=len(p)+1，则链接至q；否则克隆q，将长度改为
len(p)+1，复制转移、链接及终点，沿链接重定向受影响的转移，
并将q与新状态都链接到克隆。该构造保持P的精确子串集合。
匹配词的最后m个字符也有终点f，因此j=f−m+1是C的一个移位起点，
0≤j<m。反转后B的起点为(−j mod m)，最终输出a+1及该起点+1。

中间部分在A+A上用Manacher，仅计算L所需的奇偶类型。奇半径
不含中心，仅数匹配字符对；偶半径以中心前的缝隙为轴。V起于
a+m时，条件为radius[a+m+floor(L/2)]≥floor(L/2)。Manacher
复用最右回文内部的镜像半径，只在右边界之外扩展，总工作量线性。
若任何起点都没有回文中段，可在构造自动机前直接拒绝。所返回
起点满足两个充要条件；扫描无结果则排除了全部可能的A移位。

固定26字母下，时间和空间均O(n+m)。稠密转移使用O(26m)个整数，
状态少于2|P|个。沿后缀链接的退回可由成功字符步数摊还。
Java每次至多扫描26条稀疏出边，渐进界不变。

先反转B再匹配，恢复起点时须取负模m。匹配长度至少m即可，
不必恰好m。不能漏掉最后起点n−1。周期串可有不同合法坐标。
回文中段与匹配外段必须在同一起点同时成立。m<n保证中段非空，
其奇偶性决定半径定义。

## 各语言说明

C++、Go、Rust和Python用32位稠密转移与状态数组；Go的int32、
Rust的i32避免主数组翻倍。Python在m=99999时自动机数据占
46,399,304字节，一个半径数组另占800,000字节。Java用原生
head/next/destination/letter数组，至多3|P|+1个转移槽和字节
字母，为JVM留出内存。全部索引和表偏移可放入32位整数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1937_suffix_structures.cpp](1937_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(n+m) | AC | 0.046 s | 46824 KB |
| [1937_suffix_structures.go](1937_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(n+m) | AC | 0.062 s | 49928 KB |
| [1937_suffix_structures.java](1937_suffix_structures.java) | Java 1.8 | suffix_structures | O(n+m) | AC | 0.218 s | 16404 KB |
| [1937_suffix_structures.py](1937_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(n+m) | AC | 0.796 s | 47932 KB |
| [1937_suffix_structures.rs](1937_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(n+m) | AC | 0.046 s | 46428 KB |
