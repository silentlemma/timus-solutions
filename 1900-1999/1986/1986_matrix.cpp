#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

constexpr long long percent = 100;
constexpr long long scale = 1000000;
constexpr int digits = 6;
using Integer = __int128_t;
using Matrix = std::vector<std::vector<Integer>>;

Integer determinant(Matrix a) {
    const int n = static_cast<int>(a.size());
    if (n == 0)
        return 1;
    Integer previous = 1, sign = 1;
    for (int k = 0; k < n - 1; ++k) {
        int pivot_row = k;
        while (pivot_row < n && a[pivot_row][k] == 0)
            ++pivot_row;
        if (pivot_row == n)
            return 0;
        if (pivot_row != k) {
            std::swap(a[k], a[pivot_row]);
            sign = -sign;
        }
        const Integer pivot = a[k][k];
        for (int row = k + 1; row < n; ++row) {
            for (int col = k + 1; col < n; ++col)
                a[row][col] = (a[row][col] * pivot - a[row][k] * a[k][col]) / previous;
            a[row][k] = 0;
        }
        previous = pivot;
    }
    return sign * a.back().back();
}

std::string solve(const std::string &text) {
    std::map<std::string, std::map<std::string, int>> recipes;
    std::set<std::string> parts;
    std::istringstream input(text);
    std::string line;
    while (std::getline(input, line)) {
        const auto colon = line.find(':');
        if (colon == std::string::npos)
            continue;
        std::istringstream header(line.substr(0, colon)), body(line.substr(colon + 1));
        std::string name, part;
        header >> name;
        int value;
        while (body >> part >> value) {
            recipes[name][part] = value;
            parts.insert(part);
        }
    }
    std::vector<std::string> names, bases;
    for (const auto &recipe : recipes) {
        names.push_back(recipe.first);
        parts.erase(recipe.first);
    }
    bases.assign(parts.begin(), parts.end());
    const int n = static_cast<int>(names.size()), m = static_cast<int>(bases.size());
    Matrix a(n, std::vector<Integer>(n)), numerators(n, std::vector<Integer>(m));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            a[i][j] = (i == j ? percent : 0) - recipes[names[i]][names[j]];
    const Integer denominator = determinant(a);
    for (int col = 0; col < n; ++col)
        for (int base = 0; base < m; ++base) {
            Matrix replaced = a;
            for (int row = 0; row < n; ++row)
                replaced[row][col] = recipes[names[row]][bases[base]];
            numerators[col][base] = determinant(replaced);
        }
    std::ostringstream output;
    for (int row = 0; row < n; ++row) {
        std::vector<long long> units(m);
        long long total = 0;
        int largest = 0;
        for (int base = 0; base < m; ++base) {
            units[base] =
                static_cast<long long>(numerators[row][base] * percent * scale / denominator);
            total += units[base];
            if (numerators[row][base] > numerators[row][largest])
                largest = base;
        }
        units[largest] += percent * scale - total;
        output << names[row] << " :";
        for (int base = 0; base < m; ++base)
            output << ' ' << bases[base] << ' ' << units[base] / scale << '.' << std::setw(digits)
                   << std::setfill('0') << units[base] % scale;
        output << '\n';
    }
    return output.str();
}

int main() {
    std::ostringstream input;
    input << std::cin.rdbuf();
    std::cout << solve(input.str());
}
