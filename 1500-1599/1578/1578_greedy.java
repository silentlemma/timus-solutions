import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int total = (int)in.nval + 2;
        long[] x = new long[total], y = new long[total];
        for (int i = 0; i < total; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
            in.nextToken();
            y[i] = (long)in.nval;
        }
        // always run to the farthest point not visited yet: the point before had
        // this one as its farthest, so it was at least as far as the next one,
        // which makes every turn acute
        boolean[] seen = new boolean[total];
        int at = 0;
        seen[0] = true;
        StringBuilder out = new StringBuilder("YES\n1");
        for (int step = 1; step < total; step++) {
            int far = -1;
            long best = -1;
            for (int j = 0; j < total; j++) {
                long dx = x[j] - x[at], dy = y[j] - y[at], d = dx * dx + dy * dy;
                if (!seen[j] && d > best) {
                    best = d;
                    far = j;
                }
            }
            seen[far] = true;
            at = far;
            out.append(' ').append(far + 1);
        }
        System.out.println(out);
    }
}
