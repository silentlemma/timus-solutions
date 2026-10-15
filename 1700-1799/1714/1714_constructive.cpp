#include <iostream>
#include <map>
#include <string>

const std::string HEAD = "aabab";
const std::string BLOCK = "bbaaba";  // each block forces two more palindromes

int main() {
    int n;
    std::cin >> n;
    // the end after the blocks for each remainder of n mod 6
    const std::map<int, std::string> tails = {{5, ""},     {0, "b"},    {1, "bb"},
                                              {2, "bbaaababb"}, {3, "bbaa"}, {4, "bbaab"}};
    // short lengths where the pattern is not yet the best, found by search
    const std::map<int, std::string> special = {{2, "ab"}, {8, "aababbaa"}, {11, "aababbaabab"}};
    std::string word;
    if (special.count(n)) {
        word = special.at(n);
    } else if (n <= (int)HEAD.size()) {
        word = HEAD.substr(0, n);
    } else {
        const std::string& tail = tails.at(n % BLOCK.size());
        word = HEAD;
        for (int k = (n - HEAD.size() - tail.size()) / BLOCK.size(); k > 0; k--) {
            word += BLOCK;
        }
        word += tail;
    }
    std::cout << word << "\n";
}
