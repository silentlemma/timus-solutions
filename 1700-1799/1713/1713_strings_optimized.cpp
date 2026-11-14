#include <algorithm>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

constexpr int max_word_size = 100;
constexpr int offset_bits = 7;
constexpr std::uint32_t offset_mask = (1U << offset_bits) - 1;
static_assert(max_word_size <= 1U << offset_bits);

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    if (!(std::cin >> count))
        return 0;
    std::vector<std::string> words(count);
    std::size_t total = 0;
    for (auto &word : words) {
        std::cin >> word;
        total += word.size();
    }
    std::vector<std::uint32_t> suffixes;
    suffixes.reserve(total);
    for (std::uint32_t i = 0; i < words.size(); ++i)
        for (std::uint32_t j = 0; j < words[i].size(); ++j)
            suffixes.push_back((i << offset_bits) | j);
    const auto owner = [](std::uint32_t position) { return position >> offset_bits; };
    const auto text = [&](std::uint32_t position) {
        return words[owner(position)].c_str() + (position & offset_mask);
    };
    std::sort(suffixes.begin(), suffixes.end(),
              [&](auto a, auto b) { return std::strcmp(text(a), text(b)) < 0; });
    std::vector<std::uint8_t> adjacent(total), left(total);
    for (std::size_t i = 1; i < total; ++i) {
        const auto a = suffixes[i - 1], b = suffixes[i];
        const char *x = text(a), *y = text(b);
        std::uint8_t length = 0;
        while (x[length] && x[length] == y[length])
            ++length;
        adjacent[i] = length;
        left[i] = owner(a) == owner(b) ? std::min(left[i - 1], length) : length;
    }
    struct Key {
        std::uint8_t start, size;
    };
    std::vector<Key> keys;
    keys.reserve(words.size());
    for (const auto &word : words)
        keys.push_back({0, static_cast<std::uint8_t>(word.size())});
    std::uint8_t right = 0;
    for (std::size_t i = total; i-- > 0;) {
        const auto position = suffixes[i], word = owner(position);
        if (i + 1 < total) {
            const auto next = adjacent[i + 1];
            right = word == owner(suffixes[i + 1]) ? std::min(right, next) : next;
        }
        const auto start = static_cast<std::uint8_t>(position & offset_mask);
        const auto size = static_cast<std::uint8_t>(1 + std::max(left[i], right));
        if (size < keys[word].size && start + size <= static_cast<int>(words[word].size()))
            keys[word] = {start, size};
    }
    for (std::size_t i = 0; i < words.size(); ++i) {
        std::cout.write(words[i].data() + keys[i].start, keys[i].size);
        std::cout.put('\n');
    }
}
