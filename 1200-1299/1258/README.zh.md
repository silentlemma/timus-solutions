# 1258. 办公室里的台球

[Timus 1258](https://acm.timus.ru/problem.aspx?space=1&num=1258) · 难度 417 · geometry

原题作者 Pavel Egorov，出自 2003 年 10 月 11 日斯维尔德洛夫斯克州中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一名程序员在 W × D 的房间里（2 ≤ W, D ≤ 1000）沿直线行走，像台球一样从墙上反弹。起点
和终点是房间内部（不在墙上）的整点，按顺序给出撞到的墙：L、R、F、B 分别表示左墙
（x = 0）、右墙（x = W）、前墙（y = 0）和后墙（y = D），最多 1000 次，且从不撞到墙角。
求行走的长度，四舍五入到小数点后四位。

时间限制：1 秒。内存限制：64 MB。

## 输入

W 和 D，然后 x0 y0，然后 x1 y1，然后撞墙序列（可能为空）。

## 输出

行走的长度。

## 样例

### 样例 1

输入：

```
10 20
9 1
1 19
FLRLRB
```

输出：

```
52.8015
```

## 解法

不去转动行走的方向，而是在每次撞墙时把房间镜像翻过去：整条路径变成一条线段，它的水平
和竖直跨度可以分别计算。

在 x 方向上只有 L 和 R 有关，而且它们必然交替出现。若没有，跨度为 |x1 − x0|。否则先
走到第一面侧墙（L 为 x0，R 为 W − x0），每两次相邻的侧墙撞击之间横穿宽 W 的房间，最后
从最后一面侧墙走到终点（L 为 x1，R 为 W − x1）：

```text
dx = first + (k − 1) · W + last
```

用 F、B 和 D 同样得到 dy，答案为 √(dx² + dy²)。侧墙撞击与前后墙撞击如何交错不影响
长度。K 次撞击为 `O(K)`。

注意事项：

- 即使在最小房间内，有效路径也不能撞到墙角；可以只撞一面墙（测试 07）；
- 撞墙序列可能为空，甚至整行缺失（测试 02）；
- 某一方向上的第一次撞击可能是两面墙中的任意一面（测试 03、06）；
- dx 和 dy 可达约 10⁶，因此 dx² + dy² 需要 64 位（测试 08）。

在 200 组数据上与构造每个随机测试所用直线段的长度比较过（线段与镜像网格的交点给出
撞墙序列）。

## 优化解法

新 Python 版本按碰撞的逆序反射终点：L 将 x 变成 −x，R 变成 2W−x，F 将 y 变成 −y，B 变成 2D−y。每次反射撤销一次反弹并保持长度，最终得到起点到展开终点的直线段。无需分别保存水平、垂直碰撞列表，也无需导入 math；用 0.5 次幂开平方，输出四位小数。时间 O(K)，分词输入空间 O(K)。保留普通 Python 版与其他基础版，其余四种语言的基础版已覆盖快速集合。

已通过评测的基础实现 [1258_geometry.cpp](1258_geometry.cpp), [1258_geometry.go](1258_geometry.go), [1258_geometry.java](1258_geometry.java), [1258_geometry.rs](1258_geometry.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1258_geometry_implementation_optimized.py`. 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11328529 (Python 3.12 x64): **0.062 s / 760 KB**. 历史对照: `1258_geometry_optimized.py` (Python 3.12 x64) — 0.093 s / 396 KB (#11314897).

`1258_geometry_optimized.rs`. 单次扫描统计每个轴的碰撞次数及首末墙，常数状态替代总墙列表和两个筛选副本，展开距离公式不变。

Accepted #11328695 (Rust 1.75 x64): **0.015 s / 244 KB**. 历史对照: `1258_geometry.rs` (Rust 1.75 x64) — 0.046 s / 264 KB (#11284107).

## 各语言说明

以下说明针对基础实现。

- 所有语言都按方向统计撞击并使用同一公式。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1258_geometry.cpp](1258_geometry.cpp) | G++ 13.2 x64 | geometry | O(K) | AC | 0.001 s | 220 KB | 11284098 |
| [1258_geometry.go](1258_geometry.go) | Go 1.14 x64 | geometry | O(K) | AC | 0.031 s | 1120 KB | 11284100 |
| [1258_geometry.java](1258_geometry.java) | Java 1.8 | geometry | O(K) | AC | 0.109 s | 1532 KB | 11284105 |
| [1258_geometry.py](1258_geometry.py) | Python 3.12 x64 | geometry | O(K) | AC | 0.125 s | 504 KB | 11284104 |
| [1258_geometry.rs](1258_geometry.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.046 s | 264 KB | 11284107 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1258_geometry_optimized.py](1258_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(K) | AC | 0.093 s | 396 KB | 11314897 |
| [1258_geometry_implementation_optimized.py](1258_geometry_implementation_optimized.py) | Python 3.12 x64 | geometry, implementation | O(K) | AC | 0.062 s | 760 KB | 11328529 |
| [1258_geometry_optimized.rs](1258_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.015 s | 244 KB | 11328695 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
