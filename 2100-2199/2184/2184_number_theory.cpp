#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using Integer = long long;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<Integer> coins(n);
    Integer total = 0;
    for (Integer &value : coins) {
        std::cin >> value;
        total += value;
    }

    // The first and last nonmultiples must change these GCDs.
    std::vector<bool> marked(n, false);
    Integer current = total;
    for (int i = 0; i < n; ++i) {
        Integer next = std::gcd(current, coins[i]);
        if (next != current) {
            marked[i] = true;
            current = next;
        }
    }
    current = total;
    for (int i = n - 1; i >= 0; --i) {
        Integer next = std::gcd(current, coins[i]);
        if (next != current) {
            marked[i] = true;
            current = next;
        }
    }

    Integer fixed = total;
    std::vector<Integer> critical;
    for (int i = 0; i < n; ++i) {
        if (marked[i]) {
            critical.push_back(coins[i]);
        } else {
            fixed = std::gcd(fixed, coins[i]);
        }
    }

    int count = static_cast<int>(critical.size());
    std::vector<Integer> suffix(count + 1, fixed);
    for (int i = count - 1; i >= 0; --i) {
        suffix[i] = std::gcd(critical[i], suffix[i + 1]);
    }

    Integer answer = suffix[0];
    Integer before = fixed;
    for (int first = 0; first < count; ++first) {
        current = before;
        for (int second = first + 1; second < count; ++second) {
            answer = std::max(answer, std::gcd(current, suffix[second + 1]));
            current = std::gcd(current, critical[second]);
        }
        before = std::gcd(before, critical[first]);
    }
    std::cout << answer << '\n';
}
