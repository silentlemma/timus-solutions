#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int keyword_count, rule_count;
    std::cin >> keyword_count >> rule_count;
    const int capacity = keyword_count + 2 * rule_count;
    std::unordered_map<std::string, int> ids;
    std::vector<std::string> words;
    std::vector<std::vector<int>> edges;
    ids.reserve(capacity);
    words.reserve(capacity);
    edges.reserve(capacity);

    auto intern = [&](const std::string &word) {
        auto found = ids.find(word);
        if (found != ids.end()) {
            return found->second;
        }
        int id = static_cast<int>(words.size());
        ids.emplace(word, id);
        words.push_back(word);
        edges.emplace_back();
        return id;
    };

    std::vector<int> required;
    required.reserve(keyword_count);
    std::string first, second;
    for (int i = 0; i < keyword_count; ++i) {
        std::cin >> first;
        required.push_back(intern(first));
    }
    for (int i = 0; i < rule_count; ++i) {
        std::cin >> first >> second;
        int from = intern(first);
        int to = intern(second);
        edges[from].push_back(to);
    }

    std::vector<bool> needed(words.size(), false);
    for (int id : required) {
        needed[id] = true;
    }
    // Only rules reachable from required words matter.
    for (std::size_t i = 0; i < required.size(); ++i) {
        for (int to : edges[required[i]]) {
            if (!needed[to]) {
                needed[to] = true;
                required.push_back(to);
            }
        }
    }

    std::vector<int> indegree(words.size(), 0);
    for (int from : required) {
        for (int to : edges[from]) {
            ++indegree[to];
        }
    }
    auto later = [&](int left, int right) { return words[left] > words[right]; };
    std::priority_queue<int, std::vector<int>, decltype(later)> ready(later);
    for (int id : required) {
        if (indegree[id] == 0) {
            ready.push(id);
        }
    }

    std::vector<int> answer;
    answer.reserve(required.size());
    while (!ready.empty()) {
        int from = ready.top();
        ready.pop();
        answer.push_back(from);
        for (int to : edges[from]) {
            --indegree[to];
            if (indegree[to] == 0) {
                ready.push(to);
            }
        }
    }

    if (answer.size() != required.size()) {
        std::cout << "-1\n";
        return 0;
    }
    for (std::size_t i = 0; i < answer.size(); ++i) {
        if (i != 0) {
            std::cout << ' ';
        }
        std::cout << words[answer[i]];
    }
    std::cout << '\n';
    return 0;
}
