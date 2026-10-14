#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, long long> bags;
    cin >> bags["Blue"] >> bags["Red"] >> bags["Yellow"];
    int k;
    cin >> k;
    // one reagent from each needed bag, chosen independently
    long long ways = 1;
    for (int i = 0; i < k; i++) {
        string color;
        cin >> color;
        ways *= bags[color];
    }
    cout << ways << endl;
}
