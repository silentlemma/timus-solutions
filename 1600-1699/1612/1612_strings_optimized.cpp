#include <cstdio>
#include <cstring>
constexpr int LONGEST_TARGET = 10;
int main() {
    // only words no longer than trolleybus can match; longer words need no storage.
    char word[LONGEST_TARGET + 1] = {};
    int length = 0, trams = 0, trolleys = 0;
    for (int c = getchar();; c = getchar()) {
        if (c >= 'a' && c <= 'z') {
            if (length < LONGEST_TARGET)
                word[length] = static_cast<char>(c);
            ++length;
        } else {
            if (length <= LONGEST_TARGET) {
                word[length] = '\0';
                trams += strcmp(word, "tram") == 0;
                trolleys += strcmp(word, "trolleybus") == 0;
            }
            length = 0;
            if (c == EOF)
                break;
        }
    }
    puts(trams > trolleys ? "Tram driver" : trolleys > trams ? "Trolleybus driver" : "Bus driver");
}
