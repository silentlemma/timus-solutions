#include <cstdio>

constexpr int ALPHABET = 3;
constexpr int TARGET = 6;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int counts[ALPHABET] = {};
    int ways = 1;
    // the values are counted as they are read with scanf, and the answer is
    // printed as soon as it is known
    for (int length = 1; length <= n; ++length) {
        int value;
        if (scanf("%d", &value) != 1)
            return 0;
        ++counts[value - 1];
        ways = ways * length / counts[value - 1];
        if (ways >= TARGET) {
            puts("Yes");
            return 0;
        }
    }
    puts("No");
}
