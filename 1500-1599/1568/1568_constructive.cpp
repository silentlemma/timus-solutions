#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> cars(n), where(n + 1), run(n + 1, 0);
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &cars[i]) != 1)
            return 0;
        where[cars[i]] = i;
    }
    // cut 1..n into the fewest runs of numbers that already stand in order, and a
    // new run starts where car v + 1 stands before car v
    for (int car = 2; car <= n; car++)
        run[car] = run[car - 1] + (where[car] < where[car - 1]);
    int passes = 0;
    while ((1 << passes) <= run[n])
        passes++;
    printf("%d\n", passes);
    for (int bit = 0;; bit++) {
        for (int i = 0; i < n; i++)
            printf(i ? " %d" : "%d", cars[i]);
        printf("\n");
        if (bit == passes)
            break;
        // pass b sends the cars whose run number has bit b set to the right, and
        // like a radix sort from the low bit up, the passes leave the runs in order
        vector<int> next;
        for (int side = 0; side < 2; side++)
            for (int car : cars)
                if ((run[car] >> bit & 1) == side)
                    next.push_back(car);
        cars = next;
    }
}
