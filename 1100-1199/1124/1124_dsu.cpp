#include <cstdio>
#include <set>
#include <vector>

std::vector<int> parent;

int find(int x) {
    while (parent[x] != x)
        x = parent[x] = parent[parent[x]];
    return x;
}

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 0;
    parent.resize(m);
    for (int i = 0; i < m; i++)
        parent[i] = i;
    // a piece of colour c in box b is an edge b -> c; every box has n pieces
    // and should get n back, so each connected group of boxes is an Euler
    // circuit, walked one carried piece per move
    int moves = 0;
    std::vector<bool> touched(m, false);
    for (int box = 0; box < m; box++)
        for (int k = 0; k < n; k++) {
            int colour;
            scanf("%d", &colour);
            colour--;
            if (colour != box) {
                moves++;
                touched[box] = touched[colour] = true;
                parent[find(box)] = find(colour);
            }
        }
    std::set<int> groups;
    for (int x = 0; x < m; x++)
        if (touched[x])
            groups.insert(find(x));
    // one empty move of the hand between groups
    printf("%d\n", moves ? moves + (int)groups.size() - 1 : 0);
}
