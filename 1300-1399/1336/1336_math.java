import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        // (n^2)^2 = n^4 = n^3 * n
        System.out.println(n * n);
        System.out.println(n);
    }
}
