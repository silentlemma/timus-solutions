#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>

constexpr int MAX_EXPONENT = 30;
const std::string ADMIN = "admin";

struct Player {
    int good = 0;
    int fun = 0;
    bool online = false;
};

// Writes value as root^exponent with the largest possible exponent.
std::pair<long long, int> perfect_power(long long value) {
    for (int exponent = MAX_EXPONENT; exponent > 1; --exponent) {
        const long long guess = std::llround(std::pow(double(value), 1.0 / exponent));
        for (long long root = std::max(2LL, guess - 1); root <= guess + 1; ++root) {
            long long power = 1;
            for (int i = 0; i < exponent && power <= value; ++i) power *= root;
            if (power == value) return {root, exponent};
        }
    }
    return {value, 1};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, max_length, multiplier, divisor;
    std::cin >> n >> max_length >> multiplier >> divisor;
    const double log_good = std::log(multiplier);
    const double log_fun = std::log(divisor);
    // A^g = B^f exactly when both are powers of one root with matching
    // exponents; a base of 1 contributes nothing.
    bool related = true;
    long long scale_good = multiplier > 1;
    long long scale_fun = divisor > 1;
    if (multiplier > 1 && divisor > 1) {
        const auto good_root = perfect_power(multiplier);
        const auto fun_root = perfect_power(divisor);
        related = good_root.first == fun_root.first;
        scale_good = good_root.second;
        scale_fun = fun_root.second;
    }
    std::unordered_map<std::string, Player> players;
    players[ADMIN].online = true;
    int online = 1;
    int total_good = 0;
    int total_fun = 0;
    std::string line;
    std::getline(std::cin, line);

    for (int query = 0; query < n; ++query) {
        std::getline(std::cin, line);
        const auto name_begin = line.find(' ') + 1;
        const auto name_end = line.find(':', name_begin);
        const std::string author = line.substr(name_begin, name_end - name_begin);
        const auto command_begin = line.find('/', name_end) + 1;
        const std::string command = line.substr(command_begin);
        Player &player = players[author];
        const char kind = command[0];

        if (kind == 'j') {
            if (player.online) {
                std::cout << "Failed: " << author << " is already on the server\n";
            } else {
                player.good -= total_good;
                player.fun -= total_fun;
                player.online = true;
                ++online;
                std::cout << "Successful\n";
            }
        } else if (kind == 'q') {
            player.good += total_good;
            player.fun += total_fun;
            player.online = false;
            --online;
            std::cout << "Successful\n";
        } else if (kind == 'o') {
            std::cout << "There are " << online << " players on the server\n";
        } else if (kind == 's' || kind == 'w') {
            const auto space = command.find(' ');
            const std::string message = space == std::string::npos ? "" : command.substr(space + 1);
            const int good = static_cast<int>(std::count(message.begin(), message.end(), 'g'));
            const int fun = static_cast<int>(message.size() / 2) - good;
            if (kind == 's') {
                // Online players share the totals; cancel the author's own message.
                total_good += good;
                total_fun += fun;
                player.good -= good;
                player.fun -= fun;
                std::cout << author << ": " << message << '\n';
            } else {
                const auto begin = command.find('<') + 1;
                const auto end = command.find('>', begin);
                const std::string target = command.substr(begin, end - begin);
                const auto recipient = players.find(target);
                if (recipient != players.end() && recipient->second.online) {
                    recipient->second.good += good;
                    recipient->second.fun += fun;
                }
                std::cout << author << " (to " << target << "): " << message << '\n';
            }
        } else {
            if (author != ADMIN) {
                std::cout << "Failed: you have no such rights\n";
                continue;
            }
            const auto begin = command.find('<') + 1;
            const auto end = command.find('>', begin);
            const std::string target = command.substr(begin, end - begin);
            const auto next = command.find('<', end);
            const bool pair = next != std::string::npos;
            const std::string first = pair ? target : ADMIN;
            const std::string second =
                pair ? command.substr(next + 1, command.find('>', next) - next - 1) : target;
            const auto left = players.find(first);
            const auto right = players.find(second);
            if (left == players.end() || !left->second.online) {
                std::cout << "Failed: " << first << " is not on the server\n";
            } else if (right == players.end() || !right->second.online) {
                std::cout << "Failed: " << second << " is not on the server\n";
            } else {
                // Subtract integer offsets first: the shared totals cancel exactly.
                const long long good = left->second.good - right->second.good;
                const long long fun = left->second.fun - right->second.fun;
                const bool equal =
                    related ? good * scale_good == fun * scale_fun : good == 0 && fun == 0;
                if (equal) {
                    std::cout << (pair ? "Their luck is equal" : second + " is good") << "\n";
                } else if (good * log_good - fun * log_fun > 0) {
                    std::cout << second << " is a loser\n";
                } else {
                    std::cout << second << " is a lucky guy\n";
                }
            }
        }
    }
}
