#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <vector>

// face positions in the input: front, right, left, back, top, bottom; a
// quarter turn about the vertical axis (front goes right) and one about the
// left-right axis (top goes front), as new position from old position
const int FACES = 6, FRONT = 0, RIGHT = 1, LEFT = 2, BACK = 3;
const std::vector<int> SPIN = {2, 0, 3, 1, 4, 5}, TIP = {4, 1, 2, 5, 3, 0};

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // all 24 rotations as position -> original face
    std::vector<int> start(FACES);
    for (int p = 0; p < FACES; p++)
        start[p] = p;
    std::set<std::vector<int>> rotations = {start};
    std::vector<std::vector<int>> stack = {start};
    while (!stack.empty()) {
        auto cur = stack.back();
        stack.pop_back();
        for (const auto &turn : {SPIN, TIP}) {
            std::vector<int> next(FACES);
            for (int p = 0; p < FACES; p++)
                next[p] = cur[turn[p]];
            if (rotations.insert(next).second)
                stack.push_back(next);
        }
    }
    // each cube can show a given ring of side colours at most once, since its
    // faces all differ; the tallest tower is the most common ring
    std::map<std::string, int> rings;
    int best = 0;
    char cube[FACES + 2];
    for (int i = 0; i < n; i++) {
        scanf("%7s", cube);
        for (const auto &rot : rotations) {
            std::string ring = {cube[rot[FRONT]], cube[rot[RIGHT]], cube[rot[BACK]],
                                cube[rot[LEFT]]};
            best = std::max(best, ++rings[ring]);
        }
    }
    printf("%d\n", best);
}
