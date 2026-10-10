#include <algorithm>
#include <iostream>
#include <string>

using std::string;

// x + 1 for a decimal string
string inc(string x) {
    int k = x.size() - 1;
    while (k >= 0 && x[k] == '9') {
        x[k--] = '0';
    }
    if (k < 0) {
        return "1" + x;
    }
    x[k]++;
    return x;
}

// x - 1 for a positive decimal string
string dec(string x) {
    int k = x.size() - 1;
    while (x[k] == '0') {
        x[k--] = '9';
    }
    x[k]--;
    if (x[0] == '0' && x.size() > 1) {
        x.erase(0, 1);
    }
    return x;
}

string mulSmall(const string &x, int m) {
    string r;
    int carry = 0;
    for (int k = x.size() - 1; k >= 0; k--) {
        carry += (x[k] - '0') * m;
        r += char('0' + carry % 10);
        carry /= 10;
    }
    for (; carry > 0; carry /= 10) {
        r += char('0' + carry % 10);
    }
    std::reverse(r.begin(), r.end());
    return r;
}

string addSmall(string x, int m) {
    for (int k = 0; k < m; k++) {
        x = inc(x);
    }
    return x;
}

// a - b for decimal strings with a >= b
string sub(const string &a, const string &b) {
    string r = a;
    int borrow = 0;
    for (int k = 0; k < (int)a.size(); k++) {
        int pa = a.size() - 1 - k, pb = b.size() - 1 - k;
        int v = (a[pa] - '0') - borrow - (pb >= 0 ? b[pb] - '0' : 0);
        borrow = v < 0;
        r[pa] = char('0' + (v + 10) % 10);
    }
    size_t lead = r.find_first_not_of('0');
    return lead == string::npos ? "0" : r.substr(lead);
}

bool less(const string &a, const string &b) {
    return a.size() != b.size() ? a.size() < b.size() : a < b;
}

// position in S of the digit s places before the start of x; the numbers
// below 10^(d-1) take (d-1)·10^(d-1) - R(d-1) digits, where R(t) is the
// repunit of t ones, which leaves d·x + 1 - R(d) for x itself
string position(const string &x, int s) {
    int d = x.size();
    return sub(addSmall(mulSmall(x, d), 2), addSmall(string(d, '1'), s + 1));
}

// whether the number x can begin at position s of a, with its neighbours
// filling the rest of a on both sides
bool fits(const string &a, int s, const string &x) {
    int n = a.size();
    if (a.compare(s, x.size(), x, 0, n - s) != 0) {
        return false;
    }
    int pos = s + x.size();
    string cur = x;
    while (pos < n) {
        cur = inc(cur);
        if (a.compare(pos, cur.size(), cur, 0, n - pos) != 0) {
            return false;
        }
        pos += cur.size();
    }
    pos = s;
    cur = x;
    while (pos > 0) {
        cur = dec(cur);
        if (cur == "0") {
            return false;
        }
        int m = std::min<int>(pos, cur.size());
        if (a.compare(pos - m, m, cur, cur.size() - m, m) != 0) {
            return false;
        }
        pos -= cur.size();
    }
    return true;
}

int main() {
    string a;
    std::cin >> a;
    int n = a.size();
    // a inside one number, right after its first digit
    string best = position("1" + a, -1);
    auto consider = [&](int s, const string &x) {
        if (fits(a, s, x)) {
            string k = position(x, s);
            if (less(k, best)) {
                best = k;
            }
        }
    };
    // some number lies in a completely
    for (int s = 0; s < n; s++) {
        if (a[s] != '0') {
            for (int e = s + 1; e <= n; e++) {
                consider(s, a.substr(s, e - s));
            }
        }
    }
    // a is the end of y - 1 followed by the beginning of y; the last i digits
    // of y are those of y - 1 plus one, and they may overlap the known
    // beginning by j digits
    for (int i = 1; i < n; i++) {
        if (a[i] == '0') {
            continue;
        }
        string tail = inc(a.substr(0, i));
        tail = tail.substr(tail.size() - i);
        for (int j = 0; j <= std::min(n - i, i); j++) {
            if (a.compare(n - j, j, tail, 0, j) == 0) {
                consider(i, a.substr(i) + tail.substr(j));
            }
        }
    }
    std::cout << best << "\n";
}
