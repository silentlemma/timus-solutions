import java.io.*;

public class Main {
    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int s = next(in), n = next(in);
        // the sum of A_i - 1 over every segment must stay at most N, so only the
        // largest such sum matters: Kadane's scan keeps the best one ending here
        int best = 0, here = 0;
        for (int i = 0; i < s; i++) {
            here = Math.max(here, 0) + next(in) - 1;
            best = Math.max(best, here);
        }
        System.out.println(best <= n ? "YES" : "NO");
    }
}
