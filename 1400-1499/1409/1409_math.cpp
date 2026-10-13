#include <iostream>

using namespace std;

int main() {
    int harry, larry;
    cin >> harry >> larry;
    // the last can was shot by both, so each missed the other's count minus one
    cout << larry - 1 << " " << harry - 1 << "\n";
}
