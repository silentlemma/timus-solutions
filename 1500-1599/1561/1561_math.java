import java.io.*;
import java.util.*;

public class Main {
    static final String[] DAYS = {"Monday", "Tuesday",  "Wednesday", "Thursday",
                                  "Friday", "Saturday", "Sunday"};
    static final int WEEK = DAYS.length;

    static int dayOf(String word) { return Arrays.asList(DAYS).indexOf(word); }

    static int inverse(int x) {
        for (int y = 1; y < WEEK; y++)
            if (x * y % WEEK == 1)
                return y;
        return 0;
    }

    static int mod(int x) { return (x % WEEK + WEEK) % WEEK; }

    // a row of an echelon basis over the residues modulo 7, with a 1 at its
    // first non-zero place
    static class Row {
        int pivot, right;
        int[] coefficients;

        Row(int pivot, int[] coefficients, int right) {
            this.pivot = pivot;
            this.coefficients = coefficients;
            this.right = right;
        }
    }

    static List<Row> basis = new ArrayList<>();

    // subtract basis rows until no pivot of the basis stays non-zero
    static int reduce(int[] v, int value) {
        for (Row row : basis) {
            int c = v[row.pivot];
            if (c == 0)
                continue;
            // the row is shorter if sorts appeared after it
            for (int i = row.pivot; i < row.coefficients.length; i++)
                v[i] = mod(v[i] - c * row.coefficients[i]);
            value = mod(value - c * row.right);
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null)
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        int n = Integer.parseInt(words.nextToken()), sorts = 0;
        boolean crazy = false;
        StringBuilder out = new StringBuilder();
        for (int q = 0; q < n; q++) {
            String kind = words.nextToken();
            if (kind.equals("Add")) {
                sorts++;
                continue;
            }
            // the numbers of the query up to its first weekday
            List<Integer> numbers = new ArrayList<>();
            String word = words.nextToken();
            while (dayOf(word) < 0) {
                numbers.add(Integer.parseInt(word) % WEEK);
                word = words.nextToken();
            }
            int[] v = new int[Math.max(sorts, numbers.size())];
            for (int i = 0; i < numbers.size(); i++)
                v[i] = numbers.get(i);
            int start = dayOf(word);
            if (kind.equals("Learn")) {
                int finish = dayOf(words.nextToken());
                if (crazy)
                    continue;
                int value = reduce(v, mod(finish - start));
                int pivot = 0;
                while (pivot < v.length && v[pivot] == 0)
                    pivot++;
                if (pivot == v.length) {
                    crazy = value != 0;
                    continue;
                }
                int scale = inverse(v[pivot]);
                for (int i = 0; i < v.length; i++)
                    v[i] = v[i] * scale % WEEK;
                int at = 0;
                while (at < basis.size() && basis.get(at).pivot < pivot)
                    at++;
                basis.add(at, new Row(pivot, v, value * scale % WEEK));
            } else if (crazy)
                out.append("Already crazy\n");
            else {
                int value = reduce(v, 0);
                boolean known = true;
                for (int c : v)
                    if (c != 0)
                        known = false;
                out.append(known ? DAYS[mod(start - value)] : "Don't know").append('\n');
            }
        }
        System.out.print(out);
    }
}
