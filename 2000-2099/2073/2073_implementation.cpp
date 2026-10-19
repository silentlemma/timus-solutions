#include <iostream>
#include <string>

using namespace std;

constexpr int NAME_WIDTH = 30;
constexpr int DATE_WIDTH = 8;
const string LETTERS = "ABCDEFGHIJKLM";

string readLine() {
    string s;
    getline(cin, s);
    while (!s.empty() && (s.back() == '\r' || s.back() == ' ')) s.pop_back();
    return s;
}

string pad(const string& s, int width) {
    return s + string(width - s.size(), ' ');
}

int main() {
    string border = "+" + string(NAME_WIDTH, '-') + "+" + string(DATE_WIDTH, '-') + "+" +
                    string(LETTERS.size(), '-') + "+";
    cout << border << "\n";
    cout << "|" << pad("Contest name", NAME_WIDTH) << "|" << pad("Date", DATE_WIDTH) << "|"
         << LETTERS << "|\n";
    cout << border << "\n";
    int n = stoi(readLine());
    for (int c = 0; c < n; c++) {
        string name = readLine(), date = readLine();
        string counts = readLine();
        int p = stoi(counts), s = stoi(counts.substr(counts.find(' ') + 1));
        // '.' for a given problem, 'x' once submitted, 'o' once accepted
        string marks = string(p, '.') + string(LETTERS.size() - p, ' ');
        for (int k = 0; k < s; k++) {
            string submit = readLine();
            int i = submit[0] - 'A';
            if (submit.substr(2) == "Accepted")
                marks[i] = 'o';
            else if (marks[i] != 'o')
                marks[i] = 'x';
        }
        cout << "|" << pad(name, NAME_WIDTH) << "|" << date << "|" << marks << "|\n";
        cout << border << "\n";
    }
}
