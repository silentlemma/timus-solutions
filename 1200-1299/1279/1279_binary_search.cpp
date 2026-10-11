#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n, m;
    long long k;
    scanf("%d %d %lld", &n, &m, &k);
    std::vector<long long> heights(n * m);
    for (long long &h : heights)
        scanf("%lld", &h);
    // filling the lowest sections first raises every section to a level h
    // and some of them one higher, so the answer is the largest h whose
    // missing containers, the sum of h - height below h, fit into K
    long long lo = *std::min_element(heights.begin(), heights.end()), hi = lo + k;
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2, need = 0;
        for (long long h : heights)
            if (h < mid)
                need += mid - h;
        if (need <= k)
            lo = mid;
        else
            hi = mid - 1;
    }
    printf("%lld\n", lo);
}
