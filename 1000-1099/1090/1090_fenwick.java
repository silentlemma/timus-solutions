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
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        long best = -1;
        int bestRow = 0;
        int[] tree = new int[n + 1];
        for (int r = 1; r <= k; r++) {
            Arrays.fill(tree, 0);
            long jumps = 0;
            for (int i = 0; i < n; i++) {
                in.nextToken();
                int x = (int)in.nval;
                // each recruit jumps once for every earlier recruit with a larger
                // number: earlier minus those not larger, counted by the tree
                int smaller = 0;
                for (int j = x; j > 0; j &= j - 1) {
                    smaller += tree[j];
                }
                jumps += i - smaller;
                for (int j = x; j <= n; j += j & -j) {
                    tree[j]++;
                }
            }
            if (jumps > best) {
                best = jumps;
                bestRow = r;
            }
        }
        System.out.println(bestRow);
    }
}
