#include <cstdio>
#include <iostream>
#include <map>
#include <string>

const double R = 8.314;

int main() {
    // lines "X = value"
    std::map<std::string, long long> known;
    std::string name, eq;
    long long value;
    while (std::cin >> name >> eq >> value) known[name] = value;
    // p V = n R T, with V and T strictly positive
    if (!known.count("p")) {
        printf("p = %.6f\n", known["n"] * R * known["T"] / known["V"]);
    } else if (!known.count("n")) {
        printf("n = %.6f\n", known["p"] * known["V"] / (R * known["T"]));
    } else {
        // the unknown is V (beside p) or T (beside n R), and both must be
        // positive: a zero factor leaves 0 = 0 or a contradiction
        bool findV = !known.count("V");
        long long p = known["p"], n = known["n"];
        long long factor = findV ? p : n, other = findV ? n : p;
        if (factor == 0) {
            puts(other == 0 ? "undefined" : "error");
        } else if (other == 0) {
            puts("error");
        } else if (findV) {
            printf("V = %.6f\n", n * R * known["T"] / p);
        } else {
            printf("T = %.6f\n", p * known["V"] / (n * R));
        }
    }
    return 0;
}
