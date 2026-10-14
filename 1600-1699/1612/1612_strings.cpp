#include <cctype>
#include <cstdio>
#include <string>
using namespace std;

int main() {
    int trams = 0, trolleys = 0;
    string word;
    // a word is a run of letters; anything else ends it
    for (int c = getchar();; c = getchar()) {
        if (c != EOF && islower(c)) {
            word += (char)c;
            continue;
        }
        trams += word == "tram";
        trolleys += word == "trolleybus";
        word.clear();
        if (c == EOF)
            break;
    }
    if (trams > trolleys)
        printf("Tram driver\n");
    else if (trolleys > trams)
        printf("Trolleybus driver\n");
    else
        printf("Bus driver\n");
}
