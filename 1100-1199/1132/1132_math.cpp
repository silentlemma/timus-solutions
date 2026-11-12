#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

struct Query {
    int value;
    int prime;
    int index;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count = 0;
    std::cin >> count;
    std::vector<Query> queries(count);
    for (int i = 0; i < count; ++i) {
        std::cin >> queries[i].value >> queries[i].prime;
        queries[i].index = i;
    }
    std::sort(queries.begin(), queries.end(),
              [](const Query &a, const Query &b) { return a.prime < b.prime; });

    std::vector<int> roots;
    std::vector<std::pair<int, int>> answers(count);
    int prime = 0;
    for (const Query &query : queries) {
        if (query.prime != prime) {
            prime = query.prime;
            roots.assign(prime, 0);
            int square = 0;
            for (int x = 1; x <= prime / 2; ++x) {
                // x² differs from (x−1)² by 2x−1.
                square += 2 * x - 1;
                if (square >= prime) {
                    square -= prime;
                }
                roots[square] = x;
            }
        }
        const int x = roots[query.value % prime];
        answers[query.index] = {x, prime - x};
    }

    for (const auto &[first, second] : answers) {
        if (first == 0) {
            std::cout << "No root\n";
        } else {
            std::cout << first;
            if (second != first) {
                std::cout << ' ' << second;
            }
            std::cout << '\n';
        }
    }
}
