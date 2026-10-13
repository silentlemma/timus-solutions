#include <cstdio>
#include <vector>

using namespace std;

const int EMPTY = 0, WHITE = 1, BLACK = 2;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> hummocks(2 * n + 1, BLACK), moves;
    for (int i = 0; i < n; i++)
        hummocks[i] = WHITE;
    hummocks[n] = EMPTY;
    int hole = n;
    // runs of 1, 2, ..., n, n, n, ..., 1 moves, the colours taking turns,
    // and in a run a frog jumps into the hole when it can and slides otherwise
    vector<int> runs;
    for (int i = 1; i <= n; i++)
        runs.push_back(i);
    for (int i = n; i >= 1; i--)
        runs.push_back(i);
    runs.insert(runs.begin() + n, n);
    int colour = BLACK;
    for (int run : runs) {
        int step = colour == BLACK ? 1 : -1; // where the frogs come from
        int other = colour == BLACK ? WHITE : BLACK;
        for (int k = 0; k < run; k++) {
            int far = hole + 2 * step, near = hole + step;
            bool jump =
                far >= 0 && far <= 2 * n && hummocks[far] == colour && hummocks[near] == other;
            int frog = jump ? far : near;
            hummocks[hole] = colour;
            hummocks[frog] = EMPTY;
            hole = frog;
            moves.push_back(frog);
        }
        colour = other;
    }
    printf("%d\n", (int)moves.size());
    for (size_t i = 0; i < moves.size(); i++)
        printf(i + 1 < moves.size() ? "%d " : "%d\n", moves[i]);
}
