#include <cstdio>
#include <cstring>

constexpr int RECORDS = 6;
// each name has at most twenty characters, plus the terminating zero.
constexpr int WORD_CAPACITY = 21;

int main() {
    char models[RECORDS][WORD_CAPACITY];
    int prices[RECORDS];
    for (int i = 0; i < RECORDS; ++i) {
        char friend_name[WORD_CAPACITY];
        std::scanf("%20s%20s%d", friend_name, models[i], &prices[i]);
    }
    // with only six records, a pairwise scan avoids hash tables and allocations.
    int best = 0, best_count = 0, best_price = 0;
    for (int i = 0; i < RECORDS; ++i) {
        int count = 0, price = prices[i];
        for (int j = 0; j < RECORDS; ++j) {
            if (std::strcmp(models[i], models[j]) == 0) {
                ++count;
                if (prices[j] < price)
                    price = prices[j];
            }
        }
        if (count > best_count || (count == best_count && price < best_price) ||
            (count == best_count && price == best_price &&
             std::strcmp(models[i], models[best]) < 0)) {
            best = i;
            best_count = count;
            best_price = price;
        }
    }
    std::puts(models[best]);
}
