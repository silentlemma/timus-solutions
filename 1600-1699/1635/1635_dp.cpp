#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string s;
    if (!(cin >> s))
        return 0;
    int n = s.size();
    // dp[j]: fewest palindromes for the prefix of length j. Centres go left
    // to right, so every palindrome s[l..r] meets a final dp[l]: those that
    // end before l have their centres before l.
    vector<int> dp(n + 1, n + 1), prev(n + 1);
    dp[0] = 0;
    for (int twice = 0; twice < 2 * n - 1; twice++) {
        int l = twice / 2, r = l + twice % 2;
        while (l >= 0 && r < n && s[l] == s[r]) {
            if (dp[l] + 1 < dp[r + 1]) {
                dp[r + 1] = dp[l] + 1;
                prev[r + 1] = l;
            }
            l--, r++;
        }
    }
    vector<string> parts;
    for (int end = n; end > 0; end = prev[end])
        parts.push_back(s.substr(prev[end], end - prev[end]));
    cout << dp[n] << '\n';
    for (int i = parts.size() - 1; i >= 0; i--)
        cout << parts[i] << (i ? ' ' : '\n');
}
