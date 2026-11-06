#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <vector>

constexpr int BUFFER_SIZE = 32768;
constexpr int DECIMAL = 10;
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
        value = value * DECIMAL + ch - '0';
        ch = next_byte();
    }
    return value;
}

std::int64_t point(const std::vector<std::int64_t> &tree, int at) {
    std::int64_t total = 0;
    for (; at != 0; at &= at - 1)
        total += tree[at];
    return total;
}

void add(std::vector<std::int64_t> &tree, int at, std::int64_t value) {
    const int end = static_cast<int>(tree.size());
    for (; at < end; at += at & -at)
        tree[at] += value;
}

int main() {
    const int size = next_int();
    std::vector<std::uint32_t> initial(size + 1);
    for (int i = 1; i <= size; ++i)
        initial[i] = next_int();
    std::vector<int> offsets(size + 2);
    for (int d = 1; d * d <= size; ++d)
        for (int multiple = d * d; multiple <= size; multiple += d)
            ++offsets[multiple];
    for (int i = 1; i <= size; ++i)
        offsets[i] += offsets[i - 1];
    offsets[size + 1] = offsets[size];
    std::vector<std::uint16_t> divisors(offsets[size]);
    // Filling each slice backwards converts its end offset into its start offset.
    for (int d = 1; d * d <= size; ++d)
        for (int multiple = d * d; multiple <= size; multiple += d)
            divisors[--offsets[multiple]] = d;
    std::vector<std::int64_t> tree(size + 1);
    for (int count = next_int(); count > 0; --count) {
        if (next_int() == 1) {
            const int particle = next_int();
            std::int64_t total = initial[particle];
            for (int i = offsets[particle]; i < offsets[particle + 1]; ++i) {
                const int d = divisors[i];
                const int other = particle / d;
                total += point(tree, d);
                if (other != d)
                    total += point(tree, other);
            }
            std::printf("%" PRId64 "\n", total);
        } else {
            const int left = next_int();
            const int right = next_int();
            const std::int64_t power = next_int();
            add(tree, left, power);
            add(tree, right + 1, -power);
        }
    }
}
