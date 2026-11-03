#include <cstdio>
#include <initializer_list>

const int MIN_HEIGHT = 170, MAX_HEIGHT = 200, HEIGHTS = MAX_HEIGHT - MIN_HEIGHT + 1;
const int MAX_SIZE = 9;
int counts[HEIGHTS], grid[MAX_SIZE][MAX_SIZE], current = HEIGHTS - 1, middle;

void fill(int dr, int dc) {
    for (int sr : {-1, 1}) {
        if (dr == 0 && sr < 0)
            continue;
        for (int sc : {-1, 1}) {
            if (dc == 0 && sc < 0)
                continue;
            while (counts[current] == 0)
                current--;
            grid[middle + sr * dr][middle + sc * dc] = MIN_HEIGHT + current;
            counts[current]--;
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    middle = n / 2;
    for (int i = 0; i < n * n; i++) {
        int height;
        scanf("%d", &height);
        counts[height - MIN_HEIGHT]++;
    }
    // The rank (nearer,farther) grows outwards on each side of every line.
    // Emit its mirror cells directly instead of sorting their coordinates.
    for (int near = 0; near <= middle; near++)
        for (int far = near; far <= middle; far++) {
            fill(near, far);
            if (near != far)
                fill(far, near);
        }
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            printf("%d%c", grid[r][c], c + 1 == n ? '\n' : ' ');
}
