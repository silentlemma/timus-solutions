import java.io.*;
import java.util.*;

public class Main {
    static final int TOP = 101; // card values are 1..100
    static final int SUITS = 11;
    static int n, best;
    static int[] values, kinds, place = new int[SUITS];

    interface Visit {
        void run();
    }

    // calls visit with every ordering of a, rearranging it in place
    static void permutations(int[] a, int k, Visit visit) {
        if (k == a.length) {
            visit.run();
            return;
        }
        for (int i = k; i < a.length; i++) {
            int t = a[k];
            a[k] = a[i];
            a[i] = t;
            permutations(a, k + 1, visit);
            a[i] = a[k];
            a[k] = t;
        }
    }

    static void score() {
        for (int sign : new int[] {1, -1}) {
            // cards that stay form an increasing run of target ranks
            int[] tails = new int[n];
            int size = 0;
            for (int i = 0; i < n; i++) {
                int rank = place[kinds[i]] * TOP + sign * values[i];
                int k = Arrays.binarySearch(tails, 0, size, rank);
                if (k < 0)
                    k = -k - 1;
                tails[k] = rank;
                if (k == size)
                    size++;
            }
            best = Math.max(best, size);
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        values = new int[n];
        kinds = new int[n];
        TreeSet<Integer> blueSet = new TreeSet<>(), yellowSet = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            values[i] = (int)in.nval;
            in.nextToken();
            kinds[i] = (int)in.nval;
            (kinds[i] % 2 == 1 ? blueSet : yellowSet).add(kinds[i]);
        }
        int[] blue = blueSet.stream().mapToInt(Integer::intValue).toArray();
        int[] yellow = yellowSet.stream().mapToInt(Integer::intValue).toArray();
        // who starts: the larger colour group, or either when they are equal
        List<int[][]> starts = new ArrayList<>();
        if (blue.length >= yellow.length)
            starts.add(new int[][] {blue, yellow});
        if (yellow.length >= blue.length)
            starts.add(new int[][] {yellow, blue});
        for (int[][] pair : starts) {
            int[] a = pair[0], b = pair[1];
            permutations(a, 0, () -> permutations(b, 0, () -> {
                             for (int i = 0; i < a.length; i++)
                                 place[a[i]] = 2 * i;
                             for (int i = 0; i < b.length; i++)
                                 place[b[i]] = 2 * i + 1;
                             score();
                         }));
        }
        System.out.println(n - best);
    }
}
