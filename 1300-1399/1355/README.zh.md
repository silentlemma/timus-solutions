# 1355. 再谈秃顶

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · 难度 212 · number_theory

原题作者 Aleksandr Bikbaev，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

酒馆用正整数编号，从酒馆 n 只能走到编号为 n 的倍数的酒馆。路线从酒馆 a 出发，必须到达酒馆 b，途中每个酒馆
（包括 a 和 b）都喝一杯麦酒。对 T ≤ 20 组 1 ≤ a, b ≤ 10⁹，输出最多能喝几杯，若到不了 b 则输出 0。

时间限制：1 秒。内存限制：64 MB。

## 输入

T，然后是 T 行，每行 a 和 b。

## 输出

T 行答案。

## 评测方式

精确比较答案词元。每个新源码有完整目标环境检查、独立数学比较及哈希绑定的自身Accepted；保留简单版本的各自测量。

## 样例

### 样例 1

输入：

```
5
30 89
2 16
3 243
1 1
2 2
```

输出：

```
0
4
5
1
1
```

## 已接受提交更新

更新的文件：[1355_number_theory_math.py](1355_number_theory_math.py)。解答表列出了与当前源文件完全对应的新 Accepted 结果。这些文件此前的比较测量和排名属于旧源文件版本，作为历史数据保留。缓存审计确认该题所有可用语言均有达标实现。保留教学版本以保持清晰；若同一源文件同时承担快速版本的角色，它也必须满足性能标准。

## 解法

路线上每个数都整除下一个数，所以只有 a 整除 b 时才能到达 b。此时每一步都把编号乘上一个大于 1 的因子，所有因子
的乘积为 q = b / a。要经过尽量多的酒馆，每个因子都应是素数，于是步数为 Ω(q)，即 q 按重数计的素因子个数。答案
是 1 + Ω(q)，把酒馆 a 本身也算上。

用试除法试到 √q ≤ 31 623 即可求出 Ω(q)。`O(T · √(b / a))`。

注意事项：

- a = b 时喝一杯，而不是零杯（样例）；
- b 小于 a 或不是 a 的倍数时答案为 0（测试 04）；
- T 可以为 0，此时不输出答案（测试 02）；
- q = 2²⁹ 的步数最多，共 30 杯（测试 03）。

## 优化解法

`1355_number_theory_optimized.go`. 保留 R=B/A 因数分解：不整除返回零，R=1 返回一，先除二再试奇数。重数给出同一答案，无筛或因数列表。各查询 O(Σ√R) 时间、常数额外空间。 以 Go 1.14 syscall.Read/Write 使用有界 256 字节输入及 64 字节输出缓冲，重试 EINTR、部分写入并处理零字节 EOF，移除 fmt/bufio/os.File 初始化开销。Linux 测试和 Windows 交叉构建验证功能及构建；下列配对内存指标来自我们精确源在 Windows 评测的 Accepted。保留清晰教学源。

与 `1355_number_theory.go` 相比：时间 0.015 s → 0.046 s；内存 1100 KB → 268 KB。

`1355_number_theory_optimized.rs`. 保留 B/A 的计重素因子数及初始链元素，A 不整除 B 则零。先去二因子，再只试奇除数，条件 d<=value/d，残余素数再加一。同一试分解算法，但除法更少、查询输出流式。可整除查询总最坏 O(sum sqrt(B/A))、O(1) 辅助空间，比值一仍输出一。

与 `1355_number_theory.rs` 相比：时间 0.015 s → 0.015 s；内存 212 KB → 44 KB。

基础版本保留试除法。快速 Python 版本计算商与不超过 1000 的所有素数之积的最大公约数，以识别小素因子，再按完整重数从商中除去它们。其余素因子大于 1000，而商不超过 10^9，因此最多剩下两个。第二个固定乘积包含 1001 到 31623 之间的素数。合数余项必有此范围内的因子，而大于 10^6 的素数余项与乘积互素，据此分别计入两个或一个因子。两个乘积由筛法预先生成，并存为十六进制常量。

- `1355_number_theory_math.py`: 0.062 s / 584 KB; 基础 `1355_number_theory.py`: 0.109 s / 392 KB; 相对变化: 时间 -43.1%, 内存 +49.0%.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1355_number_theory_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB | 11285268 |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB | 11285270 |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB | 11285272 |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB | 11285271 |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB | 11285273 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1355_number_theory_math.py](1355_number_theory_math.py) | Python 3.12 x64 | number_theory, math | O(T*(P+log Q)) bounded arithmetic, P=1000 | AC | 0.062 s | 616 KB | 11330230 |
| [1355_number_theory_optimized.rs](1355_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(sum sqrt(B/A)) time; O(1) space | AC | 0.015 s | 44 KB | 11325504 |
| [1355_number_theory_optimized.go](1355_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(Σ√R) time; O(1) space | AC | 0.046 s | 268 KB | 11325656 |
