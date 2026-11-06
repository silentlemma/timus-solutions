#include <cstdint>
#include <cstdio>
#include <vector>

constexpr int MAX_DIGITS = 30;
constexpr int BASE = 10;
constexpr int DIVISOR_FIVE = 5;

int main() {
    int modulus;
    if (std::scanf("%d", &modulus) != 1)
        return 0;
    if (modulus % DIVISOR_FIVE == 0) {
        std::puts("Impossible");
        return 0;
    }
    std::vector<std::uint32_t> parent(modulus), queue;
    queue.reserve(modulus);
    // Zero means unseen; the low bit stores the appended digit minus one.
    const auto discover = [&](int previous, int digit, int remainder) {
        if (parent[remainder] == 0) {
            parent[remainder] = ((previous + 1) << 1) | (digit - 1);
            queue.push_back(remainder);
        }
    };
    discover(modulus, 1, 1 % modulus);
    discover(modulus, 2, 2 % modulus);
    std::size_t front = 0;
    for (int length = 1; length < MAX_DIGITS && front < queue.size() && parent[0] == 0; ++length) {
        const auto end = queue.size();
        while (front < end && parent[0] == 0) {
            const int previous = queue[front++];
            discover(previous, 1, (previous * BASE + 1) % modulus);
            discover(previous, 2, (previous * BASE + 2) % modulus);
        }
    }
    if (parent[0] == 0) {
        std::puts("Impossible");
        return 0;
    }
    char answer[MAX_DIGITS + 1]{};
    int offset = MAX_DIGITS;
    for (int remainder = 0; remainder != modulus;) {
        const auto entry = parent[remainder];
        answer[--offset] = '1' + (entry & 1);
        remainder = (entry >> 1) - 1;
    }
    std::puts(answer + offset);
}
