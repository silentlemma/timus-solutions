import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 10007;
    static final int MOST = 512; // the product of the sizes is at most this

    // the length of the arrays at each depth, ending with 0 for the empty ones
    static List<Integer> sizes(String text) {
        List<Integer> open = new ArrayList<>(), dims = new ArrayList<>();
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (ch == '[') {
                if (!open.isEmpty())
                    open.set(open.size() - 1, open.get(open.size() - 1) + 1);
                open.add(0);
            } else if (ch == ']') {
                int depth = open.size() - 1;
                while (dims.size() <= depth)
                    dims.add(0);
                dims.set(depth, open.remove(depth));
            }
        }
        return dims;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            text.append(line);
        List<Integer> dims = sizes(text.toString());
        if (dims.size() == 1) {
            System.out.println(1);
            return;
        }
        // Stirling numbers of the second kind: ways to split m references into k objects
        int[][] stirling = new int[MOST + 1][MOST + 1];
        stirling[0][0] = 1;
        for (int m = 1; m <= MOST; m++)
            for (int k = 1; k <= m; k++)
                stirling[m][k] = (stirling[m - 1][k - 1] + k * stirling[m - 1][k]) % MOD;
        // m references to empty arrays: any partition of them (Bell numbers)
        int[] ways = new int[MOST + 1];
        for (int m = 0; m <= MOST; m++) {
            long sum = 0;
            for (int k = 0; k <= m; k++)
                sum += stirling[m][k];
            ways[m] = (int)(sum % MOD);
        }
        // the references at depth i number at most dims[0] * ... * dims[i - 1]
        long[] slots = new long[dims.size()];
        slots[0] = 1;
        for (int i = 1; i < dims.size(); i++)
            slots[i] = slots[i - 1] * dims.get(i - 1);
        for (int i = dims.size() - 2; i >= 1; i--) {
            int width = dims.get(i);
            // m references to arrays of this depth: k distinct arrays, whose
            // k * width elements are configured one level down
            int upper = (int)Math.min(MOST / width, slots[i]);
            int[] next = new int[MOST + 1];
            for (int m = 1; m <= upper; m++) {
                long sum = 0;
                for (int k = 1; k <= m; k++)
                    sum += (long)stirling[m][k] * ways[k * width];
                next[m] = (int)(sum % MOD);
            }
            ways = next;
        }
        System.out.println(ways[dims.get(0)]);
    }
}
