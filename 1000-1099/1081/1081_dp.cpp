#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n;
    long long k;
    if (scanf("%d %lld", &n, &k) != 2)
        return 0;
    // count[r]: strings of length r without two adjacent ones (Fibonacci)
    std::vector<long long> count{1, 2};
    while ((int)count.size() <= n)
        count.push_back(count[count.size() - 1] + count[count.size() - 2]);
    if (k > count[n]) {
        puts("-1");
        return 0;
    }
    std::string out;
    for (int pos = 0; pos < n; pos++) {
        int rest = n - pos - 1;
        // strings with 0 here come first; a 1 is only possible after a 0
        if ((!out.empty() && out.back() == '1') || k <= count[rest]) {
            out += '0';
        } else {
            k -= count[rest];
            out += '1';
        }
    }
    puts(out.c_str());
}
