import java.util.Scanner;

public class Main {
    static final int YEAR = 365, LEAP = 4, CENTURY = 100, LEAP_CENTURY = 400;
    static final int MARCH = 3, MONTHS = 12;
    // the five months from March to July hold 153 days, and so do August to
    // December, which makes the days before a month a simple formula
    static final int SPAN_DAYS = 153, SPAN_MONTHS = 5;

    // days from a fixed origin, counting years from March so that the leap
    // day comes last
    static long dayNumber(String text) {
        String[] parts = text.split("\\.");
        int d = Integer.parseInt(parts[0]), m = Integer.parseInt(parts[1]);
        int y = Integer.parseInt(parts[2]);
        if (m < MARCH) {
            y--;
            m += MONTHS;
        }
        long leaps = y / LEAP - y / CENTURY + y / LEAP_CENTURY;
        return (long) YEAR * y + leaps + (SPAN_DAYS * (m - MARCH) + 2) / SPAN_MONTHS + d;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long best = -1;
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            String born = in.next(), since = in.next(), died = in.next();
            long life = dayNumber(died) - dayNumber(born) + 1;
            // the list goes in order of death, so the first record holder died first
            if (life > best) {
                best = life;
                answer = i;
            }
        }
        System.out.println(answer);
    }
}
