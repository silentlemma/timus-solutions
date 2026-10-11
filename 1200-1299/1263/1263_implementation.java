import java.io.*;
import java.math.*;

public class Main {
    static final double PERCENT = 100.0;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] votes = new int[n + 1];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            votes[(int)in.nval]++;
        }
        StringBuilder out = new StringBuilder();
        // round the exact double half to even, as printf in C does
        for (int i = 1; i <= n; i++)
            out.append(new BigDecimal(PERCENT * votes[i] / m).setScale(2, RoundingMode.HALF_EVEN))
                .append("%\n");
        System.out.print(out);
    }
}
