#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

constexpr int MAX_LINE = 250;

std::vector<std::string> tokens(const std::string &line, size_t position = 0) {
    std::vector<std::string> words;
    while (position < line.size()) {
        while (position < line.size() && line[position] <= ' ')
            ++position;
        size_t start = position;
        while (position < line.size() && line[position] > ' ')
            ++position;
        if (start != position)
            words.push_back(line.substr(start, position - start));
    }
    return words;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::string line;
    std::getline(std::cin, line);
    std::unordered_map<std::string, std::vector<uint32_t>> known;
    std::unordered_map<std::string, uint32_t> ids;
    std::vector<std::string> names;
    known.reserve(n);
    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, line);
        size_t colon = line.find(':');
        auto &list = known[line.substr(0, colon)];
        for (const auto &word : tokens(line, colon + 1)) {
            auto found = ids.find(word);
            if (found == ids.end()) {
                uint32_t id = names.size();
                names.push_back(word);
                found = ids.emplace(word, id).first;
            }
            list.push_back(found->second);
        }
        std::sort(list.begin(), list.end());
        list.erase(std::unique(list.begin(), list.end()), list.end());
    }
    int m;
    std::cin >> m;
    std::getline(std::cin, line);
    std::vector<uint32_t> common;
    common.reserve(MAX_LINE / 2);
    for (int query = 0; query < m; ++query) {
        std::getline(std::cin, line);
        auto group = tokens(line);
        const auto *seed = &known.at(group[0]);
        for (const auto &name : group) {
            const auto &list = known.at(name);
            if (list.size() < seed->size())
                seed = &list;
        }
        common.assign(seed->begin(), seed->end());
        for (const auto &name : group) {
            if (common.empty())
                break;
            const auto &other = known.at(name);
            size_t left = 0, right = 0, used = 0;
            while (left < common.size() && right < other.size()) {
                if (common[left] < other[right])
                    ++left;
                else if (other[right] < common[left])
                    ++right;
                else {
                    common[used++] = common[left++];
                    ++right;
                }
            }
            common.resize(used);
        }
        if (common.empty()) {
            std::cout << "No solution.\n";
            continue;
        }
        std::sort(common.begin(), common.end(),
                  [&](uint32_t a, uint32_t b) { return names[a] < names[b]; });
        bool first = true;
        for (uint32_t id : common) {
            if (!first)
                std::cout << ' ';
            std::cout << names[id];
            first = false;
        }
        std::cout << '\n';
    }
}
