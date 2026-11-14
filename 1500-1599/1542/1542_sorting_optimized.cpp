#include <algorithm>
#include <array>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_map>
#include <vector>

constexpr int MAX_WORD_LENGTH = 15;
constexpr int SUGGESTIONS = 10;

struct Entry {
    int frequency;
    char word[MAX_WORD_LENGTH + 1];
};

struct Matches {
    int size = 0;
    std::array<int, SUGGESTIONS> indices{};
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int wordCount;
    std::cin >> wordCount;
    std::vector<Entry> words(wordCount);
    for (Entry &entry : words) {
        std::cin >> std::setw(sizeof entry.word) >> entry.word >> entry.frequency;
    }
    std::sort(words.begin(), words.end(), [](const Entry &a, const Entry &b) {
        if (a.frequency != b.frequency)
            return a.frequency > b.frequency;
        return std::strcmp(a.word, b.word) < 0;
    });

    int queryCount;
    std::cin >> queryCount;
    std::vector<std::string> queries(queryCount);
    std::vector<const Matches *> answers(queryCount, nullptr);
    std::array<bool, MAX_WORD_LENGTH + 1> requested{};
    std::unordered_map<std::string_view, Matches> matches;
    matches.reserve(queryCount);
    for (int i = 0; i < queryCount; ++i) {
        std::cin >> queries[i];
        const std::string_view query = queries[i];
        if (query.size() <= MAX_WORD_LENGTH) {
            requested[query.size()] = true;
            answers[i] = &matches.try_emplace(query).first->second;
        }
    }
    std::vector<size_t> lengths;
    for (size_t k = 1; k < requested.size(); ++k) {
        if (requested[k])
            lengths.push_back(k);
    }
    for (int i = 0; i < wordCount; ++i) {
        const std::string_view word = words[i].word;
        for (size_t length : lengths) {
            if (length > word.size())
                break;
            auto match = matches.find(word.substr(0, length));
            if (match != matches.end() && match->second.size < SUGGESTIONS) {
                Matches &list = match->second;
                list.indices[list.size++] = i;
            }
        }
    }
    for (int i = 0; i < queryCount; ++i) {
        if (i > 0)
            std::cout << '\n';
        if (const Matches *list = answers[i]) {
            for (int j = 0; j < list->size; ++j)
                std::cout << words[list->indices[j]].word << '\n';
        }
    }
}
