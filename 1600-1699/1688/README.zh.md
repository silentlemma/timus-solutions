# 1688. Team.GOV!

[Timus 1688](https://acm.timus.ru/problem.aspx?space=1&num=1688) · 难度 134 · implementation

原题作者 Alexander Ipatov，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三名队员点的东西一样，每次都由其中一人买单。另一名队员在别人替其支付的钱（每张账单的三分之一）超过 n 时即可退出。
按顺序给出账单，判断在第几次聚餐之后会发生这件事。

## 输入

n 和 m（1 ≤ n ≤ 2 · 10⁹；0 ≤ m ≤ 3000），然后是 m 张账单，均为 1 到 2 · 10⁶ 之间的整数。

## 输出

对第一次满足条件的聚餐 x 输出 “Free after x times.”，若始终不满足则输出 “Team.GOV!”。

## 样例

### 样例 1

输入：

```
1666 5
2000
1024
900
1156
1200
```

输出：

```
Free after 4 times.
```

### 样例 2

输入：

```
3000 5
2000
1024
900
1156
1200
```

输出：

```
Team.GOV!
```

## 解法

维护账单的累计和。份额 total / 3 超过 n 当且仅当 total > 3n，这样就不用处理分数；
在第一次满足该条件时停下。`O(m)`。

注意事项：

- 3n 可达 6 · 10⁹，累计和也一样：要用 64 位整数（测试 06）；
- 份额恰好等于 n 还不够，比较是严格的（测试 04 和 06）。

答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1688_implementation.cpp](1688_implementation.cpp) | G++ 13.2 x64 | implementation | O(m) | AC | 0.015 s | 136 KB |
| [1688_implementation.go](1688_implementation.go) | Go 1.14 x64 | implementation | O(m) | AC | 0.015 s | 1124 KB |
| [1688_implementation.java](1688_implementation.java) | Java 1.8 | implementation | O(m) | AC | 0.078 s | 1016 KB |
| [1688_implementation.py](1688_implementation.py) | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 788 KB |
| [1688_implementation.rs](1688_implementation.rs) | Rust 1.75 x64 | implementation | O(m) | AC | 0.015 s | 224 KB |
