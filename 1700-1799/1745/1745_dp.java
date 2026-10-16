import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static class Word {
        final int change, low, size, id;

        Word(int change, int low, int size, int id) {
            this.change = change;
            this.low = low;
            this.size = size;
            this.id = id;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        // each word: net change of the depth, lowest depth reached, length
        List<Word> rising = new ArrayList<>(), falling = new ArrayList<>();
        int top = 0;
        for (int i = 0; i < n; i++) {
            String w = in.readLine().trim();
            int depth = 0, low = 0;
            for (int j = 0; j < w.length(); j++) {
                depth += w.charAt(j) == '(' ? 1 : -1;
                low = Math.min(low, depth);
            }
            top += w.length();
            (depth >= 0 ? rising : falling).add(new Word(depth, low, w.length(), i + 1));
        }
        // in a best answer the words that open more than they close come
        // first, those that dip least first; the rest go last, those that
        // end highest above their lowest point first
        rising.sort((a, b) -> b.low - a.low);
        falling.sort((a, b) -> (a.low - a.change) - (b.low - b.change));
        List<Word> order = new ArrayList<>(rising);
        order.addAll(falling);
        // best[d]: longest prefix built so far that ends at depth d
        int[] best = new int[top + 1], next = new int[top + 1];
        java.util.Arrays.fill(best, -1);
        best[0] = 0;
        boolean[][] taken = new boolean[order.size()][top + 1];
        for (int k = 0; k < order.size(); k++) {
            Word w = order.get(k);
            System.arraycopy(best, 0, next, 0, top + 1);
            for (int d = 0; d <= top; d++) {
                if (best[d] < 0 || d + w.low < 0) {
                    continue;
                }
                int e = d + w.change;
                if (best[d] + w.size > next[e]) {
                    next[e] = best[d] + w.size;
                    taken[k][e] = true;
                }
            }
            int[] swap = best;
            best = next;
            next = swap;
        }
        List<Integer> used = new ArrayList<>();
        for (int k = order.size() - 1, d = 0; k >= 0; k--) {
            if (taken[k][d]) {
                used.add(0, order.get(k).id);
                d -= order.get(k).change;
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(best[0]).append(' ').append(used.size()).append('\n');
        for (int i = 0; i < used.size(); i++) {
            out.append(i > 0 ? " " : "").append(used.get(i));
        }
        System.out.println(out);
    }
}
