# 1162. 一系列带手续费的货币兑换能否让钱变多

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · 难度 185 · shortest_paths

原题作者 Nick Durov，出自 2001 年 ACM ICPC 东北欧区域赛北部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `N ≤ 100` 种货币和 `M ≤ 100` 个兑换点，每个兑换点在两种货币之间双向兑换，
每个方向有各自的汇率和手续费：兑换 `x` 得到 `(x − 手续费)·汇率`，金额任何时候
都不能为负。初始持有 `V` 单位的货币 `S`，判断是否存在一系列兑换，最后回到货币
`S` 且金额大于 `V`。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`、`M`、`S` 和 `V`，然后 `M` 行，每行是两种货币以及两个方向的汇率和手续费。

`1 ≤ S ≤ N ≤ 100`，`1 ≤ M ≤ 100`，`0 ≤ V ≤ 1000`。
汇率范围为 `[0.01, 100]`，手续费范围为 `[0, 100]`，两者最多有两位小数。
`V` 的小数位数没有限制。任意不重复使用兑换点的兑换序列，其最终金额与初始
金额之比小于 `10000`。

## 输出

`YES` 或 `NO`。

## 评测方式

精确比较答案词元。每个新源码有完整目标环境检查、独立数学比较及哈希绑定的自身Accepted；保留简单版本的各自测量。

## 样例

### 样例 1

输入：

```
3 2 1 10.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

输出：

```
NO
```

### 样例 2

输入：

```
3 2 1 20.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

输出：

```
YES
```

## 解法

货币是顶点，兑换方向是边；当 `x≥fee` 时可得到 `(x−fee)·rate`。
五份简单版本使用同步 Bellman–Ford：第 `j` 轮后 `best[c]` 是至多 `j`
次兑换可达的最大金额，下一轮只读旧数组并写另一个数组。正汇率使后续操作
单调，因此每个货币只保留最大金额不会丢失更好的可行后续。不可达与可达零值
须区别。

使用精确整数。令 `P=max(2,V的小数位数)`，初始共同分母 `D=10^P`；汇率和
手续费保存为整数百分位 `R,C`。若分子 `x<C·D/100`，跳过；否则新分子为
`(x−C·D/100)·R`，新分母为 `100D`。每轮保留金额和初始本金也乘 100。
不截断 V 的小数位，不用浮点数或 epsilon。

源货币超过初值立即 YES。整轮无改进就是不动点，答案 NO。第 `N` 轮仍改进
则存在可获利环：若改进路径的所有重复顶点段均未增加入口金额，删去它们
不会破坏可行性，也不会降低单调的后缀，剩余至多 `N−1` 条边的简单路径，
与第 N 轮新改进矛盾。环是 `A·x−B`、`B≥0`；在 `x≥0` 严格增益意味着
`A>1`，重复后金额无界。每个点有正汇率反向边，资金足够时可支付回到 S 的
手续费并超过 V。零本金不会增长。

至多 N 轮后金额有 `O(P+N)` 十进制位。松弛与复制为
`O(N(N+M)(P+N))` 位运算；计入十进制解析的保守上界为
`O(P²+N(N+M)(P+N))`。活动状态占 `O(N(P+N))` 位，另有 `O(M)` 固定大小边。
C++/Rust 基础版用百进制位，Go 用 `big.Int`、Java 用 `BigInteger`、Python
用大整数。基础源码只为既有常数 100 的两种角色命名并格式化，各有自身精确
SHA 的新 Accepted；全部五份原始字节均备份，算法不变。

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。没有其他作者的可比提交时，无法确认竞赛排名。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 精确源代码 Accepted #11326984：0.001 s / 248 KB。2026-11-20 保存的 G++ 13.2 比较：时间排名 1/437，内存排名 118/437。 内存低于 1024 KB，因此本次严格审计只看时间；星号仍对应单独的语言排名目标。其余语言说明保留历史样本。

- Go: 首选教学基础 `1162_shortest_paths.go`; 覆盖源码 `1162_shortest_paths_optimized.go`; 时间/内存名次 3/5, 其他作者记录 5/5.

- Java: 首选教学基础 `1162_shortest_paths.java`; 覆盖源码 `1162_shortest_paths_optimized.java`; 时间/内存名次 43/46, 其他作者记录 117/117.

- Python/PyPy: 首选教学基础 `1162_shortest_paths.py`; 覆盖源码 `1162_shortest_paths_optimized.py`; 时间/内存名次 75/1, 其他作者记录 77/77.

- Rust: 首选教学基础 `1162_shortest_paths.rs`; 覆盖源码 `1162_shortest_paths.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 优化解法

