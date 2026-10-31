#include <algorithm>
#include <cstdio>
#include <string_view>

// the cube: A B C D around the bottom face, E F G H above them
const char *EDGES[] = {"AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"};
// the cube is bipartite; every operation changes one chamber of each side
const std::string_view EVEN = "ACFH", CELLS = "ABCDEFGH";
const int CHAR_COUNT = 128;
const int DEGREE = 3;

bool even(char c) { return EVEN.find(c) != std::string_view::npos; }

int main() {
    // ascii labels index fixed arrays; every cube vertex has three neighbors.
    int count[CHAR_COUNT] = {};
    int balance = 0;
    for (unsigned char c : CELLS) {
        std::scanf("%d", &count[static_cast<int>(c)]);
        balance += even(c) ? count[c] : -count[c];
    }
    if (balance != 0) {
        std::puts("IMPOSSIBLE");
        return 0;
    }
    char near[CHAR_COUNT][DEGREE] = {};
    int degree[CHAR_COUNT] = {};
    for (const auto &e : EDGES) {
        near[static_cast<int>(e[0])][degree[static_cast<int>(e[0])]++] = e[1];
        near[static_cast<int>(e[1])][degree[static_cast<int>(e[1])]++] = e[0];
    }
    auto emit = [&](char a, char b, char sign, int times) {
        for (int k = 0; k < times; k++)
            std::printf("%c%c%c\n", a, b, sign);
    };
    // annihilate along every edge as long as both ends hold duons; afterwards
    // every edge has an empty end
    for (const auto &e : EDGES) {
        int k = std::min(count[static_cast<unsigned char>(e[0])],
                         count[static_cast<unsigned char>(e[1])]);
        emit(e[0], e[1], '-', k);
        count[static_cast<unsigned char>(e[0])] -= k;
        count[static_cast<unsigned char>(e[1])] -= k;
    }
    // what is left can only sit at two opposite corners u and w, in equal
    // numbers; a pair made on the middle edge of a path u x y w removes both
    for (unsigned char u : EVEN) {
        if (!count[u])
            continue;
        unsigned char w = 0;
        for (unsigned char c : CELLS)
            if (!w && count[c] && !even(c))
                w = c;
        unsigned char x = near[u][0], y = 0;
        for (unsigned char c : near[x])
            for (unsigned char d : near[w])
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
}
