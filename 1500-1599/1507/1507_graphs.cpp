#include <array>
#include <cstdint>
#include <cstdio>

constexpr int MAX_VERTICES = 50;

bool reaches_all(const std::array<uint64_t, MAX_VERTICES> &edges, int n) {
    uint64_t seen = 1, pending = 1;
    while (pending != 0) {
        int vertex = __builtin_ctzll(pending);
        pending &= pending - 1;
        uint64_t fresh = edges[vertex] & ~seen;
        seen |= fresh;
        pending |= fresh;
    }
    return seen == (uint64_t(1) << n) - 1;
}

int main() {
    int n;
    scanf("%d", &n);
    std::array<uint64_t, MAX_VERTICES> forward{}, reverse{};
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int value;
            scanf("%d", &value);
            if (value != 0) {
                forward[i] |= uint64_t(1) << j;
                reverse[j] |= uint64_t(1) << i;
            }
        }
    }
    // Two reachability checks characterize strong connectivity.
    puts(reaches_all(forward, n) && reaches_all(reverse, n) ? "Yes" : "No");
}
