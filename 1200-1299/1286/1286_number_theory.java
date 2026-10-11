import java.util.*;

public class Main {
    static long gcd(long a, long b) { return b == 0 ? Math.abs(a) : gcd(b, a % b); }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long p = in.nextLong(), q = in.nextLong(), x = in.nextLong(), y = in.nextLong();
        long x1 = in.nextLong(), y1 = in.nextLong();
        long dx = x1 - x, dy = y1 - y, g = gcd(p, q);
        boolean ok;
        if (g == 0) {
            ok = dx == 0 && dy == 0;
        } else if (dx % g != 0 || dy % g != 0) {
            ok = false;
        } else {
            // with p/g and q/g coprime, the moves reach every point of the
            // lattice g Z^2, except that when both are odd every move keeps the
            // parity of (dx + dy) / g
            boolean bothOdd = (p / g) % 2 != 0 && (q / g) % 2 != 0;
            ok = !bothOdd || (dx / g + dy / g) % 2 == 0;
        }
        System.out.println(ok ? "YES" : "NO");
    }
}
