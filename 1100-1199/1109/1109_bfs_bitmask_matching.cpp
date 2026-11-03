#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

const int BUFFER_SIZE = 4096;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

const int WORD_BITS = 64;

int main() {
    int m = next_int(), n = next_int(), edges = next_int();
    int left = std::min(m, n), right = std::max(m, n);
    int words = (right + WORD_BITS - 1) / WORD_BITS;
    std::vector<uint64_t> adjacent(left * words), free(words, ~uint64_t(0));
    for (int i = 0; i < edges; i++) {
        int a = next_int() - 1, b = next_int() - 1;
        if (m > n)
            std::swap(a, b);
        adjacent[a * words + b / WORD_BITS] |= uint64_t(1) << (b % WORD_BITS);
    }
    std::vector<int> match_l(left, -1), match_r(right, -1), parent(right), queue(left);
    int size = 0;
    for (int root = 0; root < left; root++) {
        std::vector<uint64_t> seen(words);
        int head = 0, tail = 1, target = -1;
        queue[0] = root;
        while (head < tail && target < 0) {
            int v = queue[head++];
            for (int b = 0; b < words; b++) {
                uint64_t available = adjacent[v * words + b] & free[b];
                if (available) {
                    target = b * WORD_BITS + __builtin_ctzll(available);
                    parent[target] = v;
                    break;
                }
            }
            if (target >= 0)
                break;
            // No free neighbor: each unseen right vertex is matched and
            // queues its unique matched left vertex at most once.
            for (int b = 0; b < words; b++) {
                uint64_t options = adjacent[v * words + b] & ~seen[b];
                seen[b] |= options;
                while (options) {
                    int u = b * WORD_BITS + __builtin_ctzll(options);
                    parent[u] = v;
                    queue[tail++] = match_r[u];
                    options &= options - 1;
                }
            }
        }
        if (target >= 0) {
            free[target / WORD_BITS] &= ~(uint64_t(1) << (target % WORD_BITS));
            // Follow old matches and BFS parents back to the free root.
            while (target >= 0) {
                int v = parent[target], old = match_l[v];
                match_l[v] = target;
                match_r[target] = v;
                target = old;
            }
            size++;
        }
    }
    printf("%d\n", m + n - size);
}
