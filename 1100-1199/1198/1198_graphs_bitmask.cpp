#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

constexpr int MAX_VERTICES = 2000, WORD_BITS = 64;
constexpr int MAX_WORDS = (MAX_VERTICES + WORD_BITS - 1) / WORD_BITS;
uint64_t forward[MAX_VERTICES][MAX_WORDS], reverse_graph[MAX_VERTICES][MAX_WORDS];
uint64_t unseen[MAX_WORDS];
uint16_t queue[MAX_VERTICES];
int words, vertices;

void reset() {
    for (int word = 0; word < words; ++word)
        unseen[word] = UINT64_MAX;
    if (vertices % WORD_BITS != 0)
        unseen[words - 1] = (uint64_t{1} << (vertices % WORD_BITS)) - 1;
}

void visit(int root, const uint64_t graph[][MAX_WORDS]) {
    unseen[root / WORD_BITS] &= ~(uint64_t{1} << (root % WORD_BITS));
    int head = 0, tail = 0;
    queue[tail++] = root;
    while (head < tail) {
        int vertex = queue[head++];
        for (int word = 0; word < words; ++word) {
            uint64_t fresh = graph[vertex][word] & unseen[word];
            unseen[word] &= ~fresh;
            while (fresh != 0) {
                queue[tail++] = word * WORD_BITS + __builtin_ctzll(fresh);
                fresh &= fresh - 1;
            }
        }
    }
}

int main() {
    vertices = number();
    words = (vertices + WORD_BITS - 1) / WORD_BITS;
    for (int from = 0; from < vertices; ++from) {
        for (int to = number(); to != 0; to = number()) {
            --to;
            forward[from][to / WORD_BITS] |= uint64_t{1} << (to % WORD_BITS);
            reverse_graph[to][from / WORD_BITS] |= uint64_t{1} << (from % WORD_BITS);
        }
    }
    reset();
    int root = 0;
    for (int vertex = 0; vertex < vertices; ++vertex) {
        if (unseen[vertex / WORD_BITS] >> (vertex % WORD_BITS) & 1) {
            root = vertex;
            visit(root, forward);
        }
    }
    reset();
    visit(root, forward);
    for (int word = 0; word < words; ++word) {
        if (unseen[word] != 0) {
            std::puts("0");
            return 0;
        }
    }
    reset();
    visit(root, reverse_graph);
    for (int vertex = 0; vertex < vertices; ++vertex)
        if (!(unseen[vertex / WORD_BITS] >> (vertex % WORD_BITS) & 1))
            std::printf("%d ", vertex + 1);
    std::puts("0");
}
