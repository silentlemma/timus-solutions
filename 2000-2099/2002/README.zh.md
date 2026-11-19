# 2002. Test Task

[Timus 2002](https://acm.timus.ru/problem.aspx?space=1&num=2002) · 难度 72 · implementation

原题作者 Kirill Borozdin，出自 2013 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

模拟初始为空的账户库，支持注册用户名和密码、凭密码登录、按用户名退出。每个请求按指定错误优先级输出固定回复。新账户最初未登录；任何失败请求不得修改已有密码或会话。

## 输入

`1≤n≤100` 个请求，形式为 `register name password`、`login name password`、`logout name`。用户名和密码区分大小写，非空、至多 30 字符，ASCII 33–126；没有空白，但可以含标点或等于命令单词。时间 0.5 秒、内存 64 MB。

## 输出

每个请求一行，严格保持下表英文、冒号、空格和标点。同一命令的条件按表从上到下检查。

| 条件 | 回复 | 更新 |
| --- | --- | --- |
| register: 名字存在 | `fail: user already exists` | 无 |
| register: 否则 | `success: new user added` | 保存密码、未登录 |
| login: 名字缺失 | `fail: no such user` | 无 |
| login: 密码错误 | `fail: incorrect password` | 无 |
| login: 已登录 | `fail: already logged in` | 无 |
| login: 否则 | `success: user logged in` | 登录 |
| logout: 名字缺失 | `fail: no such user` | 无 |
| logout: 已退出 | `fail: already logged out` | 无 |
| logout: 否则 | `success: user logged out` | 退出 |

## 评测方式

本仓库先删除整个输出末尾的所有空白字符，再逐字符比较。末尾的空格和多余空行会被忽略，其他位置的空白必须一致。

## 样例

```
6
register vasya 12345
login vasya 1234
login vasya 12345
login anakin C-3PO
logout vasya
logout vasya
```

```
success: new user added
fail: incorrect password
success: user logged in
fail: no such user
success: user logged out
fail: already logged out
```

注册保存 `12345`，但不自动登录。错误密码不改变状态；正确登录成功，未知名字失败；第一次退出成功，再退出报告已退出。

## 解法

用哈希表把名字映射到密码和在线标志。对每个请求查找名字，并从上到下检查表中的
条件；第一个成立的条件给出回复和唯一的改动。名字长度 L ≤ 30 时为 `O(n·L)`。

注意事项：

- 登录时，密码错误要先于“已经登录”报告；
- 注册不会自动登录；
- 失败的请求什么也不改变，查找也从不创建账户；
- 名字和密码精确比较，区分大小写。

## 优化解法

`2002_implementation_optimized.rs`. 保留账户 HashMap 及登录状态机，含错误优先顺序。每命令立即读处理，仅注册账户保存字节名字/密码，直接输出固定回复，无命令历史及回复串。标准随机哈希下输入/输出字节 I/O 的期望 O(I+O) 时间；账户数据 A、最大当前命令 T 下 O(A+T) 存储。

与 `2002_implementation.rs` 相比：时间 0.046 s → 0.015 s；内存 460 KB → 280 KB。

`2002_implementation_optimized.java`. 保留账户映射及错误优先级，包括先检查密码再检查已登录。逐请求处理并输出答复，不保存全部命令、答复和拼接答案。Java 每个注册名存一个 Account，使用固定输入输出缓冲；Python 用字节名及密码，不做 ASCII 解码，去掉累积列表。空间为 O(U) 账户记录及当前有界长度请求，U<=n。名字、密码至多 30 字符时，哈希处理期望 O(n)，并非最坏情况保证。失败命令不改状态，注册仍为未登录；Python 在 os._exit(0) 前刷新输出。

与 `2002_implementation.java` 相比：时间 0.140 s → 0.109 s；内存 664 KB → 640 KB。

`2002_implementation_optimized.py`. 保留账户映射及错误优先级，包括先检查密码再检查已登录。逐请求处理并输出答复，不保存全部命令、答复和拼接答案。Java 每个注册名存一个 Account，使用固定输入输出缓冲；Python 用字节名及密码，不做 ASCII 解码，去掉累积列表。空间为 O(U) 账户记录及当前有界长度请求，U<=n。名字、密码至多 30 字符时，哈希处理期望 O(n)，并非最坏情况保证。失败命令不改状态，注册仍为未登录；Python 在 os._exit(0) 前刷新输出。

与 `2002_implementation.py` 相比：时间 0.093 s → 0.109 s；内存 576 KB → 252 KB。

优化的 C++ 解法用 `scanf` 代替 `iostream`，把单词读入 31 字节的缓冲区，并对每个
请求立即回复，而不是先保存全部请求和回复：212 KB，而不是 516 KB，时间不变。

优化的 Go 解法从 1 KB 的带缓冲读取器手工解析请求，而不是用 `fmt.Fscan`，并通过带
缓冲的写入器立即回答每个请求，不保存命令列表：0.015 s，而不是 0.046 s；936 KB，
而不是 1124 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`2002_implementation_optimized.java`：在该可比样本中，时间名次 26/249，内存名次 29/249。

`2002_implementation_optimized.py`：在该可比样本中，时间名次 47/69，内存名次 2/69。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2002_implementation.cpp](2002_implementation.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 516 KB | 11292443 |
| [2002_implementation.go](2002_implementation.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.046 s | 1124 KB | 11292444 |
| [2002_implementation.java](2002_implementation.java) | Java 1.8 | implementation | O(n L) | AC | 0.140 s | 664 KB | 11303527 |
| [2002_implementation.py](2002_implementation.py) | Python 3.12 x64 | implementation | O(n L) | AC | 0.093 s | 576 KB | 11292445 |
| [2002_implementation.rs](2002_implementation.rs) | Rust 1.75 x64 | implementation | O(n L) | AC | 0.046 s | 460 KB | 11292448 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2002_implementation_optimized.cpp](2002_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 212 KB | 11303656 |
| [2002_implementation_optimized.go](2002_implementation_optimized.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.015 s | 936 KB | 11303790 |
| [2002_implementation_optimized.java](2002_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) expected | AC | 0.109 s | 640 KB | 11325028 |
| [2002_implementation_optimized.py](2002_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) expected | AC | 0.109 s | 252 KB | 11324845 |
| [2002_implementation_optimized.rs](2002_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | Expected O(I+O) time; O(A+T) space | AC | 0.015 s | 280 KB | 11325537 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
