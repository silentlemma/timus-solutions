#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <functional>

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

constexpr int MAX_EMPLOYEES = 100000;
uint32_t employees;
uint32_t boss[MAX_EMPLOYEES], child[MAX_EMPLOYEES], sibling[MAX_EMPLOYEES];
uint32_t parent[MAX_EMPLOYEES], order[MAX_EMPLOYEES], finish[MAX_EMPLOYEES], times[MAX_EMPLOYEES];

void visit(uint32_t other, uint32_t vertex, int &tail) {
    if (other != employees && other != parent[vertex]) {
        parent[other] = vertex;
        order[tail++] = other;
    }
}

void collect(uint32_t other, uint32_t vertex, int &used) {
    if (other != employees && other != parent[vertex])
        times[used++] = finish[other];
}

int main() {
    employees = number();
    for (uint32_t vertex = 0; vertex < employees; ++vertex)
        boss[vertex] = child[vertex] = employees;
    for (uint32_t vertex = 0; vertex < employees; ++vertex) {
        uint32_t next;
        while ((next = number()) != 0) {
            --next;
            boss[next] = vertex;
            sibling[next] = child[vertex];
            child[vertex] = next;
        }
    }
    uint32_t source = number() - 1;
    parent[source] = order[0] = source;
    int tail = 1;
    for (int cursor = 0; cursor < tail; ++cursor) {
        uint32_t vertex = order[cursor];
        // The original boss is just another neighbour when rooting at Tanya.
        visit(boss[vertex], vertex, tail);
        for (uint32_t next = child[vertex]; next != employees; next = sibling[next])
            visit(next, vertex, tail);
    }
    for (int cursor = tail - 1; cursor >= 0; --cursor) {
        uint32_t vertex = order[cursor];
        int used = 0;
        collect(boss[vertex], vertex, used);
        for (uint32_t next = child[vertex]; next != employees; next = sibling[next])
            collect(next, vertex, used);
        std::sort(times, times + used, std::greater<uint32_t>());
        uint32_t best = 0;
        for (int i = 0; i < used; ++i)
            best = std::max(best, times[i] + uint32_t(i + 1));
        finish[vertex] = best;
    }
    printf("%u\n", finish[source]);
}
