#include <cstdio>
#include <string>
#include <vector>

constexpr int BITS = 20;  // every number of the message is below 2^20

int main() {
    const int size = 1 << BITS;
    // has[j][x]: some prime below 2^20 has its top j bits equal to x
    std::vector<std::vector<char>> has(BITS + 1);
    has[BITS].assign(size, 1);
    has[BITS][0] = has[BITS][1] = 0;
    for (int i = 2; (long long)i * i < size; i++)
        if (has[BITS][i])
            for (int j = i * i; j < size; j += i) has[BITS][j] = 0;
    for (int level = BITS - 1; level >= 0; level--) {
        has[level].assign(1 << level, 0);
        for (int x = 0; x < (1 << level); x++)
            has[level][x] = has[level + 1][2 * x] | has[level + 1][2 * x + 1];
    }
    int t;
    scanf("%d", &t);
    std::string out;
    while (t--) {
        int a;
        scanf("%d", &a);
        // The smallest key is the smallest a xor p over primes p below 2^20,
        // since a key below 2^20 reaches the prime 2; choose the bits of p
        // from the top, keeping the bit of a whenever some prime allows it.
        int prefix = 0;
        for (int bit = BITS - 1; bit >= 0; bit--) {
            int want = prefix * 2 + (a >> bit & 1);
            prefix = has[BITS - bit][want] ? want : want ^ 1;
        }
        out += std::to_string(a ^ prefix);
        out += '\n';
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
