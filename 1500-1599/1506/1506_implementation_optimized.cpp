#include <cstdio>

constexpr int MAX_NUMBERS = 100;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    // the statement limits the list to 100 numbers; no heap allocation is needed.
    int nums[MAX_NUMBERS];
    for (int i = 0; i < n; i++)
        scanf("%d", &nums[i]);
    int height = (n + k - 1) / k; // the fewest rows that hold n numbers in k columns
    for (int row = 0; row < height; row++) {
        // column c holds the numbers c * height ... c * height + height - 1
        for (int c = 0; c < k && c * height + row < n; c++)
            printf("%4d", nums[c * height + row]);
        printf("\n");
    }
}
