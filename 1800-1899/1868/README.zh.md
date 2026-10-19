# 1868. 预测竞赛

[Timus 1868](https://acm.timus.ru/problem.aspx?space=1&num=1868) · 难度 158 · implementation

原题作者 Denis Dublennykh，出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

世界总决赛上前四名获得金牌，接下来四名获得银牌，再接下来四名获得铜牌。几位老将做了形如"X 队获得 Y 种奖牌"的预测，Vadik 给猜对次数最多的每位老将付五美元。已知按名次排列的十二支获奖队伍和全部预测，Vadik 要付多少钱？

## 输入

从第一名到第十二名的十二个队名，然后是 n（1 ≤ n ≤ 100）和 n 份预测。每份预测先给出猜测数 kᵢ，接着 kᵢ 行 "队名 : 奖牌"，奖牌为 "gold"、"silver" 或 "bronze"。任何预测都不会给一支队两枚奖牌，也不会把同一种奖牌给四支以上的队。队名由 1 到 30 个拉丁字母、下划线、点和逗号组成。

## 输出

Vadik 支付的美元数。

## 样例

### 样例 1

输入：

```
Zhejiang_U
U_of_Michigan_at_Ann_Arbor
Tsinghua_U
St._Petersburg_SU
Nizhny_Novgorod_SU
Saratov_SU
Friedrich_Alexander_U
Donetsk_National_U
Jagiellonian_U_in_Krakow
Moscow_SU
Ural_SU
U_of_Waterloo
3
6
Moscow_SU : gold
St._Petersburg_SU_of_ITMO : gold
Warsaw_U : gold
Tsinghua_U : gold
Nizhny_Novgorod_SU : silver
Saratov_SU : silver
6
Warsaw_U : gold
Saratov_SU : gold
Tsinghua_U : gold
Donetsk_National_U : silver
St._Petersburg_SU_of_ITMO : silver
Ural_SU : bronze
6
Zhejiang_U : gold
Tsinghua_U : gold
Shanghai_Jiao_Tong_U : gold
Fudan_U : gold
Moscow_SU : silver
Nizhny_Novgorod_SU : silver
```

输出：

```
15
```

## 解法

队名中没有空格，所以输入就是一串单词：十二个队名，然后每条猜测是队名、冒号和奖牌。用一个从十二个队名到奖牌的字典（第 1–4 名金牌，5–8 名银牌，9–12 名铜牌）判断猜测是否正确；字典里没有的队什么也没得。统计每位老将猜对的次数，给次数最多的每位老将付五美元。`O(n·k)` 次字典查询。

样例中每位老将都猜对三次，所以三人都获胜，Vadik 付 15 美元。

注意事项：

- 奖牌由名次决定：队名按顺序给出，前四名是金牌，依此类推；
- 预测中可能出现根本没有获奖的队；
- 队名区分大小写，并且可能只由点和逗号组成；
- 如果谁都没猜对，所有老将以零次并列第一，每人都要付钱。

在 150 次随机竞赛上，金额与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1868_implementation.cpp](1868_implementation.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 444 KB |
| [1868_implementation.go](1868_implementation.go) | Go 1.14 x64 | implementation | O(n k) | AC | 0.015 s | 1220 KB |
| [1868_implementation.java](1868_implementation.java) | Java 1.8 | implementation | O(n k) | AC | 0.093 s | 1196 KB |
| [1868_implementation.py](1868_implementation.py) | Python 3.12 x64 | implementation | O(n k) | AC | 0.078 s | 692 KB |
| [1868_implementation.rs](1868_implementation.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 536 KB |
