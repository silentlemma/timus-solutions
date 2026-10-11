#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

const int SPACE = ' ';
const int HEX = 16;

std::vector<int> decode(const std::string &s) {
    std::vector<int> bytes(s.size() / 2);
    for (size_t i = 0; i < bytes.size(); i++)
        bytes[i] = std::stoi(s.substr(2 * i, 2), nullptr, HEX);
    return bytes;
}

int main() {
    std::string s1, s2;
    std::cin >> s1 >> s2;
    std::vector<int> shorter = decode(s1), longer = decode(s2);
    // the long message is a space followed by the short one, so its first
    // byte gives the first key byte, and byte i+1 of the long message hides
    // the same clear byte as byte i of the short one
    std::vector<int> key(longer.size());
    key[0] = longer[0] ^ SPACE;
    for (size_t i = 0; i < shorter.size(); i++)
        key[i + 1] = longer[i + 1] ^ shorter[i] ^ key[i];
    const char *digits = "0123456789ABCDEF";
    std::string out;
    for (int k : key) {
        out += digits[k / HEX];
        out += digits[k % HEX];
    }
    puts(out.c_str());
}
