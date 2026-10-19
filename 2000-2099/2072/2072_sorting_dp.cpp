#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<pair<int, int>> flowers(n);  // dryness and position
    for (int i = 0; i < n; i++) {
        scanf("%d", &flowers[i].first);
        flowers[i].second = i;
    }
    sort(flowers.begin(), flowers.end());
    // a group of equal dryness is a segment of positions, watered by walking it once.
    // The walk ends at its left or right end, and those two states carry over
    long long atLeft = 0, atRight = 0;
    int left = 0, right = 0;  // the previous group, starting from the leftmost flower
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && flowers[j].first == flowers[i].first) j++;
        int l = flowers[i].second, r = flowers[j - 1].second, width = r - l;
        long long toLeft = min(atLeft + abs(left - r), atRight + abs(right - r)) + width;
        long long toRight = min(atLeft + abs(left - l), atRight + abs(right - l)) + width;
        atLeft = toLeft, atRight = toRight, left = l, right = r;
        i = j;
    }
    printf("%lld\n", min(atLeft, atRight) + n);
}
