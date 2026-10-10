#include <iostream>
#include <string>

// sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for odd k
std::string sine(int n) {
    std::string s;
    for (int k = 1; k <= n; k++) {
        s += "sin(" + std::to_string(k);
        if (k < n)
            s += k % 2 ? "-" : "+";
    }
    return s + std::string(n, ')');
}

int main() {
    int n;
    if (!(std::cin >> n))
        return 0;
    std::string out(n - 1, '(');
    for (int i = 1; i <= n; i++)
        out += sine(i) + "+" + std::to_string(n - i + 1) + (i < n ? ")" : "");
    std::cout << out << "\n";
}
