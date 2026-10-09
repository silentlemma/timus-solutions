import java.util.Scanner;

public class Main {
    // Lagrange: every number is a sum of four squares, and Legendre: exactly the
    // numbers 4^a (8b + 7) need all four
    static final int MOST = 4;
    static final int POWER = 4;
    static final int MODULUS = 8;
    static final int REST = 7;

    static boolean isSquare(int v) {
        int r = (int)Math.round(Math.sqrt(v));
        return r * r == v;
    }

    static int count(int n) {
        if (isSquare(n)) {
            return 1;
        }
        for (int a = 1; a * a < n; a++) {
            if (isSquare(n - a * a)) {
                return 2;
            }
        }
        while (n % POWER == 0) {
            n /= POWER;
        }
        return n % MODULUS == REST ? MOST : MOST - 1;
    }

    public static void main(String[] args) {
        System.out.println(count(new Scanner(System.in).nextInt()));
    }
}
