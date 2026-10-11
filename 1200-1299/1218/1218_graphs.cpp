#include <iostream>
#include <string>
#include <vector>

const int PARAMS = 3, MAJORITY = 2;

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> names(n);
    std::vector<std::vector<int>> stats(n, std::vector<int>(PARAMS));
    for (int i = 0; i < n; i++) {
        std::cin >> names[i];
        for (int &v : stats[i]) {
            std::cin >> v;
        }
    }
    // reach[i][j]: i beats j, directly or through a chain of wins
    std::vector<std::vector<bool>> reach(n, std::vector<bool>(n, false));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int better = 0;
            for (int p = 0; p < PARAMS; p++) {
                better += stats[i][p] > stats[j][p];
            }
            reach[i][j] = i != j && better >= MAJORITY;
        }
    }
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (reach[i][k]) {
                for (int j = 0; j < n; j++) {
                    if (reach[k][j]) {
                        reach[i][j] = true;
                    }
                }
            }
        }
    }
    // a Jedi can win when every other one can be beaten along such a chain
    for (int i = 0; i < n; i++) {
        bool all = true;
        for (int j = 0; j < n; j++) {
            all = all && (i == j || reach[i][j]);
        }
        if (all) {
            std::cout << names[i] << "\n";
        }
    }
}
