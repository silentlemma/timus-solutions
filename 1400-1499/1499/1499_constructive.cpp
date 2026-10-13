#include <algorithm>
#include <cstdio>
#include <functional>
#include <vector>

using namespace std;

vector<pair<int, int>> cuts;

// a convex face is cut into triangles by diagonals from its first vertex,
// as the first and the last of its sides already exist
void fan(const vector<int> &face) {
    for (size_t i = 2; i + 1 < face.size(); i++)
        cuts.push_back({face[0], face[i]});
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<vector<int>> ending(n + 1); // the cuts u-v with u < v, kept at v
    for (int i = 0; i < k; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        ending[max(a, b)].push_back(min(a, b));
    }
    // walk the vertices in order: a cut u-v closes the face formed by u,
    // the vertices still stacked above it, and v; nearer u first
    vector<int> stack;
    for (int v = 1; v <= n; v++) {
        stack.push_back(v);
        sort(ending[v].begin(), ending[v].end(), greater<int>());
        for (int u : ending[v]) {
            stack.pop_back();
            vector<int> face;
            while (stack.back() != u) {
                face.push_back(stack.back());
                stack.pop_back();
            }
            face.push_back(u);
            reverse(face.begin(), face.end());
            face.push_back(v);
            fan(face);
            stack.push_back(v);
        }
    }
    fan(stack); // the last face, closed by the side n-1
    printf("%d\n", (int)cuts.size());
    for (auto &c : cuts)
        printf("%d %d\n", c.first, c.second);
}
