#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

int main() {
    const size_t TRIANGLE = 3;
    int n;
    std::string color;
    std::cin >> n >> color;
    std::vector<int> poly;
    for (int v = 0; v < n; v++) {
        poly.push_back(v);
    }
    std::vector<std::pair<int, int>> cuts;
    while (poly.size() > TRIANGLE) {
        int m = poly.size();
        std::map<char, int> counts;
        for (int v : poly) {
            counts[color[v]]++;
        }
        int lonely = -1;
        for (int k = 0; k < m && lonely < 0; k++) {
            if (counts[color[poly[k]]] == 1) {
                lonely = k;
            }
        }
        if (lonely >= 0) {
            // a color met once: every triangle of the fan from that vertex
            // has it plus two neighbouring vertices, which differ
            for (int j = 2; j < m - 1; j++) {
                cuts.push_back({poly[lonely], poly[(lonely + j) % m]});
            }
            break;
        }
        // every color is met twice or more; a vertex whose neighbours differ
        // exists, as otherwise two colors would alternate around the whole
        // polygon, and cutting it off leaves all three colors
        int k = 0;
        while (color[poly[(k + m - 1) % m]] == color[poly[(k + 1) % m]]) {
            k++;
        }
        cuts.push_back({poly[(k + m - 1) % m], poly[(k + 1) % m]});
        poly.erase(poly.begin() + k);
    }
    printf("%d\n", (int)cuts.size());
    for (auto [a, b] : cuts) {
        printf("%d %d\n", a + 1, b + 1);
    }
}
