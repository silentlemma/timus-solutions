#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::pair<int, int>> boxes;  // the first and the last size of every box
    bool ok = true;
    for (int i = 0; i < n; i++) {
        int k, prev = 0, first = 0, value = 0;
        scanf("%d", &k);
        for (int j = 0; j < k; j++) {
            scanf("%d", &value);
            if (j == 0) first = value;
            if (value < prev) ok = false;
            prev = value;
        }
        boxes.push_back({first, value});
    }
    // Sorting by the first size, and then by the last, gives a valid order if any exists.
    std::sort(boxes.begin(), boxes.end());
    for (int i = 1; i < n; i++)
        if (boxes[i - 1].second > boxes[i].first) ok = false;
    puts(ok ? "YES" : "NO");
    return 0;
}
