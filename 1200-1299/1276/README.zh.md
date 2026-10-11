# 1276. 火车

[Timus 1276](https://acm.timus.ru/problem.aspx?space=1&num=1276) · 难度 736 · combinatorics

原题作者 Sergey Volchenkov、Vladimir Pinaev 和 Michael Kopachev，出自 2003 年 10 月 15–16 日在雷宾斯克举行的 ACM ICPC 2003–2004 俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 N ≤ 40 节车厢，每节左右两端各有一个 A 型或 B 型挂钩（AA、AB、BA 或 BB），机车也有这样
的挂钩。任何东西都不能掉头。由 K 节车厢组成的列车，相邻挂钩必须一致，两端还必须与机车
匹配：列车以与机车右挂钩相配的挂钩开头，以与其左挂钩相配的挂钩结尾，这样机车放在哪一端
都可以。把列车当作挂钩组成的字符串来比较，求不同列车的数目；若一列也组不成，输出 NO。

时间限制：1 秒。内存限制：4 MB。

## 输入

N 和 K，机车，然后是 N 节车厢。

## 输出

`NO`，或 `YES` 以及列车数。

## 样例

### 样例 1

输入：

```
4 4
AB
AA
AB
BA
BA
```

输出：

```
YES
2
```

### 样例 2

输入：

```
4 4
BA
AA
AB
BA
BA
```

输出：

```
NO
```

## 解法

把列车看成在 A、B 两个状态之间行走。AA 车厢停留在 A，BB 停留在 B，AB 从 A 切换到 B，BA 再
切换回来。所以切换车厢必定交替出现，以离开起始状态的那一种开头。切换车厢的个数 s 决定了
用多少 AB 和 BA 以及最终处于哪个状态，并把行走分成 s + 1 段，交替处于 A 和 B。

同类车厢完全相同，所以列车由每个 A 段放几节 AA、每个 B 段放几节 BB 决定。对每个终态正确
的 s，以及把其余 K − s 节车厢分成库存范围内的 a 节 AA 和 b 节 BB 的每种分法，累加

```text
C(a + rA − 1, rA − 1) · C(b + rB − 1, rB − 1)
```

其中 rA、rB 是 A 段和 B 段的数目（某状态没有段时，该类车厢只能用零节）。所有组合数的上标
不超过 41，总数也远小于 2⁶³。`O(K²)`。

注意事项：

- 列车的第一个挂钩必须与机车的右挂钩相配，最后一个与左挂钩相配；若弄反，第二个样例就会
  得到 `NO`；
- 同类车厢可以互换：四十节 AA 只组成一列火车（测试 05）；
- 不能接在自身后面的类型（例如 AB）组不成长于一节的列车（测试 08）。

在 300 个最多七节车厢的随机数据上，与列举所有不同列车的结果比较过。

## 各语言说明

- 所有语言都建立同样的组合数表，并对切换次数求和。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1276_combinatorics.cpp](1276_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 164 KB |
| [1276_combinatorics.go](1276_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.015 s | 1120 KB |
| [1276_combinatorics.java](1276_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.125 s | 504 KB |
| [1276_combinatorics.py](1276_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 624 KB |
| [1276_combinatorics.rs](1276_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 268 KB |
