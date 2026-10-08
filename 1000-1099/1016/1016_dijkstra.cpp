#include <array>
#include <cstdio>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

const int SIZE = 8, FACES = 6, DIRECTIONS = 4, BOTTOM = 4;
const long long INF = 1LL << 60;
// faces in the input order near, far, top, right, bottom, left; a roll in
// direction d puts the face from position SOURCE[d][i] to position i
const int DX[DIRECTIONS] = {0, 0, 1, -1}, DY[DIRECTIONS] = {1, -1, 0, 0};
const int SOURCE[DIRECTIONS][FACES] = {
    {4, 2, 0, 3, 1, 5}, {2, 4, 1, 3, 0, 5}, {0, 1, 5, 2, 3, 4}, {0, 1, 3, 4, 5, 2}};

using Orientation = std::array<int, FACES>;

int main() {
    std::string from, to;
    long long value[FACES];
    if (!(std::cin >> from >> to))
        return 1;
    for (long long &v : value)
        if (!(std::cin >> v))
            return 1;

    // the 24 orientations: which original face is at each position
    Orientation identity;
    for (int i = 0; i < FACES; i++)
        identity[i] = i;
    std::vector<Orientation> orient = {identity};
    std::map<Orientation, int> id = {{identity, 0}};
    std::vector<std::array<int, DIRECTIONS>> next;
    for (size_t o = 0; o < orient.size(); o++) {
        next.emplace_back();
        for (int d = 0; d < DIRECTIONS; d++) {
            Orientation r;
            for (int i = 0; i < FACES; i++)
                r[i] = orient[o][SOURCE[d][i]];
            if (!id.count(r)) {
                id[r] = orient.size();
                orient.push_back(r);
            }
            next[o][d] = id[r];
        }
    }

    // Dijkstra over (cell, orientation); a state costs its bottom face
    int states = SIZE * SIZE * orient.size();
    auto state = [&](int x, int y, int o) { return (x * SIZE + y) * (int)orient.size() + o; };
    std::vector<long long> dist(states, INF);
    std::vector<int> prev(states, -1);
    int sx = from[0] - 'a', sy = from[1] - '1', tx = to[0] - 'a', ty = to[1] - '1';
    using Item = std::pair<long long, int>;
    std::priority_queue<Item, std::vector<Item>, std::greater<Item>> heap;
    dist[state(sx, sy, 0)] = value[BOTTOM];
    heap.push({value[BOTTOM], state(sx, sy, 0)});
    while (!heap.empty()) {
        auto [d, s] = heap.top();
        heap.pop();
        if (d > dist[s])
            continue;
        int o = s % orient.size(), x = s / orient.size() / SIZE, y = s / orient.size() % SIZE;
        for (int k = 0; k < DIRECTIONS; k++) {
            int nx = x + DX[k], ny = y + DY[k];
            if (nx < 0 || ny < 0 || nx >= SIZE || ny >= SIZE)
                continue;
            int no = next[o][k], ns = state(nx, ny, no);
            long long nd = d + value[orient[no][BOTTOM]];
            if (nd < dist[ns]) {
                dist[ns] = nd;
                prev[ns] = s;
                heap.push({nd, ns});
            }
        }
    }

    int best = state(tx, ty, 0);
    for (size_t o = 0; o < orient.size(); o++)
        if (dist[state(tx, ty, o)] < dist[best])
            best = state(tx, ty, o);
    std::vector<std::string> route;
    for (int s = best; s >= 0; s = prev[s]) {
        int c = s / orient.size();
        route.push_back(std::string(1, 'a' + c / SIZE) + std::string(1, '1' + c % SIZE));
    }
    printf("%lld", dist[best]);
    for (size_t i = route.size(); i-- > 0;)
        printf(" %s", route[i].c_str());
    printf("\n");
}
