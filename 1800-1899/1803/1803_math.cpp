#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const int LIMB_LIMIT = 1000000;

int main() {
    int k, n;
    if (!(std::cin >> k >> n)) return 0;
    // the numbers are kept in limbs of base k^m, the largest power of k up
    // to a million, and digitSum[v] is the sum of the base-k digits of a limb
    int base = 1;
    while (base <= LIMB_LIMIT / k) base *= k;
    std::vector<int> digitSum(base, 0);
    for (int v = 1; v < base; v++) digitSum[v] = digitSum[v / k] + v % k;

    std::vector<int> cost(n, 1);
    std::vector<int> a = {1}, b = {1};
    for (int i = 2; i < n; i++) {
        // a, b = b, a + b, summing the digits on the way
        int sum = 0, carry = 0;
        a.resize(b.size(), 0);
        for (size_t j = 0; j < b.size(); j++) {
            int v = a[j] + b[j] + carry;
            carry = v >= base;
            if (carry) v -= base;
            a[j] = v;
            sum += digitSum[v];
        }
        if (carry) {
            a.push_back(1);
            sum += 1;
        }
        std::swap(a, b);
        cost[i] = sum;
    }
    std::vector<int> order(n);
    for (int i = 0; i < n; i++) order[i] = i;
    std::stable_sort(order.begin(), order.end(), [&](int x, int y) { return cost[x] < cost[y]; });
    std::string out;
    for (int i = 0; i < n; i++) {
        if (i > 0) out += ' ';
        out += std::to_string(order[i] + 1);
    }
    std::cout << out << "\n";
    return 0;
}
