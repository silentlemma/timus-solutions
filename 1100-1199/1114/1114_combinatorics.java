import java.util.Scanner;

public class Main {
    static final int TOP = 40;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), a = in.nextInt(), b = in.nextInt();
        // Pascal's triangle; the binomials stay below 2^32
        long[][] c = new long[TOP][TOP];
        for (int i = 0; i < TOP; i++) {
            c[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
            }
        }
        // up to a identical balls in n boxes: put the unused ones in an extra box,
        // then it is a stars-and-bars count C(a + n, n); the product reaches
        // 1.05 * 10^19, so its 64 bits are printed as an unsigned number
        System.out.println(Long.toUnsignedString(c[a + n][n] * c[b + n][n]));
    }
}
