#include <array>
#include <cstdint>
#include <cstdio>

constexpr int MAX_VERTICES = 7163, MAX_DEGREE = 3, INPUT_SIZE = 8192;
constexpr int BAD_SAME = 2;
char input[INPUT_SIZE];
int position = 0, length = 0;

int next_byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

int number() {
    int c = next_byte();
    while (c >= 0 && c <= ' ')
        c = next_byte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = next_byte();
    }
    return value;
}

int main() {
    int n = number();
    std::array<std::array<uint16_t, MAX_DEGREE>, MAX_VERTICES> enemies{};
    std::array<uint8_t, MAX_VERTICES> degree{}, same{}, side{};
    std::array<bool, MAX_VERTICES> queued{};
    std::array<uint16_t, MAX_VERTICES> work{};
    int head = 0, tail = 0, size = 0;
    auto enqueue = [&](int vertex) {
        if (!queued[vertex]) {
            queued[vertex] = true;
            work[tail] = vertex;
            tail = (tail + 1) % n;
            ++size;
        }
    };
    for (int vertex = 0; vertex < n; ++vertex) {
        degree[vertex] = same[vertex] = number();
        for (int edge = 0; edge < degree[vertex]; ++edge)
            enemies[vertex][edge] = number() - 1;
        if (same[vertex] >= BAD_SAME)
            enqueue(vertex);
    }
    int zero_count = n;
    while (size != 0) {
        int vertex = work[head];
        head = (head + 1) % n;
        --size;
        queued[vertex] = false;
        if (same[vertex] < BAD_SAME)
            continue;
        int old_side = side[vertex];
        side[vertex] ^= 1;
        zero_count += old_side == 0 ? -1 : 1;
        same[vertex] = degree[vertex] - same[vertex];
        // Only neighbours change; the moved vertex now has at most one same-side enemy.
        for (int edge = 0; edge < degree[vertex]; ++edge) {
            int other = enemies[vertex][edge];
            if (side[other] == old_side)
                --same[other];
            else
                ++same[other];
            if (same[other] >= BAD_SAME)
                enqueue(other);
        }
    }
    int chosen = zero_count < n - zero_count ? 0 : 1;
    if (zero_count == n - zero_count)
        chosen = side[0];
    printf("%d\n", chosen == 0 ? zero_count : n - zero_count);
    for (int vertex = 0; vertex < n; ++vertex) {
        if (side[vertex] == chosen)
            printf("%d ", vertex + 1);
    }
    puts("");
}
