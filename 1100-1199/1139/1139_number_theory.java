import java.util.Scanner;

public class Main {
    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        // an a by b grid: the diagonal crosses a + b - 2 inner lines, two at once
        // at each of the gcd(a, b) - 1 inner corners; it starts in one block and
        // every crossing enters a new one
        long a = n - 1, b = m - 1;
        System.out.println(a + b - gcd(a, b));
    }
}
