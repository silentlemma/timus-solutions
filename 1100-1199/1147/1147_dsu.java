import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.TreeSet;

public class Main {
    // the colour of the white sheet
    static final int WHITE = 1;
    // colours are at most this
    static final int COLOURS = 2500;

    static int[] skip;

    static int find(int j) {
        while (skip[j] != j) {
            skip[j] = skip[skip[j]];
            j = skip[j];
        }
        return j;
    }

    static int[] sorted(TreeSet<Integer> set) {
        return set.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int width = (int)in.nval;
        in.nextToken();
        int height = (int)in.nval;
        in.nextToken();
        int n = (int)in.nval;
        int[] x1 = new int[n], y1 = new int[n], x2 = new int[n], y2 = new int[n];
        int[] colour = new int[n];
        TreeSet<Integer> xset = new TreeSet<>(Arrays.asList(0, width));
        TreeSet<Integer> yset = new TreeSet<>(Arrays.asList(0, height));
        for (int k = 0; k < n; k++) {
            int[][] fields = {x1, y1, x2, y2, colour};
            for (int[] f : fields) {
                in.nextToken();
                f[k] = (int)in.nval;
            }
            xset.add(x1[k]);
            xset.add(x2[k]);
            yset.add(y1[k]);
            yset.add(y2[k]);
        }
        int[] xs = sorted(xset), ys = sorted(yset);
        long[] area = new long[COLOURS + 1];
        skip = new int[ys.length];
        for (int i = 0; i + 1 < xs.length; i++) {
            long strip = xs[i + 1] - xs[i];
            // the top rectangles paint the cells of this strip first, and skip[j]
            // leads past painted cells to the next unpainted one
            for (int j = 0; j < skip.length; j++) {
                skip[j] = j;
            }
            int painted = 0;
            for (int k = n - 1; k >= 0 && painted < height; k--) {
                if (x1[k] > xs[i] || x2[k] < xs[i + 1]) {
                    continue;
                }
                int hi = Arrays.binarySearch(ys, y2[k]);
                int got = 0;
                for (int j = find(Arrays.binarySearch(ys, y1[k])); j < hi; j = find(j + 1)) {
                    got += ys[j + 1] - ys[j];
                    skip[j] = j + 1;
                }
                area[colour[k]] += got * strip;
                painted += got;
            }
            area[WHITE] += (height - painted) * strip;
        }
        StringBuilder out = new StringBuilder();
        for (int c = 1; c <= COLOURS; c++) {
            if (area[c] > 0) {
                out.append(c).append(' ').append(area[c]).append('\n');
            }
        }
        System.out.print(out);
    }
}
