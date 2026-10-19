#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Meter {
    const char* name;
    int foot;   // syllables in a foot
    int place;  // place of the stressed syllable, from 1
};

const Meter METERS[] = {{"trochee", 2, 1}, {"iamb", 2, 2}, {"dactyl", 3, 1},
                        {"amphibrach", 3, 2}, {"anapaest", 3, 3}};

vector<bool> stresses(const string& line) {
    vector<bool> out;
    istringstream words(line);
    string word;
    while (words >> word) {
        istringstream parts(word);
        string syllable;
        while (getline(parts, syllable, '-')) {
            if (!syllable.empty()) out.push_back(syllable.find('[') != string::npos);
        }
    }
    return out;
}

int main() {
    int n;
    cin >> n;
    string line;
    getline(cin, line);
    vector<vector<bool>> poem(n);
    for (int i = 0; i < n; i++) {
        getline(cin, line);
        poem[i] = stresses(line);
    }
    for (const Meter& m : METERS) {
        // the last foot may be cut short, so only the place within a foot
        // matters, and every syllable must agree with it
        bool fits = true;
        for (const vector<bool>& verse : poem) {
            for (size_t i = 0; i < verse.size(); i++) {
                if (verse[i] != ((int)(i % m.foot) == m.place - 1)) fits = false;
            }
        }
        if (fits) {
            cout << m.name << "\n";
            return 0;
        }
    }
    cout << "not a poem\n";
    return 0;
}
