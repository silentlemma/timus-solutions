#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> spell[2];
    spell[0].resize(n);
    spell[1].resize(n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &spell[0][i], &spell[1][i]);
        spell[0][i]--;
        spell[1][i]--;
    }
    // the army gathers exactly when every pair of garrisons can be forced
    // together, one pair after another; a pair (u, v), u < v, is the number
    // u * n + v, and a day is her spell m, then his spell k
    int size = n * n;
    std::vector<unsigned char> openMoves(2 * size, 0);  // his replies keeping the pair apart
    std::vector<int> target, source;  // pair after both spells, pair * 2 + her spell
    for (int u = 0; u < n; u++) {
        for (int v = u + 1; v < n; v++) {
            int p = u * n + v;
            for (int mine = 0; mine < 2; mine++) {
                int x = spell[mine][u], y = spell[mine][v];
                if (x == y) continue;
                for (int k = 0; k < 2; k++) {
                    int s = spell[k][x], t = spell[k][y];
                    if (s == t) continue;
                    target.push_back(s < t ? s * n + t : t * n + s);
                    source.push_back(2 * p + mine);
                    openMoves[2 * p + mine]++;
                }
            }
        }
    }
    // the replies that lead into every pair, grouped by that pair
    std::vector<int> start(size + 1, 0);
    for (int q : target) start[q + 1]++;
    for (int q = 0; q < size; q++) start[q + 1] += start[q];
    std::vector<int> place(start.begin(), start.end() - 1), from(target.size());
    for (size_t i = 0; i < target.size(); i++) from[place[target[i]]++] = source[i];
    // a pair is won when some spell of hers leaves him no reply that keeps
    // the pair apart outside the won pairs
    std::vector<char> won(size, 0);
    std::vector<int> queue;
    for (int u = 0; u < n; u++) {
        for (int v = u + 1; v < n; v++) {
            int p = u * n + v;
            if (!openMoves[2 * p] || !openMoves[2 * p + 1]) {
                won[p] = 1;
                queue.push_back(p);
            }
        }
    }
    for (size_t h = 0; h < queue.size(); h++) {
        int q = queue[h];
        for (int e = start[q]; e < start[q + 1]; e++) {
            int move = from[e], p = move >> 1;
            if (won[p]) continue;
            if (--openMoves[move] == 0) {
                won[p] = 1;
                queue.push_back(p);
            }
        }
    }
    puts((long long)queue.size() == (long long)n * (n - 1) / 2 ? "War" : "Peace");
    return 0;
}
