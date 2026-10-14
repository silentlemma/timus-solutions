import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextLong())
            return;
        long n = in.nextLong();
        // x_n = 2/3 - (-1)^n (2/3) 2^-n: an even n leaves k sixes while
        // 10^k <= 2^n, an odd n while 2 10^k < 2^n, that is 10^k <= 2^(n-1)
        long m = n % 2 == 0 ? n : n - 1;
        System.out.println((long)Math.floor(m * Math.log10(2)));
    }
}
