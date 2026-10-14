#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

const int SMALL = 2;

// english, or else the first name of one or two letters that no team
// speaks: at most 100 teams cannot take all 702 of them
string free_language(const set<string> &spoken) {
    if (!spoken.count("english"))
        return "english";
    vector<string> names;
    for (char a = 'a'; a <= 'z'; a++)
        names.push_back(string(1, a));
    for (char a = 'a'; a <= 'z'; a++)
        for (char b = 'a'; b <= 'z'; b++)
            names.push_back(string(1, a) + b);
    for (auto &name : names)
        if (!spoken.count(name))
            return name;
    return "";
}

int main() {
    int n;
    cin >> n;
    vector<string> langs(n);
    for (auto &lang : langs)
        cin >> lang;
    set<string> distinct(langs.begin(), langs.end());
    if ((int)distinct.size() < n) {
        // a third team would overhear two teams of one language
        if (n == SMALL)
            cout << 0 << endl;
        else
            cout << "Impossible" << endl;
    } else if (n == 1) {
        cout << 0 << endl;
    } else if (n == SMALL) {
        cout << 1 << endl << langs[0] << "-" << langs[1] << endl;
    } else {
        // a talk through another team's language is overheard, so every talk
        // goes through a language no team speaks
        string hub = free_language(distinct);
        cout << n << endl;
        for (auto &lang : langs)
            cout << lang << "-" << hub << endl;
    }
}
