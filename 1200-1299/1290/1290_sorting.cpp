#include <cstdio>
#include <vector>

const int LARGEST = 25000;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // counting each value is a sort in descending order, and printing the
    // conjugate partition twice gives back the sorted array
    std::vector<int> count(LARGEST + 1, 0);
    for (int i = 0; i < n; i++) {
        int p = 0;
        if (scanf("%d", &p) != 1)
            return 0;
        count[p]++;
    }
    for (int value = LARGEST; value >= 1; value--) {
        for (int k = 0; k < count[value]; k++)
            printf("%d\n", value);
    }
    return 0;
}
