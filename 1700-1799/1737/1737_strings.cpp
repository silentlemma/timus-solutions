#include <algorithm>
#include <cstdio>
#include <set>
#include <string>

const size_t LIMIT = 100000;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    // a palindrome of two or more letters has one of two or three letters
    // in its middle, so any three letters in a row must differ, and a name
    // is one order of a, b, c repeated
    std::string order = "abc";
    std::set<std::string> names;
    do {
        std::string name(n, ' ');
        for (int i = 0; i < n; i++) name[i] = order[i % order.size()];
        names.insert(name);
    } while (std::next_permutation(order.begin(), order.end()));
    if (names.size() * n > LIMIT) {
        printf("TOO LONG\n");
        return 0;
    }
    for (const auto &name : names) printf("%s\n", name.c_str());
}
