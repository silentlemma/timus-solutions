#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> nums(n);
    for (int &x : nums)
        scanf("%d", &x);
    int height = (n + k - 1) / k; // the fewest rows that hold n numbers in k columns
    for (int row = 0; row < height; row++) {
        // column c holds the numbers c * height ... c * height + height - 1
        for (int c = 0; c < k && c * height + row < n; c++)
            printf("%4d", nums[c * height + row]);
        printf("\n");
    }
}
