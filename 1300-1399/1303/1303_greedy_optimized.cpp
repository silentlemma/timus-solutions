#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

const int BUFFER_SIZE = 4096;
// refillable storage bounds memory independently of the input length.
int nextByte() {
    static unsigned char buffer[BUFFER_SIZE];
    static int at = 0, size = 0;
    if (at == size) {
        size = static_cast<int>(std::fread(buffer, 1, BUFFER_SIZE, stdin));
        at = 0;
        if (!size)
            return EOF;
    }
    return buffer[at++];
}
int nextInt() {
    int c;
    do {
        c = nextByte();
    } while (c <= ' ' && c != EOF);
    int sign = 1, value = 0;
    if (c == '-') {
        sign = -1;
        c = nextByte();
    }
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = nextByte();
    }
    return value * sign;
}

int main() {
    int m = nextInt();
    std::vector<int> left(m), right(m);
    // starts at or below zero share bucket zero; only the farthest end matters.
    // m <= 5000 bounds the bucket count, regardless of the number of intervals.
    while (true) {
        int l = nextInt(), r = nextInt();
        if (l == 0 && r == 0)
            break;
        if (l >= m || r <= 0)
            continue;
        int at = std::max(0, l);
        if (r > right[at] || (r == right[at] && l < left[at])) {
            left[at] = l;
            right[at] = r;
        }
    }
    std::vector<std::pair<int, int>> chosen;
    int covered = 0, at = 0;
    while (covered < m) {
        // among the segments that start inside the covered part, take the
        // one that reaches furthest; it is never worse than any other
        int best = -1;
        for (; at < m && at <= covered; ++at)
            if (best < 0 || right[at] > right[best])
                best = at;
        if (best < 0 || right[best] <= covered) {
            std::puts("No solution");
            return 0;
        }
        chosen.push_back({left[best], right[best]});
        covered = right[best];
    }
    std::printf("%d\n", static_cast<int>(chosen.size()));
    for (auto s : chosen)
        std::printf("%d %d\n", s.first, s.second);
}
