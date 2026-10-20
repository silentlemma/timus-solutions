import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    private static final int PADDING = 3;
    private static final long MOD = 1000000007L;

    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String line;
        do {
            line = input.readLine();
        } while (line.trim().isEmpty());
        int n = Integer.parseInt(line.trim());
        int edges = n - 1;
        int length = 2 * edges;
        long[] inverse = new long[length + 2];
        long[] choose = new long[length + PADDING];
        inverse[1] = 1;
        choose[0] = 1;
        for (int i = 1; i <= length; ++i) {
            if (i > 1) {
                inverse[i] = MOD - (MOD / i) * inverse[(int) (MOD % i)] % MOD;
            }
            choose[i] = choose[i - 1] * (length - i + 1) % MOD * inverse[i] % MOD;
        }

        // Contour walks are Dyck paths. Sum the counts whose maximum is at least h.
        // Reflection at levels -1 and h gives this second difference, with width h + 1.
        long answer = 0;
        for (int width = 2; width <= edges + 1; ++width) {
            for (int offset = width; offset <= edges + 1; offset += width) {
                int index = edges + offset;
                answer += choose[index - 1] - 2 * choose[index] + choose[index + 1];
            }
        }
        System.out.println((answer % MOD + MOD) % MOD);
    }
}
