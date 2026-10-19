#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

constexpr int WORD_BITS = 64;
using Matrix = std::vector<std::vector<uint64_t>>;
using Matching = std::pair<std::vector<int>, std::vector<int>>;
Matching maximum_matching(const Matrix &rows, int m) {
    int n = static_cast<int>(rows.size()), words = (m + WORD_BITS - 1) / WORD_BITS, remaining = m;
    std::vector<int> left(n, -1), right(m, -1);
    std::vector<uint64_t> free(words, ~uint64_t(0));
    if (m % WORD_BITS)
        free.back() = (uint64_t(1) << (m % WORD_BITS)) - 1;
    for (int start = 0; start < n && remaining; ++start) {
        int direct = -1;
        for (int w = 0; w < words; ++w) {
            uint64_t mask = rows[start][w] & free[w];
            if (mask) {
                direct = w * WORD_BITS + __builtin_ctzll(mask);
                break;
            }
        }
        if (direct >= 0) {
            left[start] = direct;
            right[direct] = start;
            free[direct / WORD_BITS] &= ~(uint64_t(1) << (direct % WORD_BITS));
            --remaining;
            continue;
        }
        std::vector<int> queue{start}, parent(m, -1);
        std::vector<uint64_t> seen(words, 0);
        int finish = -1;
        for (size_t at = 0; at < queue.size() && finish < 0; ++at) {
            int u = queue[at];
            for (int w = 0; w < words && finish < 0; ++w) {
                uint64_t mask = rows[u][w] & ~seen[w];
                while (mask) {
                    uint64_t bit = mask & (~mask + 1);
                    mask &= mask - 1;
                    seen[w] |= bit;
                    int v = w * WORD_BITS + __builtin_ctzll(bit);
                    parent[v] = u;
                    if (right[v] < 0) {
                        finish = v;
                        break;
                    }
                    queue.push_back(right[v]);
                }
            }
        }
        if (finish >= 0) {
            free[finish / WORD_BITS] &= ~(uint64_t(1) << (finish % WORD_BITS));
            --remaining;
            while (finish >= 0) {
                int u = parent[finish], old = left[u];
                left[u] = finish;
                right[finish] = u;
                finish = old;
            }
        }
    }
    return {left, right};
}
struct Reach {
    std::vector<char> own, other;
};
Reach reach(const Matrix &rows, const std::vector<int> &opposite,
            const std::vector<int> &own_match) {
    Reach result{std::vector<char>(rows.size(), 0), std::vector<char>(opposite.size(), 0)};
    std::vector<int> queue;
    int words = (static_cast<int>(opposite.size()) + WORD_BITS - 1) / WORD_BITS;
    std::vector<uint64_t> seen(words, 0);
    for (size_t u = 0; u < own_match.size(); ++u)
        if (own_match[u] < 0) {
            result.own[u] = 1;
            queue.push_back(static_cast<int>(u));
        }
    for (size_t at = 0; at < queue.size(); ++at) {
        int u = queue[at];
        for (int w = 0; w < words; ++w) {
            uint64_t mask = rows[u][w] & ~seen[w];
            while (mask) {
                uint64_t bit = mask & (~mask + 1);
                mask &= mask - 1;
                seen[w] |= bit;
                int v = w * WORD_BITS + __builtin_ctzll(bit), partner = opposite[v];
                result.other[v] = 1;
                if (partner >= 0 && !result.own[partner]) {
                    result.own[partner] = 1;
                    queue.push_back(partner);
                }
            }
        }
    }
    return result;
}
std::pair<std::string, std::string> solve(const Matrix &rows, const Matrix &reverse) {
    auto match = maximum_matching(rows, static_cast<int>(reverse.size()));
    auto forward = reach(rows, match.second, match.first);
    auto backward = reach(reverse, match.first, match.second);
    std::string a(rows.size(), 'E'), b(reverse.size(), 'E');
    for (size_t u = 0; u < a.size(); ++u)
        if (forward.own[u])
            a[u] = 'N';
        else if (backward.other[u])
            a[u] = 'A';
    for (size_t v = 0; v < b.size(); ++v)
        if (backward.own[v])
            b[v] = 'N';
        else if (forward.other[v])
            b[v] = 'A';
    return {a, b};
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m, k;
    if (!(std::cin >> n >> m >> k))
        return 0;
    Matrix rows(n, std::vector<uint64_t>((m + WORD_BITS - 1) / WORD_BITS));
    Matrix reverse(m, std::vector<uint64_t>((n + WORD_BITS - 1) / WORD_BITS));
    for (int i = 0; i < k; ++i) {
        int u, v;
        std::cin >> u >> v;
        --u;
        --v;
        rows[u][v / WORD_BITS] |= uint64_t(1) << (v % WORD_BITS);
        reverse[v][u / WORD_BITS] |= uint64_t(1) << (u % WORD_BITS);
    }
    auto answer = solve(rows, reverse);
    std::cout << answer.first << '\n' << answer.second << '\n';
}
