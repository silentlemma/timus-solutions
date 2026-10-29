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

优化的 C++ 解法用 `scanf` 代替 `iostream`，把单词读入 31 字节的缓冲区，并对每个
请求立即回复，而不是先保存全部请求和回复：212 KB，而不是 516 KB，时间不变。

优化的 Go 解法从 1 KB 的带缓冲读取器手工解析请求，而不是用 `fmt.Fscan`，并通过带
缓冲的写入器立即回答每个请求，不保存命令列表：0.015 s，而不是 0.046 s；936 KB，
而不是 1124 KB。

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
