import sys

LONGEST = 140
PREFIX = len("RT @: ")


def main():
    lines = sys.stdin.buffer.read().split(b"\n")
    n = int(lines[0])
    names, follow_names, at = [], [], 1
    for _ in range(n):
        # a description is a name, a count and that many names
        words = []
        while len(words) < 2 or len(words) < 2 + int(words[1]):
            words += lines[at].split()
            at += 1
        names.append(words[0])
        follow_names.append(words[2:])
    tweet = lines[at].rstrip(b"\r")
    index = {name: i for i, name in enumerate(names)}
    followers = [[index[f] for f in fs] for fs in follow_names]
    # length[u] is the shortest message u can hold; a retweet of u's
    # message is longer by the prefix and u's name
    length = [LONGEST + 1] * n
    length[0] = len(tweet)
    done = [False] * n
    while True:
        u = min((i for i in range(n) if not done[i]), key=length.__getitem__, default=-1)
        if u < 0 or length[u] > LONGEST:
            break
        done[u] = True
        longer = length[u] + PREFIX + len(names[u])
        for v in followers[u]:
            length[v] = min(length[v], longer)
    # everybody who holds a message shows it to all followers
    knows = [False] * n
    for u in range(n):
        if done[u]:
            knows[u] = True
            for v in followers[u]:
                knows[v] = True
    told = [names[i].decode() for i in range(n) if knows[i]]
    print(len(told))
    print("\n".join(told))


main()
