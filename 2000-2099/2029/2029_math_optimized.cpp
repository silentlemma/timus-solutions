#include <cstdio>

constexpr int MAX_DISKS = 50;
constexpr int PEG_SUM = 3;

int main() {
    int count;
    char target[MAX_DISKS + 1];
    if (std::scanf("%d%50s", &count, target) != 2)
        return 0;

    int source = 0;
    unsigned long long moves = 0;
    for (int disk = count - 1; disk >= 0; --disk) {
        const int peg = target[disk] - 'A';
        moves *= 2;
        if (peg != source) {
            ++moves;
            source = PEG_SUM - source - peg;
        }
    }
    std::printf("%llu\n", moves);
}
