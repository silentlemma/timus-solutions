# 1624. 快离开这里！

[Timus 1624](https://acm.timus.ru/problem.aspx?space=1&num=1624) · 难度 5072 · implementation

原题出自 2008 年冬季彼得罗扎沃茨克集训的 SPbSU ITMO Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

监狱是一个 W × H 的格子网（2 ≤ W · H ≤ 150），相邻格子之间有墙或门，四周都是墙。
两名失明的侦察员从未知的格子出发（可能是同一个），轮流尝试向北、南、东或西走一步，
报告方向以及是否成功；奇数号报告属于第一名侦察员。给定 K 条报告（K ≤ 10⁵），输出
两人位置都确定的第一条报告编号，或者数据不足，或者与之前报告矛盾的第一条报告（优先）。

时间限制：2 秒。内存限制：64 MB。

## 输入

W、H 和 K，然后是 K 条形如 `E+` 或 `N-` 的报告。

## 输出

三种信息之一，附报告编号。

## 样例

### 样例 1

输入：

```
2 1 4
E+
W-
N-
S-
```

输出：

```
The scouts are safe at step number 2
```

### 样例 2

输入：

```
2 1 4
N-
W-
N-
S-
```

输出：

```
There is not enough data
```

### 样例 3

输入：

```
2 1 4
N-
W-
N-
S+
```

输出：

```
A mistake has been made at step number 4
```

## 解法

每名侦察员记录相对于自己未知起点的位置、走过的位置范围，以及相对起点每条边上看到的
是门还是墙。未知量是两个起点。第一名侦察员的起点必须使其走过的范围留在监狱内，这给出
每个坐标的一个区间；第二名同理。

两人只有通过起点之间的位移才会遇到同一面墙。若第一名在相对边 e 上看到门，第二名在
同类的相对边 f 上看到墙，则位移 e − f 不可能。这些位移记在一张 (2H − 1) · (2W − 1)
的表里。剩下的起点对数是所有未标记位移之和，每个位移给出第一名起点的一个矩形；计数到
2 就停止。计数为 1 表示已经定位，为 0 表示有错，同一名侦察员在同一条边上报告了门和墙
也是错。

计数只在侦察员看到新的边或扩大范围时才会变化，这至多发生几百次，所以只在那时重新计算。
E 次这样的事件共 `O(K + E · W · H)`。

易错点：

- 即使侦察员已被定位，之后出现的错误也必须报告；
- 走得比监狱还宽是错误（测试 05）；
- 两名侦察员可以站在同一个格子里而互不察觉。

在 132 个随机监狱（报告有真实的也有篡改的）上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1624_implementation.cpp](1624_implementation.cpp) | G++ 13.2 x64 | implementation | O(K + E · W · H) | AC | 0.046 s | 412 KB |
| [1624_implementation.go](1624_implementation.go) | Go 1.14 x64 | implementation | O(K + E · W · H) | AC | 0.046 s | 3004 KB |
| [1624_implementation.java](1624_implementation.java) | Java 1.8 | implementation | O(K + E · W · H) | AC | 0.109 s | 4636 KB |
| [1624_implementation.py](1624_implementation.py) | Python 3.12 x64 | implementation | O(K + E · W · H) | AC | 0.156 s | 8036 KB |
| [1624_implementation.rs](1624_implementation.rs) | Rust 1.75 x64 | implementation | O(K + E · W · H) | AC | 0.031 s | 1436 KB |
