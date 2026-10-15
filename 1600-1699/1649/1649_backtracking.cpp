#include <cstdio>
#include <vector>
using namespace std;

const int WRAP = 4;  // a fifth bacterium leaves one: counts go 1, 2, 3, 4, 1, ...
const int MOST = 400;

enum Kind { BAD, FIRST, LAST, EITHER, WAIT };

int n, m;
// need[v]: how many free neighbours v must see settled after it, modulo 4,
// stored as 1..4 like the picture; deg[v]: free neighbours
vector<int> need, deg;
vector<char> alive;
vector<vector<int>> adj;

Kind kind(int v) {
    int d = deg[v], k = need[v];
    if (k != 1 && k - 1 > d)
        return BAD;
    if (d < WRAP && k == d + 1)
        return FIRST;  // before all free neighbours
    if (d < WRAP && k == 1)
        return LAST;  // after all of them
    if (d == WRAP && k == 1)
        return EITHER;  // an inner cell showing 1: before all or after all
    return WAIT;
}

// settle v before (first) or after all its free neighbours
void take(int v, bool first) {
    alive[v] = false;
    for (int u : adj[v])
        if (alive[u]) {
            deg[u]--;
            if (!first && --need[u] == 0)  // u now sees v settle after it
                need[u] = WRAP;
        }
}

// necessary: the later-neighbour counts must add up to the edges, and
// touching undecided cells must split into firsts and lasts
bool countsFit(const vector<int> &cells) {
    int edges = 0, fixed = 0;
    vector<char> open(n * m), seen(n * m);
    vector<int> openCells;
    for (int v : cells) {
        edges += deg[v];
        if (kind(v) == EITHER) {
            open[v] = 1;
            openCells.push_back(v);
        } else {
            fixed += need[v] - 1;
        }
    }
    edges /= 2;
    int rest = edges - fixed;
    if (rest < 0 || rest % WRAP || rest / WRAP > (int)openCells.size())
        return false;
    vector<char> reach(MOST + 1);  // reach[s]: s firsts possible so far
    reach[0] = 1;
    for (int s : openCells) {
        if (seen[s])
            continue;
        seen[s] = 1;
        vector<int> group = {s};
        int colour[2] = {0, 0};
        for (size_t i = 0; i < group.size(); i++) {
            int v = group[i];
            colour[(v / m + v % m) % 2]++;
            for (int u : adj[v])
                if (alive[u] && open[u] && !seen[u]) {
                    seen[u] = 1;
                    group.push_back(u);
                }
        }
        vector<char> next(MOST + 1);
        for (int t = 0; t <= MOST; t++)
            if (reach[t])
                for (int c : colour)
                    if (t + c <= MOST)
                        next[t + c] = 1;
        reach.swap(next);
    }
    return reach[rest / WRAP];
}

vector<vector<int>> components(const vector<int> &cells) {
    vector<char> inside(n * m), seen(n * m);
    for (int v : cells)
        inside[v] = 1;
    vector<vector<int>> parts;
    for (int s : cells) {
        if (seen[s])
            continue;
        seen[s] = 1;
        vector<int> part = {s};
        for (size_t i = 0; i < part.size(); i++)
            for (int u : adj[part[i]])
                if (inside[u] && alive[u] && !seen[u]) {
                    seen[u] = 1;
                    part.push_back(u);
                }
        parts.push_back(part);
    }
    return parts;
}

// an order of the free cells into out; false if there is none
bool solve(vector<int> cells, vector<int> &out) {
    vector<int> head, tail;
    while (true) {
        vector<int> queue;
        for (int v : cells)
            if (kind(v) != EITHER && kind(v) != WAIT)
                queue.push_back(v);
        bool moved = false;
        while (!queue.empty()) {
            int v = queue.back();
            queue.pop_back();
            if (!alive[v])
                continue;
            Kind k = kind(v);
            if (k == BAD)
                return false;
            if (k != FIRST && k != LAST)
                continue;
            take(v, k == FIRST);
            (k == FIRST ? head : tail).push_back(v);
            moved = true;
            for (int u : adj[v])
                if (alive[u])
                    queue.push_back(u);
        }
        vector<int> left;
        for (int v : cells)
            if (alive[v])
                left.push_back(v);
        cells.swap(left);
        if (!moved || cells.empty())
            break;
    }
    out.insert(out.end(), head.begin(), head.end());
    vector<int> middle;
    bool ok = true;
    if (!cells.empty()) {
        vector<vector<int>> parts = components(cells);
        if (parts.size() > 1) {
            for (const vector<int> &part : parts)
                if (!solve(part, middle))
                    return false;
        } else {
            // the first cell of any order comes before all its neighbours, so
            // with no forced cell left it must be an undecided one
            int pick = -1;
            for (int v : cells)
                if (kind(v) == EITHER) {
                    pick = v;
                    break;
                }
            if (pick < 0 || !countsFit(cells))
                return false;
            // an undecided cell comes before or after all its neighbours in
            // any order, so trying both ways for one of them misses nothing
            vector<int> rest;
            for (int v : cells)
                if (v != pick)
                    rest.push_back(v);
            ok = false;
            for (bool first : {true, false}) {
                vector<int> savedNeed = need, savedDeg = deg;
                vector<char> savedAlive = alive;
                take(pick, first);
                vector<int> order;
                bool found = solve(rest, order);
                need = savedNeed, deg = savedDeg, alive = savedAlive;
                if (found) {
                    if (first)
                        middle.push_back(pick);
                    middle.insert(middle.end(), order.begin(), order.end());
                    if (!first)
                        middle.push_back(pick);
                    ok = true;
                    break;
                }
            }
        }
    }
    if (!ok)
        return false;
    out.insert(out.end(), middle.begin(), middle.end());
    out.insert(out.end(), tail.rbegin(), tail.rend());
    return true;
}

int main() {
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    need.resize(n * m);
    for (int &k : need)
        if (scanf("%d", &k) != 1)
            return 0;
    adj.resize(n * m);
    for (int r = 0; r < n; r++)
        for (int c = 0; c < m; c++) {
            int v = r * m + c;
            if (r)
                adj[v].push_back(v - m);
            if (r + 1 < n)
                adj[v].push_back(v + m);
            if (c)
                adj[v].push_back(v - 1);
            if (c + 1 < m)
                adj[v].push_back(v + 1);
        }
    deg.resize(n * m);
    for (int v = 0; v < n * m; v++)
        deg[v] = adj[v].size();
    alive.assign(n * m, 1);
    vector<int> cells(n * m), order;
    for (int v = 0; v < n * m; v++)
        cells[v] = v;
    if (!solve(cells, order)) {
        puts("No");
        return 0;
    }
    puts("Yes");
    for (int v : order)
        printf("%d %d\n", v / m + 1, v % m + 1);
}
