#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int MAX_OPERATIONS = 100000, COMMAND_SIZE = 8, PRICE_SIZE = 16;
constexpr int CENTS = 100, DECIMAL_PLACES = 2, BID = -1, DEL = -2;

struct Operation {
    int price, amount;
};

int price(const char *text) {
    int whole = 0, fraction = 0, digits = 0;
    while (*text >= '0' && *text <= '9')
        whole = whole * 10 + *text++ - '0';
    if (*text == '.') {
        ++text;
        while (*text >= '0' && *text <= '9') {
            fraction = fraction * 10 + *text++ - '0';
            ++digits;
        }
    }
    while (digits++ < DECIMAL_PLACES)
        fraction *= 10;
    return whole * CENTS + fraction;
}

int main() {
    std::vector<Operation> operations;
    std::vector<int> prices;
    operations.reserve(MAX_OPERATIONS);
    prices.reserve(MAX_OPERATIONS);
    char command[COMMAND_SIZE], token[PRICE_SIZE];
    while (scanf("%7s", command) == 1 && command[0] != 'Q') {
        scanf("%15s", token);
        int value = price(token), amount;
        if (command[0] == 'B') {
            amount = BID;
            prices.push_back(value);
        } else if (command[0] == 'D')
            amount = DEL;
        else
            scanf("%d", &amount);
        operations.push_back({value, amount});
    }
    std::sort(prices.begin(), prices.end());
    prices.erase(std::unique(prices.begin(), prices.end()), prices.end());
    std::vector<int> tree(prices.size() + 1);
    int active = 0;
    long long revenue = 0;
    for (const auto &operation : operations) {
        int index =
            std::lower_bound(prices.begin(), prices.end(), operation.price) - prices.begin();
        if (operation.amount < 0) {
            int delta = operation.amount == BID ? 1 : -1;
            active += delta;
            for (++index; index < static_cast<int>(tree.size()); index += index & -index) {
                tree[index] += delta;
            }
        } else {
            // lower_bound counts strictly cheaper prices, retaining equal bids for the sale.
            int cheaper = 0;
            for (; index > 0; index -= index & -index)
                cheaper += tree[index];
            revenue += std::min(operation.amount, active - cheaper);
        }
    }
    printf("%lld.%02lld\n", revenue / CENTS, revenue % CENTS);
}
