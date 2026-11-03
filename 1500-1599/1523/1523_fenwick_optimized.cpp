#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;

const uint32_t MOD = 1000000000;
const int BUFFER = 8192;
char buffer[BUFFER];
int position, available;
int readByte() {
    if (position == available) {
        available = (int)fread(buffer, 1, BUFFER, stdin);
        position = 0;
        if (!available)
            return EOF;
    }
    return buffer[position++];
}
int nextInt() {
    int c = readByte(), value = 0;
    while (c <= ' ')
        c = readByte();
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return value;
}
int main() {
    int n = nextInt(), k = nextInt();
    if (k > n) {
        puts("0");
        return 0;
    }
    vector<uint16_t> flipped(n);
    for (auto &value : flipped)
        value = (uint16_t)(n + 1 - nextInt());
    vector<uint32_t> ways(n, 1), tree(n + 1);
    uint32_t total = 0;
    for (int length = 2; length <= k; length++) {
        fill(tree.begin(), tree.end(), 0);
        total = 0;
        bool nonzero = false;
        for (int i = 0; i < n; i++) {
            uint32_t old = ways[i], result = 0;
            for (int j = flipped[i] - 1; j > 0; j &= j - 1) {
                result += tree[j];
                if (result >= MOD)
                    result -= MOD;
            }
            ways[i] = result;
            if (result) {
                nonzero = true;
                total += result;
                if (total >= MOD)
                    total -= MOD;
            }
            // Insert the captured old layer after overwriting this one position.
            if (old)
                for (int j = flipped[i]; j <= n; j += j & -j) {
                    tree[j] += old;
                    if (tree[j] >= MOD)
                        tree[j] -= MOD;
                }
        }
        if (!nonzero) {
            puts("0");
            return 0;
        }
    }
    printf("%u\n", total);
}
