#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

constexpr size_t SWAPPED = 2;  // a single swap changes exactly two places

int main() {
    int n;
    scanf("%d", &n);
    vector<long long> a(n);
    for (auto& x : a) scanf("%lld", &x);
    vector<long long> ascending = a;
    sort(ascending.begin(), ascending.end());
    vector<long long> descending(ascending.rbegin(), ascending.rend());
    if (a == ascending || a == descending) {
        puts("Nothing to do here");
        return 0;
    }
    // one swap can only fix a line that differs from a sorted one in exactly
    // two places, and then the swap of those two places does it
    for (const auto* t : {&ascending, &descending}) {
        vector<int> wrong;
        for (int i = 0; i < n && wrong.size() <= SWAPPED; i++)
            if (a[i] != (*t)[i]) wrong.push_back(i);
        if (wrong.size() != SWAPPED) continue;
        int i = wrong[0], j = wrong[1];
        if (a[i] == (*t)[j] && a[j] == (*t)[i]) {
            printf("Yes\n%d %d\n", i + 1, j + 1);
            return 0;
        }
    }
    puts("No hope");
}
