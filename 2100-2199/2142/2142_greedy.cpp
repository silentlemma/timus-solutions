#include <algorithm>
#include <cstdio>

int main() {
    long long a, b, c, x, y, z;
    scanf("%lld %lld %lld %lld %lld %lld", &a, &b, &c, &x, &y, &z);
    // the dual lands first cover what the red and blue lands miss, and every
    // land left over pays for the mana of any color
    long long missing = std::max(0LL, x - a) + std::max(0LL, y - b);
    bool enough = missing <= c && a + b + c >= x + y + z;
    puts(enough ? "It is a kind of magic" : "There are no miracles in life");
    return 0;
}
