#include <array>
#include <cstdio>

constexpr int MAX_LENGTH = 100000;
constexpr int ALPHABET = 26;

constexpr int INPUT_FIELDS = 3;

int main() {
    int size, budget;
    char drum[MAX_LENGTH + 1];
    if (std::scanf("%d%d%100000s", &size, &budget, drum) != INPUT_FIELDS)
        return 0;

    for (int period = 1; period < size; ++period) {
        if (size % period != 0)
            continue;
        const int per_class = size / period;
        int changes = 0;
        std::array<char, MAX_LENGTH / 2> pattern;
        for (int residue = 0; residue < period && changes <= budget; ++residue) {
            std::array<int, ALPHABET> count{};
            int most = 0;
            for (int i = residue; i < size; i += period) {
                const int letter = drum[i] - 'a';
                if (++count[letter] > count[most])
                    most = letter;
            }
            pattern[residue] = 'a' + most;
            changes += per_class - count[most];
        }
        if (changes > budget)
            continue;

        std::printf("%d\n", period);
        for (int i = 0; i < per_class; ++i)
            std::fwrite(pattern.data(), 1, period, stdout);
        std::putchar('\n');
        return 0;
    }
    std::printf("%d\n%s\n", size, drum);
}
