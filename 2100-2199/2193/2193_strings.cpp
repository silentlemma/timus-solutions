#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

// A score is at least one half; eighteen mismatches cannot improve it.
constexpr int SCORE_BITS = 18;
constexpr std::int64_t SCORE_SCALE = std::int64_t{1} << SCORE_BITS;
constexpr int DECIMAL_BASE = 10;
constexpr int HALF_BASE = DECIMAL_BASE / 2;

struct Query {
    int first;
    int second;
    int cut;
    int index;
};

std::string format_score(std::int64_t score) {
    std::string result = std::to_string(score / SCORE_SCALE);
    std::int64_t fraction = score % SCORE_SCALE;
    if (fraction != 0) {
        for (int digit = 0; digit < SCORE_BITS; ++digit) {
            fraction *= HALF_BASE;
        }
        std::string tail = std::to_string(fraction);
        tail.insert(0, SCORE_BITS - tail.size(), '0');
        while (tail.back() == '0') {
            tail.pop_back();
        }
        result += "." + tail;
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int word_count;
    int query_count;
    std::cin >> word_count >> query_count;
    std::vector<std::string> words(word_count);
    for (std::string &word : words) {
        std::cin >> word;
        std::reverse(word.begin(), word.end());
    }
    std::vector<Query> queries(query_count);
    for (int i = 0; i < query_count; ++i) {
        Query &query = queries[i];
        std::cin >> query.first >> query.second >> query.cut;
        --query.first;
        --query.second;
        if (query.first > query.second) {
            std::swap(query.first, query.second);
        }
        query.index = i;
    }
    std::sort(queries.begin(), queries.end(), [](const Query &left, const Query &right) {
        if (left.first != right.first) {
            return left.first < right.first;
        }
        return left.second < right.second;
    });

    std::vector<std::int64_t> answers(query_count);
    int begin = 0;
    while (begin < query_count) {
        int end = begin + 1;
        const int first = queries[begin].first;
        const int second = queries[begin].second;
        while (end < query_count && queries[end].first == first && queries[end].second == second) {
            ++end;
        }
        const int length = static_cast<int>(std::min(words[first].size(), words[second].size()));
        std::vector<int> next_mismatch;
        if (first != second) {
            // Reuse this table for every query on the same unordered word pair.
            next_mismatch.resize(length + 1, length);
            for (int position = length - 1; position >= 0; --position) {
                next_mismatch[position] = words[first][position] != words[second][position]
                                              ? position
                                              : next_mismatch[position + 1];
            }
        }
        for (int i = begin; i < end; ++i) {
            const Query &query = queries[i];
            const std::int64_t upper = std::int64_t{length - query.cut} * SCORE_SCALE;
            std::int64_t best = 0;
            if (first == second) {
                best = upper;
            } else {
                int position = query.cut;
                int mismatches = 0;
                while ((upper >> mismatches) > best) {
                    const int next = next_mismatch[position];
                    const std::int64_t candidate = std::int64_t{next - query.cut}
                                                   << (SCORE_BITS - mismatches);
                    best = std::max(best, candidate);
                    if (next == length) {
                        break;
                    }
                    position = next + 1;
                    ++mismatches;
                }
            }
            answers[query.index] = best;
        }
        begin = end;
    }
    for (std::int64_t answer : answers) {
        std::cout << format_score(answer) << '\n';
    }
}
