#include <iostream>
#include <string>

// the left half with its middle digit, copied backwards onto the right half
std::string mirror(const std::string &digits) {
    std::string out = digits;
    for (size_t i = 0; i < out.size() / 2; i++)
        out[out.size() - 1 - i] = out[i];
    return out;
}

int main() {
    std::string s;
    std::cin >> s;
    size_t start = 0;
    while (start + 1 < s.size() && s[start] == '0')
        start++;
    s.erase(0, start);
    std::string best = mirror(s);
    // same length strings of digits compare like the numbers they spell
    if (best < s) {
        // add one to the left half with its middle digit; it is not all nines,
        // since all nines mirror to the largest number of this length
        std::string half = s;
        int k = (int)(s.size() + 1) / 2 - 1;
        while (half[k] == '9')
            half[k--] = '0';
        half[k]++;
        best = mirror(half);
    }
    std::cout << best << "\n";
}
