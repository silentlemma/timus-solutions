import java.util.Scanner;

public class Main {
    static final long WHOLE = 10000, NONE = -1;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] given = new long[n];
        for (int i = 0; i < n; i++) {
            in.next();
            given[i] = in.nextInt() == 1 ? in.nextLong() : NONE;
        }
        // shares never grow down the list, so an unknown share is at least
        // the next given one (or 1) and at most the last given one before it
        // (or 100%); every total between the two extremes can be reached
        long low = 0, high = 0, floor = 1, ceiling = WHOLE;
        for (int i = n - 1; i >= 0; i--) {
            floor = given[i] != NONE ? given[i] : floor;
            low += floor;
        }
        for (int i = 0; i < n; i++) {
            ceiling = given[i] != NONE ? given[i] : ceiling;
            high += ceiling;
        }
        System.out.println(low <= WHOLE && WHOLE <= high ? "YES" : "NO");
    }
}
