#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string BOOK = "dhu"; // letters in the order of the book

int step(char c) { return c == 'u' ? 1 : c == 'd' ? -1 : 0; }

// can a garland at this height end at the ground in exactly `left` links?
// on the ground a link must go up, above it horizontal links can pad
bool finishes(int height, int left) {
    return height == 0 ? left == 0 || left >= 2 : left >= height;
}

// never below the ground, and no horizontal link on it
bool allowed(char c, int height) { return height + step(c) >= 0 && !(c == 'h' && height == 0); }

int main() {
    int n;
    string s;
    cin >> n >> s;
    vector<int> heights(n + 1, 0);
    for (int i = 0; i < n; i++)
        heights[i + 1] = heights[i] + step(s[i]);
    // the last link that can take a larger letter and still be finished
    for (int i = n - 1; i >= 0; i--)
        for (char c : BOOK)
            if (c > s[i] && allowed(c, heights[i]) && finishes(heights[i] + step(c), n - i - 1)) {
                string out = s.substr(0, i) + c;
                int height = heights[i] + step(c);
                // the rest is the smallest garland that still finishes
                for (int left = n - i - 1; left > 0; left--)
                    for (char d : BOOK)
                        if (allowed(d, height) && finishes(height + step(d), left - 1)) {
                            out += d;
                            height += step(d);
                            break;
                        }
                cout << out << "\n";
                return 0;
            }
    cout << "No solution\n";
}
