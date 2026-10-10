#include <iostream>
#include <map>
#include <string>
#include <vector>

// the cube: A B C D around the bottom face, E F G H above them
const std::vector<std::string> EDGES = {"AB", "BC", "CD", "DA", "EF", "FG",
                                        "GH", "HE", "AE", "BF", "CG", "DH"};
// the cube is bipartite; every operation changes one chamber of each side
const std::string EVEN = "ACFH", CELLS = "ABCDEFGH";

bool even(char c) { return EVEN.find(c) != std::string::npos; }

int main() {
    std::map<char, int> count;
    int balance = 0;
    for (char c : CELLS) {
        std::cin >> count[c];
        balance += even(c) ? count[c] : -count[c];
    }
    if (balance != 0) {
        std::cout << "IMPOSSIBLE\n";
        return 0;
    }
    std::map<char, std::vector<char>> near;
    for (const auto &e : EDGES) {
        near[e[0]].push_back(e[1]);
        near[e[1]].push_back(e[0]);
    }
    std::string out;
    auto emit = [&](char a, char b, char sign, int times) {
        for (int k = 0; k < times; k++)
            out += std::string{a, b, sign, '\n'};
    };
    // annihilate along every edge as long as both ends hold duons; afterwards
    // every edge has an empty end
    for (const auto &e : EDGES) {
        int k = std::min(count[e[0]], count[e[1]]);
        emit(e[0], e[1], '-', k);
        count[e[0]] -= k;
        count[e[1]] -= k;
    }
    // what is left can only sit at two opposite corners u and w, in equal
    // numbers; a pair made on the middle edge of a path u x y w removes both
    for (char u : EVEN) {
        if (!count[u])
            continue;
        char w = 0;
        for (char c : CELLS)
            if (!w && count[c] && !even(c))
                w = c;
        char x = near[u][0], y = 0;
        for (char c : near[x])
            for (char d : near[w])
                if (!y && c == d)
                    y = c;
        for (int k = 0; k < count[u]; k++) {
            emit(x, y, '+', 1);
            emit(u, x, '-', 1);
            emit(y, w, '-', 1);
        }
        count[w] -= count[u];
        count[u] = 0;
    }
    std::cout << out;
}
