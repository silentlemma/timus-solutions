#include <algorithm>
#include <cstdio>

constexpr int HEADER_FIELDS = 4;

constexpr int MAX_FRIENDS = 256;
struct Friend {
    int doubled_budget, benefit, id;
};

int main() {
    int budget, alone[2], count;
    if (std::scanf("%d%d%d%d", &budget, &alone[0], &alone[1], &count) != HEADER_FIELDS)
        return 0;
    Friend friends[MAX_FRIENDS];
    int best_suffix[MAX_FRIENDS];
    for (int i = 0; i < count; ++i) {
        auto &candidate = friends[i];
        std::scanf("%d%d", &candidate.doubled_budget, &candidate.benefit);
        candidate.doubled_budget *= 2;
        candidate.id = i + 1;
    }
    std::sort(friends, friends + count,
              [](const Friend &a, const Friend &b) { return a.doubled_budget < b.doubled_budget; });
    int best_friend = -1;
    for (int i = count - 1; i >= 0; --i) {
        if (best_friend < 0 || friends[i].benefit > friends[best_friend].benefit ||
            (friends[i].benefit == friends[best_friend].benefit &&
             friends[i].id < friends[best_friend].id))
            best_friend = i;
        best_suffix[i] = best_friend;
    }

    int apartments;
    std::scanf("%d", &apartments);
    int best = -1, chosen = 0, companion = 0;
    for (int i = 1; i <= apartments; ++i) {
        int rooms, rent, benefit;
        std::scanf("%d%d%d", &rooms, &rent, &benefit);
        if (rent <= budget && benefit + alone[rooms - 1] > best) {
            best = benefit + alone[rooms - 1];
            chosen = i;
            companion = 0;
        }
        if (rooms == 2 && rent <= 2 * budget) {
            auto first = std::lower_bound(friends, friends + count, rent,
                                          [](const Friend &candidate, int value) {
                                              return candidate.doubled_budget < value;
                                          });
            if (first != friends + count) {
                const auto &candidate = friends[best_suffix[first - friends]];
                if (benefit + candidate.benefit > best) {
                    best = benefit + candidate.benefit;
                    chosen = i;
                    companion = candidate.id;
                }
            }
        }
    }
    if (!chosen)
        std::puts("Forget about apartments. Live in the dormitory.");
    else if (!companion)
        std::printf("You should rent the apartment #%d alone.\n", chosen);
    else
        std::printf("You should rent the apartment #%d with the friend #%d.\n", chosen, companion);
}
