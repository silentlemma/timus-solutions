#include <array>
#include <cstdio>
#include <functional>
#include <set>
#include <vector>

const int FACES = 6;
const int COORDS = 3; // the cell's place does not matter
typedef std::array<int, FACES> Faces;

// faces in the input order: front, up, right, down, left, back; a turn p
// gives face f the colour of face p[f]; SPIN turns the cube about the
// vertical axis, TIP about the left-right one
const Faces SPIN = {2, 1, 5, 3, 0, 4};
const Faces TIP = {1, 5, 2, 0, 4, 3};

// all 24 rotations of a cube, from two quarter turns
std::vector<Faces> rotations() {
    Faces start;
    for (int f = 0; f < FACES; f++)
        start[f] = f;
    std::set<Faces> found = {start};
    std::vector<Faces> queue = {start};
    for (size_t k = 0; k < queue.size(); k++)
        for (const Faces &g : {SPIN, TIP}) {
            Faces q;
            for (int f = 0; f < FACES; f++)
                q[f] = queue[k][g[f]];
            if (found.insert(q).second)
                queue.push_back(q);
        }
    return queue;
}

int main() {
    int n, m;
    scanf("%d", &n);
    std::vector<Faces> cubes(n);
    for (auto &cube : cubes)
        for (int &c : cube)
            scanf("%d", &c);
    scanf("%d", &m);
    std::vector<Faces> turns = rotations();
    // fits[j]: the cubes that can stand in cell j, turned somehow
    std::vector<std::vector<int>> fits(m);
    for (int j = 0; j < m; j++) {
        int skip;
        for (int k = 0; k < COORDS; k++)
            scanf("%d", &skip);
        Faces need;
        for (int &c : need)
            scanf("%d", &c);
        for (int i = 0; i < n; i++)
            for (const Faces &p : turns) {
                bool ok = true;
                for (int f = 0; f < FACES && ok; f++)
                    ok = need[f] == 0 || need[f] == cubes[i][p[f]];
                if (ok) {
                    fits[j].push_back(i);
                    break;
                }
            }
    }
    // Kuhn's augmenting paths from every cell
    std::vector<int> owner(n, -1);
    std::vector<bool> seen;
    std::function<bool(int)> augment = [&](int j) {
        for (int i : fits[j])
            if (!seen[i]) {
                seen[i] = true;
                if (owner[i] < 0 || augment(owner[i])) {
                    owner[i] = j;
                    return true;
                }
            }
        return false;
    };
    for (int j = 0; j < m; j++) {
        seen.assign(n, false);
        if (!augment(j)) {
            printf("0\n");
            return 0;
        }
    }
    std::vector<int> cubeOf(m);
    for (int i = 0; i < n; i++)
        if (owner[i] >= 0)
            cubeOf[owner[i]] = i + 1;
    for (int c : cubeOf)
        printf("%d\n", c);
}
