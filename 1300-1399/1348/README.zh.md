# 1348. 让山羊进菜园 2

[Timus 1348](https://acm.timus.ru/problem.aspx?space=1&num=1348) · 难度 177 · geometry

原题作者 Pavel Egorov，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一只山羊用长为 L 的绳子拴在点 C，能吃到距 C 不超过 L 的一切。菠萝苗圃是线段 AB。求绳子至少要加长多少才能
够到至少一个菠萝，以及加长多少才能够到全部菠萝，保留小数点后两位。所有数都是整数，L ≥ 0，坐标的绝对值不超过
10 000。

时间限制：1 秒。内存限制：64 MB。

## 输入

A、B、C 的坐标和长度 L。

## 输出

两个加长量，每行一个。

## 评测方式

仓库测试按 |实际值-参考值| <= 0.01·max(1,|参考值|) 比较数值记号，拒绝非有限值，并精确比较非数值记号。

## 样例

### 样例 1

输入：

```
8 -6 8 6
0 0 7
```

输出：

```
1.00
3.00
```

## 解法

苗圃上最近的点是 C 在直线 AB 上的投影；若投影落在线段外，就改为 A 或 B。线段上离任意点最远的点是它的某个
端点。所以答案是 max(0, d_近 − L) 和 max(0, max(|CA|, |CB|) − L)。投影使用
t = (C − A) · (B − A) / |B − A|²，并限制在 0 到 1 之间；苗圃只有一个点（A = B）时取 t = 0。

L 没有上界，所以把它读成浮点数，而不是会溢出的整数。极大的 L 会变成极大的数或无
穷大，此时两个答案都是 0，这是正确的：任何距离都不超过 20000√2 < 30000。几何计算
耗时 `O(1)`；计入输入后，时间和空间都是 `O(k)`，其中 k 是输入字符数。

注意事项：

- 苗圃可能只是一个点（测试 02 和 08）；
- C 在苗圃所在直线上、位于某端之外时，最近点是那个端点而不是投影（测试 04）；
- 绳子已经够长时答案是 0，不是负数（测试 05）；
- L 可能超出整数和浮点数范围（测试 09–11）：作为浮点数它会变成无穷大，两个答案都
  是 0，而整数类型会溢出。

## 优化解法

`1348_geometry_optimized.rs`. 保留夹到线段内的投影、较远端点及 max(distance-rope,0)。以 scanf 读取七个 f64、printf 输出两个两位小数，替代输入文本解析和 Rust 格式化。零长线段取端点，解析为无穷的绳长使延长量为零。几何计算为 O(1) 次运算且显式状态大小恒定；读取含 k 个字符的绳长词元需要 O(k) 时间。内存收益由自身 Accepted 测量确认。

与 `1348_geometry.rs` 相比：时间 0.031 s → 0.031 s；内存 244 KB → 116 KB。

`1348_geometry_optimized.cpp`. 保留线段投影，把参数截到 [0,1]，并取较远端点得到最大距离。C scanf/printf 替代 C++ 流初始化和显式绳长记号字符串。几何仍使用 f64；绳长解析为正无穷时，两种延长量均为零。读取 k 字符绳长表示需 O(k)，显式几何状态为常数。

与 `1348_geometry.cpp` 相比：时间 0.015 s → 0.015 s；内存 396 KB → 144 KB。

`1348_geometry_optimized.java`. 保留相同的截断投影与端点几何。用有界字节读取器替代 Scanner；不受长度限制的绳长记号仍被解码并交给 Double.parseDouble。无穷大正确产生两个零延长量。这样减少 Scanner 开销，但任意长绳长表示仍需 O(k) 时间和记号存储。

与 `1348_geometry.java` 相比：时间 0.140 s → 0.109 s；内存 1856 KB → 1 072 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1348_geometry_optimized.cpp`：在该可比样本中，时间名次 1/276，内存名次 8/276。

`1348_geometry_optimized.java`：在该可比样本中，时间名次 10/47，内存名次 9/47。

`1348_geometry_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1348_geometry.cpp](1348_geometry.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 396 KB | 11307276 |
| [1348_geometry.go](1348_geometry.go) | Go 1.14 x64 | geometry | O(k) | AC | 0.031 s | 1080 KB | 11307278 |
| [1348_geometry.java](1348_geometry.java) | Java 1.8 | geometry | O(k) | AC | 0.140 s | 1856 KB | 11307281 |
| [1348_geometry.py](1348_geometry.py) | Python 3.12 x64 | geometry | O(k) | AC | 0.078 s | 496 KB | 11307292 |
| [1348_geometry.rs](1348_geometry.rs) | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 244 KB | 11307285 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1348_geometry_optimized.cpp](1348_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 144 KB | 11325059 |
| [1348_geometry_optimized.java](1348_geometry_optimized.java) \* | Java 1.8 | geometry | O(k) | AC | 0.109 s | 1072 KB | 11324783 |
| [1348_geometry_optimized.rs](1348_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 116 KB | 11325502 |


\* Accepted；尚未达到排名目标，该版本仍有优化空间。
