import java.util.Scanner;

public class Main {
    static final int HOUR = 60;
    static final int DAY = 24 * HOUR;
    static final int LONGEST = 6 * HOUR;
    static final int SPREAD = 10;
    static final int MAX_SHIFT = 5;

    static int minutes(String s) {
        int dot = s.indexOf('.');
        return Integer.parseInt(s.substring(0, dot)) * HOUR +
            Integer.parseInt(s.substring(dot + 1));
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int out1 = minutes(in.next()), in1 = minutes(in.next());
        int out2 = minutes(in.next()), in2 = minutes(in.next());
        // when the second airport is k hours ahead, the real durations are the clock
        // differences minus and plus k hours, taken around the day
        for (int k = -MAX_SHIFT; k <= MAX_SHIFT; k++) {
            int t1 = Math.floorMod(in1 - out1 - k * HOUR, DAY);
            int t2 = Math.floorMod(in2 - out2 + k * HOUR, DAY);
            if (t1 <= LONGEST && t2 <= LONGEST && Math.abs(t1 - t2) <= SPREAD) {
                System.out.println(Math.abs(k));
                return;
            }
        }
    }
}
