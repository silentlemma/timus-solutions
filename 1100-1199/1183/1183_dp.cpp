#include <iostream>
#include <string>
#include <vector>

std::string s;
// add[i][j]: fewest brackets to add so that s[i, j) becomes regular; how it
// is best done: 0 pads a lone bracket, -1 wraps a pair, k splits at k
std::vector<std::vector<int>> add, how;

bool pair(char a, char b) { return (a == '(' && b == ')') || (a == '[' && b == ']'); }

void build(int i, int j, std::string &out) {
    if (i == j) {
        return;
    }
    int way = how[i][j];
    if (way == 0) {
        char c = s[i];
        out += c == '(' || c == ')' ? "()" : "[]";
    } else if (way < 0) {
        out += s[i];
        build(i + 1, j - 1, out);
        out += s[j - 1];
    } else {
        build(i, way, out);
        build(way, j, out);
    }
}

int main() {
    std::getline(std::cin, s);
    while (!s.empty() && (s.back() == '\r' || s.back() == ' ')) {
        s.pop_back();
    }
    int n = s.size();
    add.assign(n + 1, std::vector<int>(n + 1, 0));
    how.assign(n + 1, std::vector<int>(n + 1, 0));
    for (int length = 1; length <= n; length++) {
        for (int i = 0; i + length <= n; i++) {
            int j = i + length;
            if (length == 1) {
                add[i][j] = 1;
                continue;
            }
            int best = add[i][i + 1] + add[i + 1][j], way = i + 1;
            if (pair(s[i], s[j - 1]) && add[i + 1][j - 1] < best) {
                best = add[i + 1][j - 1];
                way = -1;
            }
            for (int k = i + 2; k < j; k++) {
                if (add[i][k] + add[k][j] < best) {
                    best = add[i][k] + add[k][j];
                    way = k;
                }
            }
            add[i][j] = best;
            how[i][j] = way;
        }
    }
    std::string out;
    build(0, n, out);
    std::cout << out << "\n";
}
