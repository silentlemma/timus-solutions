import sys

STEP = 100  # energy spent on one move or turn, at most
SHOT = 20  # ammunition spent on one shot, at most

PER_ENEMY = 20  # ammunition the defence wants for each enemy
STRENGTH = 3  # the attack needs three times the strength of the enemy

AIM = 5  # the angle within which a guard, defence or retreat fires
CHARGE_AIM = 10  # the angle within which an advance fires
COURSE = 20  # the patrol turns when it is off course by more than this

HALF_TURN = 180


def main():
    words = iter(sys.stdin.read().split())

    def number():
        return int(next(words))

    energy, ammo = number(), number()
    mode = next(words)
    enemies, enemy_power, angle = number(), number(), number()

    def move(direction):
        return "%s %d" % (direction, min(STEP, energy))

    def fire():
        return "FIRE %d" % min(SHOT, ammo)

    def turn(towards):
        # positive angles lie to the left
        return move("LEFT" if towards > 0 else "RIGHT")

    def guard():
        if enemies == 0:
            return "STOP"
        return fire() if abs(angle) < AIM else turn(angle)

    def retreat():
        return move("BACKWARD") if enemies == 0 or abs(angle) >= AIM else fire()

    def defence():
        return retreat() if enemies * PER_ENEMY >= ammo else guard()

    def attack(own, own_power):
        if own * own_power <= enemies * enemy_power * STRENGTH:
            return retreat()
        return move("FRONT") if enemies == 0 or abs(angle) >= CHARGE_AIM else fire()

    def patrol(course):
        if enemies > 0:
            return defence()
        # the robot may drive either way, so it heads for the point with
        # its front or its back, whichever needs the smaller turn
        back = course - HALF_TURN if course > 0 else course + HALF_TURN
        if abs(back) < abs(course):
            return move("BACKWARD") if abs(back) <= COURSE else turn(back)
        return move("FRONT") if abs(course) <= COURSE else turn(course)

    if mode == "G":
        print(guard())
    elif mode == "D":
        print(defence())
    elif mode == "A":
        own, own_power = number(), number()
        print(attack(own, own_power))
    else:
        course = number()
        print(patrol(course))


main()
