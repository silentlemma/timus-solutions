#include <cstdio>

int main() {
    long long depth, position;
    if (std::scanf("%lld %lld", &depth, &position) != 2)
        return 0;

    long long left = 1, right = 1;
    long long leadingLeft = depth - 1;
    // Follow the path backwards, tracking the coefficients of the two bounds.
    for (long long path = position - 1; path > 0; path >>= 1) {
        if (path & 1)
            right += left;
        else
            left += right;
        --leadingLeft;
    }
    std::printf("%lld %lld\n", right, left + leadingLeft * right);
}
