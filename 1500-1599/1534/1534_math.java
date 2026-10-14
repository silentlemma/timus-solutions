import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long k = in.nextLong(), l = in.nextLong(), n = in.nextLong();
        long d = k - l;
        // with W wins and R losses the team has n + 2W - R points; the goals
        // split into a common part, scored and conceded alike, plus at least
        // one goal of margin per win and per loss
        long best, worst;
        if (d >= 0) {
            // no losses: the margin d covers up to d wins, the rest are draws
            best = n + 2 * Math.min(d, n);
            worst = d == 0 ? n : n + 2;
        } else {
            // no wins: up to -d losses, at least one
            best = n - 1;
            worst = n - Math.min(-d, n);
        }
        if (k >= 1 && l >= 1 && n >= 2) {
            // wins and losses together: one goal each is enough, so one loss
            // and up to k wins, or one win and up to l losses
            best = Math.max(best, n - 1 + 2 * Math.min(k, n - 1));
            worst = Math.min(worst, n + 2 - Math.min(l, n - 1));
        }
        System.out.println(best + " " + worst);
    }
}
