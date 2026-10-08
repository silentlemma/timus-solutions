#include <cstdio>
#include <string>
#include <unordered_map>
#include <vector>

const int FACES = 6, ROTATIONS = 24, BASE = 7;
// quarter turns around the vertical and the left-right axes: the new face at
// position i is the old face at position TURNS[t][i]
const int TURNS[2][FACES] = {{3, 5, 2, 1, 4, 0}, {0, 1, 5, 2, 3, 4}};

std::vector<std::vector<int>> rotations() {
    std::vector<std::vector<int>> all(1, std::vector<int>(FACES));
    for (int i = 0; i < FACES; i++)
        all[0][i] = i;
    for (size_t k = 0; k < all.size(); k++)
        for (const int *turn : TURNS) {
            std::vector<int> r(FACES);
            for (int i = 0; i < FACES; i++)
                r[i] = all[k][turn[i]];
            bool known = false;
            for (const auto &q : all)
                known |= q == r;
            if (!known)
                all.push_back(r);
        }
    return all;
}

int main() {
    auto rots = rotations();
    int n;
    if (scanf("%d", &n) != 1 || (int)rots.size() != ROTATIONS)
        return 1;
    // the key of a die is the smallest code among its 24 rotations
    std::unordered_map<int, int> group;
    std::vector<std::vector<int>> members;
    for (int d = 1; d <= n; d++) {
        int face[FACES];
        for (int &f : face)
            if (scanf("%d", &f) != 1)
                return 1;
        int key = -1;
        for (const auto &r : rots) {
            int code = 0;
            for (int i = 0; i < FACES; i++)
                code = code * BASE + face[r[i]];
            if (key < 0 || code < key)
                key = code;
        }
        auto it = group.find(key);
        if (it == group.end()) {
            group[key] = members.size();
            members.push_back({d});
        } else {
            members[it->second].push_back(d);
        }
    }
    std::string out = std::to_string(members.size()) + "\n";
    for (const auto &m : members) {
        for (size_t i = 0; i < m.size(); i++)
            out += (i ? " " : "") + std::to_string(m[i]);
        out += "\n";
    }
    fputs(out.c_str(), stdout);
}
