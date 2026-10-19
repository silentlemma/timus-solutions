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

输出逐字符精确比较，只有最后的换行可以不同。

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

哈希表将名字映射为密码和登录布尔值。每次只查询、不因缺失而创建记录，选首个满足的条件，输出对应回复，并且仅在成功时执行规定更新。

登录先检查用户存在，再检查密码，最后检查是否已登录。即使在线，错误密码仍应报告密码错误。重复注册不能覆盖密码或重置会话；退出只清除登录标志。失败查询不插入用户。

归纳证明：初始空表正确。若请求前缀后表准确表示账户，则下一次查询找到正确记录或缺失；有序条件决定正确回复，唯一允许的更新保持表准确。因此全部输出及后续状态均正确。

设 `L≤30` 为令牌长度，哈希表期望时间 `O(n L)`，含输入和回复的空间 `O(n L)`；保守碰撞最坏时间 `O(n² L)`，在 100 请求内也很小。五种语言使用同一优先级。

不要先于密码检查在线状态，不要注册后自动登录。失败操作必须保持账户不变。完整字符串区分大小写；引号、反斜杠、命令式用户名均普通字符。只输出固定回复，不回显名字或密码。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2002_implementation.cpp](2002_implementation.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 516 KB |
| [2002_implementation.go](2002_implementation.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.046 s | 1124 KB |
| [2002_implementation.java](2002_implementation.java) | Java 1.8 | implementation | O(n L) | AC | 0.109 s | 684 KB |
| [2002_implementation.py](2002_implementation.py) | Python 3.12 x64 | implementation | O(n L) | AC | 0.093 s | 576 KB |
| [2002_implementation.rs](2002_implementation.rs) | Rust 1.75 x64 | implementation | O(n L) | AC | 0.046 s | 460 KB |
