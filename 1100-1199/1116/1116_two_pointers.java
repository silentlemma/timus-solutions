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

    // the intervals, each as its left end, right end and value
    static int[][] read() throws IOException {
        int[][] f = new int[next()][];
        for (int i = 0; i < f.length; i++) {
            f[i] = new int[] {next(), next(), next()};
        }
        return f;
    }

    public static void main(String[] args) throws IOException {
        int[][] first = read(), second = read();
        StringBuilder out = new StringBuilder();
        int count = 0, j = 0;
        for (int[] p : first) {
            int cur = p[0];
            // walk through [a, b) and keep what no interval of the second covers
            while (cur < p[1]) {
                while (j < second.length && second[j][1] <= cur) {
                    j++;
                }
                if (j < second.length && second[j][0] <= cur) {
                    cur = second[j][1];
                    continue;
                }
                int end = j < second.length ? Math.min(p[1], second[j][0]) : p[1];
                out.append(' ').append(cur).append(' ').append(end).append(' ').append(p[2]);
                count++;
                cur = end;
            }
        }
        System.out.println(count + out.toString());
    }
}
