#include <iostream>
#include <string>

const int NOTES[] = {10, 50, 100, 500, 1000, 5000};

int main() {
    long long total = 0, smallest = 0;
    for (int note : NOTES) {
        long long count;
        if (!(std::cin >> count)) return 0;
        total += count * note;
        if (count > 0 && smallest == 0) smallest = note;
    }
    long long price;
    std::cin >> price;
    // k tickets fit when k * price <= total, and taking away the smallest
    // note must leave too little: total - smallest < k * price
    long long low = (total - smallest) / price + 1, high = total / price;
    std::string line;
    for (long long k = low; k <= high; k++) {
        if (k > low) line += ' ';
        line += std::to_string(k);
    }
    std::cout << high - low + 1 << "\n" << line << "\n";
    return 0;
}
