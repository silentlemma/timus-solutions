#include <algorithm>
#include <cstdio>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    unordered_map<long long, int> where; // a value and the number of one element holding it
    where.reserve(2 * n);
    vector<long long> a;
    for (int i = 1; i <= n; i++) {
        long long s;
        scanf("%lld", &s);
        if (where.emplace(s, i).second)
            a.push_back(s);
    }
    sort(a.begin(), a.end());
    int m = a.size(), bestLength = 1;
    long long bestFirst = a[0], bestStep = 1;
    for (int i = 0; i < m; i++)
        for (int j = i + 1; j < m; j++) {
            long long d = a[j] - a[i];
            // walk each progression only from its first member, so every
            // pair of neighbours in it is visited once
            if (where.count(a[i] - d))
                continue;
            int length = 2;
            long long last = a[j];
            while (where.count(last + d)) {
                last += d;
                length++;
            }
            if (length > bestLength) {
                bestLength = length;
                bestFirst = a[i];
                bestStep = d;
            }
        }
    printf("%d\n", bestLength);
    for (int k = 0; k < bestLength; k++)
        printf("%d%c", where[bestFirst + k * bestStep], k + 1 == bestLength ? '\n' : ' ');
}