`1162_shortest_paths_optimized.java`. 保留起始货币无向分量上的精确同步 Bellman-Ford/Jacobi。边只读上一轮金额；独立拥有的 10^9 进制缓冲及分母缩放保留初始资金任意小数精度。从右往左直接构造九位一组的整数，至多补两个虚拟尾零；十次幂单位直接放入目标位。1024 字节读取器精确读取有限汇率和手续费的百分之一单位，直接输出 YES/NO，避免优化源码中的 BigInteger、字符串解析和格式化初始化。先判断能否付费再减，零本金拒绝，不连通部分无关。P 为初始小数位数、C 为保留顶点，保守界 O(P^2+C*(C+M)*(P+C)) 位工作、O(C*(P+C)+N+M) 存储。初始资金不截为两位小数。构造和算术与 BigInteger 独立比较，包含数千小数位；保留清楚的 BigInteger 教学版。

精确源代码 Java 1.8 Accepted #11327477：0.093 s / 524 KB。2026-11-20 保存的编译器组比较：时间 4/353、内存 3/353。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11308454 为 0.125 s / 1224 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1162_shortest_paths_optimized.java`: 0.093 s / 524 KB; 保留教学基础版 `1162_shortest_paths.java`: 0.125 s / 4932 KB.

`1162_shortest_paths_optimized.cpp`. 保留精确的同步 Bellman–Ford、源点连通分量压缩和可复用的 10^9 进制位数组。有限范围的汇率和手续费直接解析为整数百分之一单位，无需临时 token 字符串或异常式转换。初始资金仍沿用字符串到大整数位的路径，保留任意小数精度；比较保持精确。松弛、分母缩放和盈利环判定不变。D 为最大大整数位数、I 为输入字节数时，时间 O(N(N+M)D+I)，空间 O(ND+M+I)；D 随精度和轮数增长。

精确源代码 Accepted #11326984：0.001 s / 248 KB。2026-11-20 保存的 G++ 13.2 比较：时间排名 1/437，内存排名 118/437。

`1162_shortest_paths_optimized.rs`. 保留精确同步 Bellman–Ford 松弛，每轮共同分母乘 100。以基 10⁹ 的 u32 数位和 u64 进位替代基 100，复用两层金额及减乘临时缓冲。汇率费用仍为精确百分位，保留初始小数精度，不用浮点比较。最大数位数 D、输入 I 字节下保守 O(N(N+M)D+I) 时间、O(ND+M+I) 存储；D 随精度及轮数增长。

与 `1162_shortest_paths.rs` 相比：时间 0.046 s → 0.046 s；内存 300 KB → 128 KB。

**C++, Go, Java.** 三份优化版仍为精确 Jacobi 算法，命名 `_optimized`。先只保留 S 所在的
无向连通分量：兑换点有双向边，其他分量永远无助。保留 C 个顶点后 C 轮足够。
这只是结构裁剪，并不假定手续费一定付得起。

Go 复用各自拥有的 `big.Int` 缓冲和临时值，用 `Set` 复制，避免结构体浅拷贝。
C++/Java 改用 `10^9` 进制非负数、九位输入块，复用容量和临时对象，减少短位
或不可变中间数分配。零手续费省去成本减法。仍只读旧轮状态，不变为原地松弛。

