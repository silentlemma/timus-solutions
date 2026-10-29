import java.util.Scanner;

public class Main {
    private static final int TOTAL_TASKS = 12;
    private static final int FIRST_HOUR_MINUTES = 60;
    private static final int MINUTES_PER_TASK = 45;
    private static final int CONTEST_MINUTES = 300;

    private static boolean solve(int firstHour) {
        return FIRST_HOUR_MINUTES + (TOTAL_TASKS - firstHour) * MINUTES_PER_TASK <= CONTEST_MINUTES;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int firstHour = in.nextInt();
        System.out.println(solve(firstHour) ? "YES" : "NO");
    }
}
