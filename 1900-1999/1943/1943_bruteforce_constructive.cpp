#include <algorithm>
#include <deque>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

constexpr int LOCAL_LIMIT = 5;

bool wins(std::deque<int> first, std::deque<int> second) {
    std::set<std::pair<std::deque<int>, std::deque<int>>> seen;
    while (!first.empty() && !second.empty()) {
        if (!seen.emplace(first, second).second)
            return false;
        const int x = first.front(), y = second.front();
        first.pop_front();
        second.pop_front();
        if (x > y) {
            first.push_back(y);
            first.push_back(x);
        } else if (y > x) {
            second.push_back(x);
            second.push_back(y);
        }
    }
    return !first.empty();
}

std::vector<int> construct(const std::vector<int> &opponent) {
    const int size = std::min(static_cast<int>(opponent.size()), LOCAL_LIMIT);
    std::vector<int> candidate(opponent.begin(), opponent.begin() + size);
    const std::deque<int> local(candidate.begin(), candidate.end());
    std::sort(candidate.begin(), candidate.end());
    do {
        if (wins(std::deque<int>(candidate.begin(), candidate.end()), local)) {
            auto answer = opponent;
            std::copy(candidate.begin(), candidate.end(), answer.begin());
            return answer;
        }
    } while (std::next_permutation(candidate.begin(), candidate.end()));
    return {};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::cin >> size;
    std::vector<int> opponent(size);
    for (int &card : opponent)
        std::cin >> card;
    const auto answer = construct(opponent);
    if (answer.empty())
        std::cout << "NO\n";
    else {
        std::cout << "YES\n";
        for (int index = 0; index < size; ++index) {
            if (index != 0)
                std::cout << ' ';
            std::cout << answer[index];
        }
        std::cout << '\n';
    }
    return 0;
}
