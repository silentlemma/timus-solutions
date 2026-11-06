#include <cstdio>
#include <vector>

enum State : unsigned char { fresh, walking, done };

int main() {
    int size;
    if (std::scanf("%d", &size) != 1)
        return 0;
    std::vector<int> successor(size + 1);
    std::vector<unsigned char> incoming(size + 1);
    for (int city = 1; city <= size; ++city) {
        std::scanf("%d", &successor[city]);
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
