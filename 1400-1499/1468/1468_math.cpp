#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const string DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

string whole(int x, int k) {
    string out;
    do {
        out += DIGITS[x % k];
        x /= k;
    } while (x);
    reverse(out.begin(), out.end());
    return out;
}

int main() {
    int a, b, k;
    while (scanf("%d %d", &a, &b) == 2 && (a || b)) {
        scanf("%d", &k);
        string text = whole(a / b, k);
        int rest = a % b;
        if (rest) {
            // long division; a remainder seen before starts the period
            vector<int> seen(b, -1);
            string frac;
            while (rest && seen[rest] < 0) {
                seen[rest] = frac.size();
                rest *= k;
                frac += DIGITS[rest / b];
                rest %= b;
            }
            if (rest)
                frac = frac.substr(0, seen[rest]) + "(" + frac.substr(seen[rest]) + ")";
            text += "." + frac;
        }
        puts(text.c_str());
    }
}
