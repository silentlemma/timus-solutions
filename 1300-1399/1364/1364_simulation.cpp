#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

// east, south, west, north: turning right moves one step along this list
const int DR[] = {0, 1, 0, -1};
const int DC[] = {1, 0, -1, 0};
const int DIRECTIONS = 4;
const int FIELDS = 7;

int main() {
    int n = 0, m = 0, rt = 0, ct = 0, rl = 0, cl = 0, t = 0;
    if (scanf("%d %d %d %d %d %d %d", &n, &m, &rt, &ct, &rl, &cl, &t) != FIELDS)
        return 0;
    // dig the spiral up to the treasure, remembering the order of the graves,
    // with a frame of dug cells around the cemetery standing for the wall
    std::vector<std::vector<bool>> seen(n + 2, std::vector<bool>(m + 2, false));
    for (int r = 0; r < n + 2; r++)
        seen[r][0] = seen[r][m + 1] = true;
    for (int c = 0; c < m + 2; c++)
        seen[0][c] = seen[n + 1][c] = true;
    std::vector<std::pair<int, int>> path(1, {1, 1});
    seen[1][1] = true;
    int r = 1, c = 1, d = 0;
    while (r != rt || c != ct) {
        if (seen[r + DR[d]][c + DC[d]]) {
            d = (d + 1) % DIRECTIONS;
            continue;
        }
        r += DR[d];
        c += DC[d];
        seen[r][c] = true;
        path.push_back({r, c});
    }
    // Lara runs along the tunnel, at most t graves either way
    int here = 0;
    while (path[here] != std::make_pair(rl, cl))
        here++;
    int lo = std::max(0, here - t), hi = std::min((int)path.size() - 1, here + t);
    std::string out;
    for (int i = lo; i <= hi; i++)
        out += std::to_string(path[i].first) + " " + std::to_string(path[i].second) + "\n";
    fputs(out.c_str(), stdout);
    return 0;
}
