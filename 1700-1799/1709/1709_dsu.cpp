#include <iostream>
#include <string>
#include <vector>

std::vector<int> parent;

int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

int main() {
    int n;
    long long d, a;
    std::cin >> n >> d >> a;
    std::vector<std::string> flights(n);
    for (std::string& row : flights) {
        std::cin >> row;
    }
    parent.resize(n);
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
    // the result must be a spanning tree: keep a spanning forest of the
    // existing flights, cancel the rest, then join the trees with new flights
    std::vector<std::string> plan(n, std::string(n, '0'));
    long long cost = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (flights[i][j] == '1') {
                int ri = find(i), rj = find(j);
                if (ri != rj) {
                    parent[ri] = rj;
                } else {
                    plan[i][j] = plan[j][i] = 'd';
                    cost += d;
                }
            }
        }
    }
    for (int j = 1; j < n; j++) {
        int r0 = find(0), rj = find(j);
        if (r0 != rj) {
            parent[rj] = r0;
            plan[0][j] = plan[j][0] = 'a';
            cost += a;
        }
    }
    std::cout << cost << "\n";
    for (const std::string& row : plan) {
        std::cout << row << "\n";
    }
}
