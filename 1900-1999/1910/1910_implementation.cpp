#include <cstdio>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> a(n);
    for (int &x : a)
        scanf("%d", &x);
    // try every section as the middle of the three
    int best = 0, middle = 0;
    for (int i = 1; i + 1 < n; i++) {
        int sum = a[i - 1] + a[i] + a[i + 1];
        if (sum > best) {
            best = sum;
            middle = i;
        }
    }
    printf("%d %d\n", best, middle + 1);
}
