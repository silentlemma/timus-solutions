#include <algorithm>
#include <cstdio>
#include <vector>

const int MANY = 2;

int main() {
    int weight, n;
    scanf("%d %d", &weight, &n);
    std::vector<int> cards(n + 1);
    int total = 0;
    for (int i = 1; i <= n; i++) {
        scanf("%d", &cards[i]);
        total += cards[i];
    }
    bool selectMissing = total - weight < weight;
    int target = std::min(weight, total - weight);
    std::vector<unsigned char> ways(target + 1), last(target + 1);
    ways[0] = 1;
    // Complementing a subset preserves uniqueness. Descending sums prevent
    // reusing a card; record its first witness only, so parents never change.
    for (int i = 1; i <= n; i++) {
        for (int sum = target; sum >= cards[i]; sum--) {
            if (ways[sum] == 0 && ways[sum - cards[i]] != 0)
                last[sum] = i;
            ways[sum] = std::min(MANY, ways[sum] + ways[sum - cards[i]]);
        }
        if (ways[target] == MANY) {
            puts("-1");
            return 0;
        }
    }
    if (ways[target] == 0) {
        puts("0");
        return 0;
    }
    std::vector<bool> chosen(n + 1);
    for (int sum = target; sum > 0; sum -= cards[last[sum]])
        chosen[last[sum]] = true;
    bool first = true;
    for (int i = 1; i <= n; i++)
        if (chosen[i] == selectMissing) {
            printf(first ? "%d" : " %d", i);
            first = false;
        }
    puts("");
}
