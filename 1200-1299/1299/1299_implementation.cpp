#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>

const int STEP = 100; // energy spent on one move or turn, at most
const int SHOT = 20;  // ammunition spent on one shot, at most

const int PER_ENEMY = 20; // ammunition the defence wants for each enemy
const int STRENGTH = 3;   // the attack needs three times the strength of the enemy

const int AIM = 5;         // the angle within which a guard, defence or retreat fires
const int CHARGE_AIM = 10; // the angle within which an advance fires
const int COURSE = 20;     // the patrol turns when it is off course by more than this

const int HALF_TURN = 180;

int energy, ammo, enemies, enemyPower, angle;

std::string move(const char *direction) {
    return std::string(direction) + " " + std::to_string(std::min(STEP, energy));
}

std::string fire() { return "FIRE " + std::to_string(std::min(SHOT, ammo)); }

// positive angles lie to the left
std::string turn(int towards) { return move(towards > 0 ? "LEFT" : "RIGHT"); }

std::string guard() {
    if (enemies == 0)
        return "STOP";
    return std::abs(angle) < AIM ? fire() : turn(angle);
}

std::string retreat() { return enemies == 0 || std::abs(angle) >= AIM ? move("BACKWARD") : fire(); }

std::string defence() { return enemies * PER_ENEMY >= ammo ? retreat() : guard(); }

std::string attack(int own, int ownPower) {
    if (own * ownPower <= enemies * enemyPower * STRENGTH)
        return retreat();
    return enemies == 0 || std::abs(angle) >= CHARGE_AIM ? move("FRONT") : fire();
}

std::string patrol(int course) {
    if (enemies > 0)
        return defence();
    // the robot may drive either way, so it heads for the point with
    // its front or its back, whichever needs the smaller turn
    int back = course > 0 ? course - HALF_TURN : course + HALF_TURN;
    if (std::abs(back) < std::abs(course)) {
        return std::abs(back) <= COURSE ? move("BACKWARD") : turn(back);
    }
    return std::abs(course) <= COURSE ? move("FRONT") : turn(course);
}

int main() {
    char mode[2] = {0};
    if (scanf("%d %d %1s %d %d %d", &energy, &ammo, mode, &enemies, &enemyPower, &angle) < 1) {
        return 0;
    }
    std::string command;
    if (mode[0] == 'G') {
        command = guard();
    } else if (mode[0] == 'D') {
        command = defence();
    } else if (mode[0] == 'A') {
        int own = 0, ownPower = 0;
        if (scanf("%d %d", &own, &ownPower) < 1)
            return 0;
        command = attack(own, ownPower);
    } else {
        int course = 0;
        if (scanf("%d", &course) < 1)
            return 0;
        command = patrol(course);
    }
    puts(command.c_str());
    return 0;
}
