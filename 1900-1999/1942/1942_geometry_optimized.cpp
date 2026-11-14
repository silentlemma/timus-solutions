#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

constexpr int SCALE = 1000;
constexpr int INPUT_BUFFER = 8192;

class Input {
    unsigned char buffer[INPUT_BUFFER];
    std::size_t offset = 0, size = 0;

    int byte() {
        if (offset == size) {
            size = std::fread(buffer, 1, sizeof buffer, stdin);
            offset = 0;
            if (!size)
                return EOF;
        }
        return buffer[offset++];
    }

    int start() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        return c;
    }

  public:
    int count() {
        int value = 0;
        int c = start();
        if (c == '+')
            c = byte();
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value;
    }

    int residue() {
        int c = start();
        const bool negative = c == '-';
        while (c > ' ' && c != '.')
            c = byte();
        if (c != '.')
            return 0;

        int value = 0, place = SCALE / 10;
        for (c = byte(); c >= '0' && c <= '9'; c = byte()) {
            value += (c - '0') * place;
            place /= 10;
        }
        return negative && value ? SCALE - value : value;
    }
};

int main() {
    Input input;
    const int size = input.count();
    std::vector<int> pairs(size);
    for (int &key : pairs) {
        const int x = input.residue();
        const int y = input.residue();
        key = x * SCALE + y;
    }
    std::sort(pairs.begin(), pairs.end());

    int best_count = 0, best_distance = 0;
    for (int first = 0; first < size;) {
        const int key = pairs[first];
        int end = first + 1;
        while (end < size && pairs[end] == key)
            ++end;
        const int count = end - first;
        if (count >= best_count) {
            const int x = key / SCALE;
            const int y = key % SCALE;
            const int dx = std::min(x, SCALE - x), dy = std::min(y, SCALE - y);
            const int distance = dx * dx + dy * dy;
            if (count > best_count || distance < best_distance) {
                best_count = count;
                best_distance = distance;
            }
        }
        first = end;
    }
    std::printf("%d %.9f\n", best_count, std::sqrt(best_distance) / SCALE);
}
