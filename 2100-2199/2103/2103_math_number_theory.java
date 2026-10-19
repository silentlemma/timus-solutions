import java.io.IOException;

public class Main {
    private static final int SMALL_SENDER = 5;
    private static final int BASE = 6;
    private static final int BOARD_SIZE = 7;
    private static final int POWER_OF_TWO = 8;
    private static final int POWER_OF_THREE = 9;
    private static final int SECOND_PRIME = 3;

    private static int readInt() throws IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch <= ' ' && ch != -1);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        return value;
    }

    private static void output(int cost, int... route) {
        StringBuilder path = new StringBuilder();
        int count = 0;
        int previous = 0;
        for (int employee : route) {
            if (employee != previous) {
                if (count > 0) {
                    path.append(' ');
                }
                path.append(employee);
                previous = employee;
                count++;
            }
        }
        System.out.println(cost);
        System.out.println(count);
        System.out.println(path);
    }

    private static void solve(int sender, int target) {
        if (target <= sender) {
            output(sender - target, sender, target);
            return;
        }
        if (target % sender == 0) {
            output(0, sender, target);
            return;
        }

        // One paid step joins a multiple of sender to a divisor of target.
        for (int divisor = 1; divisor <= target / divisor; divisor++) {
            if (target % divisor != 0) {
                continue;
            }
            for (int receiver : new int[] {divisor, target / divisor}) {
                for (int before : new int[] {receiver - 1, receiver + 1}) {
                    if (before >= sender && before % sender == 0) {
                        output(1, sender, before, receiver, target);
                        return;
                    }
                }
            }
        }

        if (sender <= SMALL_SENDER) {
            int before = target / sender * sender;
            if (target - before > before + sender - target) {
                before += sender;
            }
            output(2, sender, before, target);
            return;
        }

        int remainder = target;
        for (int prime : new int[] {2, SECOND_PRIME}) {
            while (remainder % prime == 0) {
                remainder /= prime;
            }
        }
        if (remainder > 1) {
            int before = remainder % BASE == 1 ? remainder - 1 : remainder + 1;
            output(2, sender, BASE, before, remainder, target);
        } else if (target % BASE == 0) {
            output(2, sender, BASE, target);
        } else if (target % POWER_OF_TWO == 0) {
            output(2, sender, POWER_OF_TWO, target);
        } else if (sender == BOARD_SIZE) {
            output(2, sender, POWER_OF_THREE, target);
        } else {
            output(2, sender, SMALL_SENDER, 10, POWER_OF_THREE, target);
        }
    }

    public static void main(String[] args) throws IOException {
        solve(readInt(), readInt());
    }
}
