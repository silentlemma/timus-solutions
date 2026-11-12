#include <cstdint>
#include <cstdio>
#include <vector>

const int OUTPUT_SIZE = 8192;
const int NUMBER_RESERVE = 16;

struct Output {
    char bytes[OUTPUT_SIZE];
    int used = 0;
    bool first = true;

    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }

    void number(int value) {
        if (used + NUMBER_RESERVE >= OUTPUT_SIZE)
            flush();
        if (!first)
            bytes[used++] = ' ';
        first = false;
        char digits[NUMBER_RESERVE];
        int count = 0;
        do {
            digits[count++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (count)
            bytes[used++] = digits[--count];
    }

    void line() {
        bytes[used++] = '\n';
        first = true;
    }
};

const int INPUT_SIZE = 4096;

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

constexpr uint32_t MODULUS = 1000000007;

uint32_t addMod(uint32_t a, uint32_t b) {
    uint32_t sum = a + b;
    return sum >= MODULUS ? sum - MODULUS : sum;
}

struct Edge {
    uint32_t next, vertex;
};

int main() {
    Input input;
    int n = input.number();
    std::vector<uint32_t> direct(n + 1), parent(n + 1);
    for (int vertex = 1; vertex <= n; ++vertex)
        direct[vertex] = uint32_t(input.number());
    {
        std::vector<uint32_t> head(n + 1), order;
        std::vector<Edge> edges(2 * n - 1);
        uint32_t used = 0;
        auto add = [&](int a, int b) {
            edges[++used] = {head[a], uint32_t(b)};
            head[a] = used;
        };
        for (int i = 1; i < n; ++i) {
            int a = input.number(), b = input.number();
            add(a, b);
            add(b, a);
        }
        order.reserve(n);
        order.push_back(1);
        for (size_t at = 0; at < order.size(); ++at) {
            uint32_t vertex = order[at];
            for (uint32_t edge = head[vertex]; edge; edge = edges[edge].next) {
                uint32_t target = edges[edge].vertex;
                if (target != parent[vertex]) {
                    parent[target] = vertex;
                    order.push_back(target);
                }
            }
        }
    }
    std::vector<uint32_t> broadcast(n + 1);
    Output output;
    int count = input.number();
    while (count--) {
        int kind = input.number(), vertex = input.number();
        uint32_t value = addMod(direct[vertex], broadcast[parent[vertex]]);
        if (kind == 2) {
            output.number(int(value));
            output.line();
        } else {
            broadcast[vertex] = addMod(broadcast[vertex], value);
            // Vertex zero is a sentinel: its direct value is never queried, broadcast stays zero.
            direct[parent[vertex]] = addMod(direct[parent[vertex]], value);
        }
    }
    output.flush();
}
