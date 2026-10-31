#include <algorithm>
#include <cstdio>
const int MAX_FRIENDS = 100;

const int MONEY = 100;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // the statement limits the input to one hundred friends.
    int bought[MAX_FRIENDS];
    int total = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &bought[i]);
        total += bought[i];
    }
    // everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
    // litre, friend i paid for bought[i] (n + 1) - total litres of others
    int over[MAX_FRIENDS];
    int all = 0;
    for (int i = 0; i < n; i++) {
        over[i] = std::max(0, bought[i] * (n + 1) - total);
        all += over[i];
    }
    for (int i = 0; i < n; i++)
        printf(i ? " %d" : "%d", MONEY * over[i] / all);
    printf("\n");
    return 0;
}
