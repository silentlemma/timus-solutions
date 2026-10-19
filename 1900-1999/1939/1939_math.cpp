#include <iostream>

bool canCrash(long long length, long long height, long long gateHeight, long long speed,
              long long gateSpeed, long long deceleration) {
    const long long stoppingBound = gateSpeed * (speed * speed + 2 * deceleration * length);
    const long long passingBound = 2 * deceleration * speed * (gateHeight - height);
    return stoppingBound >= passingBound;
}

int main() {
    long long length, height, gateHeight, speed, gateSpeed, deceleration;
    std::cin >> length >> height >> gateHeight >> speed >> gateSpeed >> deceleration;
    std::cout << (canCrash(length, height, gateHeight, speed, gateSpeed, deceleration) ? "Crash\n"
                                                                                       : "Safe\n");
    return 0;
}
