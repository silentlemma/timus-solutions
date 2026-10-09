#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const int DIVISOR = 7;
const std::string KEY = "1234";

int remainder_of(const std::string &s) {
    int r = 0;
    for (char c : s)
        r = (r * 10 + (c - '0')) % DIVISOR;
    return r;
}

int main() {
    std::ios::sync_with_stdio(false);
    // the 24 orders of 1, 2, 3, 4 leave every remainder modulo 7
    std::vector<std::string> orders;
    std::string order = KEY;
    do
        orders.push_back(order);
    while (std::next_permutation(order.begin(), order.end()));
    int n;
    std::cin >> n;
    std::string out;
    while (n-- > 0) {
        std::string number;
        std::cin >> number;
        for (char d : KEY)
            number.erase(number.find(d), 1);
        // zeros go to the end, where they do not change divisibility by 7
        std::string head, zeros;
        for (char c : number)
            (c == '0' ? zeros : head) += c;
        for (const std::string &o : orders)
            if (remainder_of(head + o) == 0) {
                out += head + o + zeros + "\n";
                break;
            }
    }
    std::cout << out;
}
