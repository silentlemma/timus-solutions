#include <array>
#include <cctype>
#include <cstdint>
#include <cstdio>

constexpr int MAX_PAIRS = 5000;
constexpr int CASE_BIT = 32;

int main() {
    int pairs;
    if (std::scanf("%d", &pairs) != 1) {
        return 0;
    }
    int letter;
    do {
        letter = std::getchar();
    } while (std::isspace(letter));
    std::array<char, 2 * MAX_PAIRS> pending_letter;
    std::array<std::uint16_t, 2 * MAX_PAIRS> pending_index;
    std::array<std::uint16_t, MAX_PAIRS> answer;
    int upper = 0;
    int lower = 0;
    int size = 0;
    for (int i = 0; i < 2 * pairs; ++i) {
        const bool is_upper = letter >= 'A' && letter <= 'Z';
        const int index = is_upper ? upper++ : lower++;
        if (size > 0 && (pending_letter[size - 1] ^ letter) == CASE_BIT) {
            const int previous = pending_index[--size];
            if (is_upper) {
                answer[index] = previous + 1;
            } else {
                answer[previous] = index + 1;
            }
        } else {
            pending_letter[size] = static_cast<char>(letter);
            pending_index[size] = index;
            ++size;
        }
        if (i + 1 < 2 * pairs) {
            letter = std::getchar();
        }
    }
    if (size != 0) {
        std::puts("Impossible");
        return 0;
    }
    for (int i = 0; i < pairs; ++i) {
        std::printf(i ? " %u" : "%u", static_cast<unsigned>(answer[i]));
    }
    std::putchar('\n');
}
