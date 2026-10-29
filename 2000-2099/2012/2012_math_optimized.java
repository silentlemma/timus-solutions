import java.io.IOException;

public class Main {
    private static final int TOTAL_TASKS = 12;
    private static final int FIRST_HOUR_MINUTES = 60;
    private static final int MINUTES_PER_TASK = 45;
    private static final int CONTEST_MINUTES = 300;

    // the number is parsed by hand from System.in, much lighter than Scanner
    private static int nextInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = System.in.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value * sign;
    }

    public static void main(String[] args) throws IOException {
        int firstHour = nextInt();
        boolean fits =
            FIRST_HOUR_MINUTES + (TOTAL_TASKS - firstHour) * MINUTES_PER_TASK <= CONTEST_MINUTES;
        System.out.println(fits ? "YES" : "NO");
    }
}
