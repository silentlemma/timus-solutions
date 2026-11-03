#include <cstdio>
#include <map>
#include <string>
#include <utility>

const int MAX_PRODUCTS = 1000, MAX_CUSTOMERS = 1000, NAME_SIZE = 21;
struct Customer {
    int product, wanted, seen;
};
int stock[MAX_PRODUCTS + 1];
Customer line[MAX_CUSTOMERS];

int main() {
    int m;
    if (scanf("%d", &m) != 1)
        return 0;
    std::map<std::string, int> ids;
    char name[NAME_SIZE];
    for (int id = 1; id <= m; id++) {
        scanf("%d %*s %20s", &stock[id], name);
        ids[name] = id;
    }
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int amount;
        scanf("%d %*s %20s", &amount, name);
        auto found = ids.find(name);
        line[i] = {found == ids.end() ? 0 : found->second, amount, -1};
    }
    int front = 0, minutes = 0;
    while (front < n) {
        Customer &customer = line[front];
        int &left = stock[customer.product];
        minutes++;
        if (left >= customer.wanted)
            left -= customer.wanted;
        else if (left == customer.seen)
            left = 0;
        else if (left > 0) {
            customer.seen = left;
            if (front + 1 == n)
                break;
            std::swap(line[front], line[front + 1]);
            continue;
        }
        front++;
    }
    printf("%d\n", minutes);
}
