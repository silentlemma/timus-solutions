#include <cstdio>
#include <string>
#include <vector>

const int SIDE = 4, ROOMS = SIDE * SIDE, MAX_LEVELS = 16;
// moves inside a level: name, row step, column step
const char NAMES[] = "NESW";
const int DR[] = {-1, 0, 1, 0}, DC[] = {0, 1, 0, -1};
const int DIRS = 4;

int n, food[MAX_LEVELS][ROOMS], door[MAX_LEVELS][ROOMS];
// best[lv][s][e][k]: most food on a path of k rooms from s to e in a level
int best[MAX_LEVELS][ROOMS][ROOMS][ROOMS + 1];

int step(int u, int d) {
    int r = u / SIDE + DR[d], c = u % SIDE + DC[d];
    return r >= 0 && r < SIDE && c >= 0 && c < SIDE ? r * SIDE + c : -1;
}

void walk(int lv, int s, int u, int mask, int k, int total) {
    int &b = best[lv][s][u][k];
    if (total > b) {
        b = total;
    }
    for (int d = 0; d < DIRS; d++) {
        int v = step(u, d);
        if (v >= 0 && !(mask >> v & 1)) {
            walk(lv, s, v, mask | 1 << v, k + 1, total + food[lv][v]);
        }
    }
}

// some path of `left` rooms from u to e with exactly `rest` food
bool findMoves(int lv, int u, int e, int mask, int left, int rest, std::string &path) {
    if (left == 1) {
        return u == e && rest == food[lv][u];
    }
    for (int d = 0; d < DIRS; d++) {
        int v = step(u, d);
        if (v >= 0 && !(mask >> v & 1)) {
            path += NAMES[d];
            if (findMoves(lv, v, e, mask | 1 << v, left - 1, rest - food[lv][u], path)) {
                return true;
            }
            path.pop_back();
        }
    }
    return false;
}

struct Plan {
    int s, e, k;
};

int start;

// the path maximising den * food - num * rooms, as per-level choices, with
// its food and room count
std::vector<Plan> bestPath(long long num, long long den, long long &total, long long &rooms) {
    const long long NONE = -(1LL << 62);
    std::vector<long long> after(ROOMS, 0);
    std::vector<std::vector<Plan>> choice(n, std::vector<Plan>(ROOMS));
    for (int lv = n - 1; lv >= 0; lv--) {
        std::vector<long long> here(ROOMS, NONE);
        for (int s = 0; s < ROOMS; s++) {
            for (int e = 0; e < ROOMS; e++) {
                if ((lv < n - 1 && !door[lv][e]) || after[e] == NONE) {
                    continue;
                }
                for (int k = 1; k <= ROOMS; k++) {
                    int w = best[lv][s][e][k];
                    long long v = den * w - num * k + after[e];
                    if (w >= 0 && v > here[s]) {
                        here[s] = v;
                        choice[lv][s] = {s, e, k};
                    }
                }
            }
        }
        after = here;
    }
    std::vector<Plan> plan;
    total = rooms = 0;
    for (int lv = 0, s = start; lv < n; lv++) {
        Plan p = choice[lv][s];
        plan.push_back(p);
        total += best[lv][s][p.e][p.k];
        rooms += p.k;
        s = p.e;
    }
    return plan;
}

int main() {
    scanf("%d", &n);
    for (int lv = 0; lv < n; lv++) {
        for (int u = 0; u < ROOMS; u++) {
            scanf("%d", &food[lv][u]);
        }
        for (int u = 0; u < ROOMS; u++) {
            scanf("%d", &door[lv][u]);
        }
    }
    int r, c;
    scanf("%d %d", &r, &c);
    start = (r - 1) * SIDE + c - 1;
    for (int lv = 0; lv < n; lv++) {
        for (int s = 0; s < ROOMS; s++) {
            for (int e = 0; e < ROOMS; e++) {
                for (int k = 0; k <= ROOMS; k++) {
                    best[lv][s][e][k] = -1;
                }
            }
            walk(lv, s, s, 1 << s, 1, food[lv][s]);
        }
    }
    // Dinkelbach: move to the better ratio until no path beats the current
    long long num = 0, den = 1, total, rooms;
    std::vector<Plan> chosen;
    while (true) {
        std::vector<Plan> plan = bestPath(num, den, total, rooms);
        if (total * den <= num * rooms) {
            break;
        }
        num = total;
        den = rooms;
        chosen = plan;
    }
    std::string moves;
    for (int lv = 0; lv < n; lv++) {
        if (lv > 0) {
            moves += 'D';
        }
        Plan p = chosen[lv];
        findMoves(lv, p.s, p.e, 1 << p.s, p.k, best[lv][p.s][p.e][p.k], moves);
    }
    printf("%.4f\n%d\n", (double)num / den, (int)moves.size());
    if (!moves.empty()) {
        printf("%s\n", moves.c_str());
    }
}
