#include <iostream>
#include <vector>

using namespace std;

int ceilDivide(int numerator, int denominator) {
    int result = numerator / denominator;
    if (numerator > 0 && numerator % denominator != 0)
        ++result;
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int height, width;
    if (!(cin >> height >> width))
        return 0;
    int far = height + width;
    vector<int> distances(height * width), last(width, -far);
    for (int row = 0; row < height; ++row) {
        for (int column = 0; column < width; ++column) {
            char bit;
            cin >> bit;
            if (bit == '1')
                last[column] = row;
            distances[row * width + column] = row - last[column];
        }
    }
    vector<int> following(width, height + far);
    for (int row = height - 1; row >= 0; --row) {
        for (int column = 0; column < width; ++column) {
            int &value = distances[row * width + column];
            if (value == 0)
                following[column] = row;
            else if (following[column] - row < value)
                value = following[column] - row;
        }
    }
    vector<int> costs(width), intercepts(width), sites(width), starts(width);
    for (int row = 0; row < height; ++row) {
        int used = 0;
        for (int q = 0; q < width; ++q) {
            int vertical = distances[row * width + q];
            if (vertical >= far)
                continue;
            costs[q] = vertical * vertical;
            intercepts[q] = costs[q] + q * q;
            int first = 0;
            while (used > 0) {
                int p = sites[used - 1];
                first = ceilDivide(intercepts[q] - intercepts[p], 2 * (q - p));
                if (first > starts[used - 1])
                    break;
                --used;
            }
            if (used == 0)
                first = 0;
            sites[used] = q;
            starts[used++] = first;
        }
        int current = 0;
        for (int x = 0; x < width; ++x) {
            while (current + 1 < used && starts[current + 1] <= x)
                ++current;
            int p = sites[current], delta = x - p;
            if (x != 0)
                cout << ' ';
            cout << delta * delta + costs[p];
        }
        cout << '\n';
    }
}
