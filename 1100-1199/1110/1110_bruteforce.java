import java.util.Scanner;

public class Main {
    // x^n mod m by repeated squaring
    static int power(int x, int n, int m) {
        int result = 1 % m;
        for (x %= m; n > 0; n >>= 1) {
            if ((n & 1) == 1) {
                result = result * x % m;
            }
            x = x * x % m;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt(), y = in.nextInt();
        // only M candidates; a Y of M or more is never a remainder
        StringBuilder roots = new StringBuilder();
        for (int x = 0; x < m; x++) {
            if (power(x, n, m) == y) {
                roots.append(roots.length() > 0 ? " " : "").append(x);
            }
        }
        System.out.println(roots.length() > 0 ? roots.toString() : "-1");
    }
}
