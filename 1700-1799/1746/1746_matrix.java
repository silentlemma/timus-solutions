import java.util.Scanner;

public class Main {
    static long[][] multiply(long[][] a, long[][] b, long mod) {
        int n = a.length;
        long[][] c = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (a[i][k] == 0) {
                    continue;
                }
                for (int j = 0; j < n; j++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod;
                }
            }
        }
        return c;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long m = in.nextLong(), d = in.nextLong(), mod = in.nextLong();
        int q = in.nextInt();
        long[][] points = new long[q][n];
        for (int i = 0; i < q; i++) {
            for (int k = 0; k < n; k++) {
                points[i][k] = in.nextLong();
            }
        }
        // the number of routes depends only on how many coordinates differ
        // from the target: a move fixes one of them, changes one of them to
        // another wrong value, or spoils one that was right
        int size = n + 1;
        long[][] step = new long[size][size], power = new long[size][size];
        for (int h = 0; h < size; h++) {
            if (h > 0) {
                step[h][h - 1] = h % mod;
                step[h][h] = h * (m - 2) % mod;
            }
            if (h < n) {
                step[h][h + 1] = (n - h) * (m - 1) % mod;
            }
            power[h][h] = 1 % mod;
        }
        for (; d > 0; d >>= 1) {
            if ((d & 1) == 1) {
                power = multiply(power, step, mod);
            }
            step = multiply(step, step, mod);
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < q; i++) {
            for (int j = 0; j < q; j++) {
                int differ = 0;
                for (int k = 0; k < n; k++) {
                    if (points[i][k] != points[j][k]) {
                        differ++;
                    }
                }
                out.append(j > 0 ? " " : "").append(power[differ][0]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
