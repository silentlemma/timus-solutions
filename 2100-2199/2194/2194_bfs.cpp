#include <algorithm>
#include <cstdio>
#include <deque>
#include <vector>

constexpr int FACES = 6;  // a six lets the player roll again in the same turn

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> jump(n + 1, 0);
    for (int i = 2; i < n; i++) scanf("%d", &jump[i]);
    // land[i]: where the token rests after arriving at i and following snakes
    std::vector<int> land(n + 1);
    for (int i = 1; i <= n; i++) land[i] = jump[i] ? land[i - jump[i]] : i;

    // turns holds the fewest turns begun when the token is about to roll at a
    // cell, and a six keeps the turn going at weight 0 while other rolls cost 1
    const int infinity = n + 1;
    std::vector<int> turns(n + 1, infinity);
    turns[1] = 1;
    std::deque<int> queue = {1};
    int best = infinity;
    while (!queue.empty()) {
        int cell = queue.front();
        queue.pop_front();
        int current = turns[cell];
        if (current >= best) continue;
        for (int face = 1; face <= FACES; face++) {
            int target = land[std::min(cell + face, n)];
            if (target == n) {
                best = std::min(best, current);
                continue;
            }
            int cost = face == FACES ? current : current + 1;
            if (cost < turns[target]) {
                turns[target] = cost;
                if (face == FACES) queue.push_front(target);
                else queue.push_back(target);
            }
        }
    }
    printf("%d\n", best < infinity ? best : -1);
    return 0;
}
