#include <iostream>
#include <string>

using namespace std;

// the counts for N = 1 and N = 2; from N = 3 on, 1575 and N - 3 zeros
const string SMALL[] = {"", "14", "155"};
const int SHORT = 3;
const string BASE = "1575";

int main() {
    int n;
    cin >> n;
    if (n < SHORT)
        cout << SMALL[n] << "\n";
    else
        cout << BASE << string(n - SHORT, '0') << "\n";
}
