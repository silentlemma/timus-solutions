#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    long long capacity;
    std::cin >> count >> capacity;
    long long unused = 0, survivors = 0;
    for (int i = 0; i < count; ++i) {
        long long amount;
        std::cin >> amount;
        if (amount > capacity)
            unused += amount - capacity;
        else
            survivors += capacity - amount;
    }
    std::cout << unused << ' ' << survivors << '\n';
}
