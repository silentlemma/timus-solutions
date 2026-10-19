#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int MAX_TERM = 300;
constexpr int BLOCK_SIZE = 1 << 16;
constexpr int RING_SIZE = MAX_TERM + 1;

std::vector<int> primes_up_to(int bound) {
    std::vector<bool> composite(bound + 1);
    std::vector<int> primes;
    for (int p = 2; p <= bound; ++p)
        if (!composite[p]) {
            primes.push_back(p);
            for (int multiple = p * p; multiple <= bound; multiple += p)
                composite[multiple] = true;
        }
    return primes;
}

std::vector<std::uint16_t> divisor_block(int left, int right, const std::vector<int> &primes) {
    int size = right - left + 1;
    std::vector<int> remaining(size);
    std::vector<std::uint16_t> counts(size, 1);
    for (int i = 0; i < size; ++i)
        remaining[i] = left + i;
    for (int p : primes) {
        if (p * p > right)
            break;
        for (int offset = (p - left % p) % p; offset < size; offset += p) {
            int exponent = 0;
            while (remaining[offset] % p == 0) {
                remaining[offset] /= p;
                ++exponent;
            }
            counts[offset] *= exponent + 1;
        }
    }
    for (int i = 0; i < size; ++i)
        if (remaining[i] > 1)
            counts[i] *= 2;
    return counts;
}

std::vector<int> solve(int n) {
    int limit = MAX_TERM * n, root = 1;
    while ((root + 1) * (root + 1) <= limit)
        ++root;
    auto primes = primes_up_to(root);
    std::vector<std::uint16_t> history;
    std::vector<int> depth(RING_SIZE);
    for (int left = 1; left <= limit; left += BLOCK_SIZE) {
        int right = std::min(limit, left + BLOCK_SIZE - 1);
        auto counts = divisor_block(left, right, primes);
        for (int offset = 0; offset < static_cast<int>(counts.size()); ++offset) {
            int total = left + offset, term = counts[offset];
            history.push_back(counts[offset]);
            int current = total <= MAX_TERM ? 1 : 0;
            if (term <= MAX_TERM && total > term) {
                int previous = depth[(total - term) % RING_SIZE];
                if (previous > 0)
                    current = std::max(current, previous + 1);
            }
            depth[total % RING_SIZE] = current;
            if (current >= n) {
                std::vector<int> answer(n);
                for (int i = n - 1; i > 0; --i) {
                    answer[i] = history[total - 1];
                    total -= answer[i];
                }
                answer[0] = total;
                return answer;
            }
        }
    }
    return {};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    auto answer = solve(n);
    if (answer.empty())
        std::cout << "Impossible\n";
    else
        for (int i = 0; i < n; ++i)
            std::cout << answer[i] << (i + 1 == n ? '\n' : ' ');
}
