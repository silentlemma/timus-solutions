#include <cstdio>
#include <string>
#include <utility>
#include <vector>

using Runs = std::vector<std::pair<int, int>>;

// cut the values 1 .. n greedily into runs of consecutive values whose
// positions alternately rise and fall, the first one as asked
Runs blocks(const std::vector<int> &pos, int n, bool rising) {
    Runs cuts;
    for (int v = 1; v <= n; rising = !rising) {
        int w = v;
        while (w < n && (pos[w + 1] > pos[w]) == rising) w++;
        cuts.push_back({v, w});
        v = w + 1;
    }
    return cuts;
}

// the least k with 2^k >= count
int passes(int count) {
    int k = 0;
    while ((1 << k) < count) k++;
    return k;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> cars(n), pos(n + 1);
    for (int i = 0; i < n; i++) {
        scanf("%d", &cars[i]);
        pos[cars[i]] = i;
    }
    // one pass keeps a chosen set of cars in order and appends the others
    // reversed; over k passes cars end up ordered by their codes of choices
    // in reflected Gray order, reversed once per one in the code
    Runs rising = blocks(pos, n, true), falling = blocks(pos, n, false);
    bool fromRising = passes(rising.size()) <= passes(falling.size() + 1);
    const Runs &runs = fromRising ? rising : falling;
    int first = fromRising ? 0 : 1;
    int k = passes(runs.size() + first);
    std::vector<int> code(n + 1);
    for (size_t i = 0; i < runs.size(); i++) {
        int rank = i + first;
        for (int v = runs[i].first; v <= runs[i].second; v++) code[v] = rank ^ (rank >> 1);
    }
    std::string out = std::to_string(k) + "\n";
    for (int bit = 0; bit < k; bit++) {
        std::vector<int> next;
        for (int v : cars) {
            if (!(code[v] >> bit & 1)) next.push_back(v);
        }
        for (int i = n - 1; i >= 0; i--) {
            if (code[cars[i]] >> bit & 1) next.push_back(cars[i]);
        }
        cars = next;
        for (int i = 0; i < n; i++) out += std::to_string(cars[i]) + (i + 1 < n ? " " : "\n");
    }
    fputs(out.c_str(), stdout);
    return 0;
}
