import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long m = in.nextLong(), d1 = in.nextLong(), d2 = in.nextLong();
        // the work is m * d1 digger-days; spreading it as evenly as possible
        // over d2 days needs the fewest diggers, the rounded-up average
        long work = m * d1, low = work / d2, extra = work % d2;
        StringBuilder sb = new StringBuilder();
        for (long day = 0; day < d2; day++) {
            if (day > 0) sb.append(' ');
            sb.append(day < d2 - extra ? low : low + 1);
        }
        System.out.println(sb);
    }
}
