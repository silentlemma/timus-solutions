#include <cstdio>
#include <vector>

constexpr int MAX_DESTROYED = 10000;

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    // Original labels never exceed 1e9, so 32-bit entries suffice.
    std::vector<int> gone;
    gone.reserve(MAX_DESTROYED);
    for (int event = 0; event < m; ++event) {
        char command;
        int room;
        scanf(" %c%d", &command, &room);
        int low = 0, high = gone.size();
        while (low < high) {
            int middle = (low + high) / 2;
            if (gone[middle] - middle <= room)
                low = middle + 1;
            else
                high = middle;
        }
        int original = room + low;
        if (command == 'D')
            gone.insert(gone.begin() + low, original);
        else
            printf("%d\n", original);
    }
}
