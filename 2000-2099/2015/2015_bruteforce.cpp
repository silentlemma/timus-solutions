#include <array>
#include <iostream>
#include <vector>

constexpr int APARTMENT_FIELDS = 3;
using Friend = std::array<int, 2>;
using Apartment = std::array<int, APARTMENT_FIELDS>;

std::array<int, 2> solve(int budget, const std::array<int, 2> &alone,
                         const std::vector<Friend> &friends,
                         const std::vector<Apartment> &apartments) {
    int best = -1;
    std::array<int, 2> choice{};
    for (int i = 0; i < static_cast<int>(apartments.size()); ++i) {
        auto [rooms, price, benefit] = apartments[i];
        if (price <= budget) {
            int score = benefit + alone[rooms - 1];
            if (score > best) {
                best = score;
                choice = {i + 1, 0};
            }
        }
        if (rooms == 2 && price <= 2 * budget) {
            for (int j = 0; j < static_cast<int>(friends.size()); ++j) {
                if (price <= 2 * friends[j][0]) {
                    int score = benefit + friends[j][1];
                    if (score > best) {
                        best = score;
                        choice = {i + 1, j + 1};
                    }
                }
            }
        }
    }
    return choice;
}

int main() {
    int budget, n, m;
    std::array<int, 2> alone;
    std::cin >> budget >> alone[0] >> alone[1] >> n;
    std::vector<Friend> friends(n);
    for (auto &row : friends)
        std::cin >> row[0] >> row[1];
    std::cin >> m;
    std::vector<Apartment> apartments(m);
    for (auto &row : apartments)
        std::cin >> row[0] >> row[1] >> row[2];
    auto choice = solve(budget, alone, friends, apartments);
    if (choice[0] == 0)
        std::cout << "Forget about apartments. Live in the dormitory.\n";
    else if (choice[1] == 0)
        std::cout << "You should rent the apartment #" << choice[0] << " alone.\n";
    else
        std::cout << "You should rent the apartment #" << choice[0] << " with the friend #"
                  << choice[1] << ".\n";
}
