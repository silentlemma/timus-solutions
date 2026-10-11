import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), k = in.nextLong();
        // with r = N mod K, an s x s corner square is left over, s = min(r, K - r)
        long r = n % k, s = Math.min(r, k - r);
        System.out.println(n < k ? 0 : (n * n - s * s) / k);
    }
}
