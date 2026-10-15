#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

std::vector<int> zFunction(const std::string& s) {
    int n = s.size();
    std::vector<int> z(n, 0);
    for (int i = 1, left = 0, right = 0; i < n; i++) {
        int k = i < right ? std::min(z[i - left], right - i) : 0;
        while (i + k < n && s[k] == s[i + k]) {
            k++;
        }
        z[i] = k;
        if (i + k > right) {
            left = i;
            right = i + k;
        }
    }
    return z;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::string word, last;
    std::cin >> word >> last;
    int m = word.size(), n = last.size();
    std::vector<int> z = zFunction(word + "#" + last);
    // from a cut at position p the next piece can end anywhere in
    // p + 1 .. p + z[p]; so the reachable cuts are always 0 .. reach
    std::vector<int> parent(n + 1, 0);
    int reach = 0;
    for (int p = 0; p <= reach && p < n; p++) {
        int far = p + z[m + 1 + p];
        for (int q = reach + 1; q <= far; q++) {
            parent[q] = p;
        }
        reach = std::max(reach, far);
    }
    if (reach < n) {
        std::cout << "Yes\n";
        return 0;
    }
    std::vector<std::string> pieces;
    for (int q = n; q > 0; q = parent[q]) {
        pieces.push_back(last.substr(parent[q], q - parent[q]));
    }
    std::reverse(pieces.begin(), pieces.end());
    std::string out = "No\n";
    for (size_t i = 0; i < pieces.size(); i++) {
        out += (i ? " " : "") + pieces[i];
    }
    std::cout << out << "\n";
}
