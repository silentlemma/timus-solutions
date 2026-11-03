#include <array>
#include <cstdio>
#include <string>
#include <vector>

const int TEAM_SIZE = 3, MAX_NAME_LENGTH = 20;
std::vector<unsigned> clash;
int answer;

void search(unsigned mask, int selected) {
    if (selected + __builtin_popcount(mask) <= answer)
        return;
    int chosen = 0, degree = 0;
    for (unsigned remaining = mask; remaining; remaining &= remaining - 1) {
        int i = __builtin_ctz(remaining), count = __builtin_popcount(mask & clash[i]);
        if (count > degree) {
            degree = count;
            chosen = i;
        }
    }
    // An edgeless remainder is taken whole. Otherwise branch on the team
    // with most conflicts, taking it first to improve the pruning bound.
    if (degree <= 1) {
        int value = selected + __builtin_popcount(mask);
        if (value > answer)
            answer = value;
        return;
    }
    search(mask & ~clash[chosen], selected + 1);
    search(mask & ~(1u << chosen), selected);
}

int main() {
    int k;
    scanf("%d", &k);
    std::vector<std::array<std::string, TEAM_SIZE>> teams(k);
    char name[MAX_NAME_LENGTH + 1];
    for (auto &team : teams)
        for (auto &member : team) {
            scanf("%20s", name);
            member = name;
        }
    clash.assign(k, 0);
    for (int i = 0; i < k; i++)
        for (int j = 0; j < k; j++)
            for (const auto &first : teams[i])
                for (const auto &second : teams[j])
                    if (first == second)
                        clash[i] |= 1u << j;
    search((1u << k) - 1, 0);
    printf("%d\n", answer);
}
