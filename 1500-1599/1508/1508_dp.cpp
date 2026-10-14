#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> groups(k);
    for (int &g : groups)
        cin >> g;
    string line;
    cin >> line;
    vector<int> dots(n + 1, 0); // dots[i]: known empty cells among the first i
    for (int i = 0; i < n; i++)
        dots[i + 1] = dots[i] + (line[i] == '.');
    // whether a group can cover the cells s ... s + length - 1
    auto fits = [&](int s, int length) {
        return s >= 0 && s + length <= n && dots[s + length] == dots[s];
    };
    // pre[i][j]: the first i cells can hold the first j groups
    vector<vector<char>> pre(n + 1, vector<char>(k + 1, 0));
    pre[0][0] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= k; j++) {
            bool ok = line[i - 1] != 'X' && pre[i - 1][j];
            if (!ok && j > 0 && fits(i - groups[j - 1], groups[j - 1])) {
                int s = i - groups[j - 1];
                ok = s == 0 ? j == 1 : line[s - 1] != 'X' && pre[s - 1][j - 1];
            }
            pre[i][j] = ok;
        }
    if (!pre[n][k]) {
        cout << "Impossible\n";
        return 0;
    }
    // suf[i][j]: the cells from i on can hold the groups from j on
    vector<vector<char>> suf(n + 2, vector<char>(k + 1, 0));
    suf[n][k] = 1;
    for (int i = n - 1; i >= 0; i--)
        for (int j = k; j >= 0; j--) {
            bool ok = line[i] != 'X' && suf[i + 1][j];
            if (!ok && j < k && fits(i, groups[j])) {
                int end = i + groups[j];
                ok = end == n ? j + 1 == k : line[end] != 'X' && suf[end + 1][j + 1];
            }
            suf[i][j] = ok;
        }
    vector<int> cover(n + 1, 0); // difference array of the cells some group can cover
    for (int j = 0; j < k; j++)
        for (int s = 0; s + groups[j] <= n; s++) {
            int end = s + groups[j];
            if (!fits(s, groups[j]))
                continue;
            bool left = s == 0 ? j == 0 : line[s - 1] != 'X' && pre[s - 1][j];
            bool right = end == n ? j + 1 == k : line[end] != 'X' && suf[end + 1][j + 1];
            if (left && right) {
                cover[s]++;
                cover[end]--;
            }
        }
    string out(n, '.');
    for (int c = 0, run = 0; c < n; c++) {
        run += cover[c];
        bool white = false;
        for (int j = 0; j <= k && line[c] != 'X'; j++)
            white = white || (pre[c][j] && suf[c + 1][j]);
        out[c] = white && run ? '?' : (white ? '.' : 'X');
    }
    cout << out << "\n";
}
