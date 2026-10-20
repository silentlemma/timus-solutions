#include <algorithm>
#include <iostream>

int main() {
    constexpr long long MIN_DISTINCT_SUM = 3;
    long long smaller, larger;
    std::cin >> smaller >> larger;
    if (smaller > larger) {
        std::swap(smaller, larger);
    }

    const long long difference = larger - smaller;
    long long answer;
    if (difference == 0) {
        answer = 2;
    } else if (difference == 1) {
        answer = larger - 1;
    } else if (difference == 2) {
        answer = larger % 2 == 0 ? larger / 2 : larger - 1;
    } else {
        // Each component pairs residues; the smallest distinct positive residues sum to three.
        answer = 2 * ((larger - MIN_DISTINCT_SUM) / difference + 1);
    }
    std::cout << answer << '\n';
}
