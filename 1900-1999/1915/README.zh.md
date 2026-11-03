# 1915. 泰坦遗迹：重现往昔

[Timus 1915](https://acm.timus.ru/problem.aspx?space=1&num=1915) · difficulty 228 · simulation

原题作者 Denis Dublennykh，出自 NEERC 2012 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

从空栈开始。正数入栈，−1 弹出并输出栈顶，0 把整个栈的副本
放到原栈上方，保持从底到顶的顺序。按操作顺序输出所有弹出值。
保证每次弹出时栈非空。实际高度可能随复制次数指数增长。
限制：2 秒，128 MB。

## 输入

n，1≤n≤1 000 000，随后 n 行，每行一个整数 x：
−1、0，或 [1,1 000 000 000] 内的值。

## 输出

每行一个弹出值，保持时间顺序。没有弹出时输出为空。

## 评测方式

精确比较整数词元及其顺序。

## 样例

```
8
3
4
0
-1
-1
-1
-1
1
```

```
4
3
4
3
```

## 解法

先保存操作并统计总弹出次数 P。令 r 表示尚未执行的弹出次数，
只保留实际栈顶的 min(h,r) 个值，h 是真实高度。更深的值不可能
在剩余 r 次弹出中出现。P=0 时无需输出；r=0 后其余操作无关。

用容量 P 的循环数组表示保留部分，逻辑底部为 b，大小为 s。
下标按 P 取模。逻辑容量 r 会缩小，可能小于物理容量 P。
入栈时向逻辑末尾追加；若 s=r，先丢弃保留部分的底部。
弹出时输出末尾值，并同时令 s、r 减一。

复制时保持当前顶部不变。若 s=r，所有未来可见值已经保留，
直接忽略。否则真实栈完整保存在数组中，大小就是 s。
只需在其下方补入 q=min(s,r−s) 个值，即旧栈最后 q 个元素。
把此后缀放到逻辑底部之前，新底部为 (b−q) mod P，源位置为
(b+s−q) mod P。目标全是空闲位置，不会覆盖源数据。
空栈或逻辑容量已满时 q=0。

### 正确性

保持“存储序列恰为真实栈最后 min(h,r) 个值”的不变量。
入栈只需要原顶部 r−1 个值与新值，因此丢掉底部安全。
弹出后所需长度 min(h−1,r−1) 恰比原长度少一，输出也是真实栈顶。
复制时 h≥r 则顶部 r 个值不变；h<r 则完整栈已知，双倍序列
以原栈结尾，之前的保留部分正是上述后缀。因此所有操作保持不变量。

### 摊还复杂度

弹出让 s 减一，非满入栈让 s 加一，满入栈净变化为零，
复制让 s 增加 q。初始 s=0，最后一次弹出后 r=s=0，
因此所有复制量之和等于 P 减去增加大小的入栈次数，至多 P。
时间 `O(n)`，空间 `O(n)`。即使连续大量复制，也不会产生重复的大量工作。

样例中 [3,4] 变为 [3,4,3,4]，弹出顺序为 4,3,4,3。
最后一次入栈不再影响输出。

复制保持顺序，不会反转。补入的是原栈后缀，位置在保留部分下方。
逻辑容量只随弹出缩小。r<P 时，满容量入栈必须先删底部再向
逻辑末尾追加，不能只覆盖旧底部单元。处理空栈复制和无输出；
不能展开指数大小的栈，也不能反复移动整个数组。

## 优化解法

按已证明的收缩环不变量，只保留可能影响剩余弹出的栈顶部分。弹出硬币分块输出，不复制到完整答案数组。热路径的取余改为条件回绕。复杂度统计整个执行中的复制元素总量，而非逐命令分别计数。Python 使用 Accepted 行注明的实际解释器。

- `1915_simulation_optimized.cpp`: 0.062 s / 7492 KB; 基础版 `1915_simulation.cpp`: 0.187 s / 11640 KB; 相对基础版的变化: 时间 -66.8%, 内存 -35.6%.
- `1915_simulation_optimized.go`: 0.078 s / 9548 KB; 基础版 `1915_simulation.go`: 0.093 s / 21804 KB; 相对基础版的变化: 时间 -16.1%, 内存 -56.2%.
- `1915_simulation_optimized.java`: 0.250 s / 8448 KB; 基础版 `1915_simulation.java`: 0.390 s / 12292 KB; 相对基础版的变化: 时间 -35.9%, 内存 -31.3%.
- `1915_simulation_optimized.py`: 0.359 s / 37668 KB; 基础版 `1915_simulation.py`: 0.515 s / 16716 KB; 相对基础版的变化: 时间 -30.3%, 内存 +125.3%.
- `1915_simulation_optimized.rs`: 0.062 s / 7856 KB; 基础版 `1915_simulation.rs`: 0.046 s / 16904 KB; 相对基础版的变化: 时间 +34.8%, 内存 -53.5%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1915_simulation.cpp`; 覆盖实现 `1915_simulation_optimized.cpp`; 时间/内存名次 4/9, 其他作者记录 45/45.

- Go: 优先教学基础版 `1915_simulation.go`; 覆盖实现 `1915_simulation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1915_simulation.java`; 覆盖实现 `1915_simulation_optimized.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `1915_simulation.py`; 覆盖实现 `1915_simulation_optimized.py`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Rust: 优先教学基础版 `1915_simulation.rs`; 覆盖实现 `1915_simulation.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1915_simulation.cpp](1915_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.187 s | 11640 KB | 11291421 |
| [1915_simulation.go](1915_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.093 s | 21804 KB | 11291424 |
| [1915_simulation.java](1915_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.390 s | 12292 KB | 11309214 |
| [1915_simulation.py](1915_simulation.py) | PyPy 3.10 x64 | simulation | O(n) | AC | 0.515 s | 16716 KB | 11291425 |
| [1915_simulation.rs](1915_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 16904 KB | 11291432 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1915_simulation_optimized.cpp](1915_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N+P) | AC | 0.062 s | 7492 KB | 11308596 |
| [1915_simulation_optimized.go](1915_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N+P) | AC | 0.078 s | 9548 KB | 11308605 |
| [1915_simulation_optimized.java](1915_simulation_optimized.java) | Java 1.8 | simulation | O(N+P) | AC | 0.250 s | 8448 KB | 11308601 |
| [1915_simulation_optimized.py](1915_simulation_optimized.py) | PyPy 3.10 x64 | simulation | O(N+P) | AC | 0.359 s | 37668 KB | 11309401 |
| [1915_simulation_optimized.rs](1915_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N+P) | AC | 0.062 s | 7856 KB | 11308602 |
