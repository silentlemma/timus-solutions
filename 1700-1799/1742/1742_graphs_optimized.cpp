#include <cstdio>
#include <vector>

constexpr int IO_SIZE = 4096;
constexpr int DECIMAL_DIGITS = 16;
class Input {
    char data[IO_SIZE];
    int position = 0, size = 0;

  public:
    int byte() {
        if (position == size) {
            size = std::fread(data, 1, sizeof data, stdin);
            position = 0;
            if (size == 0)
                return EOF;
        }
        return static_cast<unsigned char>(data[position++]);
    }
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = byte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value * sign;
    }
};

enum State : unsigned char { fresh, walking, done };

int main() {
    Input input;
    int size = input.number();
    std::vector<int> successor(size + 1);
    std::vector<unsigned char> incoming(size + 1);
    for (int city = 1; city <= size; ++city) {
        successor[city] = input.number();
        auto &count = incoming[successor[city]];
        if (count < 2)
            ++count;
    }
    std::vector<State> state(size + 1, fresh);
    int starts = 0, cycles = 0, cycle_nodes = 0, isolated_cycles = 0;
    for (int start = 1; start <= size; ++start) {
        starts += incoming[start] == 0;
        int node = start;
        while (state[node] == fresh) {
            state[node] = walking;
            node = successor[node];
        }
        if (state[node] == walking) {
            ++cycles;
            const int first = node;
            bool isolated = true;
            do {
                ++cycle_nodes;
                isolated &= incoming[node] == 1;
                node = successor[node];
            } while (node != first);
            isolated_cycles += isolated;
        }
        // Follow the arrows again to clear the walk without a separate path array.
        for (node = start; state[node] == walking; node = successor[node])
            state[node] = done;
    }
    std::printf("%d %d\n", starts + isolated_cycles, size - cycle_nodes + cycles);
}
