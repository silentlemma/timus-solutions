#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const vector<string> HOUSES = {"Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"};

string trim(const string &s) {
    size_t from = s.find_first_not_of(" \r"), to = s.find_last_not_of(" \r");
    return from == string::npos ? "" : s.substr(from, to - from + 1);
}

int main() {
    string line;
    getline(cin, line);
    int n = stoi(line);
    map<string, vector<string>> lists;
    for (int i = 0; i < n; i++) {
        // names keep their inner spaces, so only the line break is dropped
        string name, house;
        getline(cin, name);
        getline(cin, house);
        if (!name.empty() && name.back() == '\r')
            name.pop_back();
        lists[trim(house)].push_back(name);
    }
    for (size_t h = 0; h < HOUSES.size(); h++) {
        if (h > 0)
            cout << "\n";
        cout << HOUSES[h] << ":\n";
        for (auto &name : lists[HOUSES[h]])
            cout << name << "\n";
    }
}
