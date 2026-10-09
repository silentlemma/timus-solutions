#include <iostream>
#include <string>

int main() {
    int n;
    std::string marks;
    if (!(std::cin >> n >> marks))
        return 0;
    int k = (int)marks.size();
    // multiply n, n - k, ... while the factor stays positive
    long long product = 1;
    for (int factor = n; factor > 0; factor -= k)
        product *= factor;
    std::cout << product << "\n";
}
