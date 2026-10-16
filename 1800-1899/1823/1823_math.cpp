#include <cstdio>
#include <iostream>
#include <map>
#include <string>

const long long R_NUM = 8314, R_DEN = 1000, SCALE = 1000000;

void printValue(const char* name, long long numerator, long long denominator) {
    long long value = (numerator * SCALE + denominator / 2) / denominator;
    printf("%s = %lld.%06lld\n", name, value / SCALE, value % SCALE);
}

int main() {
    // lines "X = value"
    std::map<std::string, long long> known;
    std::string name, eq;
    long long value;
    while (std::cin >> name >> eq >> value) known[name] = value;
    // p V = n R T, with V and T strictly positive
    if (!known.count("p")) {
        printValue("p", known["n"] * R_NUM * known["T"], R_DEN * known["V"]);
    } else if (!known.count("n")) {
        printValue("n", known["p"] * known["V"] * R_DEN, R_NUM * known["T"]);
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
            printValue("V", n * R_NUM * known["T"], R_DEN * p);
        } else {
            printValue("T", p * known["V"] * R_DEN, n * R_NUM);
        }
    }
    return 0;
}
