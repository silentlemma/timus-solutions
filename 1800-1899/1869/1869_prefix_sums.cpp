#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int SEATS = 36;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    // change[k] is how many people get on at station k minus how many get
    // off there; the eastbound and westbound trains are counted apart
    vector<long long> east(n + 1), west(n + 1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int a;
            scanf("%d", &a);
            if (i < j) {
                east[i] += a;
                east[j] -= a;
            } else if (i > j) {
                west[j] += a;
                west[i] -= a;
            }
        }
    }
    long long best = 0, load_e = 0, load_w = 0;
    for (int k = 0; k < n; k++) {
        load_e += east[k];
        load_w += west[k];
        best = max(best, max(load_e, load_w));
    }
    printf("%lld\n", (best + SEATS - 1) / SEATS);
    return 0;
}
