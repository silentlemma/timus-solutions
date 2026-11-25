# 1181. 把三色多边形切成三色三角形

[Timus 1181](https://acm.timus.ru/problem.aspx?space=1&num=1181) · 难度 456 · constructive

原题作者 Dmitry Filimonenkov，出自 2002 年 2 月 16 日在叶卡捷琳堡举行的第三届乌拉尔国立大学个人程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个有 `4 ≤ N ≤ 1000` 个顶点的凸多边形，顶点涂成 R、G、B 三色；三种颜色都
出现，且相邻顶点颜色不同。用互不相交的对角线把多边形切成三角形，使每个三角形
三种颜色的顶点各一个；若不可能则输出 0。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后是按环绕顺序给出的颜色。

## 输出

对角线条数，然后是用顶点编号对表示的各条对角线。

## 评测方式

只要 `N − 3` 条互不相同的对角线不相交，且切出的每个三角形都有三种颜色，就被
接受。这样的切法总是存在，所以 `0` 永远是错的。

## 样例

### 样例 1

输入：

```
7
RBGBRGB
```

输出：

```
4
1 3
3 7
5 7
5 3
```

## 解法

若某种颜色只出现一次，就从那个顶点向其他顶点画出所有对角线。扇形中的每个三角形
都由该顶点和其余部分的两个相邻顶点组成，它们彼此不同，也与该顶点不同。

否则每种颜色至少出现两次。这时存在一个两侧邻居颜色不同的顶点：如果每个顶点的
两个邻居颜色都相同，颜色就会沿多边形以周期二重复，只会出现两种颜色。用连接它
两个邻居的对角线把这个顶点切下；这个三角形三色齐全，剩下的部分仍然三色都有
（被删顶点的颜色在别处还有），也没有同色的邻居。重复这一步，直到某种颜色只剩
一个或只剩一个三角形。所以答案总是存在，共 `N − 3` 条对角线。用列表直接删除，
`O(N²)`。

注意事项：

- 答案永远不是 0，尽管题目提到了它；
- 切掉顶点后颜色计数会变化，某种颜色可能后来才变成只有一个，这时由扇形收尾；
- 奇数边形不可能两色交替，这也说明寻找邻居不同色的顶点总能成功。

每个输出的切法都在 200 个至多 33 个顶点的随机多边形和所有测试（包括一千个顶点
的多边形）上通过了检查程序。

## 优化解法

线性版本保留三色耳的正确性证明，以及某种颜色只剩一个顶点时的扇形收尾。left、right 数组构成循环双向链表，每次删耳只需 O(1)，同时更新颜色计数。先把左右邻居颜色不同的顶点加入队列；每次删除后，只有两个幸存邻居的资格可能改变。过期或已删除的队列项直接跳过。只要每种颜色至少出现两次，就必有合适的耳，否则多边形只能交替使用两种颜色。某种颜色唯一时，从该顶点作扇形剖分。初始至多 N 项，每刀只添加两项，因此总时间和空间为 O(N)，并保留原始顶点编号。

通过评测的 Python 3.12 x64 版本耗时 0.093 秒，基础版为 0.203 秒，内存为 900 KB，基础版为 760 KB。

## 各语言说明

原有列表实现作为 O(N²) 的简单版本保留。所有新版本使用线性队列和邻接链。C++、Go、Rust 按 N ≤ 1000 确定数组上限，队列至多需要 3N 项。Go、Rust 的 12000 字节输出缓冲足够保存 N−3 对四位数编号。Go 使用标准句柄，Rust 使用有界 C runtime 输入输出和 C 入口。Python 使用 deque，Java 使用基本类型数组队列。任意正确的三色三角剖分均可通过。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1181_constructive.cpp](1181_constructive.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 408 KB | 11283313 |
| [1181_constructive.go](1181_constructive.go) | Go 1.14 x64 | constructive | O(N²) | AC | 0.031 s | 1188 KB | 11283315 |
| [1181_constructive.java](1181_constructive.java) | Java 1.8 | constructive | O(N²) | AC | 0.218 s | 6632 KB | 11283326 |
| [1181_constructive.py](1181_constructive.py) | Python 3.12 x64 | constructive | O(N²) | AC | 0.203 s | 760 KB | 11283321 |
| [1181_constructive.rs](1181_constructive.rs) | Rust 1.75 x64 | constructive | O(N²) | AC | 0.031 s | 476 KB | 11283329 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1181_constructive_optimized.cpp](1181_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 132 KB | 11314704 |
| [1181_constructive_optimized.go](1181_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 388 KB | 11314727 |
| [1181_constructive_optimized.java](1181_constructive_optimized.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 552 KB | 11314749 |
| [1181_constructive_optimized.py](1181_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.093 s | 900 KB | 11314762 |
| [1181_constructive_optimized.rs](1181_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 92 KB | 11314780 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
