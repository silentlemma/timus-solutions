#include <algorithm>
#include <iostream>

// everyone on the far side of Vasya can be made to trip except the two
// seats at the far end, who always come in from their own end
const int SAFE = 2;

int main() {
    int n, k;
    std::cin >> n >> k;
    int far = std::max(k - 1, n - k);
    std::cout << std::max(0, far - SAFE) << "\n";
}
