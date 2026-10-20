#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

constexpr int ROWS = 3;
constexpr int FRONTIER = 2 * ROWS;
constexpr int CELLS = FRONTIER + ROWS;
constexpr int MASKS = 1 << ROWS;
constexpr int GAIN = ROWS - 1;
constexpr int UNREACHABLE = -1;
using State = std::array<int, FRONTIER>;

struct Edge {
    int target, mask, weight;
};

struct Layer {
    std::vector<int> previous, masks;
};

struct Sets {
    std::array<int, CELLS> parent;

    Sets() { std::iota(parent.begin(), parent.end(), 0); }

    int root(int v) {
        while (v != parent[v]) {
            parent[v] = parent[parent[v]];
            v = parent[v];
        }
        return v;
    }
};

bool transition(const State &state, int mask, const State &finished, State &result) {
    Sets sets;
    for (int i = 0; i < FRONTIER; ++i) {
        for (int j = 0; j < i; ++j) {
            if (state[i] != 0 && state[i] == state[j]) {
                sets.parent[sets.root(i)] = sets.root(j);
            }
        }
    }
    std::array<bool, CELLS> active{};
    for (int i = 0; i < FRONTIER; ++i) {
        active[i] = state[i] != 0;
    }
    for (int r = 0; r < ROWS; ++r) {
        active[FRONTIER + r] = (mask >> r & 1) != 0;
    }
    for (int r = 0; r < ROWS; ++r) {
        if (!active[FRONTIER + r]) {
            continue;
        }
        for (int c = 0; c < 2; ++c) {
            for (int s = 0; s < ROWS; ++s) {
                int old = c * ROWS + s;
                if (std::abs(r - s) != c + 1 || !active[old]) {
                    continue;
                }
                int a = sets.root(old), b = sets.root(FRONTIER + r);
                if (a == b) {
                    return false;
                }
                sets.parent[a] = b;
            }
        }
    }
    std::array<bool, CELLS> old_roots{}, new_roots{};
    for (int i = 0; i < CELLS; ++i) {
        if (active[i]) {
            (i < ROWS ? old_roots : new_roots)[sets.root(i)] = true;
        }
    }
    bool lost = false;
    for (int i = 0; i < CELLS; ++i) {
        lost = lost || (old_roots[i] && !new_roots[i]);
    }
    if (lost) {
        if (std::count(new_roots.begin(), new_roots.end(), true) == 0 &&
            std::count(old_roots.begin(), old_roots.end(), true) == 1) {
            result = finished;
            return true;
        }
        return false;
    }
    std::array<int, CELLS> labels{};
    int count = 0;
    for (int i = ROWS; i < CELLS; ++i) {
        int label = 0;
        if (active[i]) {
            int root = sets.root(i);
            if (labels[root] == 0) {
                labels[root] = ++count;
            }
            label = labels[root];
        }
        result[i - ROWS] = label;
    }
    return true;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    State empty{}, finished{};
    finished.fill(-1);
    std::vector<State> states{empty, finished};
    std::map<State, int> indices{{empty, 0}, {finished, 1}};
    std::vector<std::vector<Edge>> edges;
    for (int i = 0; i < static_cast<int>(states.size()); ++i) {
        State state = states[i];
        std::vector<Edge> outgoing;
        if (state == finished) {
            outgoing.push_back({i, 0, 0});
        } else {
            for (int mask = 0; mask < MASKS; ++mask) {
                State target{};
                if ((state == empty && mask == 0) || !transition(state, mask, finished, target)) {
                    continue;
                }
                if (indices.count(target) == 0) {
                    indices[target] = static_cast<int>(states.size());
                    states.push_back(target);
                }
                int weight = 0;
                for (int r = 0; r < ROWS; ++r) {
                    weight += mask >> r & 1;
                }
                outgoing.push_back({indices[target], mask, weight});
            }
        }
        edges.push_back(outgoing);
    }
    int size = static_cast<int>(states.size());
    std::vector<int> scores(size, UNREACHABLE);
    scores[0] = 0;
    std::vector<Layer> history;
    bool stable = false;
    while (static_cast<int>(history.size()) < n && !stable) {
        std::vector<int> following(size, UNREACHABLE);
        Layer layer{std::vector<int>(size, UNREACHABLE), std::vector<int>(size)};
        for (int source = 0; source < size; ++source) {
            if (scores[source] == UNREACHABLE) {
                continue;
            }
            for (const Edge &edge : edges[source]) {
                int candidate = scores[source] + edge.weight;
                if (candidate > following[edge.target]) {
                    following[edge.target] = candidate;
                    layer.previous[edge.target] = source;
                    layer.masks[edge.target] = edge.mask;
                }
            }
        }
        // An equal score shift is preserved by every subsequent DP step.
        stable = true;
        for (int i = 0; i < size; ++i) {
            if (!(scores[i] == UNREACHABLE && following[i] == UNREACHABLE) &&
                !(scores[i] != UNREACHABLE && following[i] == scores[i] + GAIN)) {
                stable = false;
            }
        }
        scores = following;
        history.push_back(layer);
    }
    int best = UNREACHABLE, vertex = 0;
    for (int i = 0; i < size; ++i) {
        if ((states[i] == finished || *std::max_element(states[i].begin(), states[i].end()) == 1) &&
            scores[i] > best) {
            best = scores[i];
            vertex = i;
        }
    }
    std::vector<int> board(n);
    for (int column = n - 1; column >= 0; --column) {
        int layer = std::min(column, static_cast<int>(history.size()) - 1);
        board[column] = history[layer].masks[vertex];
        vertex = history[layer].previous[vertex];
    }
    for (int row = 0; row < ROWS; ++row) {
        std::string line;
        line.reserve(2 * n);
        for (int column = 0; column < n; ++column) {
            if (column != 0) {
                line += ' ';
            }
            line += static_cast<char>('0' + (board[column] >> row & 1));
        }
        std::cout << line << '\n';
    }
}
