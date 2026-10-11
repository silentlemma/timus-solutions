import java.util.*;

public class Main {
    static final int STEP = 100; // energy spent on one move or turn, at most
    static final int SHOT = 20;  // ammunition spent on one shot, at most

    static final int PER_ENEMY = 20; // ammunition the defence wants for each enemy
    static final int STRENGTH = 3;   // the attack needs three times the strength of the enemy

    static final int AIM = 5;         // the angle within which a guard, defence or retreat fires
    static final int CHARGE_AIM = 10; // the angle within which an advance fires
    static final int COURSE = 20;     // the patrol turns when it is off course by more than this

    static final int HALF_TURN = 180;

    static int energy, ammo, enemies, enemyPower, angle;

    static String move(String direction) { return direction + " " + Math.min(STEP, energy); }

    static String fire() { return "FIRE " + Math.min(SHOT, ammo); }

    // positive angles lie to the left
    static String turn(int towards) { return move(towards > 0 ? "LEFT" : "RIGHT"); }

    static String guard() {
        if (enemies == 0)
            return "STOP";
        return Math.abs(angle) < AIM ? fire() : turn(angle);
    }

    static String retreat() {
        return enemies == 0 || Math.abs(angle) >= AIM ? move("BACKWARD") : fire();
    }

    static String defence() { return enemies * PER_ENEMY >= ammo ? retreat() : guard(); }

    static String attack(int own, int ownPower) {
        if (own * ownPower <= enemies * enemyPower * STRENGTH)
            return retreat();
        return enemies == 0 || Math.abs(angle) >= CHARGE_AIM ? move("FRONT") : fire();
    }

    static String patrol(int deviation) {
        if (enemies > 0)
            return defence();
        // the robot may drive either way, so it heads for the point with
        // its front or its back, whichever needs the smaller turn
        int back = deviation > 0 ? deviation - HALF_TURN : deviation + HALF_TURN;
        if (Math.abs(back) < Math.abs(deviation)) {
            return Math.abs(back) <= COURSE ? move("BACKWARD") : turn(back);
        }
        return Math.abs(deviation) <= COURSE ? move("FRONT") : turn(deviation);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        energy = in.nextInt();
        ammo = in.nextInt();
        String mode = in.next();
        enemies = in.nextInt();
        enemyPower = in.nextInt();
        angle = in.nextInt();
        String command;
        if (mode.equals("G")) {
            command = guard();
        } else if (mode.equals("D")) {
            command = defence();
        } else if (mode.equals("A")) {
            int own = in.nextInt(), ownPower = in.nextInt();
            command = attack(own, ownPower);
        } else {
            command = patrol(in.nextInt());
        }
        System.out.println(command);
    }
}
