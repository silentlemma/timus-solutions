import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), a = in.nextLong(), b = in.nextLong();
        // each panel has two sides of A * B square metres
        System.out.println(2 * n * a * b);
    }
}
