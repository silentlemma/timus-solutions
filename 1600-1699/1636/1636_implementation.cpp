#include <cstdio>

const int PROBLEMS = 10;
const int PER_ATTEMPT = 20;  // minutes for each rejected attempt

int main() {
    int t1, t2;
    if (scanf("%d %d", &t1, &t2) != 2)
        return 0;
    int clean = t2;
    for (int i = 0; i < PROBLEMS; i++) {
        int attempts;
        if (scanf("%d", &attempts) != 1)
            return 0;
        clean -= PER_ATTEMPT * attempts;
    }
    // without the rejected attempts ZZZ wins only with strictly less time
    puts(clean < t1 ? "Dirty debug :(" : "No chance.");
}
