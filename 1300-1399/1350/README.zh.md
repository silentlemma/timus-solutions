# 1350. 食堂

[Timus 1350](https://acm.timus.ru/problem.aspx?space=1&num=1350) · 难度 384 · implementation

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

平均 `O(N · K)`；C++ 为 `O(N · K · log N)`。

注意事项：

- M = 0 时什么都没吃，大家都没事（测试 02）；
- 名字区分大小写：`Milk` 和 `milk` 是两种食材（测试 04）；
- 不在 S 中的危险食材无关紧要，因为它们不可能出现在饭菜里。

在 400 个最多 6 种食材的随机食堂上，与枚举所有可能饭菜的结果比较过。

## 优化解法

紧凑版本为菜单上的每种食物分配索引。C++ 和 Rust 在排序数组中查找索引，Go 使用哈希表。Rust 复用同一缓冲区读取每个输入词。数组记录最后提到每种食物的学生，因此同一份名单中的重复名称只计一次。排除第一位学生的危险食物后，只保留每位其他学生的危险且可能入餐的食物数量。读到餐中食物种类数后，这些计数就足够了。

已通过评测的基础实现 [1350_implementation.java](1350_implementation.java), [1350_implementation.py](1350_implementation.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- 五种解答都统计 S 中属于和不属于 D 的食材数。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1350_implementation.cpp](1350_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·K·log N) | AC | 0.062 s | 1344 KB | 11285155 |
| [1350_implementation.go](1350_implementation.go) | Go 1.14 x64 | implementation | O(N·K) | AC | 0.031 s | 2156 KB | 11285156 |
| [1350_implementation.java](1350_implementation.java) \* | Java 1.8 | implementation | O(N·K) | AC | 0.140 s | 6524 KB | 11285160 |
| [1350_implementation.py](1350_implementation.py) \* | Python 3.12 x64 | implementation | O(N·K) | AC | 0.078 s | 2240 KB | 11285157 |
| [1350_implementation.rs](1350_implementation.rs) | Rust 1.75 x64 | implementation | O(N·K) | AC | 0.015 s | 1560 KB | 11285161 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1350_implementation_optimized.cpp](1350_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(N·K·log N) | AC | 0.015 s | 424 KB | 11310451 |
| [1350_implementation_optimized.go](1350_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(N·K) expected | AC | 0.031 s | 944 KB | 11310453 |
| [1350_implementation_optimized.rs](1350_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N·K·log N) | AC | 0.015 s | 192 KB | 11310869 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
