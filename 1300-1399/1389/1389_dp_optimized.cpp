#include <cstdint>
#include <cstdio>
#include <vector>

const int BUFFER_SIZE = 8192;
const int NUMBER_RESERVE = 24;
const uint32_t CHOSEN = uint32_t(1) << 31;

struct Reader {
    unsigned char data[BUFFER_SIZE];
    int position = 0, length = 0;
    int byte() {
        if (position == length) {
            length = int(fread(data, 1, sizeof(data), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return data[position++];
    }
    int number() {
        int c = byte();
        while (c && (c < '0' || c > '9') && c != '-' && c != '+')
            c = byte();
        bool negative = c == '-';
        if (c == '-' || c == '+')
            c = byte();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return negative ? -value : value;
    }
};

struct Writer {
    char data[BUFFER_SIZE];
    int used = 0;
    void flush() {
        fwrite(data, 1, used, stdout);
        used = 0;
    }
    void number(int64_t value) {
        if (used + NUMBER_RESERVE > BUFFER_SIZE)
            flush();
        if (value < 0) {
            data[used++] = '-';
            value = -value;
        }
        char digits[NUMBER_RESERVE];
        int length = 0;
        do {
            digits[length++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (length)
            data[used++] = digits[--length];
        data[used++] = '\n';
    }
};

int main() {
    Reader in;
    Writer out;
    int n = in.number(), m = in.number();
    std::vector<uint32_t> head(n), to(2 * m), next(2 * m), parent_edge(n), order(n);
    for (int i = 0; i < m; ++i) {
        uint32_t a = in.number() - 1, b = in.number() - 1;
        to[2 * i] = b;
        next[2 * i] = head[a];
        head[a] = 2 * i + 1;
        to[2 * i + 1] = a;
        next[2 * i + 1] = head[b];
        head[b] = 2 * i + 2;
    }
    int tail = 1;
    for (int position = 0; position < tail; ++position) {
        uint32_t v = order[position];
        for (uint32_t link = head[v]; link; link = next[link - 1]) {
            uint32_t edge = link - 1;
            if (parent_edge[v] && edge == ((parent_edge[v] - 1) ^ 1))
                continue;
            uint32_t u = to[edge];
            parent_edge[u] = edge + 1;
            order[tail++] = u;
        }
    }
    std::vector<uint8_t> used(n);
    int count = 0;
    for (int position = n - 1; position > 0; --position) {
        uint32_t v = order[position], edge = parent_edge[v] - 1, parent = to[edge ^ 1];
        if (used[v] || used[parent])
            continue;
        used[v] = used[parent] = 1;
        ++count;
        // Traversal is over: high bits of its links can now mark selected roads.
        next[edge & ~uint32_t(1)] |= CHOSEN;
    }
    out.number(count);
    for (int i = 0; i < m; ++i)
        if (next[2 * i] & CHOSEN) {
            out.number(to[2 * i + 1] + 1);
            out.data[out.used - 1] = ' ';
            out.number(to[2 * i] + 1);
        }
    out.flush();
}
