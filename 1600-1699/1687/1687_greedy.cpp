#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    std::vector<std::vector<int>> boxes(k);
    for (auto& box : boxes) {
        int size;
        scanf("%d", &size);
        box.resize(size);
        for (int& c : box) {
            scanf("%d", &c);
        }
    }
    int m;
    scanf("%d", &m);
    std::vector<bool> wanted(n + 1, false);
    for (int i = 0; i < m; i++) {
        int c;
        scanf("%d", &c);
        wanted[c] = true;
    }
    std::vector<int> useful;
    std::set<int> coverable;
    for (int i = 0; i < k; i++) {
        bool any = false;
        for (int c : boxes[i]) {
            if (wanted[c]) {
                any = true;
                coverable.insert(c);
            }
        }
        if (any) {
            useful.push_back(i);
        }
    }
    // no set of boxes is worth more than all coverable coins, nor holds more
    // than all useful boxes; one box per coverable coin reaches every coin,
    // so the answer is min(useful, coverable): those boxes, then any others
    std::vector<bool> chosen(k, false), covered(n + 1, false);
    size_t count = 0;
    for (int coin : coverable) {
        for (int i : useful) {
            if (covered[coin]) {
                break;
            }
            if (std::find(boxes[i].begin(), boxes[i].end(), coin) != boxes[i].end()) {
                chosen[i] = true;
                count++;
                for (int c : boxes[i]) {
                    covered[c] = true;
                }
            }
        }
    }
    for (int i : useful) {
        if (count < coverable.size() && !chosen[i]) {
            chosen[i] = true;
            count++;
        }
    }
    printf("%d\n", (int)count);
    bool first = true;
    for (int i = 0; i < k; i++) {
        if (chosen[i]) {
            printf(first ? "%d" : " %d", i + 1);
            first = false;
        }
    }
    printf("\n");
}
