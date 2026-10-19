#include <iostream>
#include <string>

using namespace std;

constexpr int HOSTS = 2;  // Marshall and Lily
constexpr int UNLUCKY = 13;
constexpr int PRICE = 100;
const string PLUS = "+one";

int main() {
    int n;
    cin >> n;
    int people = HOSTS;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        bool partner = s.size() > PLUS.size() && s.substr(s.size() - PLUS.size()) == PLUS;
        people += partner ? 2 : 1;
    }
    if (people == UNLUCKY) people++;  // a dummy takes the extra seat
    cout << people * PRICE << "\n";
}
