import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final String ROLES = "WMCR";
    private static final String[] ROLE_NAMES = {"warrior", "mage", "cleric", "rogue"};
    private static final int ROLE_COUNT = ROLES.length();
    private static final int MASK_COUNT = 1 << ROLE_COUNT;
    private static final int FULL_MASK = MASK_COUNT - 1;

    private static String nextToken(BufferedInputStream input) throws IOException {
        StringBuilder token = new StringBuilder();
        int value;
        do {
            value = input.read();
        } while (value != -1 && value <= ' ');
        while (value != -1 && value > ' ') {
            token.append((char) value);
            value = input.read();
        }
        return token.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int people = Integer.parseInt(nextToken(input));
        boolean[] reachable = new boolean[MASK_COUNT];
        reachable[0] = true;

        for (int person = 0; person < people; person++) {
            String skills = nextToken(input);
            int qualifications = 0;
            for (int index = 0; index < skills.length(); index++) {
                qualifications |= 1 << ROLES.indexOf(skills.charAt(index));
            }
            // Adding a role raises the mask, so each person is used only once.
            for (int mask = FULL_MASK; mask >= 0; mask--) {
                if (!reachable[mask]) {
                    continue;
                }
                for (int role = 0; role < ROLE_COUNT; role++) {
                    int bit = 1 << role;
                    if ((qualifications & bit) != 0 && (mask & bit) == 0) {
                        reachable[mask | bit] = true;
                    }
                }
            }
        }

        int bestSize = 0;
        int requiredRoles = FULL_MASK;
        for (int mask = 0; mask < MASK_COUNT; mask++) {
            if (!reachable[mask]) {
                continue;
            }
            int size = Integer.bitCount(mask);
            if (size > bestSize) {
                bestSize = size;
                requiredRoles = mask;
            } else if (size == bestSize) {
                requiredRoles &= mask;
            }
        }

        StringBuilder answer = new StringBuilder();
        answer.append(bestSize).append('\n');
        if (bestSize < ROLE_COUNT) {
            answer.append("Looking for");
            for (int role = 0; role < ROLE_COUNT; role++) {
                if ((requiredRoles & (1 << role)) == 0) {
                    answer.append(' ').append(ROLE_NAMES[role]);
                }
            }
            answer.append('\n');
        }
        System.out.print(answer);
    }
}
