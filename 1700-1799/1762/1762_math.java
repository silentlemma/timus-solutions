import java.util.Scanner;

public class Main {
    static long gcd(long x, long y) {
        return y == 0 ? x : gcd(y, x % y);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        long a = n - 1, b = m - 1, g = gcd(a, b);
        // the walk takes lcm(a, b) steps and turns every tile it passes over, so
        // a tile passed twice ends up white again; in units of g the crossings
        // are the inner points (x, y) with x and y both odd or both even
        long steps = a / g * b;
        long wide = a / g, tall = b / g;
        long crossings = (wide / 2) * (tall / 2) + ((wide - 1) / 2) * ((tall - 1) / 2);
        System.out.println(steps + 1 - 2 * crossings);
    }
}
