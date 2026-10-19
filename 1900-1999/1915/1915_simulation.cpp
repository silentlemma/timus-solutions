#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> poppedCoins(const std::vector<int> &operations) {
    int remaining = int(std::count(operations.begin(), operations.end(), -1));
    std::vector<int> answer;
    if (remaining == 0) {
        return answer;
    }
    const int capacity = remaining;
    std::vector<int> coins(capacity);
    answer.reserve(capacity);
    int bottom = 0;
    int size = 0;
    for (int operation : operations) {
        if (remaining == 0) {
            break;
        }
        if (operation > 0) {
            if (size == remaining) {
                bottom = (bottom + 1) % capacity;
                --size;
            }
            coins[(bottom + size) % capacity] = operation;
            ++size;
        } else if (operation == -1) {
            --remaining;
            --size;
            answer.push_back(coins[(bottom + size) % capacity]);
        } else {
            const int extra = std::min(size, remaining - size);
            const int newBottom = (bottom + capacity - extra) % capacity;
            int source = (bottom + size - extra) % capacity;
            int destination = newBottom;
            for (int index = 0; index < extra; ++index) {
                coins[destination] = coins[source];
                if (++source == capacity) {
                    source = 0;
                }
                if (++destination == capacity) {
                    destination = 0;
                }
            }
            bottom = newBottom;
            size += extra;
        }
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int> operations(count);
    for (int &operation : operations) {
        std::cin >> operation;
    }
    for (int coin : poppedCoins(operations)) {
        std::cout << coin << '\n';
    }
    return 0;
}
