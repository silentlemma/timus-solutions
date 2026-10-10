import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int m = (int)in.nval;
        int[] values = new int[1];
        int n = 0;
        while (in.nextToken() != StreamTokenizer.TT_EOF && in.nval >= 0) {
            if (n == values.length) {
                values = Arrays.copyOf(values, 2 * n);
            }
            values[n++] = (int)in.nval;
        }
        // indices of the window whose values decrease from front to back: the
        // front is the maximum, and a value never matters once a later one is larger
        int[] window = new int[n];
        int head = 0, tail = 0;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            while (tail > head && values[window[tail - 1]] <= values[i]) {
                tail--;
            }
            window[tail++] = i;
            if (window[head] <= i - m) {
                head++;
            }
            if (i >= m - 1) {
                out.append(values[window[head]]).append('\n');
            }
        }
        System.out.print(out);
    }
}
