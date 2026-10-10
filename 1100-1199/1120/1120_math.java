import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        long s = new Scanner(System.in).nextLong();
        // s = n*a + n(n-1)/2 with a >= 1 needs n(n+1)/2 <= s; try the longest first
        long n = (long)Math.sqrt(2.0 * s);
        while (n * (n + 1) / 2 > s) {
            n--;
        }
        while ((s - n * (n - 1) / 2) % n != 0) {
            n--;
        }
        System.out.println((s - n * (n - 1) / 2) / n + " " + n);
    }
}
