import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final int END = 1000000000;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] a = new int[n], b = new int[n];
        char[] colour = new char[n];
        int[] all = new int[2 * n + 2];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            a[i] = (int)in.nval;
            in.nextToken();
            b[i] = (int)in.nval;
            in.nextToken();
            colour[i] = in.sval.charAt(0);
            all[2 * i] = a[i];
            all[2 * i + 1] = b[i];
        }
        all[2 * n] = 0;
        all[2 * n + 1] = END;
        int[] xs = Arrays.stream(all).sorted().distinct().toArray();

        // piece i is [xs[i], xs[i + 1]); repaint the pieces of every segment
        char[] piece = new char[xs.length - 1];
        Arrays.fill(piece, 'w');
        for (int i = 0; i < n; i++) {
            int lo = Arrays.binarySearch(xs, a[i]), hi = Arrays.binarySearch(xs, b[i]);
            Arrays.fill(piece, lo, hi, colour[i]);
        }

        // the longest run of white pieces; a strict comparison keeps the leftmost
        int bestX = 0, bestY = 0;
        for (int i = 0, j; i < piece.length; i = j) {
            j = i;
            while (j < piece.length && piece[j] == piece[i]) {
                j++;
            }
            if (piece[i] == 'w' && xs[j] - xs[i] > bestY - bestX) {
                bestX = xs[i];
                bestY = xs[j];
            }
        }
        System.out.println(bestX + " " + bestY);
    }
}
