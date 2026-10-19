#include <array>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

constexpr int kOctaveSize = 12;
constexpr int kPitchCount = 96;
constexpr int kOutputPrecision = 12;
const std::string kNaturalScale = "C D EF G A B";
using Positions = std::array<std::vector<int>, kPitchCount>;

int parseNote(const std::string &token) {
    int pitch = (token[0] - '1') * kOctaveSize;
    pitch += static_cast<int>(kNaturalScale.find(token[1]));
    if (token.size() > 2)
        pitch += token[2] == '+' ? 1 : -1;
    return pitch;
}

int absoluteSimilarity(const Positions &positions, int sourceLength, const std::vector<int> &song) {
    int length = static_cast<int>(song.size());
    std::vector<int> counts(sourceLength + length - 1);
    for (int j = 0; j < length; ++j) {
        int offset = length - 1 - j;
        for (int i : positions[song[j]])
            ++counts[i + offset];
    }
    int best = 0;
    for (int count : counts)
        if (count > best)
            best = count;
    return best;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    Positions positions;
    std::string token;
    for (int i = 0; i < n; ++i) {
        std::cin >> token;
        positions[parseNote(token)].push_back(i);
    }
    int melodies;
    std::cin >> melodies;
    std::cout << std::fixed << std::setprecision(kOutputPrecision);
    while (melodies-- != 0) {
        int length;
        std::cin >> length;
        std::vector<int> song(length);
        for (int &pitch : song) {
            std::cin >> token;
            pitch = parseNote(token);
        }
        int best = absoluteSimilarity(positions, n, song);
        std::cout << static_cast<double>(best) / length << '\n';
    }
}
