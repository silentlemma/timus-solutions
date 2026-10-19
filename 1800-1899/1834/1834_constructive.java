import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    // cut the values 1 .. n greedily into runs of consecutive values whose
    // positions alternately rise and fall, the first one as asked
    static List<int[]> blocks(int[] pos, int n, boolean rising) {
        List<int[]> cuts = new ArrayList<>();
        for (int v = 1; v <= n; rising = !rising) {
            int w = v;
            while (w < n && (pos[w + 1] > pos[w]) == rising) {
                w++;
            }
            cuts.add(new int[] {v, w});
            v = w + 1;
        }
        return cuts;
    }

    // the least k with 2^k >= count
    static int passes(int count) {
        int k = 0;
        while ((1 << k) < count) {
            k++;
        }
        return k;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int) in.nval;
        int[] cars = new int[n], pos = new int[n + 1];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            cars[i] = (int) in.nval;
            pos[cars[i]] = i;
        }
        // one pass keeps a chosen set of cars in order and appends the others
        // reversed; over k passes cars end up ordered by their codes of
        // choices in reflected Gray order, reversed once per one in the code
        List<int[]> runs = blocks(pos, n, true), falling = blocks(pos, n, false);
        int first = 0;
        if (passes(runs.size()) > passes(falling.size() + 1)) {
            runs = falling;
            first = 1;
        }
        int k = passes(runs.size() + first);
        int[] code = new int[n + 1];
        for (int i = 0; i < runs.size(); i++) {
            int rank = i + first;
            for (int v = runs.get(i)[0]; v <= runs.get(i)[1]; v++) {
                code[v] = rank ^ (rank >> 1);
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(k).append('\n');
        for (int bit = 0; bit < k; bit++) {
            int[] next = new int[n];
            int size = 0;
            for (int v : cars) {
                if ((code[v] >> bit & 1) == 0) {
                    next[size++] = v;
                }
            }
            for (int i = n - 1; i >= 0; i--) {
                if ((code[cars[i]] >> bit & 1) == 1) {
                    next[size++] = cars[i];
                }
            }
            cars = next;
            for (int i = 0; i < n; i++) {
                out.append(cars[i]).append(i + 1 < n ? ' ' : '\n');
            }
        }
        System.out.print(out);
    }
}
