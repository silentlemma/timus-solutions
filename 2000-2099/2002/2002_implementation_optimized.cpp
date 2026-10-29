#include <cstdio>
#include <cstring>
#include <string>
#include <unordered_map>

constexpr int MAX_TOKEN_LENGTH = 30;

struct Account {
    std::string password;
    bool online;
};

int main() {
    int count;
    scanf("%d", &count);
    std::unordered_map<std::string, Account> accounts;
    for (int i = 0; i < count; ++i) {
        // every request is read with scanf into fixed buffers and answered at once
        char action[MAX_TOKEN_LENGTH + 1];
        char name[MAX_TOKEN_LENGTH + 1];
        char password[MAX_TOKEN_LENGTH + 1];
        scanf("%30s%30s", action, name);
        if (std::strcmp(action, "logout") != 0) {
            scanf("%30s", password);
        }
        auto found = accounts.find(name);
        const char *reply;
        if (std::strcmp(action, "register") == 0) {
            if (found != accounts.end()) {
                reply = "fail: user already exists";
            } else {
                accounts.emplace(name, Account{password, false});
                reply = "success: new user added";
            }
        } else if (std::strcmp(action, "login") == 0) {
            if (found == accounts.end()) {
                reply = "fail: no such user";
            } else if (found->second.password != password) {
                reply = "fail: incorrect password";
            } else if (found->second.online) {
                reply = "fail: already logged in";
            } else {
                found->second.online = true;
                reply = "success: user logged in";
            }
        } else {
            if (found == accounts.end()) {
                reply = "fail: no such user";
            } else if (!found->second.online) {
                reply = "fail: already logged out";
            } else {
                found->second.online = false;
                reply = "success: user logged out";
            }
        }
        puts(reply);
    }
}
