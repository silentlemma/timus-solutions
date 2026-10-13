#include <cstdio>
#include <vector>

using namespace std;

int main() {
    long long n;
    int m;
    scanf("%lld %d", &n, &m);
    vector<long long> gone; // original numbers of destroyed rooms, sorted
    for (int i = 0; i < m; i++) {
        char letter;
        long long x;
        scanf(" %c %lld", &letter, &x);
        // gone[j] - j <= x holds for a prefix: the rooms gone below room x
        int lo = 0, hi = gone.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (gone[mid] - mid <= x)
                lo = mid + 1;
            else
                hi = mid;
        }
        long long original = x + lo;
        if (letter == 'D')
            gone.insert(gone.begin() + lo, original);
        else
            printf("%lld\n", original);
    }
}
