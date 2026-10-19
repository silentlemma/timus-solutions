#include <cstdio>
#include <vector>

struct Step {
    bool call;
    int mage;
};

static std::vector<Step> readPlan(int length) {
    std::vector<Step> plan(length);
    for (auto &s : plan) {
        char sign;
        scanf(" %c %d", &sign, &s.mage);
        s.call = sign == '+';
    }
    return plan;
}

int main() {
    int tests;
    if (scanf("%d", &tests) != 1) return 0;
    while (tests--) {
        int n, m, k;
        scanf("%d %d %d", &n, &m, &k);
        std::vector<Step> sandro = readPlan(n), zagamius = readPlan(m);
        // cell (i, j): Sandro has done i steps and Zagamius j; it is taken
        // when both offices hold one mage, and a step is blocked exactly when
        // it leads into a taken cell. Row n + 1 is all taken: no step down.
        std::vector<std::vector<char>> taken(n + 2, std::vector<char>(m + 1, 1));
        std::vector<char> withSandro(k + 1, 0);
        for (int i = 0; i <= n; i++) {
            if (i > 0) withSandro[sandro[i - 1].mage] = sandro[i - 1].call;
            int shared = 0;  // mages in both offices
            for (int j = 0; j <= m; j++) {
                if (j > 0 && withSandro[zagamius[j - 1].mage]) {
                    shared += zagamius[j - 1].call ? 1 : -1;
                }
                taken[i][j] = shared > 0;
            }
        }
        std::vector<std::vector<char>> reach(n + 1, std::vector<char>(m + 1, 0));
        reach[0][0] = 1;
        bool stuck = false;
        for (int i = 0; i <= n && !stuck; i++) {
            for (int j = 0; j <= m; j++) {
                if (!reach[i][j]) continue;
                bool down = !taken[i + 1][j];
                bool right = j < m && !taken[i][j + 1];
                if (!down && !right && (i < n || j < m)) {
                    stuck = true;
                    break;
                }
                if (down) reach[i + 1][j] = 1;
                if (right) reach[i][j + 1] = 1;
            }
        }
        puts(stuck ? ":-(" : ":-)");
    }
    return 0;
}
