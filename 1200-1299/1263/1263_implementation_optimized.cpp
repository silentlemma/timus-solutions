#include <cstdint>
#include <cstdio>

constexpr int MAX_CANDIDATES = 10000;
constexpr double PERCENT = 100.0;
// a fixed array of 16-bit counters: at most 10000 candidates and 10000 votes
std::uint16_t votes[MAX_CANDIDATES + 1];

// the numbers are parsed with getchar instead of scanf
int readInt() {
    int c;
    do {
        c = getchar();
    } while (c != EOF && c <= ' ');
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    int n = readInt();
    int m = readInt();
    for (int i = 0; i < m; ++i)
        ++votes[readInt()];
    for (int i = 1; i <= n; ++i)
        printf("%.2f%%\n", PERCENT * votes[i] / m);
}
