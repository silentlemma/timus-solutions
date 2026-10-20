#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int suits, ranks, rows;
    std::cin >> suits >> ranks >> rows;
    const int total = suits * ranks;
    std::vector<int> left(total, -1);
    std::vector<int> degree(total, 1);
    for (int card = 0; card < total; card += ranks) {
        degree[card] = 0;
    }

    for (int row = 0; row < rows; ++row) {
        int length;
        std::cin >> length;
        int previous = -1;
        for (int position = 0; position < length; ++position) {
            int suit, rank;
            std::cin >> suit >> rank;
            const int card = (suit - 1) * ranks + rank - 1;
            left[card] = previous;
            if (previous != -1) {
                ++degree[previous];
            }
            previous = card;
        }
    }

    std::vector<int> order;
    order.reserve(total);
    for (int card = 0; card < total; ++card) {
        if (degree[card] == 0) {
            order.push_back(card);
        }
    }
    for (std::size_t head = 0; head < order.size(); ++head) {
        const int card = order[head];
        // The two prerequisites may give parallel edges to the same card.
        if ((card + 1) % ranks != 0 && --degree[card + 1] == 0) {
            order.push_back(card + 1);
        }
        if (left[card] != -1 && --degree[left[card]] == 0) {
            order.push_back(left[card]);
        }
    }

    if (order.size() != static_cast<std::size_t>(total)) {
        std::cout << "NO\n";
        return 0;
    }
    std::cout << "YES\n";
    for (int card : order) {
        std::cout << card / ranks + 1 << ' ' << card % ranks + 1 << '\n';
    }
}
