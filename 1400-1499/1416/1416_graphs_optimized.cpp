#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <limits>
#include <vector>

constexpr int BUFFER_SIZE = 16384;
constexpr int DECIMAL = 10;
constexpr auto ABSENT = std::numeric_limits<std::uint16_t>::max();
static unsigned char input[BUFFER_SIZE];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        position = 0;
        if (available == 0)
            return EOF;
    }
    return input[position++];
}

int next_int() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = DECIMAL * value + ch - '0';
        ch = next_byte();
    }
    return value;
}

int main() {
    const int size = next_int();
    const int edges = next_int();
    std::vector<std::uint16_t> weights(size * size, ABSENT), heaviest(size * size);
    for (int i = 0; i < edges; ++i) {
        const int a = next_int() - 1;
        const int b = next_int() - 1;
        const auto cost = static_cast<std::uint16_t>(next_int());
        weights[a * size + b] = weights[b * size + a] = cost;
    }
    std::vector<std::uint16_t> distance(weights.begin(), weights.begin() + size);
    std::vector<int> parent(size), order;
    std::vector<unsigned char> done(size);
    order.reserve(size);
    order.push_back(0);
    done[0] = 1;
    int total = 0;
    for (int step = 1; step < size; ++step) {
        int city = -1;
        auto best = ABSENT;
        for (int i = 0; i < size; ++i) {
            if (!done[i] && distance[i] < best) {
                best = distance[i];
                city = i;
            }
        }
        const int source = parent[city];
        total += best;
        // Both endpoints are settled, so remove the tree edge from the later scan.
        auto *row = weights.data() + city * size;
        row[source] = weights[source * size + city] = ABSENT;
        auto *path = heaviest.data() + city * size;
        const auto *previous = heaviest.data() + source * size;
        for (int other : order)
            path[other] = heaviest[other * size + city] = std::max(previous[other], best);
        done[city] = 1;
        order.push_back(city);
        for (int other = 0; other < size; ++other) {
            if (!done[other] && row[other] < distance[other]) {
                distance[other] = row[other];
                parent[other] = city;
            }
        }
    }
    int extra = ABSENT;
    for (int a = 0; a < size && extra != 0; ++a) {
        for (int b = 0; b < a; ++b) {
            const int index = a * size + b;
            if (weights[index] != ABSENT)
                extra = std::min(extra, weights[index] - heaviest[index]);
        }
    }
    std::printf("Cost: %d\nCost: %d\n", total, extra == ABSENT ? -1 : total + extra);
}
