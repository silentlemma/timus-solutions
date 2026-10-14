#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// a name split into letters and numbers; a number is compared by its length
// without leading zeros and then digit by digit, and numbers come before letters
struct Key {
    vector<pair<int, string>> main; // (0 and the digits, or 1 and the letter)
    vector<int> zeros;              // minus the leading zeros of each number
};

Key keyOf(const string &s) {
    Key k;
    size_t i = 0;
    while (i < s.size()) {
        if (!isdigit(s[i])) {
            k.main.push_back({1, string(1, s[i])});
            i++;
            continue;
        }
        size_t start = i;
        while (i < s.size() && s[i] == '0')
            i++;
        size_t digits = i;
        while (i < s.size() && isdigit(s[i]))
            i++;
        k.main.push_back({0, s.substr(digits, i - digits)});
        k.zeros.push_back((int)start - (int)digits);
    }
    return k;
}

bool lessMain(const pair<int, string> &a, const pair<int, string> &b) {
    if (a.first != b.first)
        return a.first < b.first;
    if (a.second.size() != b.second.size())
        return a.second.size() < b.second.size();
    return a.second < b.second;
}

int main() {
    ios::sync_with_stdio(false);
    vector<string> names;
    string s;
    while (cin >> s)
        names.push_back(s);
    vector<Key> keys;
    for (auto &n : names)
        keys.push_back(keyOf(n));
    vector<int> order(names.size());
    for (size_t i = 0; i < order.size(); i++)
        order[i] = i;
    // letters and numbers by value first; then, run by run, more leading zeros first
    stable_sort(order.begin(), order.end(), [&](int x, int y) {
        const Key &a = keys[x], &b = keys[y];
        if (lexicographical_compare(a.main.begin(), a.main.end(), b.main.begin(), b.main.end(),
                                    lessMain))
            return true;
        if (lexicographical_compare(b.main.begin(), b.main.end(), a.main.begin(), a.main.end(),
                                    lessMain))
            return false;
        return a.zeros < b.zeros;
    });
    string out;
    for (int i : order)
        out += names[i] + "\n";
    cout << out;
}
