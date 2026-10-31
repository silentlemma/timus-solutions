import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // one ordinary token avoids scanner's regular-expression machinery.
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // ways[s]: sets of distinct step sizes, each used at most once, summing
        // to s; sizes are added one by one, going over s downwards
        long[] ways = new long[n + 1];
        ways[0] = 1;
        for (int size = 1; size <= n; size++) {
            for (int s = n; s >= size; s--) {
                ways[s] += ways[s - size];
            }
        }
        // a staircase needs at least two steps: drop the single step of n cubes
        System.out.println(ways[n] - 1);
    }
}
