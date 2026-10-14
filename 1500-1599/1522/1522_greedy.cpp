#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<long long> a(n), b(n), c(n);
    for (int i = 0; i < n; i++)
        scanf("%lld %lld %lld", &a[i], &b[i], &c[i]);
    // machine B never holds the line, so the line behaves like two machines
    // with times a + b and b + c, where Johnson's rule is optimal: toys
    // faster on the first come first, by its time, the rest by the second
    vector<int> early, late;
    for (int i = 0; i < n; i++)
        (a[i] + b[i] < b[i] + c[i] ? early : late).push_back(i);
    sort(early.begin(), early.end(), [&](int x, int y) { return a[x] + b[x] < a[y] + b[y]; });
    sort(late.begin(), late.end(), [&](int x, int y) { return b[x] + c[x] > b[y] + c[y]; });
    early.insert(early.end(), late.begin(), late.end());
    long long doneA = 0, doneB = 0, doneC = 0;
    for (int i : early) {
        doneA += a[i];
        doneB = max(doneB, doneA) + b[i];
        doneC = max(doneC, doneB) + c[i];
    }
    string out = to_string(doneC) + "\n";
    for (int i = 0; i < n; i++)
        out += to_string(early[i] + 1) + (i + 1 < n ? " " : "\n");
    fputs(out.c_str(), stdout);
}
