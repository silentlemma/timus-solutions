#include <cstdint>
#include <cstdio>
#include <vector>

constexpr int FACES = 6;
constexpr int WORD_BITS = 64;
constexpr int INPUT_SIZE = 4096;

struct Input {
    unsigned char bytes[INPUT_SIZE];
    int position = 0, length = 0;

    int next() {
        if (position == length) {
            length = int(fread(bytes, 1, sizeof(bytes), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return bytes[position++];
    }

    int number() {
        int c = next(), value = 0;
        while (c && c <= ' ')
            c = next();
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = next();
        }
        return value;
    }
};

int main() {
    Input input;
    int n = input.number();
    std::vector<uint32_t> land(n + 1);
    land[1] = 1;
    for (int i = 2; i < n; ++i) {
        int jump = input.number();
        land[i] = jump ? land[i - jump] : uint32_t(i);
    }
    land[n] = uint32_t(n);
    std::vector<uint64_t> visited((n + WORD_BITS) / WORD_BITS);
    auto mark = [&](uint32_t cell) {
        uint64_t bit = uint64_t(1) << (cell % WORD_BITS);
        uint64_t &word = visited[cell / WORD_BITS];
        if (word & bit)
            return false;
        word |= bit;
        return true;
    };
    std::vector<uint32_t> queue;
    queue.reserve(n);
    queue.push_back(1);
    mark(1);
    size_t first = 0;
    int turns = 1;
    while (first < queue.size()) {
        size_t end = queue.size();
        // Complete every free six-roll path before discovering the next turn's states.
        for (size_t head = first; head < end; ++head) {
            uint32_t cell = queue[head];
            if (cell + FACES >= uint32_t(n)) {
                printf("%d\n", turns);
                return 0;
            }
            uint32_t target = land[cell + FACES];
            if (mark(target)) {
                queue.push_back(target);
                ++end;
            }
        }
        for (size_t head = first; head < end; ++head) {
            uint32_t cell = queue[head];
            for (int face = 1; face < FACES; ++face) {
                uint32_t target = land[cell + face];
                if (mark(target))
                    queue.push_back(target);
            }
        }
        first = end;
        ++turns;
    }
    puts("-1");
}
