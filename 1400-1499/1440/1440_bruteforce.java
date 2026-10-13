import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final List<String> DAYS =
        Arrays.asList("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday");
    // the months and the days from September 1 to the first day of each of them
    static final List<String> MONTHS =
        Arrays.asList("September", "October", "November", "December");
    static final int[] OFFSETS = {0, 30, 61, 91};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String first = in.next(), month = in.next();
        int day = in.nextInt(), a = in.nextInt(), b = in.nextInt();
        int week = DAYS.size(), start = DAYS.indexOf(first);
        int match = OFFSETS[MONTHS.indexOf(month)] + day - 1; // September 1 is day 0
        int[] count = new int[week]; // training days from September 2 to the eve of the match
        for (int i = 1; i < match; i++)
            count[(start + i) % week]++;
        for (int mask = 1; mask < 1 << week; mask++) {
            List<String> chosen = new ArrayList<>();
            int total = 0;
            for (int d = 0; d < week; d++)
                if ((mask >> d & 1) == 1) {
                    chosen.add(DAYS.get(d));
                    total += count[d];
                }
            if (a <= total && total <= b) {
                System.out.println(chosen.size());
                System.out.println(String.join("\n", chosen));
                return;
            }
        }
        System.out.println("Impossible");
    }
}
