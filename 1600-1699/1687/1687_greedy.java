import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.StringJoiner;

public class Main {
    static StreamTokenizer in;

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next();
        int k = next();
        int[][] boxes = new int[k][];
        for (int i = 0; i < k; i++) {
            boxes[i] = new int[next()];
            for (int j = 0; j < boxes[i].length; j++) {
                boxes[i][j] = next();
            }
        }
        int m = next();
        boolean[] wanted = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            wanted[next()] = true;
        }
        List<Integer> useful = new ArrayList<>();
        boolean[] coverable = new boolean[n + 1];
        int coverableCount = 0;
        for (int i = 0; i < k; i++) {
            boolean any = false;
            for (int c : boxes[i]) {
                if (wanted[c]) {
                    any = true;
                    if (!coverable[c]) {
                        coverable[c] = true;
                        coverableCount++;
                    }
                }
            }
            if (any) {
                useful.add(i);
            }
        }
        // no set of boxes is worth more than all coverable coins, nor holds more
        // than all useful boxes; one box per coverable coin reaches every coin,
        // so the answer is min(useful, coverable): those boxes, then any others
        boolean[] chosen = new boolean[k];
        boolean[] covered = new boolean[n + 1];
        int count = 0;
        for (int coin = 1; coin <= n; coin++) {
            if (!coverable[coin] || covered[coin]) {
                continue;
            }
            for (int i : useful) {
                boolean holds = false;
                for (int c : boxes[i]) {
                    holds |= c == coin;
                }
                if (holds) {
                    chosen[i] = true;
                    count++;
                    for (int c : boxes[i]) {
                        covered[c] = true;
                    }
                    break;
                }
            }
        }
        for (int i : useful) {
            if (count < coverableCount && !chosen[i]) {
                chosen[i] = true;
                count++;
            }
        }
        StringJoiner picked = new StringJoiner(" ");
        for (int i = 0; i < k; i++) {
            if (chosen[i]) {
                picked.add(Integer.toString(i + 1));
            }
        }
        System.out.println(count);
        System.out.println(picked);
    }
}
