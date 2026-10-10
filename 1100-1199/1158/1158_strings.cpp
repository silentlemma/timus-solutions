#include <cstdint>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

// counts reach 50^50, so they are kept in limbs of nine decimal digits
const uint32_t LIMB = 1000000000;
const int LIMB_DIGITS = 9;
const int BYTES = 256;

typedef std::vector<uint32_t> Big; // lowest limb first

void add(Big &a, const Big &b) {
    if (a.size() < b.size())
        a.resize(b.size(), 0);
    uint32_t carry = 0;
    for (size_t i = 0; i < a.size(); i++) {
        uint64_t v = (uint64_t)a[i] + (i < b.size() ? b[i] : 0) + carry;
        a[i] = v % LIMB;
        carry = v / LIMB;
    }
    if (carry)
        a.push_back(carry);
}

std::string text(const Big &a) {
    if (a.empty())
        return "0";
    std::string out = std::to_string(a.back());
    for (int i = (int)a.size() - 2; i >= 0; i--) {
        std::string part = std::to_string(a[i]);
        out += std::string(LIMB_DIGITS - part.size(), '0') + part;
    }
    return out;
}

// a line without the spaces and line breaks around it; letters are above 32
std::string trim(const std::string &s) {
    size_t b = 0, e = s.size();
    while (b < e && (unsigned char)s[b] <= ' ')
        b++;
    while (e > b && (unsigned char)s[e - 1] <= ' ')
        e--;
    return s.substr(b, e - b);
}

int main() {
    // letters may be any bytes above 32, so the input is read as bytes
    std::string data((std::istreambuf_iterator<char>(std::cin)), std::istreambuf_iterator<char>());
    std::vector<std::string> lines;
    std::istringstream split(data);
    for (std::string line; std::getline(split, line);)
        lines.push_back(trim(line));
    int n, m, p;
    std::istringstream(lines[0]) >> n >> m >> p;
    std::string letters = lines[1];
    std::vector<int> index(BYTES, -1);
    for (int k = 0; k < n; k++)
        index[(unsigned char)letters[k]] = k;
    std::vector<std::string> words;
    for (size_t i = 2; i < lines.size() && (int)words.size() < p; i++)
        if (!lines[i].empty())
            words.push_back(lines[i]);
    // Aho-Corasick automaton over the forbidden words; a state is bad when
    // some word ends there
    std::vector<std::vector<int>> go(1, std::vector<int>(n, -1));
    std::vector<bool> bad(1, false);
    for (const auto &w : words) {
        int s = 0;
        for (unsigned char c : w) {
            int &next = go[s][index[c]];
            if (next < 0) {
                next = go.size();
                go.push_back(std::vector<int>(n, -1));
                bad.push_back(false);
            }
            s = go[s][index[c]];
        }
        bad[s] = true;
    }
    std::vector<int> fail(go.size(), 0);
    std::queue<int> order;
    for (int c = 0; c < n; c++) {
        if (go[0][c] < 0)
            go[0][c] = 0;
        else
            order.push(go[0][c]);
    }
    while (!order.empty()) {
        int s = order.front();
        order.pop();
        bad[s] = bad[s] || bad[fail[s]];
        for (int c = 0; c < n; c++) {
            int t = go[s][c];
            if (t < 0)
                go[s][c] = go[fail[s]][c];
            else {
                fail[t] = go[fail[s]][c];
                order.push(t);
            }
        }
    }
    // count the sentences letter by letter, never stepping into a bad state
    std::vector<Big> ways(go.size());
    ways[0] = {1};
    for (int step = 0; step < m; step++) {
        std::vector<Big> next(go.size());
        for (size_t s = 0; s < go.size(); s++)
            if (!ways[s].empty())
                for (int t : go[s])
                    if (!bad[t])
                        add(next[t], ways[s]);
        ways = next;
    }
    Big total;
    for (const auto &w : ways)
        add(total, w);
    std::cout << text(total) << "\n";
}
