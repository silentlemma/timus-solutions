#include <cstdio>

constexpr int ALICE = 1;

int main() {
    long long length, total, va, vb;
    int n;
    scanf("%lld %lld %lld %lld %d", &length, &total, &va, &vb, &n);
    // riding in opposite directions, they meet whenever the distance ridden by
    // both together reaches a new multiple of the length; the intervals of one
    // kid do not overlap, so their durations add up
    long long resting[2] = {0, 0};
    for (int i = 0; i < n; i++) {
        long long kid, start, duration;
        scanf("%lld %lld %lld", &kid, &start, &duration);
        resting[kid == ALICE ? 0 : 1] += duration;
    }
    long long ridden = va * (total - resting[0]) + vb * (total - resting[1]);
    printf("%lld\n", ridden / length);
}
