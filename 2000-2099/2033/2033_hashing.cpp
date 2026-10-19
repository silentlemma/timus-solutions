#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

constexpr int RECORDS = 6;

struct Record {
    std::string model;
    int price;
};

std::string solve(const std::vector<Record> &records) {
    std::unordered_map<std::string, std::pair<int, int>> groups;
    for (const auto &record : records) {
        auto &stats = groups[record.model];
        if (stats.first == 0 || record.price < stats.second)
            stats.second = record.price;
        ++stats.first;
    }
    std::string answer;
    int best_count = -1, best_price = 0;
    for (const auto &entry : groups) {
        int count = entry.second.first, price = entry.second.second;
        if (count > best_count || (count == best_count && price < best_price) ||
            (count == best_count && price == best_price && entry.first < answer)) {
            answer = entry.first;
            best_count = count;
            best_price = price;
        }
    }
    return answer;
}

int main() {
    std::vector<Record> records;
    for (int i = 0; i < RECORDS; ++i) {
        std::string name, model;
        int price;
        if (!(std::cin >> name >> model >> price))
            return 0;
        records.push_back({model, price});
    }
    std::cout << solve(records) << '\n';
}
