#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

struct Account {
    std::string password;
    bool online;
};

std::vector<std::string> process(const std::vector<std::vector<std::string>> &commands) {
    std::unordered_map<std::string, Account> accounts;
    std::vector<std::string> replies;
    for (const auto &command : commands) {
        const auto &action = command[0];
        const auto &name = command[1];
        auto found = accounts.find(name);
        std::string reply;
        if (action == "register") {
            if (found != accounts.end())
                reply = "fail: user already exists";
            else {
                accounts.emplace(name, Account{command[2], false});
                reply = "success: new user added";
            }
        } else if (action == "login") {
            if (found == accounts.end())
                reply = "fail: no such user";
            else if (found->second.password != command[2])
                reply = "fail: incorrect password";
            else if (found->second.online)
                reply = "fail: already logged in";
            else {
                found->second.online = true;
                reply = "success: user logged in";
            }
        } else {
            if (found == accounts.end())
                reply = "fail: no such user";
            else if (!found->second.online)
                reply = "fail: already logged out";
            else {
                found->second.online = false;
                reply = "success: user logged out";
            }
        }
        replies.push_back(reply);
    }
    return replies;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<std::vector<std::string>> commands(count);
    for (auto &command : commands) {
        std::string action, name, password;
        std::cin >> action >> name;
        command = {action, name};
        if (action != "logout") {
            std::cin >> password;
            command.push_back(password);
        }
    }
    for (const auto &reply : process(commands))
        std::cout << reply << '\n';
}
