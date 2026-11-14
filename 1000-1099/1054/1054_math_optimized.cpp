#include <cstdio>
#include <utility>

constexpr int MAX_DISKS = 31;
constexpr int SOURCE = 1;
constexpr int TARGET = 2;
constexpr int SPARE = 3;

int main() {
    int count;
    if (std::scanf("%d", &count) != 1)
        return 0;
    int rods[MAX_DISKS];
    for (int i = 0; i < count; ++i) {
        if (std::scanf("%d", &rods[i]) != 1)
            return 0;
    }

    int source = SOURCE, target = TARGET, spare = SPARE;
    unsigned moves = 0;
    // Each disk determines the next bit of the move number.
    for (int i = count - 1; i >= 0; --i) {
        if (rods[i] == spare) {
            std::puts("-1");
            return 0;
        }
        const bool moved = rods[i] == target;
        moves = 2 * moves + moved;
        if (moved)
            std::swap(source, spare);
        else
            std::swap(target, spare);
    }
    std::printf("%u\n", moves);
}
