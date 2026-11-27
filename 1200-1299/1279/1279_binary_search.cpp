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
    // Filling the lowest sections raises stacks below the final minimum h to h.
    // Some stacks at h may get one more container; initially taller ones stay put.
    // The answer is the largest h with sum(max(0, h - height)) <= K.
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
