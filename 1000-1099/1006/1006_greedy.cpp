#include <cstdio>
#include <vector>

const int WIDTH = 50, HEIGHT = 20, MIN_SIDE = 2;
const unsigned char EMPTY = '.';
const unsigned char UPPER_LEFT = 218, UPPER_RIGHT = 191, LOWER_LEFT = 192, LOWER_RIGHT = 217;
const unsigned char VERTICAL = 179, HORIZONTAL = 196;

unsigned char screen[HEIGHT][WIDTH];
bool peeled[HEIGHT][WIDTH];

struct Frame {
    int x, y, side;
};

// A peeled cell is covered by a frame drawn later, so it may hold anything.
bool fits(int x, int y, unsigned char c, int &fresh) {
    if (peeled[y][x])
        return true;
    if (screen[y][x] != c)
        return false;
    fresh++;
    return true;
}

// The frame matches the picture where it is visible and shows something new.
bool frameFits(int x, int y, int side) {
    int last = side - 1, fresh = 0;
    if (!fits(x, y, UPPER_LEFT, fresh) || !fits(x + last, y, UPPER_RIGHT, fresh) ||
        !fits(x, y + last, LOWER_LEFT, fresh) || !fits(x + last, y + last, LOWER_RIGHT, fresh))
        return false;
    for (int i = 1; i < last; i++)
        if (!fits(x + i, y, HORIZONTAL, fresh) || !fits(x + i, y + last, HORIZONTAL, fresh) ||
            !fits(x, y + i, VERTICAL, fresh) || !fits(x + last, y + i, VERTICAL, fresh))
            return false;
    return fresh > 0;
}

void peelCell(int x, int y, int &left) {
    if (!peeled[y][x]) {
        peeled[y][x] = true;
        left--;
    }
}

void peel(int x, int y, int side, int &left) {
    int last = side - 1;
    for (int i = 0; i <= last; i++) {
        peelCell(x + i, y, left);
        peelCell(x + i, y + last, left);
        peelCell(x, y + i, left);
        peelCell(x + last, y + i, left);
    }
}

int main() {
    std::vector<unsigned char> data;
    for (int ch; (ch = getchar()) != EOF;)
        data.push_back(ch);
    int left = 0;
    size_t pos = 0;
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            unsigned char c = EMPTY;
            if (pos < data.size() && data[pos] != '\n' && data[pos] != '\r')
                c = data[pos++];
            screen[y][x] = c;
            left += c != EMPTY;
        }
        while (pos < data.size() && data[pos] != '\n')
            pos++;
        pos++;
    }

    // Undo the drawing: a frame that fits can be the last one drawn among the
    // remaining ones; its cells then may hold anything.
    std::vector<Frame> frames;
    while (left > 0) {
        int before = left;
        for (int y = 0; y < HEIGHT; y++)
            for (int x = 0; x < WIDTH; x++)
                for (int side = MIN_SIDE; x + side <= WIDTH && y + side <= HEIGHT; side++)
                    if (frameFits(x, y, side)) {
                        frames.push_back({x, y, side});
                        peel(x, y, side, left);
                    }
        if (left == before)
            break;
    }

    printf("%d\n", (int)frames.size());
    for (int i = (int)frames.size() - 1; i >= 0; i--)
        printf("%d %d %d\n", frames[i].x, frames[i].y, frames[i].side);
}
