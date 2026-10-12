# 1350. 食堂

[Timus 1350](https://acm.timus.ru/problem.aspx?space=1&num=1350) · 难度 389 · implementation

原题作者 Pavel Egorov，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

菜单上有 N ≤ 100 种食材，当天的饭菜用了其中 M 种不同的食材，但不知道是哪几种。K + 1 ≤ 101 名学生吃了这顿饭；
已知每个人对哪些食材有危险。第一个学生吃完后安然无恙。对其余 K 名学生，若饭菜对其一定无害输出 `YES`，若一定
含有对其有害的食材输出 `NO`，两种情况都可能时输出 `MAYBE`。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 N 个食材名，然后是 K，再是 K + 1 个块：每块先给数量，再给相应个数的危险食材，第一块属于第一个学生。输入
以 M 结尾。

## 输出

K 行，每行 `YES`、`NO` 或 `MAYBE`。

## 样例

### 样例 1

输入：

```
7
Rafinad
Kefir
Pastila
Smetana
Chokolade
Kljukva
Imbir
3
3
Rafinad
Kefir
Imbir
1
Rafinad
3
Kefir
Kljukva
Smetana
2
Imbir
Smetana
3
```

输出：

```
YES
NO
MAYBE
```

## 解法

第一个学生没事，所以对其有危险的食材一个都不在饭菜里：饭菜是其余食材（安全集合 S）中的某 M 种。对另一个
危险食材集合为 D 的学生：

- 若 M = 0，或 S 中没有食材属于 D，任何可能的饭菜都无害：`YES`；
- 若 S 中不属于 D 的食材少于 M 种，任何 M 种食材的饭菜都必须取到 D 中的某种：`NO`；
- 否则有的饭菜能避开 D，有的会包含它：`MAYBE`。

用集合实现，`O(N · K)`。

注意事项：

- M = 0 时什么都没吃，大家都没事（测试 02）；
- 名字区分大小写：`Milk` 和 `milk` 是两种食材（测试 04）；
- 不在 S 中的危险食材无关紧要，因为它们不可能出现在饭菜里。

在 400 个最多 6 种食材的随机食堂上，与枚举所有可能饭菜的结果比较过。

## 各语言说明

- 五种解答都统计 S 中属于和不属于 D 的食材数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1350_implementation.cpp](1350_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·K) | AC | 0.062 s | 1344 KB |
| [1350_implementation.go](1350_implementation.go) | Go 1.14 x64 | implementation | O(N·K) | AC | 0.031 s | 2156 KB |
| [1350_implementation.java](1350_implementation.java) | Java 1.8 | implementation | O(N·K) | AC | 0.140 s | 6524 KB |
| [1350_implementation.py](1350_implementation.py) | Python 3.12 x64 | implementation | O(N·K) | AC | 0.078 s | 2240 KB |
| [1350_implementation.rs](1350_implementation.rs) | Rust 1.75 x64 | implementation | O(N·K) | AC | 0.015 s | 1560 KB |
