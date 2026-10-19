#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const char* MEDALS[] = {"gold", "silver", "bronze"};
const int PER_MEDAL = 4;
const int PRIZE = 5;

int main() {
    ios::sync_with_stdio(false);
    map<string, string> medal;
    for (const char* kind : MEDALS) {
        for (int i = 0; i < PER_MEDAL; i++) {
            string team;
            cin >> team;
            medal[team] = kind;
        }
    }
    int n;
    cin >> n;
    vector<int> scores(n);
    for (int& right : scores) {
        int k;
        cin >> k;
        right = 0;
        for (int i = 0; i < k; i++) {
            string team, colon, kind;
            cin >> team >> colon >> kind;
            auto it = medal.find(team);
            if (it != medal.end() && it->second == kind) right++;
        }
    }
    int best = *max_element(scores.begin(), scores.end());
    cout << PRIZE * count(scores.begin(), scores.end(), best) << "\n";
    return 0;
}
