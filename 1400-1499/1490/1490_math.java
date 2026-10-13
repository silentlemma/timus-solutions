import java.util.Scanner;

public class Main {
    static final long QUARTERS = 4;

    static long isqrt(long n) {
        long s = (long)Math.sqrt((double)n);
        while (s * s > n)
            s--;
        while ((s + 1) * (s + 1) <= n)
            s++;
        return s;
    }

    public static void main(String[] args) {
        long r = new Scanner(System.in).nextLong();
        // a tile shares more than one point with the disc exactly when its
        // corner nearest to the centre lies strictly inside: in one quarter,
        // tiles (i, j) with i^2 + j^2 < r^2, that is j <= isqrt(r^2 - i^2 - 1)
        long total = 0;
        for (long i = 0; i < r; i++)
            total += isqrt(r * r - i * i - 1) + 1;
        System.out.println(QUARTERS * total);
    }
}
