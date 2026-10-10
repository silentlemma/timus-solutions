import java.util.Scanner;

public class Main {
    static final String[] NAMES = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"};
    static final int[] LENGTHS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    static final int WEEK = 7, YEAR = 365, CELL = 5;
    static final int LEAP = 4, CENTURY = 100, ERA = 400;

    public static void main(String[] args) {
        int[] lengths = LENGTHS.clone();
        Scanner in = new Scanner(System.in);
        int d = in.nextInt(), m = in.nextInt(), y = in.nextInt();
        if (y % LEAP == 0 && (y % CENTURY != 0 || y % ERA == 0)) {
            lengths[1]++;
        }
        // days from 1 January of year 1, a Monday, to the first of the month
        int past = y - 1;
        int before = YEAR * past + past / LEAP - past / CENTURY + past / ERA;
        for (int i = 0; i < m - 1; i++) {
            before += lengths[i];
        }
        int first = before % WEEK, days = lengths[m - 1];
        int cols = (first + days + WEEK - 1) / WEEK;
        StringBuilder out = new StringBuilder();
        for (int row = 0; row < WEEK; row++) {
            out.append(NAMES[row]);
            for (int col = 0; col < cols; col++) {
                int day = col * WEEK + row - first + 1;
                boolean last = col == cols - 1;
                // every column is five characters wide, the last one four,
                // unless the bracketed date sits in it
                if (day == d) {
                    out.append(String.format(" [%2d]", day));
                } else if (day >= 1 && day <= days) {
                    out.append(String.format(last ? "  %2d" : "  %2d ", day));
                } else {
                    for (int i = 0; i < (last ? CELL - 1 : CELL); i++) {
                        out.append(' ');
                    }
                }
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
