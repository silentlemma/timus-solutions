#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string word;
    std::cin >> word;
    // the added part is never empty, so look for the longest palindromic
    // suffix of the word without its first letter
    std::string tail = word.substr(1);
    std::string text(tail.rbegin(), tail.rend());
    text += '#';
    text += tail;
    std::vector<int> border(text.size(), 0);
    for (size_t i = 1; i < text.size(); i++) {
        int k = border[i - 1];
        while (k > 0 && text[i] != text[k])
            k = border[k - 1];
        if (text[i] == text[k])
            k++;
        border[i] = k;
    }
    int longest = tail.empty() ? 0 : border.back();
    std::string head = word.substr(0, word.size() - longest);
    std::reverse(head.begin(), head.end());
    std::cout << word << head << '\n';
    return 0;
}
