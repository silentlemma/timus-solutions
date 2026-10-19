#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>

std::vector<int> order(const std::vector<int> &scores) {
    std::vector<int> ids(scores.size());
    std::iota(ids.begin(), ids.end(), 0);
    std::sort(ids.begin(), ids.end(),
              [&](int a, int b) { return std::tie(scores[a], a) < std::tie(scores[b], b); });
    return ids;
}

std::vector<std::array<int, 2>> solve(const std::vector<int> &first,
                                      const std::vector<int> &second) {
    auto a = order(first), b = order(second);
    int total_a = std::accumulate(first.begin(), first.end(), 0);
    int total_b = std::accumulate(second.begin(), second.end(), 0);
    if (total_a > total_b)
        std::reverse(b.begin(), b.end());
    else if (total_a < total_b)
        std::reverse(a.begin(), a.end());
    std::vector<std::array<int, 2>> answer;
    for (std::size_t i = 0; i < a.size(); ++i)
        answer.push_back({a[i], b[i]});
    return answer;
}

void run(std::istream &in, std::ostream &out) {
    int n;
    in >> n;
    std::vector<int> first(n), second(n);
    for (int &value : first)
        in >> value;
    for (int &value : second)
        in >> value;
    for (const auto &row : solve(first, second))
        out << row[0] + 1 << ' ' << row[1] + 1 << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    run(std::cin, std::cout);
    return 0;
}
