import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        // each number of dots v sits on n + 2 ends: on the tiles v-w for every w,
        // and twice on the double v-v; so the dots add up to (n + 2) * (0 + ... + n)
        System.out.println((n + 2) * n * (n + 1) / 2);
    }
}
