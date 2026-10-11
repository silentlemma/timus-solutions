"""Checker: the output gives the same, minimal number of minutes and then
a group of calls for each minute. A call goes along a pair from the
input, from someone who already knew the news before that minute to
someone who did not, nobody makes two calls in one minute or is called
twice, and in the end the whole class knows."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    words = open(inp).read().split()
    m = int(words[1])
    links = set()
    people = {words[2 + 2 * m]}
    for i in range(m):
        a, b = words[2 + 2 * i], words[3 + 2 * i]
        links |= {(a, b), (b, a)}
        people |= {a, b}
    expected = int(open(ans).read().split()[0])
    got = open(output).read().split()
    if not got or not got[0].isdigit():
        fail("expected the number of minutes")
    minutes = int(got[0])
    if minutes != expected:
        fail("%d minutes, the minimum is %d" % (minutes, expected))
    knows = {words[2 + 2 * m]}
    pos = 1
    for minute in range(1, minutes + 1):
        if pos >= len(got) or not got[pos].isdigit():
            fail("minute %d: expected the number of calls" % minute)
        count = int(got[pos])
        pos += 1
        if pos + 2 * count > len(got):
            fail("minute %d: the output ends early" % minute)
        busy, fresh = set(), set()
        for _ in range(count):
            caller, callee = got[pos], got[pos + 1]
            pos += 2
            if (caller, callee) not in links:
                fail("%s cannot call %s" % (caller, callee))
            if caller not in knows:
                fail("minute %d: %s does not know the news yet" % (minute, caller))
            if callee in knows or callee in fresh:
                fail("minute %d: %s is told twice" % (minute, callee))
            if caller in busy:
                fail("minute %d: %s makes two calls" % (minute, caller))
            busy.add(caller)
            fresh.add(callee)
        knows |= fresh
    if pos != len(got):
        fail("extra output after the plan")
    if knows != people:
        fail("%d of %d people do not know the news" % (len(people - knows), len(people)))


if __name__ == "__main__":
    main()
