# 1650. 亿万富翁

[Timus 1650](https://acm.timus.ru/problem.aspx?space=1&num=1650) · 难度 174 · segment_tree

原题作者 Pavel Atnashev，出自 NEERC 2008 东部分区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 位财富已知的亿万富翁起初在给定的城市。m 天中他们会旅行：第 d 天的行程晚上出发、次日早上到达，所以
从第 d + 1 天起生效。对每个城市，统计其亿万富翁财富总和严格高于所有其他城市的天数，并按名称排序列出
至少有一天这样的城市。

## 输入

n（1 ≤ n ≤ 10000），然后 n 行“姓名 城市 财富”（财富在 1 到 10¹¹ 之间）。然后是 m
和 k（1 ≤ m ≤ 50000，0 ≤ k ≤ 50000），以及按天递增的 k 行“天 姓名 目的城市”
（1 ≤ 天 ≤ m − 1），每人每天最多旅行一次。姓名和城市至多 20 个拉丁字母，区分大小
写。

## 输出

每个至少领先一天的城市输出“城市 天数”，按普通字符顺序（ABC…Zabc…z）排列。

## 样例

### 样例 1

输入：

```
5
Abramovich London 15000000000
Deripaska Moscow 10000000000
Potanin Moscow 5000000000
Berezovsky London 2500000000
Khodorkovsky Chita 1000000000
25 9
1 Abramovich Anadyr
5 Potanin Courchevel
10 Abramovich Moscow
11 Abramovich London
11 Deripaska StPetersburg
15 Potanin Norilsk
20 Berezovsky Tbilisi
21 Potanin StPetersburg
22 Berezovsky London
```

输出：

```
Anadyr 5
London 14
Moscow 1
```

## 解法

给每个出现过的城市编号，并在城市总财富上维护一棵线段树。每个节点保存其下的最大总和、达到它的叶子数
以及其中一个叶子，于是根节点立刻告诉我们是否有唯一领先的城市以及是哪一个。一次旅行就是两次单点修改：
财富离开一个城市并加入另一个。

两个旅行日之间领先者不变，所以按段计数：在执行第 d 天的行程之前，当前领先者（若唯一）获得从上次计数到
第 d 天的天数；最后一次行程之后获得到第 m 天为止的天数。总和可达 10¹⁵，要用 64 位。C 个城市时为
`O((n + k) log C)`。

易错点：

- 最高处平局意味着那天无人领先（测试 03），所以输出可能完全为空；
- 第 d 天的行程仍把第 d 天留给原来的城市；
- 顺序按字符编码，所以大写开头的名称排在所有小写名称之前（测试 05）。

在 60 段随机历史上答案与逐日计数一致，在生成的测试上与一个独立的已通过实现一致。那个实现在有人“旅行”
到自己已在的城市时会出错，评测数据显然不含这种情况；这里的程序把这样的旅行视为原地不动。

## 优化解法

优化的 C++ 解法逐条读取行程并立即处理，而不是先全部存下：每次行程最多带来一个新
城市，所以线段树一开始就按初始城市数加 k 分配大小。用一个从名字到城市和财富的映
射代替两个映射，结点保存唯一领先城市的编号（平局时为平局标记），而不是叶子的个
数，树由初始总额自底向上建立，更新时一旦某个结点的最大值和领先者都没有变化就停止
上溯，因为更上面的结点不会再变。名字用 `scanf` 读入 21 字节的缓冲区，而不是用
`iostream`：{1650_segment_tree_optimized.cpp}。

优化的 Go 解法逐条读取行程并立即处理，而不是先全部存下：每次行程最多带来一个新城
市，所以线段树一开始就按初始城市数加 k 分配大小。用一个从名字到城市和财富的映射
代替两个映射，结点保存唯一领先城市的编号（平局时为平局标记），而不是叶子的个数，
树由初始总额自底向上建立，更新时一旦某个结点的最大值和领先者都没有变化就停止上
溯，因为更上面的结点不会再变。单词来自 `bufio.Scanner`，而不是 `fmt.Fscan`：
{1650_segment_tree_optimized.go}。

优化的 Java 解法逐条读取行程并立即处理，而不是先全部存下：每次行程最多带来一个新
城市，所以线段树一开始就按初始城市数加 k 分配大小。用一个从名字到城市和财富的映
射代替两个映射，结点保存唯一领先城市的编号（平局时为平局标记），而不是叶子的个
数，树由初始总额自底向上建立，更新时一旦某个结点的最大值和领先者都没有变化就停止
上溯，因为更上面的结点不会再变。记号逐行读取，而不是先把全部输入收集到
`StringBuilder` 中：{1650_segment_tree_optimized.java}。

优化的 Python 解法逐条读取行程并立即处理，而不是先全部存下：每次行程最多带来一个
新城市，所以线段树一开始就按初始城市数加 k 分配大小。用一个从名字到城市和财富的
映射代替两个映射，结点保存唯一领先城市的编号（平局时为平局标记），而不是叶子的个
数，树由初始总额自底向上建立，更新时一旦某个结点的最大值和领先者都没有变化就停止
上溯，因为更上面的结点不会再变。输入逐行读取（每行一条记录），而不是一次全部读
入：{1650_segment_tree_optimized.py}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1650_segment_tree_optimized.cpp`: 时间降低 -49.60%; 内存降低 +50.94%; 基础版本: `1650_segment_tree.cpp`.

- `1650_segment_tree_optimized.go`: 时间降低 +45.61%; 内存降低 +1.04%; 基础版本: `1650_segment_tree.go`.

- `1650_segment_tree_optimized.java`: 时间降低 -15.27%; 内存降低 +46.58%; 基础版本: `1650_segment_tree.java`.

- `1650_segment_tree_optimized.py`: 时间降低 +1.51%; 内存降低 +41.56%; 基础版本: `1650_segment_tree.py`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree.cpp](1650_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.125 s | 20700 KB | 11304018 |
| [1650_segment_tree.go](1650_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.171 s | 18416 KB | 11288517 |
| [1650_segment_tree.java](1650_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.203 s | 27324 KB | 11288519 |
| [1650_segment_tree.py](1650_segment_tree.py) | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.062 s | 27776 KB | 11288518 |
| [1650_segment_tree.rs](1650_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log C) | AC | 0.046 s | 13036 KB | 11304019 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree_optimized.cpp](1650_segment_tree_optimized.cpp) \* | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.187 s | 10156 KB | 11307264 |
| [1650_segment_tree_optimized.go](1650_segment_tree_optimized.go) \* | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.093 s | 18224 KB | 11307269 |
| [1650_segment_tree_optimized.java](1650_segment_tree_optimized.java) \* | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.234 s | 14596 KB | 11307271 |
| [1650_segment_tree_optimized.py](1650_segment_tree_optimized.py) \* | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.046 s | 16232 KB | 11307267 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
