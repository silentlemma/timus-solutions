#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int ALPHABET = 256;

int main() {
    int n;
    scanf("%d", &n);
    string text;
    text.reserve(n);
    for (int ch; (int)text.size() < n && (ch = getchar()) != EOF;)
        if (ch > ' ')
            text.push_back((char)ch);
    // the shortest period p of the cyclic string: T is u repeated n / p times
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int k = pi[i - 1];
        while (k > 0 && text[i] != text[k])
            k = pi[k - 1];
        pi[i] = k + (text[i] == text[k]);
    }
    int p = n - pi[n - 1];
    if (n % p != 0)
        p = n;
    pi.clear();
    pi.shrink_to_fit();
    // sort the rotations of u by doubling, all of them distinct
    vector<int> order(p), cls(p), cnt(max(ALPHABET, p), 0), tmp(p), tmpCls(p);
    for (int i = 0; i < p; i++)
        cnt[(unsigned char)text[i]]++;
    for (int i = 1; i < ALPHABET; i++)
        cnt[i] += cnt[i - 1];
    for (int i = p - 1; i >= 0; i--)
        order[--cnt[(unsigned char)text[i]]] = i;
    int classes = 1;
    cls[order[0]] = 0;
    for (int i = 1; i < p; i++) {
        if (text[order[i]] != text[order[i - 1]])
            classes++;
        cls[order[i]] = classes - 1;
    }
    for (int len = 1; len < p && classes < p; len *= 2) {
        // sorted by the second half already: shift each start back by len
        for (int i = 0; i < p; i++)
            tmp[i] = (order[i] - len + p) % p;
        fill(cnt.begin(), cnt.begin() + classes, 0);
        for (int i = 0; i < p; i++)
            cnt[cls[tmp[i]]]++;
        for (int i = 1; i < classes; i++)
            cnt[i] += cnt[i - 1];
        for (int i = p - 1; i >= 0; i--)
            order[--cnt[cls[tmp[i]]]] = tmp[i];
        tmpCls[order[0]] = 0;
        classes = 1;
        for (int i = 1; i < p; i++) {
            int a = order[i], b = order[i - 1];
            if (cls[a] != cls[b] || cls[(a + len) % p] != cls[(b + len) % p])
                classes++;
            tmpCls[a] = classes - 1;
        }
        swap(cls, tmpCls);
    }
    // Kasai: the common prefix with the previous rotation drops by at most one per step
    long long total = 0;
    int h = 0;
    for (int i = 0; i < p; i++) {
        if (cls[i] == 0) {
            h = 0;
            continue;
        }
        int j = order[cls[i] - 1];
        while (h < p && text[(i + h) % p] == text[(j + h) % p])
            h++;
        total += h;
        if (h > 0)
            h--;
    }
    // each rotation of u appears n / p times in a row, with common prefixes of n
    total += (long long)p * (n / p - 1) * n;
    printf("%.3f\n", (double)total / (n - 1));
}
