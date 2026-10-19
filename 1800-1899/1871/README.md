# 1871. Seismic Waves

[Timus 1871](https://acm.timus.ru/problem.aspx?space=1&num=1871) · difficulty 624 · dijkstra

Original problem by Dmitry Ivankov, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every Twitter user has a list of followers, who see all of the user's
tweets. A follower may retweet a tweet: the string "RT @nick: " is put
in front of it, where nick is the user whose tweet or retweet is
repeated. A message longer than 140 characters is never sent. The first
user tweets about an earthquake; who learns about it?

## Input

n (2 ≤ n ≤ 100), then n lines "name k follower₁ … followerₖ" with
distinct names of 1 to 30 Latin letters, and finally the tweet: a
non-empty line of at most 140 characters with ASCII codes 32 to 127.

## Output

The number of users who learn about the earthquake, then their names in
any order, one per line.

## Examples

### Example 1

Input:

```
5
Miyako 1 Sae
Yuno 2 Miyako Sae
Nazuna 1 Nori
Sae 1 Yuno
Nori 1 Nazuna
Hidamari is going to collapse!!!
```

Output:

```
3
Miyako
Sae
Yuno
```

## Solution

A user who holds a message of at most 140 characters shows it to all
followers. A retweet of user u's message is longer by 6 + |u|
characters, the prefix "RT @: " and the name. Shorter is always
better, so each user should hold the shortest message that can reach
them. That is a shortest path from the first user, starting at the
length of the tweet, with edge weight 6 + |u| on every edge leaving u.
Dijkstra's algorithm over n ≤ 100 users finds it, and users whose
shortest message is over 140 hold nothing. The answer is the users
holding a message together with all their followers: a follower sees
the message even when their own retweet would be too long. `O(n²)`.

In the example Miyako's tweet has 32 characters. Sae sees it and
retweets it as 44 characters, Yuno sees that and retweets 53
characters, which reach Miyako and Sae again. Nazuna and Nori never
hear of it.

Pitfalls:

- the fewest retweets do not give the shortest message: a long name on
  a short path can lose to several short names;
- the tweet may start or end with spaces, which count, so the line must
  be read whole;
- a message of exactly 140 characters is still sent;
- users who cannot retweet still learn the news if someone they follow
  holds it.

The users agree with an independent accepted implementation on 180
random networks, including ones where the path with fewer retweets
gives the longer message.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1871_dijkstra.cpp](1871_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(n^2) | AC | 0.015 s | 684 KB |
| [1871_dijkstra.go](1871_dijkstra.go) | Go 1.14 x64 | dijkstra | O(n^2) | AC | 0.031 s | 1556 KB |
| [1871_dijkstra.java](1871_dijkstra.java) | Java 1.8 | dijkstra | O(n^2) | AC | 0.125 s | 1616 KB |
| [1871_dijkstra.py](1871_dijkstra.py) | Python 3.12 x64 | dijkstra | O(n^2) | AC | 0.078 s | 1228 KB |
| [1871_dijkstra.rs](1871_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(n^2) | AC | 0.046 s | 564 KB |
