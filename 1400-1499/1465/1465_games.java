import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int LIMIT = 200; // the values repeat with PERIOD from 52 on, well below this
    static final int PERIOD = 34;
    static final int TAKE = 3; // a move takes up to three files out of play

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        // Dawson's chess: a row of n files plays like the octal game 0.137, where
        // a move takes one file (only if it is all), two (leaving one row) or three
        // (leaving up to two rows); White, moving first, wins when the value is not 0
        int[] g = new int[LIMIT + 1];
        for (int size = 1; size <= LIMIT; size++) {
            Set<Integer> seen = new HashSet<>();
            if (size == 1)
                seen.add(0);
            if (size >= 2)
                seen.add(g[size - 2]);
            for (int left = 0; left <= size - TAKE; left++)
                seen.add(g[left] ^ g[size - TAKE - left]);
            while (seen.contains(g[size]))
                g[size]++;
        }
        if (n > LIMIT)
            n = LIMIT - PERIOD + (n - LIMIT) % PERIOD;
        System.out.println(g[(int)n] != 0 ? "White" : "Black");
    }
}
