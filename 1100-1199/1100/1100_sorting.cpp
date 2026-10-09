#include <cstdio>
#include <vector>

const int MOST = 100;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // bubble sort never swaps equal scores, so teams with the same score keep
    // their input order: a counting sort by score does the same
    std::vector<std::vector<int>> buckets(MOST + 1);
    for (int i = 0; i < n; i++) {
        int team, solved;
        scanf("%d %d", &team, &solved);
        buckets[solved].push_back(team);
    }
    for (int solved = MOST; solved >= 0; solved--)
        for (int team : buckets[solved])
            printf("%d %d\n", team, solved);
}
