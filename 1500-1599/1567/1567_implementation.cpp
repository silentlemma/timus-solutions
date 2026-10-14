#include <iostream>
#include <string>
using namespace std;

// the characters of each key in the order of presses; the space has a key of
// its own
const string KEYS[] = {"abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " "};

int main() {
    // the whole first line, spaces included; anything else costs nothing
    string line;
    getline(cin, line);
    int total = 0;
    for (char c : line)
        for (const string &key : KEYS) {
            size_t at = key.find(c);
            if (at != string::npos)
                total += at + 1;
        }
    cout << total << endl;
}
