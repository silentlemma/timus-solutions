#include <cstdio>
#include <vector>

// marks in free (clearing it) every cell reachable from start through cells
// where free is set, moving along the given steps; returns them
std::vector<int> flood(int start, std::vector<char> &free, const std::vector<int> &steps) {
    std::vector<int> reached{start}, stack{start};
    free[start] = 0;
    int size = free.size();
    while (!stack.empty()) {
        int c = stack.back();
        stack.pop_back();
        for (int d : steps) {
            int n = c + d;
            if (n >= 0 && n < size && free[n]) {
                free[n] = 0;
                reached.push_back(n);
                stack.push_back(n);
            }
        }
    }
    return reached;
}

int main() {
    int w, h, x, y;
    scanf("%d %d %d %d", &w, &h, &x, &y);
    // the map padded by a ring of outside cells
    int pw = w + 2, size = (w + 2) * (h + 2);
    std::vector<char> land(size, 0), sea(size, 0);
    for (int i = 1; i <= h; i++)
        for (int j = 1; j <= w;) {
            int c = getchar();
            if (c == EOF)
                break;
            if (c == '#' || c == '.') {
                land[i * pw + j] = c == '#';
                sea[i * pw + j] = c == '.';
                j++;
            }
        }
    std::vector<int> step4{1, -1, pw, -pw};
    std::vector<int> step8{1, -1, pw, -pw, pw + 1, pw - 1, -pw + 1, -pw - 1};
    // the sacred sea: sea cells joined to the drowning point by 8 directions
    std::vector<char> free(size, 1);
    int start = y * pw + x;
    if (sea[start])
        for (int c : flood(start, sea, step8))
            free[c] = 0;
    // an eight-connected sea stops every four-connected path, so what the
    // outside cannot reach without crossing the sacred sea lies inside it
    for (int c : flood(0, free, step4))
        land[c] = 0;
    int count = 0;
    for (int c = 0; c < size; c++)
        if (land[c]) {
            count++;
            flood(c, land, step4);
        }
    printf("%d\n", count);
}
