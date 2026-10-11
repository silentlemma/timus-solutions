#include <iostream>
#include <string>

// Roman digits needed for each decimal digit: -, I, II, III, IV, V, VI,
// VII, VIII, IX
const int LENGTHS[] = {0, 1, 2, 3, 2, 1, 2, 3, 4, 2};

int main() {
    std::string s;
    std::cin >> s;
    int total = 0;
    for (char c : s)
        total += LENGTHS[c - '0'];
    std::cout << total << "\n";
}
