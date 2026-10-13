#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n;
    string s, t;
    cin >> n >> s >> t;
    // t is s turned left by k, that is right by n - k: find it in s + s with KMP
    vector<int> fail(n, 0);
    for (int i = 1, k = 0; i < n; i++) {
        while (k > 0 && t[i] != t[k])
            k = fail[k - 1];
        if (t[i] == t[k])
            k++;
        fail[i] = k;
    }
    string text = s + s;
    for (int i = 0, k = 0; i + 1 < (int)text.size(); i++) {
        while (k > 0 && text[i] != t[k])
            k = fail[k - 1];
        if (text[i] == t[k])
            k++;
        if (k == n) {
            int start = i - n + 1;
            printf("%d\n", (n - start) % n);
            return 0;
        }
    }
    printf("-1\n");
}
