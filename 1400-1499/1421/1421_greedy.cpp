#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int CAP = 100; // the largest single credit

int main() {
    int n;
    scanf("%d", &n);
    vector<int> rows(n), cols(n);
    for (int &r : rows)
        scanf("%d", &r);
    for (int &c : cols)
        scanf("%d", &c);
    // take from the fullest columns first: lower them all towards a level
    auto taken = [&](int level) {
        int sum = 0;
        for (int c : cols)
            sum += min(CAP, max(0, c - level));
        return sum;
    };
    vector<vector<int>> matrix;
    for (int need : rows) {
        if (taken(0) < need) {
            printf("NO\n");
            return 0;
        }
        int lo = 0, hi = *max_element(cols.begin(), cols.end());
        while (lo < hi) { // the lowest level that takes no more than needed
            int mid = (lo + hi) / 2;
            if (taken(mid) <= need)
                hi = mid;
            else
                lo = mid + 1;
        }
        vector<int> row(n);
        int extra = need;
        for (int j = 0; j < n; j++) {
            row[j] = min(CAP, max(0, cols[j] - lo));
            extra -= row[j];
        }
        for (int j = 0; j < n && extra > 0; j++)
            // one more unit from columns that stand exactly at the level
            if (row[j] < CAP && cols[j] - row[j] == lo && lo > 0) {
                row[j]++;
                extra--;
            }
        for (int j = 0; j < n; j++)
            cols[j] -= row[j];
        matrix.push_back(row);
    }
    string out = "YES\n";
    for (auto &row : matrix)
        for (int j = 0; j < n; j++)
            out += to_string(row[j]) + (j + 1 < n ? " " : "\n");
    fputs(out.c_str(), stdout);
}
