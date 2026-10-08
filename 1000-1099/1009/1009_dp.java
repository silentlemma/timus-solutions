import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), k = in.nextLong();
        // numbers of valid prefixes ending with a zero and with another digit,
        // where the first digit is not zero
        long zero = 0, other = k - 1;
        for (long i = 1; i < n; i++) {
            long nextZero = other;
            other = (zero + other) * (k - 1);
            zero = nextZero;
        }
        System.out.println(zero + other);
    }
}
