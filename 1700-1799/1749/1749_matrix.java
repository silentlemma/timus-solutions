import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int SIZE = 4;
    static final long BASE = 10;

    static long[][] multiply(long[][] a, long[][] b, long m) {
        long[][] c = new long[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            for (int k = 0; k < SIZE; k++) {
                for (int j = 0; j < SIZE; j++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % m;
                }
            }
        }
        return c;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String digits = in.readLine().trim();
        StringTokenizer st = new StringTokenizer(in.readLine());
        long k = Long.parseLong(st.nextToken()), m = Long.parseLong(st.nextToken());
        // going left to right, E is the sum of the substrings ending at the
        // current digit: E' = 10 E + digit * (its position), and S adds up
        // E; one copy of p acts linearly on (S, E, J, 1), J digits before it
        long power = 1 % m, value = 0, weighted = 0;
        long sumPower = 0, sumValue = 0, sumWeighted = 0;
        for (int i = 0; i < digits.length(); i++) {
            long d = digits.charAt(i) - '0';
            power = power * BASE % m;
            value = (value * BASE + d) % m;
            weighted = (weighted * BASE + d * (i + 1)) % m;
            sumPower = (sumPower + power) % m;
            sumValue = (sumValue + value) % m;
            sumWeighted = (sumWeighted + weighted) % m;
        }
        long[][] block = {{1 % m, sumPower, sumValue, sumWeighted},
                          {0, power, value, weighted},
                          {0, 0, 1 % m, digits.length() % m},
                          {0, 0, 0, 1 % m}};
        long[][] result = new long[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            result[i][i] = 1 % m;
        }
        for (; k > 0; k >>= 1) {
            if ((k & 1) == 1) {
                result = multiply(result, block, m);
            }
            block = multiply(block, block, m);
        }
        // starting from S = E = J = 0, the total is the constant column of S
        System.out.println(result[0][SIZE - 1]);
    }
}
