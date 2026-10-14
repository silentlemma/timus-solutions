#include <algorithm>
#include <array>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int SHOOTERS = 3;
const int INDEX_SUM = 0 + 1 + 2;
const int RATIO_DIGITS = 16;
const int OUTPUT_SCALE = 100000;
const double ROUND_EPS = 1e-8; // absorb floating-point noise at output rounding midpoints

typedef array<double, SHOOTERS> Chances;

double acc[SHOOTERS];
array<int, SHOOTERS> order;

array<string, SHOOTERS> values;
int stronger, weaker;
bool attack[2];

string canonical(string s) {
    size_t first = s.find_first_not_of('0');
    return first == string::npos ? "0" : s.substr(first);
}

bool lessThan(const string &a, const string &b) {
    return a.size() != b.size() ? a.size() < b.size() : a < b;
}

string subtract(string a, const string &b) {
    int borrow = 0;
    for (int i = (int)a.size() - 1, j = (int)b.size() - 1; i >= 0; i--, j--) {
        int digit = a[i] - '0' - borrow - (j >= 0 ? b[j] - '0' : 0);
        borrow = digit < 0;
        a[i] = char('0' + digit + 10 * borrow);
    }
    return canonical(a);
}

string multiply(const string &a, const string &b) {
    vector<int> digits(a.size() + b.size());
    for (size_t i = 0; i < a.size(); i++) {
        int carry = 0;
        for (size_t j = 0; j < b.size(); j++) {
            int value = digits[i + j] + (a[a.size() - 1 - i] - '0') *
                        (b[b.size() - 1 - j] - '0') + carry;
            digits[i + j] = value % 10;
            carry = value / 10;
        }
        digits[i + b.size()] = carry;
    }
    string result;
    for (auto it = digits.rbegin(); it != digits.rend(); it++)
        result += char('0' + *it);
    return canonical(result);
}

double ratio(int first, int second) {
    string a = values[first], b = values[second];
    string x = a.substr(0, RATIO_DIGITS), y = b.substr(0, RATIO_DIGITS);
    int exponent = ((int)a.size() - (int)x.size()) - ((int)b.size() - (int)y.size());
    return (stod(x) / stod(y)) * pow(10.0, exponent);
}

// two left, first to shoot: first wins p / (p + q - p q)
Chances duel(int first, int second) {
    double p = acc[first], q = acc[second];
    Chances c = {0, 0, 0};
    if (!lessThan(values[first], values[second]))
        c[first] = 1 / (1 + ratio(second, first) * (1 - p));
    else {
        double r = ratio(first, second);
        c[first] = r / (1 + r * (1 - q));
    }
    c[second] = 1 - c[first];
    return c;
}

// the duel left after a hit, with the next living shooter first
Chances afterHit(int turn, int killed) {
    int first = order[(turn + 1) % SHOOTERS];
    if (first == killed)
        first = order[(turn + 2) % SHOOTERS];
    return duel(first, INDEX_SUM - killed - first);
}

// chances when all three live and order[turn] shoots; A never misses, so the
// shooting stops at A's turn at the latest
Chances three(int turn) {
    int shooter = order[turn];
    if (shooter == 0)
        return afterHit(turn, stronger);
    double p = acc[shooter];
    Chances miss = three((turn + 1) % SHOOTERS);
    // the weaker shooter attacks A iff (1-h)^k (1-l) >= h; ties attack
    bool nextIsStronger = order[(turn + 1) % SHOOTERS] != 0;
    if (shooter == weaker && !attack[nextIsStronger])
        return miss;
    Chances hit = afterHit(turn, 0), mixed;
    for (int i = 0; i < SHOOTERS; i++)
        mixed[i] = p * hit[i] + (1 - p) * miss[i];
    return mixed;
}

int main() {
    array<string, SHOOTERS> tokens;
    size_t precision = 0;
    for (int i = 0; i < SHOOTERS; i++) {
        if (!(cin >> tokens[i]))
            return 0;
        acc[i] = strtod(tokens[i].c_str(), nullptr);
        size_t point = tokens[i].find('.');
        if (point != string::npos)
            precision = max(precision, tokens[i].size() - point - 1);
    }
    for (int i = 0; i < SHOOTERS; i++) {
        size_t point = tokens[i].find('.'), fraction = 0;
        if (point != string::npos) {
            fraction = tokens[i].size() - point - 1;
            tokens[i].erase(point, 1);
        }
        values[i] = canonical(tokens[i] + string(precision - fraction, '0'));
    }
    stronger = lessThan(values[1], values[2]) ? 2 : 1;
    weaker = INDEX_SUM - stronger;
    string scale = "1" + string(precision, '0');
    string high = values[stronger], low = values[weaker];
    string complement = subtract(scale, high);
    string product = multiply(complement, subtract(scale, low));
    string bound = multiply(high, scale);
    attack[0] = low == "0" || !lessThan(product, bound);
    attack[1] = low == "0" || !lessThan(multiply(product, complement), multiply(bound, scale));
    order = {0, 1, 2};
    Chances total = {0, 0, 0};
    int orders = 0;
    do {
        Chances c = three(0);
        for (int i = 0; i < SHOOTERS; i++)
            total[i] += c[i];
        orders++;
    } while (next_permutation(order.begin(), order.end()));
    array<int, SHOOTERS> rounded;
    for (int i = 0; i < SHOOTERS; i++)
        rounded[i] = int(total[i] * (1.0 / orders) * OUTPUT_SCALE + 0.5 + ROUND_EPS);
    printf("%d.%05d %d.%05d %d.%05d\n", rounded[0] / OUTPUT_SCALE, rounded[0] % OUTPUT_SCALE,
           rounded[1] / OUTPUT_SCALE, rounded[1] % OUTPUT_SCALE,
           rounded[2] / OUTPUT_SCALE, rounded[2] % OUTPUT_SCALE);
}
