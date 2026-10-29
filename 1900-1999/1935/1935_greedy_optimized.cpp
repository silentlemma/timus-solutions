#include <cstdio>

// the sum and the maximum are taken as scanf reads the numbers
int main() {
    int count;
    if (std::scanf("%d", &count) != 1) {
        return 0;
    }
    int total = 0;
    int largest = 0;
    for (int i = 0; i < count; ++i) {
        int clearance;
        std::scanf("%d", &clearance);
        total += clearance;
        if (clearance > largest) {
            largest = clearance;
        }
    }
    std::printf("%d\n", total + largest);
}
