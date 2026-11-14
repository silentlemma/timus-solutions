#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string source, target;
    if (!std::getline(std::cin, source) || !std::getline(std::cin, target))
        return 0;
    if (!source.empty() && source.back() == '\r')
        source.pop_back();
    if (!target.empty() && target.back() == '\r')
        target.pop_back();

    const auto erase_letters = [&](std::size_t begin, std::size_t end) {
        for (std::size_t i = begin; i < end; ++i) {
            if (source[i] != ' ')
                source[i] = '_';
        }
    };

    std::vector<int> prefix;
    std::size_t search = 0, kept_until = 0;
    const std::string_view words(target);
    for (std::size_t begin = 0; begin < words.size();) {
        const auto word_end = words.find(' ', begin);
        const auto word = words.substr(begin, word_end - begin);
        const int length = static_cast<int>(word.size());
        prefix.resize(length);
        for (int i = 1, matched = 0; i < length; ++i) {
            while (matched && word[i] != word[matched])
                matched = prefix[matched - 1];
            if (word[i] == word[matched])
                ++matched;
            prefix[i] = matched;
        }

        int matched = 0;
        while (search < source.size()) {
            const char letter = source[search++];
            while (matched && letter != word[matched])
                matched = prefix[matched - 1];
            if (letter == word[matched] && ++matched == length)
                break;
        }
        if (matched != length) {
            std::cout << "I HAVE FAILED!!!\n";
            return 0;
        }

        // Leave one separator before the next kept word.
        erase_letters(kept_until, search - length);
        kept_until = search++;
        begin = word_end == std::string_view::npos ? words.size() : word_end + 1;
    }
    erase_letters(kept_until, source.size());
    std::cout << source << '\n';
}
