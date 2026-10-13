#include <algorithm>
#include <array>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int LETTERS = 26;
typedef array<int, LETTERS> Powers;
typedef map<Powers, long long> Poly;

// the number of digits starting at pos; pos moves past it
long long number(const string &s, size_t &pos) {
    long long value = 0;
    while (pos < s.size() && isdigit((unsigned char)s[pos]))
        value = value * 10 + (s[pos++] - '0');
    return value;
}

// a polynomial as a map from the powers of a .. z to coefficients
Poly parse(const string &line) {
    string s;
    for (char c : line)
        if (!isspace((unsigned char)c))
            s += c; // spaces may stand anywhere
    Poly poly;
    size_t pos = 0;
    int sign = 1;
    while (pos < s.size()) {
        if (s[pos] == '+' || s[pos] == '-')
            sign = s[pos++] == '-' ? -1 : 1;
        long long coef = 1;
        Powers powers{};
        while (true) {
            if (isdigit((unsigned char)s[pos]))
                coef *= number(s, pos);
            else {
                int var = s[pos++] - 'a', power = 1;
                if (pos < s.size() && s[pos] == '^') {
                    pos++;
                    power = (int)number(s, pos);
                }
                powers[var] += power;
            }
            if (pos < s.size() && s[pos] == '*')
                pos++;
            else
                break;
        }
        poly[powers] += sign * coef;
    }
    return poly;
}

int main() {
    string a, b;
    getline(cin, a);
    getline(cin, b);
    Poly first = parse(a), second = parse(b), product;
    for (auto &[p, x] : first)
        for (auto &[q, y] : second) {
            Powers r;
            for (int v = 0; v < LETTERS; v++)
                r[v] = p[v] + q[v];
            product[r] += x * y;
        }
    vector<pair<Powers, long long>> terms;
    for (auto &t : product)
        if (t.second != 0)
            terms.push_back(t);
    // by total degree, then by the powers of a, b, ... from the largest
    sort(terms.begin(), terms.end(), [](const auto &l, const auto &r) {
        int sl = 0, sr = 0;
        for (int v = 0; v < LETTERS; v++) {
            sl += l.first[v];
            sr += r.first[v];
        }
        if (sl != sr)
            return sl > sr;
        return l.first > r.first;
    });
    string out;
    for (size_t k = 0; k < terms.size(); k++) {
        long long coef = terms[k].second;
        vector<string> factors;
        for (int v = 0; v < LETTERS; v++)
            if (int e = terms[k].first[v])
                factors.push_back(string(1, char('a' + v)) + (e == 1 ? "" : "^" + to_string(e)));
        if (llabs(coef) != 1 || factors.empty())
            factors.insert(factors.begin(), to_string(llabs(coef)));
        string body;
        for (size_t i = 0; i < factors.size(); i++)
            body += (i ? "*" : "") + factors[i];
        if (k == 0)
            out += (coef < 0 ? "-" : "") + body;
        else
            out += (coef < 0 ? " - " : " + ") + body;
    }
    cout << (out.empty() ? "0" : out) << endl;
}
