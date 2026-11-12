#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>

constexpr int MAX_SIDE = 50, MAX_CELLS = MAX_SIDE * MAX_SIDE, COLORS = 10, PLAYERS = 2;

struct Simulation {
    int width = 0, cells = 0;
    std::array<uint8_t, MAX_CELLS> color{}, owner{};
    std::array<int, PLAYERS> area{};
    std::array<std::vector<uint16_t>, PLAYERS * COLORS> frontier;
    std::array<size_t, PLAYERS * COLORS> head{};

    void offer(int side, int cell) {
        if (owner[cell] == 0)
            frontier[side * COLORS + color[cell]].push_back(cell);
    }
    void claim(int side, int cell) {
        owner[cell] = side + 1;
        ++area[side];
        if (cell >= width)
            offer(side, cell - width);
        if (cell + width < cells)
            offer(side, cell + width);
        if (cell % width != 0)
            offer(side, cell - 1);
        if (cell % width + 1 < width)
            offer(side, cell + 1);
    }
    void expand(int side, int alliance) {
        int bucket = side * COLORS + alliance;
        auto &pending = frontier[bucket];
        while (head[bucket] < pending.size()) {
            int cell = pending[head[bucket]++];
            // Another path or the opponent may already have claimed this boundary cell.
            if (owner[cell] == 0)
                claim(side, cell);
        }
    }
};

int main() {
    int height, width;
    scanf("%d%d", &height, &width);
    Simulation simulation;
    simulation.width = width;
    simulation.cells = height * width;
    char row[MAX_SIDE + 1];
    for (int r = 0; r < height; ++r) {
        scanf("%50s", row);
        for (int c = 0; c < width; ++c)
            simulation.color[r * width + c] = row[c] - '0';
    }
    int seeds[PLAYERS] = {(height - 1) * width, width - 1};
    for (int side = 0; side < PLAYERS; ++side) {
        simulation.claim(side, seeds[side]);
        simulation.expand(side, simulation.color[seeds[side]]);
    }
    int moves;
    scanf("%d", &moves);
    for (int turn = 0; turn < moves; ++turn) {
        int alliance;
        scanf("%d", &alliance);
        simulation.expand(turn % PLAYERS, alliance);
    }
    printf("%d\n%d\n", simulation.area[0], simulation.area[1]);
}
