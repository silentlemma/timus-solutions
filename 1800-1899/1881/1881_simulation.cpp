#include <iostream>
#include <string>

using namespace std;

int main() {
    int h, w, n;
    cin >> h >> w >> n;
    int lines = 1, used = -1;
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        // a word after another one on the line needs a space before it
        if (used + 1 + (int)word.size() > w) {
            lines++;
            used = -1;
        }
        used += 1 + word.size();
    }
    cout << (lines + h - 1) / h << "\n";
    return 0;
}
