#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string p, q;
    cin >> n >> p >> q;
    // A xor B equals A + B exactly when no position holds two ones. With a
    // equal to p, b follows q up to a 0 that becomes 1, then zeros, and that
    // prefix of q must avoid the ones of p, so it ends before the first clash
    int clash = 0;
    while (clash < n && !(p[clash] == '1' && q[clash] == '1'))
        clash++;
    for (int j = clash - 1; j >= 0; j--)
        if (p[j] == '0' && q[j] == '0') {
            cout << p << "\n" << q.substr(0, j) << '1' << string(n - j - 1, '0') << "\n";
            return 0;
        }
    // otherwise the next a after p with b all zeros, or start over
    size_t last = p.rfind('0');
    string a =
        last == string::npos ? string(n, '0') : p.substr(0, last) + '1' + string(n - last - 1, '0');
    cout << a << "\n" << string(n, '0') << "\n";
}
