#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    std::vector<int> a(n);
    for (int &x : a)
        if (scanf("%d", &x) != 1)
            return 1;
    // n + 1 prefix sums modulo n take at most n values: two of them are
    // equal, and the numbers between them sum to a multiple of n
    std::vector<int> first(n, -1);
    first[0] = 0;
    for (int i = 1, sum = 0; i <= n; i++) {
        sum = (sum + a[i - 1]) % n;
        if (first[sum] >= 0) {
            std::string out = std::to_string(i - first[sum]) + "\n";
            for (int j = first[sum]; j < i; j++)
                out += std::to_string(a[j]) + "\n";
            fputs(out.c_str(), stdout);
            return 0;
        }
        first[sum] = i;
    }
}
