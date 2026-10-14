#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int PERIOD = 6; // the simple pattern fails exactly when n mod 6 is 2

// the row of the queen in each column 1 ... n for even n; the main
// diagonal stays free
vector<int> evenRows(int n) {
    int half = n / 2;
    vector<int> rows(n);
    for (int i = 1; i <= half; i++)
        if (n % PERIOD != 2) {
            // the even rows in the left half, the odd rows in the right half
            rows[i - 1] = 2 * i;
            rows[half + i - 1] = 2 * i - 1;
        } else {
            int shift = (2 * (i - 1) + half - 1) % n;
            rows[i - 1] = 1 + shift;
            rows[n - i] = n - shift;
        }
    return rows;
}

int main() {
    int n;
    scanf("%d", &n);
    // an odd board is an even one plus the free corner (n, n)
    vector<int> rows = evenRows(n - n % 2);
    if (n % 2 == 1)
        rows.push_back(n);
    string out;
    for (int col = 1; col <= n; col++)
        out += to_string(col) + " " + to_string(rows[col - 1]) + "\n";
    fputs(out.c_str(), stdout);
}
