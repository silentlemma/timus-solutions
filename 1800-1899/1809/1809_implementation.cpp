#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

const int SIDE = 20, COUNT = 4;
typedef std::pair<int, int> Cell;
const Cell STEPS[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

// whether potatoes a and b share a line with nobody between them
bool sees(const std::vector<Cell> &p, int a, int b) {
    auto [xa, ya] = p[a];
    auto [xb, yb] = p[b];
    if (xa != xb && ya != yb) return false;
    for (int k = 0; k < COUNT; k++) {
        if (k == a || k == b) continue;
        auto [x, y] = p[k];
        if (std::min(xa, xb) <= x && x <= std::max(xa, xb) && std::min(ya, yb) <= y &&
            y <= std::max(ya, yb))
            return false;
    }
    return true;
}

bool good(const std::vector<Cell> &p) {
    for (int a = 0; a < COUNT; a++) {
        auto [x, y] = p[a];
        if (x < 1 || x > SIDE || y < 1 || y > SIDE) return false;
        for (int b = 0; b < a; b++) {
            if (p[a] == p[b]) return false;
        }
    }
    for (int a = 0; a < COUNT; a++) {
        int seen = 0;
        for (int b = 0; b < COUNT; b++) {
            if (b != a && sees(p, a, b)) seen++;
        }
        if (seen != 1) return false;
    }
    return true;
}

std::vector<Cell> solve(const std::vector<Cell> &start) {
    if (good(start)) return start;
    for (int k = 0; k < COUNT; k++) {
        for (int x = 1; x <= SIDE; x++) {
            for (int y = 1; y <= SIDE; y++) {
                std::vector<Cell> p = start;
                p[k] = {x, y};
                if (good(p)) return p;
            }
        }
    }
    // two moves always do: next to the two kept potatoes, or as a pair of
    // their own in rows and columns nobody else uses
    for (int k = 0; k < COUNT; k++) {
        for (int l = k + 1; l < COUNT; l++) {
            std::vector<Cell> kept, near;
            for (int i = 0; i < COUNT; i++) {
                if (i != k && i != l) kept.push_back(start[i]);
            }
            for (auto [x, y] : kept) {
                for (auto [dx, dy] : STEPS) near.push_back({x + dx, y + dy});
            }
            std::vector<std::pair<Cell, Cell>> options;
            for (Cell a : near) {
                for (Cell b : near) options.push_back({a, b});
            }
            int fx = 1, fy = 1;
            auto usedX = [&](int x) { return x == kept[0].first || x == kept[1].first; };
            auto usedY = [&](int y) { return y == kept[0].second || y == kept[1].second; };
            while (usedX(fx)) fx++;
            while (usedY(fy) || usedY(fy + 1)) fy++;
            options.push_back({{fx, fy}, {fx, fy + 1}});
            for (auto [a, b] : options) {
                std::vector<Cell> p = start;
                p[k] = a;
                p[l] = b;
                if (good(p)) return p;
            }
        }
    }
    return start;
}

int main() {
    std::vector<Cell> start(COUNT);
    for (auto &[x, y] : start) {
        if (scanf("%d %d", &x, &y) != 2) return 0;
    }
    for (auto [x, y] : solve(start)) printf("%d %d\n", x, y);
    return 0;
}
