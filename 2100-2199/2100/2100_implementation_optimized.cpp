#include <cstdio>
#include <cstring>

constexpr int REPLY_CAPACITY = 25;
constexpr int UNLUCKY = 13;
constexpr int PRICE = 100;

int main() {
    int n;
    scanf("%d", &n);
    // the guests plus Marshall and Lily
    int people = n + 2;
    for (int i = 0; i < n; ++i) {
        // a name has at most 20 letters, so a reply with +one and the final zero
        // fit in 25 bytes
        char reply[REPLY_CAPACITY];
        scanf("%24s", reply);
        // only a reply ending in +one contains a plus: it brings a second person
        people += std::strchr(reply, '+') != nullptr;
    }
    // a dummy takes the extra seat
    if (people == UNLUCKY) {
        ++people;
    }
    printf("%d\n", people * PRICE);
}
