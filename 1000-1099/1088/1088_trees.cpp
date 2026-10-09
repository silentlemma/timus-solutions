#include <cstdio>
#include <iostream>

int main() {
    long long d, e, f, dp, ep, h;
    if (!(std::cin >> d >> e >> f >> dp >> ep >> h))
        return 0;
    // pier p - 1 written in F bits is the path to it, a left turn being 1 and
    // the first turn the highest bit; a stone k hours from the sea is that
    // path without its last k turns
    long long a = (ep - 1) >> e, depth_a = f - e;
    long long b = (dp - 1) >> d, depth_b = f - d;
    long long hours = 0;
    for (; depth_a > depth_b; depth_a--, hours++)
        a >>= 1;
    for (; depth_b > depth_a; depth_b--, hours++)
        b >>= 1;
    for (; a != b; hours += 2)
        a >>= 1, b >>= 1;
    puts(hours <= h ? "YES" : "NO");
}
