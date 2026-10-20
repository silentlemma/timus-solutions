import java.util.Scanner;

public class Main {
    private static boolean blueWins(long n, int r1, long c1, int r2, long c2) {
        // Reflect the board so Blue starts to the left of Red.
        if (c1 > c2) {
            c1 = n + 1 - c1;
            c2 = n + 1 - c2;
        }
        long gap = c2 - c1;
        long left = c1 - 1;
        long right = n - c2;
        if (r1 == r2) {
            return left > right || (left == right && gap % 2 == 0);
        }
        if (gap == 0 || left == right) {
            return false;
        }
        if (gap == 1) {
            return true;
        }
        // A one-column tail advantage makes the gap parity decisive.
        if (left == right + 1 || right == left + 1) {
            return gap % 2 == 1;
        }
        return left > right;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();
        int r1 = in.nextInt();
        long c1 = in.nextLong();
        int r2 = in.nextInt();
        long c2 = in.nextLong();
        System.out.println(blueWins(n, r1, c1, r2, c2) ? "Blue" : "Red");
    }
}