当 `B=10^9`，单个位小于 B，汇率/手续费乘数至多 10000；含进位的乘积小于
`B·10000=10^13`，适合 C++ `uint64_t`、Java `long`。只在金额足够时做减法；
借位为 0 或 1，所用类型能容纳。原地乘法先读旧位后写新位，其他缓冲拥有独立
存储。覆盖零、进制幂及长借位链。渐近复杂度不变，减少位数、分配和顶点数。

**Python/PyPy.** Python保留精确同步Bellman–Ford和100^N预留尺度，使至多N次兑换除100不丢位。初始十进制数按至多1000位分块转换，不受一次转换长度上限影响。边元组保留预计算精确佣金。每八行兑换输入收集已失效解析对象，只改变内存寿命，不改变金额或可达性；以内存峰值换收集耗时。保留全部五种清晰精确版本。O(NM)精确松弛、O(N+M)数值记录，另有实测收集开销。

- `1162_shortest_paths_optimized.cpp`: 0.001 s / 248 KB; 基础: `1162_shortest_paths.cpp`, 0.046 s / 676 KB; 时间变化 -67.4%; 内存变化 -63.3%; 时间下限 0.015 s.
- `1162_shortest_paths_optimized.go`: 0.031 s / 1304 KB; 基础 `1162_shortest_paths.go`: 0.031 s / 5436 KB; 相对变化: 时间 -0.0%, 内存 -76.0%.

- `1162_shortest_paths_optimized.py`: 0.156 s / 416 KB; 基础 `1162_shortest_paths.py`: 0.078 s / 708 KB; 相对变化: 时间 +100.0%, 内存 -41.2%.

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1162_parsing_optimized.go`. 两位小数汇率和手续费直接解析为精确 int64 百分单位，避免每条边的临时大整数。保留任意精度初始金额、公共分母 Bellman–Ford 和独立复用的 big.Int，无浮点近似。 词元转换及数值输出按实际类型专门化，移除未使用的通用分支，保留算法和注释。 在当前输入块内转换完整数字段，仅在词元或块边界提交局部游标。负值累积支持有符号最小值，去掉逐位符号分支或读取调用，保留 EOF 和可选符号。

Accepted #11329137 (Go 1.14 x64): **0.015 s / 1168 KB**. 历史对照: `1162_shortest_paths.go` (Go 1.14 x64) — 0.031 s / 5436 KB (#11308459).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.046 s | 676 KB | 11308458 |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.031 s | 5436 KB | 11308459 |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.125 s | 4932 KB | 11308466 |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.078 s | 708 KB | 11308471 |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.046 s | 300 KB | 11308481 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1162_shortest_paths_optimized.cpp](1162_shortest_paths_optimized.cpp) | G++ 13.2 x64 | shortest_paths | O(N(N+M)D+I) time; O(ND+M+I) space | AC | 0.001 s | 248 KB | 11326984 |
| [1162_shortest_paths_optimized.go](1162_shortest_paths_optimized.go) \* | Go 1.14 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.031 s | 1304 KB | 11308453 |
| [1162_shortest_paths_optimized.java](1162_shortest_paths_optimized.java) | Java 1.8 | shortest_paths | O(P^2+C*(C+M)*(P+C)) digit time; O(C*(P+C)+N+M) storage | AC | 0.093 s | 524 KB | 11327477 |
| [1162_shortest_paths_optimized.py](1162_shortest_paths_optimized.py) \* | PyPy 3.10 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.156 s | 416 KB | 11309920 |
| [1162_shortest_paths_optimized.rs](1162_shortest_paths_optimized.rs) | Rust 1.75 x64 | shortest_paths | O(N(N+M)D+I) time; O(ND+M+I) space | AC | 0.046 s | 128 KB | 11325629 |
| [1162_parsing_optimized.go](1162_parsing_optimized.go) | Go 1.14 x64 | parsing | O(P^2 + N(N+M)(P+N)) | AC | 0.015 s | 1168 KB | 11329137 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
