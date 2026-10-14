import java.io.*;
import java.util.*;

public class Main {
    static int k;
    static int[] bound, radix, grundy;
    static int[][] cutsOf; // legal cuts by edge length

    static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

    static int offset(int[] x) {
        int idx = 0;
        for (int i = 0; i < x.length; i++)
            idx += x[i] * radix[i];
        return idx;
    }

    // steps x through all tuples below dims, last axis fastest; false when done
    static boolean advance(int[] x, int[] dims) {
        int i = dims.length - 1;
        while (i >= 0 && ++x[i] == dims[i])
            x[i--] = 0;
        return i >= 0;
    }

    // the XOR over all parts for every tuple of cuts, last cut fastest: table
    // holds the values of the parts by piece lengths, and each axis in turn is
    // replaced by its cuts, a cut c of an edge d joining the pieces c - 1, d - c
    static int[] cutValues(int[] table, int[] dims) {
        int[] sizes = dims.clone();
        for (int axis = k - 1; axis >= 0; axis--) {
            int inner = 1;
            for (int j = axis + 1; j < k; j++)
                inner *= sizes[j];
            int d = sizes[axis];
            int[] cuts = cutsOf[d];
            int[] out = new int[table.length / d * cuts.length];
            int w = 0;
            for (int start = 0; start < table.length; start += d * inner)
                for (int c : cuts) {
                    int low = start + (c - 1) * inner, high = start + (d - c) * inner;
                    for (int j = 0; j < inner; j++)
                        out[w++] = table[low + j] ^ table[high + j];
                }
            table = out;
            sizes[axis] = cuts.length;
        }
        return table;
    }

    // turns a into the next ordering, false after the last one
    static boolean nextPermutation(int[] a) {
        int i = a.length - 2;
        while (i >= 0 && a[i] >= a[i + 1])
            i--;
        if (i < 0)
            return false;
        int j = a.length - 1;
        while (a[j] <= a[i])
            j--;
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
        for (int l = i + 1, r = a.length - 1; l < r; l++, r--) {
            t = a[l];
            a[l] = a[r];
            a[r] = t;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        k = (int)in.nval;
        int[] edges = new int[k];
        boolean hasOne = false;
        for (int i = 0; i < k; i++) {
            in.nextToken();
            edges[i] = (int)in.nval;
            hasOne |= edges[i] == 1;
        }
        if (k == 1) {
            // pieces of a segment of length d total d - 1, so by induction its
            // value is d mod 2, and from an odd length every cut wins
            System.out.println(edges[0] % 2 == 1 ? "1\n1" : "2");
            return;
        }
        if (hasOne) {
            // any cut empties a box with an edge of 1, so Alice cuts and wins
            StringJoiner ones = new StringJoiner(" ");
            for (int i = 0; i < k; i++)
                ones.add("1");
            System.out.println("1\n" + ones);
            return;
        }
        // every ordering of a box's edges is stored with the same value, indexed
        // by a mixed radix over the sorted edges of the whole box
        bound = edges.clone();
        Arrays.sort(bound);
        radix = new int[k];
        radix[k - 1] = 1;
        for (int i = k - 2; i >= 0; i--)
            radix[i] = radix[i + 1] * (bound[i + 1] + 1);
        grundy = new int[radix[0] * (bound[0] + 1)]; // boxes with an empty edge stay 0
        int longest = bound[k - 1];
        cutsOf = new int[longest + 1][];
        cutsOf[0] = cutsOf[1] = new int[0];
        for (int d = 2; d <= longest; d++) {
            List<Integer> list = new ArrayList<>();
            for (int c = 1; c <= d; c++)
                if ((c > 1 && gcd(c - 1, d) == 1) || (d > c && gcd(d - c, d) == 1))
                    list.add(c);
            cutsOf[d] = list.stream().mapToInt(Integer::intValue).toArray();
        }
        // the boxes with sorted edges, smaller ones first
        List<int[]> boxes = new ArrayList<>();
        int[] box = new int[k];
        do {
            int[] b = new int[k];
            boolean sorted = true;
            for (int i = 0; i < k; i++) {
                b[i] = box[i] + 1;
                sorted &= i == 0 || b[i - 1] <= b[i];
            }
            if (sorted)
                boxes.add(b);
        } while (advance(box, bound));
        boxes.sort(Comparator.comparingInt(b -> Arrays.stream(b).sum()));
        int[] seen = new int[grundy.length + 2];
        int stamp = 0;
        for (int[] b : boxes) {
            int g = 0;
            boolean movable = true;
            for (int d : b)
                movable &= cutsOf[d].length > 0;
            if (b[0] == 1)
                g = 1;
            else if (movable) {
                // the parts by piece lengths, a row along the last axis at a time
                int count = 1;
                for (int d : b)
                    count *= d;
                int[] table = new int[count], prefix = new int[k], head = Arrays.copyOf(b, k - 1);
                int w = 0;
                do {
                    int base = offset(prefix);
                    System.arraycopy(grundy, base, table, w, b[k - 1]);
                    w += b[k - 1];
                } while (advance(prefix, head));
                stamp++;
                for (int v : cutValues(table, b))
                    seen[v] = stamp;
                while (seen[g] == stamp)
                    g++;
            }
            // only orderings within the bounds are ever looked up
            do {
                boolean fits = true;
                for (int i = 0; i < k; i++)
                    fits &= b[i] <= bound[i];
                if (fits)
                    grundy[offset(b)] = g;
            } while (nextPermutation(b));
        }
        if (grundy[offset(bound)] == 0) {
            System.out.println(2);
            return;
        }
        // the first winning cut in lexicographic order, in the input's order
        int total = 1;
        for (int e : edges)
            total *= e;
        int[] table = new int[total], x = new int[k];
        int w = 0;
        do {
            int[] sorted = x.clone();
            Arrays.sort(sorted);
            table[w++] = grundy[offset(sorted)];
        } while (advance(x, edges));
        int[] counts = new int[k], pos = new int[k];
        for (int i = 0; i < k; i++)
            counts[i] = cutsOf[edges[i]].length;
        for (int v : cutValues(table, edges)) {
            if (v == 0) {
                StringJoiner move = new StringJoiner(" ");
                for (int i = 0; i < k; i++)
                    move.add(String.valueOf(cutsOf[edges[i]][pos[i]]));
                System.out.println("1\n" + move);
                return;
            }
            advance(pos, counts);
        }
    }
}
