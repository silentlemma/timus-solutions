import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long k = in.nextLong(), p = in.nextLong();
        // root[v]: some y with y^2 = v (mod p), or -1 when v is not a square
        int[] root = new int[(int)p];
        Arrays.fill(root, -1);
        for (long y = 0; y < p; y++) {
            int v = (int)(y * y % p);
            if (root[v] < 0)
                root[v] = (int)y;
        }
        // half the values are squares, so some x soon leaves a square k - x^2
        for (long x = 0; x < p; x++) {
            int y = root[(int)(((k - x * x) % p + p) % p)];
            if (y >= 0) {
                System.out.println(x + " " + y);
                return;
            }
        }
        System.out.println("NO SOLUTION");
    }
}
