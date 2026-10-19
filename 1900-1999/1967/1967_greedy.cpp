#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

constexpr int kDecimalBase = 10;

std::string timesTen(const std::string &value) {
    int carry = 0;
    std::string result;
    for (auto at = value.rbegin(); at != value.rend(); ++at) {
        carry += (*at - '0') * kDecimalBase;
        result.push_back(static_cast<char>('0' + carry % 2));
        carry /= 2;
    }
    while (carry) {
        result.push_back(static_cast<char>('0' + carry % 2));
        carry /= 2;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

std::vector<int> optimalLengths(const std::string &bits) {
    std::vector<std::string> powers;
    std::string power = "1";
    int end = static_cast<int>(bits.size());
    std::vector<int> lengths;
    while (end) {
        std::size_t index = 0;
        while (true) {
            if (index == powers.size()) {
                power = timesTen(power);
                powers.push_back(power);
            }
            const auto &threshold = powers[index];
            int length = static_cast<int>(threshold.size());
            if (length >= end) {
                lengths.push_back(end);
                std::reverse(lengths.begin(), lengths.end());
                return lengths;
            }
            int start = end - length;
            if (bits[start] == '1' && bits.compare(start, length, threshold) < 0) {
                lengths.push_back(length);
                end = start;
                break;
            }
            ++index;
        }
    }
    std::reverse(lengths.begin(), lengths.end());
    return lengths;
}

std::string makeBits(int maximum) {
    std::string bits;
    for (int value = 1; value <= maximum; ++value) {
        int bit = 1;
        while (bit <= value / 2)
            bit *= 2;
        for (; bit > 0; bit /= 2)
            bits.push_back(value & bit ? '1' : '0');
    }
    return bits;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int maximum;
    std::cin >> maximum;
    auto lengths = optimalLengths(makeBits(maximum));
    std::cout << lengths.size() << '\n';
    for (int length : lengths)
        std::cout << length << ' ';
    std::cout << '\n';
}
