import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static StreamTokenizer in =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        // before[i] is the sum of the first i readings
        long[] before = new long[n + 1];
        for (int i = 1; i <= n; i++)
            before[i] = before[i - 1] + next();
        int q = next();
        StringBuilder out = new StringBuilder();
        for (int t = 0; t < q; t++) {
            int i = next(), j = next();
            out.append(before[j] - before[i - 1]).append('\n');
        }
        System.out.print(out);
    }
}
