#include <array>
#include <charconv>
#include <cstdio>
#include <vector>

namespace {
constexpr int types = 8;
constexpr int states = 1 << types;
constexpr int unreachable = 100;
constexpr int buffer_size = 4096;
constexpr int max_number_width = 12;
constexpr int apple = 1;
constexpr int banana = 2;
constexpr int pineapple = 4;
constexpr std::array<int, types> bits{0, 1, 1, 2, 1, 2, 2, 3};

class Input {
    char buffer[buffer_size];
    int cursor = 0;
    int end = 0;

  public:
    int next() {
        if (cursor == end) {
            end = static_cast<int>(std::fread(buffer, 1, sizeof(buffer), stdin));
            cursor = 0;
            if (!end)
                return EOF;
        }
        return buffer[cursor++];
    }

    int token() {
        int ch;
        do {
            ch = next();
        } while (ch != EOF && ch <= ' ');
        return ch;
    }
};

class Output {
    char buffer[buffer_size];
    char *cursor = buffer;

  public:
    void flush() {
        std::fwrite(buffer, 1, cursor - buffer, stdout);
        cursor = buffer;
    }

    void number(int value, char separator) {
        if (cursor > buffer + buffer_size - max_number_width)
            flush();
        cursor = std::to_chars(cursor, buffer + buffer_size, value).ptr;
        *cursor++ = separator;
    }
};
} // namespace

int main() {
    Input input;
    int n = 0;
    for (int ch = input.token(); ch >= '0' && ch <= '9'; ch = input.next())
        n = n * 10 + ch - '0';

    std::array<int, types> head{}, tail{};
    std::vector<int> link(n + 1);
    int present = 0;
    for (int i = 1; i <= n; ++i) {
        int kind = 0;
        for (int ch = input.token(); ch > ' '; ch = input.next())
            kind |= ch == 'A' ? apple : (ch == 'B' ? banana : pineapple);
        if (tail[kind])
            link[tail[kind]] = i;
        else
            head[kind] = i;
        tail[kind] = i;
        present |= 1 << kind;
    }

    std::array<std::array<unsigned char, types>, states> best, previous{};
    for (auto &row : best)
        row.fill(unreachable);
    best[0][0] = 0;
    for (int mask = 0; mask <= present; ++mask) {
        if (mask & ~present)
            continue;
        for (int last = 0; last < types; ++last) {
            if (best[mask][last] == unreachable)
                continue;
            for (int kind = 1; kind < types; ++kind) {
                const int bit = 1 << kind;
                if (!(present & bit) || (mask & bit))
                    continue;
                const int cost = best[mask][last] + bits[kind & ~last];
                if (cost < best[mask | bit][kind]) {
                    best[mask | bit][kind] = cost;
                    previous[mask | bit][kind] = last;
                }
            }
        }
    }

    int last = 0;
    for (int kind = 1; kind < types; ++kind)
        if (best[present][kind] < best[present][last])
            last = kind;
    Output output;
    output.number(best[present][last], '\n');
    std::array<int, types> order{};
    int count = 0;
    for (int mask = present; mask;) {
        order[count++] = last;
        const int old = last;
        last = previous[mask][last];
        mask ^= 1 << old;
    }
    while (count)
        for (int glass = head[order[--count]]; glass; glass = link[glass])
            output.number(glass, --n ? ' ' : '\n');
    output.flush();
}
