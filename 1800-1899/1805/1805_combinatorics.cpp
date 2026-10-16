#include <iostream>
#include <string>
#include <vector>

const int TURNS = 4;

int main() {
    int n;
    unsigned long long k;
    if (!(std::cin >> n >> k)) return 0;
    // the four cells a quarter turn takes into each other form an orbit; a
    // grille opens exactly one cell of every orbit
    std::vector<std::vector<int>> orbit(n, std::vector<int>(n, -1));
    int orbits = 0;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            if (orbit[r][c] != -1) continue;
            int rr = r, cc = c;
            for (int t = 0; t < TURNS; t++) {
                orbit[rr][cc] = orbits;
                int keep = rr;
                rr = cc;
                cc = n - 1 - keep;
            }
            orbits++;
        }
    }
    // left[o]: cells of orbit o not passed yet, -1 once its window is cut
    std::vector<int> left(orbits, TURNS);
    for (int r = 0; r < n; r++) {
        std::string row;
        for (int c = 0; c < n; c++) {
            int o = orbit[r][c];
            if (left[o] == -1) {
                row += '0';
                continue;
            }
            left[o]--;
            // grilles with a 0 here: every open orbit picks one of its
            // remaining cells
            unsigned long long withZero = 1;
            for (int rest : left) {
                if (rest != -1) withZero *= rest;
            }
            if (k <= withZero) {
                row += '0';
            } else {
                k -= withZero;
                row += '1';
                left[o] = -1;
            }
        }
        std::cout << row << "\n";
    }
    return 0;
}
