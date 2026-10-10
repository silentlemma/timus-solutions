#include <cstdio>
#include <vector>

// rows of the maze are at most this long
const int WIDEST = 820;

int cols;
std::vector<char> freeCell;

// breadth-first search; the free cells form a tree, so distances along it
// are the only paths; returns the last cell reached and its distance
std::pair<int, int> farthest(int start) {
    std::vector<int> dist(freeCell.size(), -1), queue = {start};
    dist[start] = 0;
    const int steps[] = {1, -1, cols, -cols};
    for (size_t head = 0; head < queue.size(); head++)
        for (int s : steps) {
            int next = queue[head] + s;
            if (freeCell[next] && dist[next] < 0) {
                dist[next] = dist[queue[head]] + 1;
                queue.push_back(next);
            }
        }
    return {queue.back(), dist[queue.back()]};
}

int main() {
    int width, height;
    if (scanf("%d %d", &width, &height) != 2)
        return 0;
    // a border of walls around the maze keeps every neighbour in range
    cols = width + 2;
    freeCell.assign((size_t)(height + 2) * cols, 0);
    static char row[WIDEST + 2];
    int start = -1;
    for (int r = 1; r <= height; r++) {
        if (scanf("%s", row) != 1)
            return 0;
        for (int c = 1; c <= width; c++)
            if (row[c - 1] == '.') {
                freeCell[r * cols + c] = 1;
                if (start < 0)
                    start = r * cols + c;
            }
    }
    // the farthest cell from any cell is an end of a longest path
    int end = farthest(start).first;
    printf("%d\n", farthest(end).second);
}
