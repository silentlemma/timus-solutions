#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

constexpr int MOD = 998244353;
constexpr int ROOT = 3;
constexpr int DIRECT_LIMIT = 32;

int power(int base, int exponent) {
    int result = 1;
    while (exponent) {
        if (exponent & 1)
            result = static_cast<int>(int64_t(result) * base % MOD);
        base = static_cast<int>(int64_t(base) * base % MOD);
        exponent >>= 1;
    }
    return result;
}

void transform(std::vector<int> &data, bool inverse) {
    int n = static_cast<int>(data.size());
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j)
            std::swap(data[i], data[j]);
    }
    for (int length = 2; length <= n; length <<= 1) {
        int root = power(ROOT, (MOD - 1) / length);
        if (inverse)
            root = power(root, MOD - 2);
        for (int start = 0; start < n; start += length) {
            int factor = 1;
            for (int j = 0; j < length / 2; ++j) {
                int first = data[start + j];
                int second = static_cast<int>(int64_t(data[start + j + length / 2]) * factor % MOD);
                int sum = first + second;
                if (sum >= MOD)
                    sum -= MOD;
                int difference = first - second;
                if (difference < 0)
                    difference += MOD;
                data[start + j] = sum;
                data[start + j + length / 2] = difference;
                factor = static_cast<int>(int64_t(factor) * root % MOD);
            }
        }
    }
    if (inverse) {
        int scale = power(n, MOD - 2);
        for (int &value : data)
            value = static_cast<int>(int64_t(value) * scale % MOD);
    }
}

std::vector<int> matches(const std::vector<int> &a, const std::vector<int> &b) {
    int n = static_cast<int>(a.size()), m = static_cast<int>(b.size());
    std::vector<int> prefix(m), starts;
    for (int i = 1, j = 0; i < m; ++i) {
        while (j && (b[i] >> 1) != (b[j] >> 1))
            j = prefix[j - 1];
        if ((b[i] >> 1) == (b[j] >> 1))
            ++j;
        prefix[i] = j;
    }
    for (int i = 0, j = 0; i < n; ++i) {
        while (j && (a[i] >> 1) != (b[j] >> 1))
            j = prefix[j - 1];
        if ((a[i] >> 1) == (b[j] >> 1))
            ++j;
        if (j == m) {
            starts.push_back(i - m + 1);
            j = prefix[j - 1];
        }
    }
    return starts;
}

std::pair<int, int> solve(const std::vector<int> &a, const std::vector<int> &b) {
    int n = static_cast<int>(a.size()), m = static_cast<int>(b.size());
    if (m > n)
        return {-1, -1};
    std::vector<int> starts = matches(a, b);
    if (starts.empty())
        return {-1, -1};
    int best = m + 1, answer = -1;
    if (static_cast<int>(starts.size()) <= DIRECT_LIMIT) {
        for (int start : starts) {
            int changes = 0;
            for (int j = 0; j < m; ++j)
                changes += (a[start + j] ^ b[j]) & 1;
            if (changes < best) {
                best = changes;
                answer = start + 1;
            }
        }
        return {best, answer};
    }
    int size = 1;
    while (size < n + m - 1)
        size <<= 1;
    std::vector<int> first(size), second(size), prefix(n + 1);
    for (int i = 0; i < n; ++i) {
        first[i] = a[i] & 1;
        prefix[i + 1] = prefix[i] + first[i];
    }
    int ones = 0;
    for (int i = 0; i < m; ++i) {
        second[m - 1 - i] = b[i] & 1;
        ones += b[i] & 1;
    }
    transform(first, false);
    transform(second, false);
    for (int i = 0; i < size; ++i)
        first[i] = static_cast<int>(int64_t(first[i]) * second[i] % MOD);
    transform(first, true);
    for (int start : starts) {
        int changes = prefix[start + m] - prefix[start] + ones - 2 * first[start + m - 1];
        if (changes < best) {
            best = changes;
            answer = start + 1;
        }
    }
    return {best, answer};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m;
    std::cin >> n >> m;
    std::vector<int> a(n), b(m);
    std::string token;
    for (int &value : a) {
        std::cin >> token;
        value = std::stoi(token, nullptr, 2);
    }
    for (int &value : b) {
        std::cin >> token;
        value = std::stoi(token, nullptr, 2);
    }
    auto result = solve(a, b);
    if (result.first < 0)
        std::cout << "No\n";
    else
        std::cout << "Yes\n" << result.first << ' ' << result.second << '\n';
}
