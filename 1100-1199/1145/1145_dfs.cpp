#include <cstdio>

constexpr int MAX_WIDTH = 820;
constexpr int PADDED_WIDTH = MAX_WIDTH + 2;
constexpr int FREE = 1;
constexpr int PARENT_MARK = FREE + 1;
constexpr int DIRECTIONS = 4;
static unsigned char maze[PADDED_WIDTH * PADDED_WIDTH];

struct Endpoint {
    int cell;
    int distance;
};

Endpoint farthest(int root, int stride) {
    // Opposite directions differ in the low bit.
    const int steps[DIRECTIONS] = {1, -1, stride, -stride};
    int cell = root, depth = 0, direction = 0;
    Endpoint best{root, 0};
    maze[root] = PARENT_MARK;
    for (;;) {
        if (direction == DIRECTIONS) {
            if (cell == root)
                break;
            // The tree has no cross edges. Restore this cell and resume in its parent.
            const int back = maze[cell] - PARENT_MARK;
            maze[cell] = FREE;
            cell += steps[back];
            --depth;
            direction = (back ^ 1) + 1;
            continue;
        }
        const int next = cell + steps[direction];
        if (maze[next] != FREE) {
            ++direction;
            continue;
        }
        maze[next] = PARENT_MARK + (direction ^ 1);
        cell = next;
        ++depth;
        direction = 0;
        if (depth > best.distance)
            best = {cell, depth};
    }
    maze[root] = FREE;
    return best;
}

int main() {
    int width, height;
    if (std::scanf("%d%d", &width, &height) != 2)
        return 0;
    const int stride = width + 2;
    char row[PADDED_WIDTH];
    int start = 0;
    for (int y = 1; y <= height; ++y) {
        if (std::scanf("%s", row) != 1)
            return 0;
        for (int x = 0; x < width; ++x) {
            if (row[x] != '.')
                continue;
            const int cell = y * stride + x + 1;
            maze[cell] = FREE;
            if (start == 0)
                start = cell;
        }
    }
    const int diameter = start ? farthest(farthest(start, stride).cell, stride).distance : 0;
    std::printf("%d\n", diameter);
}
